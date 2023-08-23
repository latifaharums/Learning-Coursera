#Requirement
#Func only supports the letter: a,b,c,d
#a = 1, b=2, c=3, d=4

#Create function if elif else
def letter_translator(letter):
    if letter == "a":
        return 1
    elif letter == "b":
        return  2
    elif letter == "c":
        return  3
    elif letter == "d":
        return  4
    else:
        return  "unknown"

#Print value
print(letter_translator("a")) # Should print 1
print(letter_translator("b")) # Should print 2
print(letter_translator("c")) # Should print 3
print(letter_translator("d")) # Should print 4
print(letter_translator("e")) # Should print unknown
print(letter_translator("A")) # Should print unknown
print(letter_translator("")) # Should print unknown