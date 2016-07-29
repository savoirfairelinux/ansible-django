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
GIT_ROOT = '{{ django_project_path }}'
SRC_ROOT = '{{ django_src_path }}'
PROJECT_DOMAIN = '{{ django_domain_name }}'
EXTRA_DOMAINS = [
    {% for domain in django_extra_domain_names|default([]) -%}
    '{{ domain }}',
    {%- endfor %}
]
ALLOWED_HOSTS = [PROJECT_DOMAIN] + EXTRA_DOMAINS
PROJECT_ENVPATH = '{{ django_env }}'

{{ django_env_settings_extra }}

