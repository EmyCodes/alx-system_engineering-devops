# 0x12. Web stack debugging #2
An introductory project on:
- web stack debugging

# Requirements
- Files are to be executed on Ubuntu 20.04 LTS - The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- Bash script must pass `Shellcheck` (version 0.3.7) without any error

# File Descriptions
## Mandatory
[0-iamsomeoneelse](./0-iamsomeoneelse) - runs the `whoami` command under the user passed as an argument
```
root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeoneelse www-data
www-data
root@ubuntu:~# whoami
root
root@ubuntu:~#
```
