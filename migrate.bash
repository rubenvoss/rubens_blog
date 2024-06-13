#!/bin/bash
docker exec -it rubens_blog sh -c "python manage.py makemigrations && python manage.py migrate"