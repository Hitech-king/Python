# Hitesh
def union_logical_operator(list1, list2):
    return list(set(list1) | set(list2))  

list1 = [1, 2, 3, 4]
list2 = [3, 4, 1,5, 6]

result = union_logical_operator(list1, list2)
print("Union using logical operator:", result)
