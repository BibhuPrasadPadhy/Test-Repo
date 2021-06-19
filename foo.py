def sum(a,b):
    return a+b

a,b = map(int,input("Enter Two Numbers separated by space: ").split(" "))
print(f'Entered Numbers are a={a} and b={b}')
print(f'Result of sum = {sum(a,b)}')