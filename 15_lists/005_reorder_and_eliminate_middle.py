def reorder_and_eliminate_middle(words):
    if not words or len(words) <= 2:
        return []
    
    sorted_words = sorted(words, key = len, reverse = True)
    middle = len(sorted_words) // 2
    if len(sorted_words) % 2 == 0:
        del sorted_words[middle-1:middle+1]
    else:
        del sorted_words[middle]
    return sorted_words

print(reorder_and_eliminate_middle(["apple", "banana", "kiwi", "grapes", "mango"]))  
# Output: ["banana", "grapes", "mango", "kiwi"]
