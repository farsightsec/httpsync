HTTP Sync

A librsync-based synchronization tool.  It works like rsync, but over HTTP.

Example usage:

httpsync -u username -p secret https://example.com/file.txt file.txt

Requires:

http://www.python-requests.org/
https://github.com/smartfile/python-librsync/
https://github.com/librsync/librsync
