import os
import sys

# Django projesinin yolunu ekleyin
path = '/var/www/html'
if path not in sys.path:
    sys.path.insert(0, path)

from django.core.wsgi import get_wsgi_application

# Settings modülünü açıkça belirtin
os.environ['DJANGO_SETTINGS_MODULE'] = 'my_website.settings'

application = get_wsgi_application()