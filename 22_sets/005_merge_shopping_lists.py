def merge_shopping_lists(*lists):
    
    if not lists:
        return set()
    
    result = set.union(*lists)
    
    return result
    
list1 = {"apples", "bananas", "cherries"}
list2 = {"bananas", "dates", "eggs"}
list3 = {"cherries", "dates", "figs"}
 
print(merge_shopping_lists(list1, list2, list3))
# Output: {"apples", "bananas", "cherries", "dates", "eggs", "figs"}

list4 = {"bread", "milk"}
list5 = {"milk", "eggs", "juice"}
print(merge_shopping_lists(list4, list5))
# Output: {"bread", "milk", "eggs", "juice"}
