import os

os.mkdir("app")
os.chdir("app")
os.system("sudo apt update && sudo apt install wget nginx -y")
os.system("wget https://raw.githubusercontent.com/Invizabel/HomeLab/refs/heads/main/Assets/webrcade.html")
os.system("wget https://raw.githubusercontent.com/Invizabel/HomeLab/refs/heads/main/Assets/docker_setup.py")
os.system("python3 docker_setup.py")
os.system("sudo docker run -d --name=webrcade -p 8080:80 -p 8443:443 --restart always webrcade/webrcade:latest")
os.system("sudo cp webrcade.html /var/www/html/index.html")
