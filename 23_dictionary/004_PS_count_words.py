def count_words(str):
    word_occurances = {}
    for word in str.split():
        if word in word_occurances:
            word_occurances[word] += 1
        else:
            word_occurances[word] = 1
    return word_occurances
    
    
print(count_words("This is an example.")) 
 
# {'This': 1, 'is': 1, 'an': 1, 'example.': 1}