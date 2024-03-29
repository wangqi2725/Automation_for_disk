"""
Django settings for Automation_management_platform project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-cen*bp^x$o@ri59zcrw8g2izx=7#i&#@)g_h3##%6*b4p=_h*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 如果想打印orm转换过程中的sql，需要在settings中进行配置日志：
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#         'standard': {
#             'format': '%(asctime)s,%(process)d,%(name)s,%(levelname)s,%(filename)s:%(lineno)d,%(message)s'
#         },
#     },
#     'filters': {
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'include_html': True,
#             # 'filters': ['special'],
#         },
#         'default': {
#             'level': 'ERROR',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join(os.path.curdir, 'all.log'),
#             'maxBytes': 1024 * 1024 * 50,  # 50 MB
#             'backupCount': 5,
#             'formatter': 'standard',
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'standard'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['default', 'console'] if DEBUG else ["default"],
#             'level': 'ERROR',
#             'propagate': False
#         },
#         '': {
#             'handlers': ['default', 'console'] if DEBUG else ["default"],
#             'level': 'DEBUG',
#             'propagate': False
#         },
#     }
# }

ALLOWED_HOSTS = ['*','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app.apps.AppConfig',
    # 'app',
    'django_apscheduler',#定时任务
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'Automation_management_platform/static')
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Automation_management_platform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Automation_management_platform.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'flask_api',
        'USER':'root',
        'PASSWORD':'Easy104818',
        'HOST':'127.0.0.1',
        'PORT':'3306',
#         'ATOMIC_REQUEST':True,#设置为True代表同一个http请求所对应的所有sql都放在一个事务中执行
# #要么所有都成功，要么所有都失败)，这是全局性的配置，如果要对某个http请求放水（然后自定义事务），可以用non_atomic_requests修饰器
#         'OPTIONS':{
#             "init_command":'SET storage_engine=INNODB'
#         },
    }
}

LOGGING = {
    'version':1,
    'disable_existing_loggers':False,
    'handlers':{

    }

}
# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

