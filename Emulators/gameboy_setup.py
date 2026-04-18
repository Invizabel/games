import os

os.mkdir("app")
os.chdir("app")
os.system("sudo apt update && sudo apt install nginx git -y")
os.system("git clone https://github.com/mitxela/swotGB")
os.system("sudo cp -r swotGB/gbjs.htm /var/www/html/index.html")
