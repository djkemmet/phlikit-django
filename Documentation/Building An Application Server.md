# Building a Digital Ocean Droplet to Host Our Application
1. apt update && apt upgrade
2. apt install python3-pip nginx
3. python3 -m pip install django
4. cd /var/local/ && git clone https://github.com/djkemmet/phlikit-django.git
5. nano /etc/init.d/start_poztd

<code>

    #!/bin/bash

    python3 /var/local/phlikit-django/phlikit/manage.py 0.0.0.0:8000

</code>

6. chmod +x /etc/init.d/start_poztd && cd /etc/init.d/ && update-rc.d start_poztd defaults
7. TODO: Figure out how to make this start on boot
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

