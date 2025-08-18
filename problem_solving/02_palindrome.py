def check_palindrome(word):
    # reversed_word = ""
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False
    # for ch in word:
    #     reversed_word = ch + reversed_word
    # if word == reversed_word:
    #     return True
    # else:
    #     return False


print(check_palindrome("madam"))
print(check_palindrome("hello"))
