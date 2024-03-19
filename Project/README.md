
# Weather app deployment


This project is a weather restfull API written in python, using Flask framework.
This project was uploaded to a VM using ESXi and Gunicorn.


## Requirements

- Python
- Flask
- Jinja
- Gunicorn
- Nginx



## Documentation
1. scp (secure copy) project to virtual machine
2. install flask, nginx, Gunicorn
3. configure nginx
4. run gunicorn as deamon


## Nginx Configuration

/etc/nginx/sites-available/weatherapp.conf

server{  

        listen 80;
        listen 9090;
        deny 10.1.0.103;
        server_name 10.1.0.86;
        limit_conn addr 5;

        location / {
                limit_req zone=one burst=5 nodelay;
                proxy_pass http://127.0.0.1:5000;
        }
}


/etc/nginx/nginx.conf


        limit_req_zone $binary_remote_addr zone=one:10m rate=1r/s;
        limit_conn_zone $binary_remote_addr zone=addr:10m;



