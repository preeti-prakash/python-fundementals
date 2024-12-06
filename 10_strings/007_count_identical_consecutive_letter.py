def has_consecutive_identical_characters(text):
    for i in range(0, len(text) - 2):
        if text[i] == text[i+1]:
            return True
    return False


print(has_consecutive_identical_characters('Hello World'))  # Output: True
print(has_consecutive_identical_characters('I love Switzerland'))  # Output: False