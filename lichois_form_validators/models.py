from django.conf import settings

if settings.APP_NAME == 'lichois_form_validators':
    from .tests import models