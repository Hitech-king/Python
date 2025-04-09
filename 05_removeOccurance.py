# code for removing the "i"th occurance element from the list 
a=[]
n  =int(input("enter the no. of elements :- "))

for i in range(n):
    b = input("enter the word:- ")
    a.append(b)

print(a)

target = input("give the word you want to remove :-")
occurance = int(input("enter the occurance no. of the element :- "))
count = 0
for i in range(len(a)):
    if a[i] == target:
        count += 1
        if count == occurance:
            a.pop(i)
            break

print(a)
