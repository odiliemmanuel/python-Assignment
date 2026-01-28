def counting_how_many_vowels_are_in_a_word(word):
    count = 0
    vowels = 'aeiou'
    vowels_in_word= ""
    word = word.lower()
    for character in word:
        if character in vowels:
            if character not in vowels_in_word:
                vowels_in_word += character
                count += 1
    return count

print(counting_how_many_vowels_are_in_a_word("Eoaswnd,iieeoouuwwo"))
