print('How many cat do you have?')
numCats = input()
try: 
    if int(numCats) >= 4:
        print('That is a lot of cats')
    else:
        print('That is not that many')
except ValueError:
    print('You does not enter number')
kllkjkl

#the problem is that, even if you put zero cat, it's doesn't reflect the feedback.
