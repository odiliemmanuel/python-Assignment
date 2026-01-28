def reverse_words_in_a_particular_word(word):
    reverse = ""
    for character in word:
        reverse = character + reverse
    return reverse 
 
print(reverse_words_in_a_particular_word("odili"))
    
