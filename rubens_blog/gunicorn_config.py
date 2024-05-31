bind = "0.0.0.0:8000"
module = "rubens_blog.wsgi"

workers = 4  # Adjust based on your server's resources
worker_connections = 1000
threads = 4

certfile = "/etc/letsencrypt/live/rubenvoss.de/fullchain.pem"
keyfile = "/etc/letsencrypt/live/rubenvoss.de/privkey.pem"