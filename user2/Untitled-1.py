#import math
#from Missing.user1.models import Reports as u

from django.conf import settings

settings.configure(DEBUG=True)
import sys



sys.path.insert(1, '/path/to/Missing/user1/models.py')

import models.Reports as u

query=u.object.all()

print(query)

x=math.floor(5454.545)
print(x)

def fun():
    print('hello world')
    
fun()