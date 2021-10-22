class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg
 
 
try:
    raise MyError('rrr')
except MyError as e:
    print('My exception occurred', e.msg)