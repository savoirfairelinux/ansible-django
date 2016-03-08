# local settings files to use for local development

DEBUG = {% if django_debug %}True{% else %}False{% endif %}

DATABASES = {
    'default': {
        'ENGINE': '{{ django_dbengine_name }}',
        'NAME': '{{ django_dbname }}',
        'USER': '{{ django_dbuser }}',
        'PASSWORD': '{{ django_dbpass }}',
        'HOST': 'localhost',
    }
}

SECRET_KEY = '{{ django_secret_key }}'

PROJECT_ROOT = '{{ django_path }}'
PROJECT_DOMAIN = '{{ django_domain_name }}'
PROJECT_ENVPATH = '{{ django_env }}'

