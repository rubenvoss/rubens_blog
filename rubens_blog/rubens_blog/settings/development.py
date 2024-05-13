print("--- Using development Settings ---")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-vyz+wmkwwa-scgtnr@nzqx#%a860!5)d%mcv6g9@n0_-$64!=q"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# database
import os
from .base import BASE_DIR
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        # "NAME": BASE_DIR / "db.sqlite3",
        "NAME": os.path.join(BASE_DIR + "db.sqlite3"),
    }
}
