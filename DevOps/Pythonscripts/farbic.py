from fabric.api import *

def greetings(msg):
    print("Hello, {}".format(msg))

#local command
def system_info():
    print("Disk space.")
    local("df -h")

    print("Memory info.")
    local("free -m")

    print("System uptime")
    local("uptime")

#remote command

def remote_exec():
    run("hostname")
    run("uptime")
    run("df -h")
    run("free -m")

#installing package at remote
sudo("yum install unzip zip wget -y")

def web_setup(WEBURL, DIRNAME):
    print("###############################################")
    print("Installing dependencies")
    print("###############################################")
    sudo("yum install httpd wget unzip -y")

    print("###############################################")
    print("Start & ENable service")
    print("###############################################")
    sudo("systemctl start httpd")
    sudo("systemctl enable httpd")

    print("###############################################")
    local("apt install zip unzip -y")

    print("###############################################")
    print("Downloading and pushing website to webservers.")
    print("###############################################")
    local(("wget -O website.zip %s") % WEBURL)
    local("unzip -o website.zip")

    print("###############################################")
    with lcd(DIRNAME):
        local("zip -r tooplate.zip * ")
        put("tooplate.zip", "/var/www/html", use_sudo=True)

    with cd("/var/www/html"):
        sudo("unzip -o tooplate.zip")

    sudo("systemctl restart httpd")

    print("Website setup is done")
