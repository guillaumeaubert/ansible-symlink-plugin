#!/usr/bin/python

# -*- coding: utf-8 -*-
#
# Copyright 2014-2016 Guillaume Aubert.
#
# This software is released under the MIT license. See the LICENSE file for
# details.

import shutil

def main():
    # Define module's arguments and supported features.
    module = AnsibleModule(
        argument_spec = dict(
            src            = dict(required=True),
            dest           = dict(required=True),
            archive        = dict(required=False, default=True, type='bool'),
            archive_suffix = dict(required=False, default='_original'),
        ),
        add_file_common_args=False,
        supports_check_mode=False
    )

    # Read the parameters passed.
    params = module.params
    dest = params['dest']
    archive = params['archive']
    src = params['src']
    archive_suffix = params['archive_suffix']

    # Clean up the various paths needed.
    src = os.path.expanduser(src)
    dest = os.path.expanduser(params['dest'])
    dest_archive = dest+archive_suffix

    # Determine the state of the target.
    dest_state = 'absent'
    if os.path.lexists(dest):
        if os.path.islink(dest) or os.stat(dest).st_nlink > 1:
            dest_state = 'link'
        else:
            dest_state = 'file'

    # Determine the state of the target's archive.
    dest_archive_state = 'absent'
    if os.path.lexists(dest_archive):
        if os.path.islink(dest_archive) or os.stat(dest_archive).st_nlink > 1:
            dest_archive_state = 'link'
        else:
            dest_archive_state = 'file'

    # If dest is correctly set up to the right symlink path, skip.
    if dest_state == 'link' and os.path.realpath(dest) == src:
        module.exit_json(path=dest, changed=False)

    # If the destination archive doesn't exist, move the destination to it.
    if dest_state != 'absent' and dest_archive_state == 'absent':
        shutil.move(dest, dest_archive)
        dest_state = 'absent'
        dest_archive_state = 'file'

    # If the destination doesn't exist, just symlink and exit.
    if dest_state == 'absent':
        try:
            os.symlink(src, dest)
        except OSError, e:
            module.fail_json(path=dest, msg='Error while linking: %s' % str(e))
        module.exit_json(path=dest, changed=True)

    # If the destination is a link, delete and override it.
    elif dest_state == 'link':
        try:
            os.unlink(dest)
            os.symlink(src, dest)
        except OSError, e:
            module.fail_json(path=dest, msg='Error while linking: %s' % str(e))
        module.exit_json(path=dest, changed=True)

    # Otherwise, the destination exists, it's not a link, and the archive
    # already exists so we can't move it. It means someone has set this dest
    # manually, and we can't fix it.
    else:
        module.fail_json(path=dest, msg='The original dest was previously archived, and the current dest is not a link - cannot turn into a link.')

# Import module snippets.
from ansible.module_utils.basic import *
main()
