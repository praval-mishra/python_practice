# problem 18. Reverse a string
# n=input("enter the string:")
# for i in range(len(n)-1,-1,-1):
#     print(n[i],end="")
#------------------------------------------

#Problem 19 — Palindrome String check 

# n=input("enter the string:")
# rev=''
# for i in range(len(n)-1,-1,-1):
#   rev+=n[i]
# if n==rev:
#   print('palindrome')
# else : print('not a palindorme ')

###############
#method 2 
# n=input("enter the string:")
# left=0
# right=len(n)
# while left<right:
#     if n[left]!=n[right] :
#         print("not a palindrome")
#         break
#     left+=1
#     right-=1
# else :print(n,"is a palindrome ")

#--------------------------------------------------------

#Problem 20 — Count Vowels and Consonants.
n = input("Enter the string: ")
vcnt = 0
Ccnt = 0

for i in n.lower():
    if i in "aeiou":
        vcnt += 1
    elif i.isalpha(): 
        Ccnt += 1

print("Vowels:", vcnt)
print("Consonants:", Ccnt)

