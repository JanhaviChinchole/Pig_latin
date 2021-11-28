def pig_latin(word):
    first_letter=word[0]
    if first_letter in "aeiouAEIOU":
        pig_word=word+"ay"
    else:
        pig_word=word[1:]+first_letter+"ay"
    return pig_word
print(pig_latin("umesh"))
print(pig_latin("janhavi"))
print(pig_latin("apple"))
