Symlink plugin for Ansible
==========================

[![Build Status](https://travis-ci.org/guillaumeaubert/ansible-symlink-plugin.svg?branch=master)](https://travis-ci.org/guillaumeaubert/ansible-symlink-plugin)


Synopsis
--------

This Ansible plugin allows creating symlinks while optionally backing up the destination if it already exists and it isn't a symlink. This is particularly useful to replace default configuration files, when you don't want to just overwrite the default without a way to check it again in the future.


Installation
------------

Options
-------

<table>
	<thead>
		<tr>
			<th>Parameter</th>
			<th>Required</th>
			<th>Default</th>
			<th>Choices</th>
			<th>Comments</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>src</td>
			<td>yes</td>
			<td></td>
			<td></td>
			<td>Path of the file or directory to symlink to.</td>
		</tr>
		<tr>
			<td>dest</td>
			<td>yes</td>
			<td></td>
			<td></td>
			<td>Remote absolute path where the symlink should be created.</td>
		</tr>
		<tr>
			<td>archive</td>
			<td>no</td>
			<td>True</td>
			<td>
				<ul>
					<li>True</li>
					<li>False</li>
				</ul>
			</td>
			<td>
				This flag indicates whether a backup of the destination should be made,
				if the destination exists and is not a symlink.
			</td>
		</tr>
		<tr>
			<td>archive_suffix</td>
			<td>no</td>
			<td>_original</td>
			<td></td>
			<td>
				If the destination needs to be archived, the file or directory will be
				renamed using this suffix.
			</td>
		</tr>
	</thead>
</table>


Examples
--------

TODO


Copyright
---------

Copyright (C) 2014-2015 Guillaume Aubert


License
-------

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License version 3 as published by the Free
Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see http://www.gnu.org/licenses/
