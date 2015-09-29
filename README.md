django_mysqlpool
django 数据库长链接支持

(1) download packages

(2) make build

(3) easyinstall dist/codoonmysqlpool-1.0.0-py2.7.egg

(4) modify django settings
    
    'default': {
        'ENGINE': 'codoonmysqlpool.backends.mysqlpool', 
        'NAME': 'www', 
        'USER': dbuser, 
        'PASSWORD': dbpassword, 
        'HOST': dbhost, 
        'PORT': '3306',
        'OPTIONS': {'charset':'utf8mb4'},
    },

