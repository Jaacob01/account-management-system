"""
Django settings for AMS_Django project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import datetime
import mimetypes
import os
from pathlib import Path

import pymysql as pymysql

from .secret import LOCAL as DB

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fqk$j=s1&0njz0qtdy@wa%a=1)y3u2v75@xx=q0xnsm+&gt%kp'

# SECURITY WARNING: don't run with debug turned on in production!
from . import _DEBUG

DEBUG = _DEBUG

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AMS',
    'static',
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

"""解决使用内网穿透用https登录时响应CSRF验证失败. 请求被中断.（403）"""
CSRF_TRUSTED_ORIGINS = ['https://83k0973l46.yicp.fun']

ROOT_URLCONF = 'AMS_Django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'AMS_Django.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB.MYSQL_DATABASE_NAME,
        'USER': DB.MYSQL_USERNAME,
        'PASSWORD': DB.MYSQL_PASSWORD,
        'PORT': DB.MYSQL_PORT,
        'HOST': DB.MYSQL_HOST
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = False

DATETIME_FORMAT = 'Y/m/d H:i:s'

DATE_FORMAT = 'Y/m/d'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, os.path.join('static'))
]
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

mimetypes.add_type('text/css', '.css')
mimetypes.add_type('text/css', '.min.css')
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/html', '.html')

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "AMS.pagination.StandardPagination",
    "PAGE_SIZE": 10
}

JWT_EXPIRED_DELTA = datetime.timedelta(hours=1)


# SIMPLEUI 配置
SIMPLEUI_STATIC_OFFLINE = True
SIMPLEUI_LOGO = '/static/img/logo.png'
# 隐藏右侧SimpleUI广告链接和使用分析
SIMPLEUI_HOME_INFO = False
SIMPLEUI_ANALYSIS = False
# 隐藏首页的快捷操作和最近动作
SIMPLEUI_HOME_QUICK = True
SIMPLEUI_HOME_ACTION = True
# 默认主题
SIMPLEUI_DEFAULT_THEME = 'OrangeLavender.css'
SIMPLEUI_DEFAULT_ICON = False
SIMPLEUI_HOME_TITLE = 'VaultKey'

# 自定义菜单
SIMPLEUI_CONFIG = {
    'system_keep': False,
    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时刷新展示菜单内容。
    # 一般建议关闭。
    'dynamic': False,
    # 用于菜单排序和过滤, 不填此字段为默认排序和全部显示。 空列表[] 为全部不显示.
    'menu_display': ['账号管理🔑', '高度隐私❗', '权限认证❗'],
    'menus': [
        {
            'app': 'auth',
            'name': '权限认证❗',
            'icon': 'fas fa-users-cog',
            'codename': 'auth',
            'models': [
                {
                    'name': '用户列表',
                    'icon': 'fa fa-user',
                    'url': 'auth/user/',
                    'codename': 'auth.userList',
                },
                {
                    'name': '用户组',
                    'icon': 'fa fa-th-list',
                    'url': 'auth/group/'
                }
            ]
        },
        {
            'app': 'AMS',
            'name': '高度隐私❗',
            'icon': 'fas fa-building',
            'models': [
                {
                    'name': '个体/组织管理',
                    'icon': '',
                    'url': 'AMS/human/'
                },
                {
                    'name': '手机号管理',
                    'icon': '',
                    'url': 'AMS/tel/'
                },
                {
                    'name': '银行卡管理',
                    'icon': '',
                    'url': 'AMS/bankcard/'
                }
            ]
        },
        {
            'app': 'AMS',
            'name': '账号管理🔑',
            'icon': 'fas fa-building',
            'models': [
                {
                    'name': '所有微信',
                    'icon': '',
                    'url': 'AMS/wechat/'
                },
                {
                    'name': '所有通用账号',
                    'icon': '',
                    'url': 'AMS/account/'
                },
                {
                    'name': '所有电子邮箱',
                    'icon': '',
                    'url': 'AMS/email/'
                },
                {
                    'name': '所有项目管理',
                    'icon': '',
                    'url': 'AMS/projectmodels/'
                },
                {
                    'name': '所有服务器',
                    'icon': '',
                    'url': 'AMS/server/'
                },
                {
                    'name': '所有服务器账号',
                    'icon': '',
                    'url': 'AMS/serveruser/'
                },
                {
                    'name': '所有数据服务',
                    'icon': '',
                    'url': 'AMS/dbservice/'
                },
                {
                    'name': '所有数据库用户',
                    'icon': '',
                    'url': 'AMS/dbserviceuser/'
                },
                {
                    'name': '所有宝塔',
                    'icon': '',
                    'url': 'AMS/bt/'
                },
                {
                    'name': '所有WIFI管理',
                    'icon': '',
                    'url': 'AMS/wifi/'
                },
                {
                    'name': 'ElasticSearches',
                    'icon': '',
                    'url': 'AMS/elasticsearch/'
                }
            ]
        }
    ]
}
