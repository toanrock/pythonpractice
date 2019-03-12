

def commalist(alist):
    result = alist[0]
    for element in alist[1:]:
        result += ', '+str(element) 
    return result


spam = ['apples', 'bananas', 'tofu', 'cats',11, 25]
print(spam)
print(commalist(spam))