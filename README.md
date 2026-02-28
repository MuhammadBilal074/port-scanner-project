## What is this?
This is a simple port scanner I built 
to learn about network security. 
It scans a target computer and tells 
you which ports are open and what 
services are running on them.

## Why I made this
I wanted to understand how hackers 
find weaknesses in a network. Building 
this tool helped me understand how 
reconnaissance works in ethical hacking.

## What I used
- Python 3 for writing the script
- Kali Linux as my working environment
- Metasploitable VM as my target machine
- Nmap to verify my results

## How it works
The script goes through ports 1 to 1024 
and knocks on each one. If something 
answers, it means that port is open and 
a service is running there.

## What I found
When I ran it against my Metasploitable 
VM (192.168.75.132), I discovered 
these open ports:

Port 21  - FTP (File Transfer)
Port 22  - SSH (Remote Login)
Port 23  - Telnet (Unencrypted Login)
Port 25  - SMTP (Email Server)
Port 53  - DNS (Domain Name Service)
Port 80  - HTTP (Web Server)
Port 139 - NetBIOS (Network Sharing)
Port 445 - Samba (File Sharing)
Port 512 - Remote Exec (Dangerous!)
Port 513 - Remote Login (Dangerous!)
Port 514 - Remote Shell (Dangerous!)
Port 3306 - MySQL (Database)
Port 5432 - PostgreSQL (Database)
Port 5900 - VNC (Remote Desktop)

## What I learned
I was surprised how many ports were 
open on Metasploitable. This taught 
me that leaving unnecessary ports open 
is a huge security risk. In a real 
network, all these dangerous ports 
should be closed immediately.

## Important Note
I only scanned my own lab machine 
which is intentionally vulnerable 
for learning purposes. Scanning 
someone elses computer without 
permission is illegal and unethical.
