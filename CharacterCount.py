import pprint
message = 'It was a bright cold day at April, and the clocks were striking thirteen'
count = {} #count dictionary start off with empty, it doesn't have any keys in it.

for character in message.upper():
    #and have to make sure we start count as zero.
    #.upper for count uppercase and lowercase
    count.setdefault(character, 0) #hey, if you don't have an i for key, go ahead and use 0 value
    count[character] = count[character] + 1

rjtext = pprint.pformat(count)
print(rjtext)

 
