a=[]
n  =int(input("enter the no. of elements :- "))

for i in range(n):
    b = input("enter the word:- ")
    a.append(b)

print(a)
word = input ("enter the word you want to count:- ")
count = 0
for i in range (len(a)):
    if a[i]== word :
        count +=1
    
print (f"the your word is occured :-{count}")