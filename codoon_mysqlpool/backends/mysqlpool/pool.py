# -*- coding: utf-8 -*-
__author__ = 'huangxin'

import time, MySQLdb

proxies = {}

class _ConnectionWrapper(object):
    def __init__(self,conn):
        self.conn = conn

    def close(self):
        pass

    def __getattr__(self,key):
        return getattr(self.conn, key)

class _DbWrapper():
    def __init__(self,module,max_idle):
        self.connection=None
        self.db=module
        self.max_idle=max_idle
        self.connected=0

    def __getattr__(self, key):
        return getattr(self.db, key)

    def connect(self,*argv,**kwargv):
        if not self.connection or time.time() - self.connected >= self.max_idle:
            try:
                if self.connection:
                    self.connection.close()
            except:
                pass
            self.connection=self.db.connect(*argv,**kwargv)
        self.connected=time.time()
        #add reconnection
        try:
            self.connection.ping()
        except MySQLdb.Error:
            self.connection = self.db.connect(*argv,**kwargv)

        # print id(self.connection)
        return _ConnectionWrapper(self.connection)

def manage(module, keepalive=7*3600):
    try:
        return proxies[module]
    except KeyError:
        return proxies.setdefault(module,_DbWrapper(module,keepalive))