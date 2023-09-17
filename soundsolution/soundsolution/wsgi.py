#
# The below has been auto-generated for your Django project

import os
import sys

# add your project directory to the sys.path
path = '/home/Dest1ni/SoundSolution/soundsolution/'
if path not in sys.path:
    # sys.path.insert(0, path)
    sys.path.append(path)

os.chdir(path)

# set environment variable to tell django where your settings.py is
# os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'soundsolution.settings')

# Import your Django project's configuration
import django
django.setup()

# Import the Django WSGI to handle any requests
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

# # serve django via WSGI
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()