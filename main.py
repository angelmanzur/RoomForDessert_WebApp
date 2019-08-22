from leave_room.wsgi import application
import os
#from google.appengine.api import app_identity
#import cloudstorage as gcs
# App Engine by default looks for a main.py file at the root of the app
# directory with a WSGI-compatible object called app.
# This file imports the WSGI-compatible object of your Django app,
# application from mysite/wsgi.py and renames it app so it is discoverable by
# App Engine without additional configuration.
# Alternatively, you can add a custom entrypoint field in your app.yaml:
# entrypoint: gunicorn -b :$PORT mysite.wsgi
app = application

# def get(self):
#     bucket_name = os.environ.get('BUCKET_NAME',
#                                  app_identity.get_default_gcs_bucket_name())
  
#     self.response.headers['Content-Type'] = 'text/plain'
#     self.response.write('Demo GCS Application running from Version: '
#                         + os.environ['CURRENT_VERSION_ID'] + '\n')
#     self.response.write('Using bucket name: ' + bucket_name + '\n\n')


