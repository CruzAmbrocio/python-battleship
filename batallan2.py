from random import randint
x = input('Ingrese un numero por favor\n')
while x < 1000:
    if x % 2 is 0:
        x = x + 3
        continue
    elif x % 3 is 0:
        x = x + 1
    else:
        break
    x = x + randint(0, 10)
print 'El numero final es: ' + str(x)