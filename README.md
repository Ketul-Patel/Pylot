# Pylot MVC (beta)
Pylot MVC is a lightweight MVC framework built in Python leveraging flask.

This framework is currently still in development. If you want to play around with it read on or clone the stable version!

# Installation

First make sure you have pip installed. If you don't have it installed there are great instructions here: https://pip.pypa.io/en/latest/installing.html

Next install virtualenv
```
sudo pip install virtualenv
```

Clone pylot
```
PARENT
git clone -b stable https://github.com/Ketul-Patel/Pylot.git
THIS FORK WORKS FOR AWS DEPLOYMENT:
git clone https://github.com/MikeHannon/Pylot.git
```

cd into pylot (or rename and cd in) and source the setup file
```
cd Pylot
. setup
FOLLOW DIRECTIONS OUTLINED BY SETUP!
note: there might be some fixes needed here, feel free to send them as FAQ's for this Readme (see below)
```

Now you can start your development server like so:
```
python manage.py runserver
```

Enjoy! More details/features coming soon!

# DEPLOYMENT AWS
Assumption: You can get an AWS ec2 instance up and running from your console, and this is a super basic setup!

in that instance set your security groups:

- http: 80 0.0.0.0/0 //anywhere
- ssh: myaddress // just your computer
- mysql aurora publicIP of your instance! /32 // just your instance!

Do all the key stuff and launch!
# Ubuntu System setup
$ sudo apt-get update \
$ sudo apt-get install python-pip python-dev nginx git \
$ sudo apt-get install build-essential libmysqlclient-dev
## below are req's for alternative python versions e.g. 2.7.11 (ubuntu comes with 2.7.6, don't mess with it!)
$ sudo apt-get install -y \\\
autotools-dev      \\\
blt-dev            \\\
bzip2              \\\
dpkg-dev           \\\
g++-multilib       \\\
gcc-multilib       \\\
libbluetooth-dev   \\\
libbz2-dev         \\\
libexpat1-dev      \\\
libffi-dev         \\\
libffi6            \\\
libffi6-dbg        \\\
libgdbm-dev        \\\
libgpm2            \\\
libncursesw5-dev   \\\
libreadline-dev    \\\
libsqlite3-dev     \\\
libssl-dev         \\\
libtinfo-dev       \\\
mime-support       \\\
net-tools          \\\
netbase            \\\
python-crypto      \\\
python-mox3        \\\
python-pil         \\\
python-ply         \\\
quilt              \\\
tk-dev             \\\
zlib1g-dev

$ wget https://www.python.org/ftp/python/2.7.11/Python-2.7.11.tgz \
$ tar xfz Python-2.7.11.tgz \
$ cd Python-2.7.11/
##### these take a few minutes!
$ ./configure --prefix /usr/local/lib/python2.7.11 --enable-ipv6 \
$ sudo make \
$ sudo make install
#### TEST IT
$ /usr/local/lib/python2.7.11/bin/python -V
###### Python 2.7.11 ??? Hopefully?
$ cd .\.  
$ sudo pip install virtualenv \
$ virtualenv --python=/usr/local/lib/python2.7.11/bin/python venv
$ source venv/bin/activate
##### Test It
(venv)$ python -V
###### Python 2.7.11 ??? Hopefully?
(venv)$ git clone **PROJECT** \
(venv)$ cd **PROJECT** \
(venv)$ . setup \
(venv)$ pip install -r system\\dependenciesPC.txt
###### TEST

(venv)$ python manage.py runserver \
running \
turn it off \
#### Setup WSGI/uWSGI -- WSGI.py is preset!
(venv)$ sudo nano ~/**PROJECT**/**PROJECT**.ini\
```
This is a file - just add the stuff below in!
```

[uwsgi] \
module = wsgi \
master = true \
processes = 5 \
socket = **PROJECT**.sock \
chmod-socket = 660 \
vacuum = true \
plugin = python \
die-on-term = true \

```
ctrl-x and then yes to saving, to exit
```

#### UWSGI Upstart Configuration

(venv)$ deactivate

$ sudo nano /etc/init/**PROJECT**.conf
```
This is a file - just add the stuff below in!
```

description "uWSGI server instance configured to serve **PROJECT**" \
start on runlevel [2345] \
stop on runlevel [!2345] \
\
setuid root \
setgid www-data \
\
env PATH=/home/ubuntu/venv/bin \
chdir /home/ubuntu/**PROJECT** \
exec uwsgi --ini **PROJECT**.ini

```
ctrl-x and then yes to saving, to exit
```

$ sudo start **PROJECT**
## NGINX Configuration
$ sudo nano /etc/nginx/sites-available/**PROJECT**

```
This is a file - just add the stuff below in!
```

server { \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; listen 80; \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; server_name AWS_PUBLIC_IP; \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;location / { \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; include uwsgi_params; \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; uwsgi_pass unix:/home/ubuntu/**PROJECT**/**PROJECT**.sock; \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}  

}


```
ctrl-x and then yes to saving, to exit
```
$ sudo ln -s /etc/nginx/sites-available/**PROJECT** /etc/nginx/sites-enabled

# Setting up mysql database
$ sudo apt-get install mysql-server
###### NOTE: this installation will ask you for a password - make sure that the one you choose is reflected in your database.py code!
$ mysql -u root -p \
enter password: **YOUR DB PASSWORD HERE** \
\> **YOU DB BUILDING CODE HERE** \
\> show databases; \
\> use **DB_NAME_HERE** \
\> exit

ALT: \
$ mysql -u root -p **YOUR.SQL**\
\> show databases; \
\> use **DB_NAME_HERE** \
\> exit

# FAQs
