"""
Django settings for SwordPHISH project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY_FILE = os.path.join(BASE_DIR, 'secretkey.txt')

if os.path.exists(SECRET_KEY_FILE):
    with open(SECRET_KEY_FILE) as f:
        SECRET_KEY = f.read().strip()
else:
    SECRET_KEY = 'DUMMY_KEY_FOR_DEVELOPMENT_DO_NOT_USE_IN_PRODUCTION'

ADMINS = []

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

PROJECT_NAME = "SwordPHISH"

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_generate_secret_key',
    'bootstrap3',
    'bootstrap3_datetime',
    'pure_pagination',
    'ckeditor',
    'LocalUsers',
    'Main',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'Swordphish.urls'

WSGI_APPLICATION = 'Swordphish.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'swordphish',
        'USER': 'swordphish',
        'PASSWORD': 'FIXME',
        'HOST': 'FIXME',
        'PORT': '',
    }

}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': True,
        },
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en', 'English'),
]

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    'locale',)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'


LOGIN_URL = 'Authent:login'
LOGOUT_URL = 'Authent:logout'


PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 2,
    'MARGIN_PAGES_DISPLAYED': 3,
}

SESSION_SAVE_EVERY_REQUEST = True

# Default settings
BOOTSTRAP3 = {
    'jquery_url': f'{STATIC_URL}jquery.min.js',
    'css_url': f'{STATIC_URL}bootstrap-3.3.7/css/bootstrap.min.css',
    'theme_url': None,
    'javascript_url': f'{STATIC_URL}bootstrap-3.3.7/js/bootstrap.min.js',
    'javascript_in_head': True,
    'include_jquery': True,
    'horizontal_label_class': 'col-md-2',
    'horizontal_field_class': 'col-md-4',
    'set_required': True,
    'set_placeholder': True,
    'required_css_class': '',
    'error_css_class': 'has-error',
    'success_css_class': 'has-success',
    'formset_renderers': {
        'default': 'bootstrap3.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'bootstrap3.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'bootstrap3.renderers.FieldRenderer',
        'inline': 'bootstrap3.renderers.InlineFieldRenderer',
    },
}


CKEDITOR_BASEPATH = f"{STATIC_URL}ckeditor/ckeditor"

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['Table', 'NumberedList', 'BulletedList', 'HorizontalRule'],
            ['Outdent', 'Indent'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['TextColor', 'BGColor'], ['base64image', 'Link', 'Unlink'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['RemoveFormat', 'Source', 'DocProps', 'Maximize']
        ],
        'extraPlugins': 'base64image,docprops,font,maximize',
        'width': '100%',
        'fullPage': 'true',
        'removeDialogTabs': 'link:Upload;link:upload;link:advanced;docProps:meta;docProps:preview;',
        'filebrowserBrowseUrl': '',
        'filebrowserImageBrowseUrl': '',
        'filebrowserFlashBrowseUrl': '',
    },
    'withforms': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['Table', 'NumberedList', 'BulletedList', 'HorizontalRule'],
            ['Outdent', 'Indent'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['TextColor', 'BGColor'], ['base64image', 'Link', 'Unlink'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['RemoveFormat', 'Source', 'DocProps', 'Maximize'],
            ['Form', 'TextField', 'Button']
        ],
        'extraPlugins': 'base64image,docprops,font,maximize,forms',
        'width': '100%',
        'fullPage': 'true',
        'removeDialogTabs': 'link:Upload;link:upload;link:advanced;docProps:meta;docProps:preview;',
        'filebrowserBrowseUrl': '',
        'filebrowserImageBrowseUrl': '',
        'filebrowserFlashBrowseUrl': '',
    }
}

# Redis configuration used by Celery
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0


# URL to reach the app (used in mail creation mails)
SWORPDHISH_URL = "https://hostname"

# Swordphish creation account mail template
NEW_ACCOUNT_TEMPLATE = u"""Hello %s

Please find your SwordPhish credentials below.

URL: %s
Login: %s
Password: %s

The password must be changed at the first connection.

Best regards,

Swordphish administrators
"""

# Swordphish lost password mail template
LOST_PASSWORD_TEMPLATE = u"""Hello %s

Please find your SwordPhish credentials below.

URL: %s
Login: %s
Password: %s

The password must be changed at the first connection.

Best regards,

Swordphish administrators
"""


USER_ACCOUNT_CREATION_MAIL_SENDER = "SwordPhish <swordphish@invalid.notld>"

USER_ACCOUNT_CREATION_MAIL_TITLE = "[SwordPhish] Account creation"

USER_ACCOUNT_LOST_PASS_MAIL_TITLE = "[SwordPhish] New password request"

USER_ACCOUNT_CREATION_MAIL_CONTACT = "contact_swordphish@invalid.notld"

USER_ACCOUNT_LOCKED_MAIL_TITLE = "[Swordphish] Your account has been locked !"


# Mail address used to send mails
SERVER_EMAIL = "SwordPhish <swordphish@invalid.notld>"

# Mail server information
EMAIL_HOST = "localhost"
EMAIL_PORT = 2525
# EMAIL_HOST_USER = "FIXME"
# EMAIL_HOST_PASSWORD = "FIXME"

# Used to alert when a campaign starts
ALERT_RECIPIENTS = ["fixme@invalid.notld"]

# After AUTOLOCK_DELAY days of inactivity account will be blocked
AUTOLOCK_DELAY = 180

# Mail sent when an account is auto locked
AUTOLOCK_TEMPLATE = u"""Hello %s

You have an active account on Swordphish but you never logged in.

As a security measure, your account has been locked. If you need it reply to this email !

Best regards,

Swordphish administrators
"""

# AUTOLOCK_NEVER_USED_DELAY days after creation an account will be locked if not used
AUTOLOCK_NEVER_USED_DELAY = 30

# Mail sent when an account is never used
AUTOLOCK_NEVER_USED_TEMPLATE = u"""Hello %s

You have an active account on Swordphish but haven't used it during the last %s days.

As a security measure, your account has been locked. If you need it reply to this email !

Best regards,

Swordphish administrators
"""

# After AUTOCLEAN_DELAY days the campaigns / targets will be automatically deleted
AUTOCLEAN_DELAY = 90

# The day of the week when the auto delete is performed
AUTOCLEAN_DAY = "saturday"

# Used to filter access to swordphih pages when reaching phishing pages
HOSTING_DOMAIN = "FIXME"

# Phishing mail header
PHISHING_MAIL_HEADER = "X-Swordphish-Awareness-Campaign"
