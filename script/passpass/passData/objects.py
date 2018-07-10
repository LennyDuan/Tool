class PassPass:

    def __init__(self, name, account, password, extra):
        self.name = name
        self.account = account
        self.password = password
        if extra:
            self.extra = extra
        else:
            self.extra = 'None'

    def toString(self):
        print('Name: [' + self.name + '] Account: [' + self.account
        + '] Password: [' + self.password + '] Extra: ['
        + self.extra + ']')
