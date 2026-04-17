import os

os.system("sudo apt update && sudo apt install nginx git -y")
os.mkdir("emu")
os.chdir("emu")
os.system("git clone https://github.com/ppeccin/javatari.js")
os.system("sudo cp -r javatari.js/release/stable/5.0/standalone/* /var/www/html/")
