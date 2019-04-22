import re
def strongpassdetection(password):
    lowercase = re.compile(r'[a-z]')
    uppercase = re.compile(r'[A-Z]')
    number = re.compile(r'[0-9]')
    
    if lowercase.search(password)!=None and uppercase.search(password)!= None and number.search(password)!= None and len(password)>=8:
        print('pass:'+password+' is Strong password')
    else:
        print('pass:'+password+' is weak password')


strongpass= 'Abcd11S3456'
weakpass ='AAAs1'
strongpassdetection(strongpass)
strongpassdetection(weakpass)
 