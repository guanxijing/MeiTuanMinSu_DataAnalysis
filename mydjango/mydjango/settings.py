"""
Django settings for mydjango project.

Generated by 'django-admin_hello startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 内置登录后跳转的页面
LOGIN_REDIRECT_URL = "/hotelapp"


APPEND_SLASH = False
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i)$%9h^ltdq!9yo&x=obtx)4-p8w#5r5(y*u*4d(9q5h*j34hi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# SESSION_COOKIE_AGE = 60*60*3  #设置session过期时间为30分钟，3h

# ROOT_URLCONF = 'simpleui_demo.urls'

# Application definition
STATIC_ROOT = os.path.join(BASE_DIR, "static")  # 这儿也给我改了原来是static

INSTALLED_APPS = [
    # 'simpleui',
    # "simpleui",    # 这个是放在前面用的，美化admin管理界面, todo
    # 'SuitConfig',  # 需要添加的内容，要放在'django.contrib.admin_hello'之前
    # 'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages', 
    'django.contrib.staticfiles',
    'hotelapp',   # /这个是最新的美团hotelapp ，这个调试好后继续载入
    # 'rest_framework',  # 这个库可以创造出符合resetful的api方便前后端分离
    'rest_framework',

]
# simple-ui
SIMPLEUI_HOME_INFO = False
SIMPLEUI_LOGO = "http://127.0.0.1/static/media/%E6%B0%91%E5%AE%BF.png"


# AUTH_USER_MODEL = "hotelapp.myUser"  # 前面是封装了使用新的拓展User类来增加收藏夹字段
DATA_UPLOAD_MAX_MEMORY_SIZE = None

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mydjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 原来是[]
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

WSGI_APPLICATION = 'mydjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# 数据库配置好mysql的
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "scrapy_django",
        'USER': 'root',
        'PASSWORD': 'Czcp1000fg,bsqtwmc.',
        'OPTIONS': {
                'charset':'utf8mb4',
                 # "init_command": "SET foreign_key_checks = 0;",
                },     # 都该成这种编码，避免emoji无法存储
        'HOST': "127.0.0.1",  # 要不要都改成远程的地址
        'PORT': '3306'
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

LANGUAGE_CODE = 'zh-hans'  #'en-us'  # 界面语言

USE_TZ = True

TIME_ZONE = 'Asia/Shanghai' #'UTC'  # 时区

USE_I18N = True

USE_L10N = True

# USE_TZ = True

CACHES = {  # redis做缓存
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        "LOCATION": "redis://127.0.0.1:6378/3",  # 本机django的redis缓存路径
        # 'LOCATION':"redis://127.0.0.1:6378/3",
        'OPTIONS':{
            "CLIENT_CLASS":"django_redis.client.DefaultClient",
            'PASSWORD':'Zz123zxc',
        }
    }
}


# Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/

# 这个是配置静态文件的目录的
STATIC_URL = '/static/'
# STATICFILES_DIRS = [    # 这个是为多app而准备的，这样就可以不同的app来这儿注册
    # os.path.join(BASE_DIR, "seo_app", "static"),
    # os.path.join(BASE_DIR, "site", "static"),
    # os.path.join(BASE_DIR, "login", "static"),
# ]
STATICFILES_DIRS = [
      os.path.join(BASE_DIR, "/static/"),
]
# STATICFILES_DIRS = [   # 增加的 todo simpleui
#      os.path.join(BASE_DIR, "static"),
#  ]



# 启用缓存,还没配好东西的时候可以不开这个，实际跑的时候可以开
HTTPCACHE_ENABLED = True  # 这个
#HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'  # 这个
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
