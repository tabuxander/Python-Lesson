def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('You try to divide the zero, beb')
            

print(div42by(2))
print(div42by(23))
print(div42by(0))
print(div42by(1))
 
