# Building a Digital Ocean Droplet to Host Our Application


## Prep the Droplet
1. apt update && apt upgrade
2. apt install python3-pip nginx
3. python3 -m pip install django
4. cd /var/local/ && git clone https://github.com/djkemmet/phlikit-django.git


## Configure service to run app on Boot
1.nano /usr/local/bin/start_phlikit.sh

<code>

    #! /bin/bash

    python3 /var/local/phlikit-django/phlikit/manage.py runserver 0.0.0.0:8000

</code>

2. chmod +x
3. Review Existing Service files: systemctl list-unit-files --type-service
4. Create New Service def to run our app: sudo nano /etc/systemd/system/start-phlikit.service

<code>

    [Unit]
    Description=Start Phlikit Application    

    Wants=network.target
    After=syslog.target network-online.target

    [Service]
    Type=simple
    ExecStart=/usr/local/bin/start-phlikit.sh
    Restart=on-failure
    RestartSec=10
    KillMode=process

    [Install]
    WantedBy=multi-user.target

</code>
<br />

5. chmod 640 /etc/systemd/system/start-phlikit.service
6. Reload all service defs: systemctl daemon-reload
7. systemctl enable start-phlikit.service
8. reboot and make sure the web app comes online.


## Configure nginx to proxy app
8. Configure <b>[/etc/nginx/sites-available](https://mattsegal.dev/nginx-django-reverse-proxy-config.html)</b> with the following root location in the standard (port 80) server definition:

<code>

    server_name poztd.it;

    location / {
                proxy_pass http://127.0.0.1:8000;
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
                proxy_redirect http://127.0.0.1:8000 https://poztd.it;
        }

</code>

9. After the website is up and running, run through <b>[certbot](https://certbot.eff.org)</b>

