# Loppies

## Handy Snippets for BASH env

- [backit](#Backit)  
- [clean](#clean)
- [rm-docker](#rm-docker)
- [net-hosts](#net-hosts)
- [html-open](#html-open)

#### Backit  
A snippet to make `.bak` of everyfile parsed into it. If the file exists.   

* why it is even needed :
  * It is very helpful for me to take a backup before editing a conf or important file. Because if something happen i will ended up having a last working version of a file.
  * So, I can use it across my machines.

#### clean
A script which clear all not needed temp files from both *swap* and *ram*
* It will drop caches from ram and remount swap partition to delete temp files

#### rm-docker
The script can be used to remove the docker instances from system memory which id parsed into it.

#### net-hosts
The script will display all hosts inside the network with ip address like arp table.

#### HTML-OPEN
It will open html index file on the web browser if it presents.
	* need to specify PATH or file as an argument.
	* firefox and chrome is supported for opening in private.