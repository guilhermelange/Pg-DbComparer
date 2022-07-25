class Database(object):
    _host = ""
    _port = 0
    _db = ""
    _user = ""
    _password = ""

    def __init__(self, host, port, db, user, password):
        self._host = host
        self._port = port
        self._db = db
        self._user = user
        self._password = password

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def db(self):
        return self._db

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password

    @host.setter
    def host(self, host):
        self._host = host
    
    @port.setter
    def port(self, port):
        self._port = port

    @db.setter
    def db(self, db):
        self._db = db

    @user.setter
    def user(self, user):
        self._user = user

    @password.setter
    def password(self, password):
        self._password = password
