letter = str(input("Enter One Letter ")).lower()

#vowel = ["a", "e", "i", "o", "u"]
#consonant = ["b", "c"]

#if(letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
#    print("Vowel")
#
#elif letter in consonant:
#
#    print("Consonant")
#
#else:
#    print("invalid input")
#
#
#
#

lower_case = letter.lower()
if(lower_case >= 'a' and lower_case <= 'z'):
    if(letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
        print("Vowel")
    else:
        print("Consonant")

else:
    print("invalid input")





