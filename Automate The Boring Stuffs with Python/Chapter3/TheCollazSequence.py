
def collatz(number):
    if number %2 == 0:
        return number //2
    else:
        return number*3 +1

print('Enter the number')
while True :
    try:
        num = int(input())
        result = collatz(num)
        print(result)
        if result==1:
            break
    except ValueError:
        print('Please enter the number')

    

