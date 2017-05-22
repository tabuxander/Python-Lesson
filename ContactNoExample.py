def isPhoneNumber(text) : #415-555-0000
    if len(text) != 12:
        return False #not a phone number size
    for i in range (0, 3):
        if not text[i].isdecimal():
            return False #no area code
    if text[3] != '-': #to check it is not a dash
        return False # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # no first three digits
    if text[7] != '-':
        return False #missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False # missing the last 4 digits
    return True

message = 'Call me 415-555-4567 tomorrow, or at 314-455-9034'
foundNumber = False
for i in range(len(message)):
    chunk = message[ i:i+12 ]
    if isPhoneNumber(chunk):
        print('Phone number found '+ chunk)
        foundNumber = True
if not foundNumber :
    print('Couldnt found phone number.')


