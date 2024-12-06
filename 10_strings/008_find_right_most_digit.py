def find_right_most_digit(text):
    reversed_text = reversed(text)

    for ch in reversed_text:
        if ch.isdigit():
            return int(ch)
    return -1

print(find_right_most_digit('The value is 42'))  # Output: 2
print(find_right_most_digit('No digits here'))  # Output: -1