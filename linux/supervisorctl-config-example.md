# supervisorctl config example

Example of a supervisor process control config file.

Supervisor helps avoid the need to restart your application should the server have to reboot. 
Otherwise, we would manually have to launch the gunicorn server with the `gunicorn -b <...>` command.
Supervisor handles this in the background.

```bash
# /etc/supervisor/conf.d/main-site.conf
[program:personal_site]
command=/home/ubuntu/repos/main-site/venv/bin/gunicorn -b localhost:8050 -w 4 app:app
directory=/home/ubuntu/repos/main-site
user=pz-dev
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
```
