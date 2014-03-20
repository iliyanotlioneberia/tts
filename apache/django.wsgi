import os
import os.path
import sys

sys.path.append('/Users/Iliyan/Django')
sys.path.append('/Users/Iliyan/Django/university')

os.environ['PYTHON_EGG_CACHE'] = '/Users/Iliyan/Django/egg_cache'
os.environ['DJANGO_SETTINGS_MODULE'] = 'university.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()