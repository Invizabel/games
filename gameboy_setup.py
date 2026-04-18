import os

os.mkdir("emu")
os.chdir("emu")
os.system("sudo apt update && sudo apt install nginx git -y")
os.system("git clone https://github.com/mitxela/swotGB")
os.system("sudo cp -r swotGB/gbjs.htm /var/www/html/index.html")
