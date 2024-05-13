print("--- Using development Settings ---")
SECRET_KEY = "django-insecure-=jmn_^-g2#+c!*@kmd&058iq+*3y(2%wkqu$!c3hkhvffb3+ax"
DEBUG = True
ALLOWED_HOSTS = []

# database
from .base import BASE_DIR
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}