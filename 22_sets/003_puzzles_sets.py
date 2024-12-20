
s1 = {1, 2, 3}
s2 = {3, 4, 5}
result = s1.union(s2) # Same as s1 | s2
print(result) 
#Output: {1,2,3,4,5}

list_of_sets_1 = [set([1, 2]), set([3, 4]), set([5, 6])]
list_of_sets_2 = [set([5, 6]), set([7, 8])]
 
union_result = set.union(*list_of_sets_1, *list_of_sets_2)
#similar functions exist for union and difference
print(union_result)
# Output: {1,2,3,4,5,6,7,8}

s1 = {1, 2, 3}
s2 = {3, 4, 5}
result = s1.difference(s2) # Same as s1 - s2
print(result)
# Output: {1,2}

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = {x**2 for x in numbers if x % 2 == 0}
print(result)
# Output: {64, 100, 4, 36, 16}

num = 5
result = {x for x in range(num, 101, num)}
print(result)
# Output: {5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100}
 
 
my_list = [1, 2, 3, 2, 1, 4, 5, 3]
result = set(my_list)
print(result)
# Output: {1,2,3,4,5}
 
string_1 = "hello"
string_2 = "world"
 
result = set(string_1) | set(string_2)
print(result)
# Output:  {'e', 'l', 'h', 'd', 'r', 'w', 'o'}

list_of_sets = [{1, 2, 3}, {3, 4, 5}, {3,5, 6, 7}]
result = set.intersection(*list_of_sets)
print(result)
#  Output: {3}