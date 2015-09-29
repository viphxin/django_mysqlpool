# django_mysqlpool
django 数据库长链接支持
(1) download packages
(2) make build
(3) easy_install dist/codoon_mysqlpool-1.0.0-py2.7.egg
(4) modify django settings
    'default': {
            'ENGINE': 'codoon_mysqlpool.backends.mysqlpool', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            # 'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'www', # Or path to database file if using sqlite3.
            'USER': db_user, # Not used with sqlite3.
            'PASSWORD': db_password, # Not used with sqlite3.
            'HOST': db_host, # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '3306', # Set to empty string for default. Not used with sqlite3.
            'OPTIONS': {'charset':'utf8mb4'},
        },
