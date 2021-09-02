
# nginx web server

Here is an example of an `nginx` web server configuration. This site has main domain (my_domain.com), supports separate backends (app1.my_domain.com), 
and supports HTTs/SSL certificates. The configuration also redirects HTTP traffic.

The proxy redirects are can be specified by port on the same or separate servers (note to add extra security for multiple servers and inter-serveer comms).

Ex: a gunicorn Python WSGI process (or gunicorn process managed by supervisorctl / daemon process) can be listening on port 8050. An HTTPS request will be re-routed to the WSGI app. We can support multiple backend sites on one domain too.

```bash

# redirect http to https
server {
    if ($host = www.my_domain.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    if ($host = my_domain.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    # listen on port 80 (http)
    listen 80;
    server_name my_domain.com www.my_domain.com;
    location / {
        # redirect any requests to the same URL but on https
        return 301 https://$host$request_uri;
    }
}

# main domain
server {
    # listen on port 443 (https)
    listen 443 ssl;
    server_name my_domain.com www.my_domain.com;

    # location of the self-signed SSL certificate
    ssl_certificate /etc/letsencrypt/live/my_domain.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/my_domain.com/privkey.pem; # managed by Certbot

    # write access and error logs to /var/log
    access_log /var/log/main-site_access.log;
    error_log /var/log/main-site_error.log;

    location / {
        # forward application requests to the gunicorn server
        proxy_pass http://localhost:8050;
        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static {
        # handle static files directly, without forwarding to the application
        alias /home/ubuntu/repos/main-site/app/static;
        expires 30d;
    }


}

# Demo: using Nginx as a Reverse Proxy for Multiple Sites
  # this domain must have a CNAME DNS entry created to link, say, "app1.my_domain.com" to "my_domain.com"
  # the CNAME URL will also need a separate SSL cert for HTTPs  
server {
    listen 443 ssl;
    server_name app1.my_domain.com www.app1.my_domain.com;
    ssl_certificate /etc/letsencrypt/live/app1.my_domain.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/app1.my_domain.com/privkey.pem; # managed by Certbot

    location / {
        # forward application requests to the gunicorn server
        proxy_pass http://localhost:8000;
        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    access_log /var/log/app1_access.log;
    error_log /var/log/app1_error.log;
}
```

