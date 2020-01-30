class MyException(Exception):
    def __init__(self,arg):
        self.msg=arg
def check(dict):
    for k,v in dict.items():
        print('name={} balance={}'.format(k,v))
        if (v<2000):
            raise MyException('balance is less in account of '+k)
bank={'madhu':2000,'harsha':1000,'bharath':1200}
try:
    check(bank)
except MyException as E:
    print(E)
