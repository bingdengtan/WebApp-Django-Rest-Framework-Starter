"""
WSGI config for framework project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""


import os
import sys

# Add current project and the virtual env to the path.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PYTHON_HOME = BASE_DIR + '\\env'
activate_this = PYTHON_HOME + '\\Scripts\\activate_this.py'
if os.path.isfile(activate_this):
    with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))
    sys.path.append(BASE_DIR)
# End add

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'framework.settings')

application = get_wsgi_application()