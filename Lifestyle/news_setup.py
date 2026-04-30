import os

os.system("sudo docker run -d -p 80:80 -e TZ=America/Chicago -e 'CRON_MIN=1,31' -v freshrss_data:/var/www/FreshRSS/data -v freshrss_extensions:/var/www/FreshRSS/extensions --name freshrss --restart always ghcr.io/freshrss/freshrss")
