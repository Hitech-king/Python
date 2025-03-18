print("hi")

a = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    b = input("Enter the word: ")
    a.append(b)

print(a)

target = input("Give the word you want to remove: ")
occurrence = int(input("Enter the occurrence number of the element: "))

count = 0
for i in range(len(a)):  
    if a[i] == target:  # Check the element, not index
        count += 1
        if count == occurrence:
            a.pop(i)
            break  # Stop after removing the desired occurrence

print(a)
