# remote-edit
Sublime-text-3 plugin to scp files to a remote server when saving a file.
Requires that you have previously copied your ssh-key to the remote machine
using ssh-copy-id.
For example:

```ssh-copy-id user@myhost1```

Supports copying to multiple hosts, given that the files are located on the same place.