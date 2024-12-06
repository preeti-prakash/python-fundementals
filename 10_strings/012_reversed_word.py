def reverse_word(word):
    reverse_word = ''
    for ch in word:
        reverse_word = ch + reverse_word
    return reverse_word
print(reverse_word("Python"))  # Output: "nohtyP"
