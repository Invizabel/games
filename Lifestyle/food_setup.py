import os

os.mkdir("app")
os.chdir("app")
os.system("sudo apt update && sudo apt install wget -y")
os.system("wget https://raw.githubusercontent.com/Invizabel/Scripts/refs/heads/main/Setup/docker_ubuntu.py")
os.system("python3 docker_ubuntu.py")
os.system("sudo docker run -d --name=mealie --restart always -p 80:9000 ghcr.io/mealie-recipes/mealie:latest")
