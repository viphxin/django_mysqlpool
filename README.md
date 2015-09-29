django_mysqlpool
django 数据库长链接支持

(1) download packages
(2) make build
(3) easyinstall dist/codoonmysqlpool-1.0.0-py2.7.egg
(4) modify django settings
	'default': {
		'ENGINE': 'codoonmysqlpool.backends.mysqlpool', 
		'NAME': 'www', # Or path to database file if using sqlite3.
		'USER': dbuser, # Not used with sqlite3.
		'PASSWORD': dbpassword, # Not used with sqlite3.
		'HOST': dbhost, # Set to empty string for localhost. Not used with sqlite3.
		'PORT': '3306', # Set to empty string for default. Not used with sqlite3.
		'OPTIONS': {'charset':'utf8mb4'},
	},

