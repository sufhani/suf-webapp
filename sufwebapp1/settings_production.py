from sufwebapp1.settings import *


import dj_database_url
DATABASES['default'] = dj_database_url.config()

#Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#Allow all host headers
ALLOWED_HOSTS = ['*']

# Set debug to False
DEBUG = False

# static asset configuration
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
