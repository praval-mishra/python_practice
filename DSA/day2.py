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

########################################
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
# n = input("Enter the string: ")
# vcnt = 0
# Ccnt = 0

# for i in n.lower():
#     if i in "aeiou":
#         vcnt += 1
#     elif i.isalpha(): 
#         Ccnt += 1

# print("Vowels:", vcnt)
# print("Consonants:", Ccnt)
##############################
#method 2

# n = input("Enter the string: ")
# vcnt = 0
# Ccnt = 0

# for ch in n:
#     code = ord(ch)
#     # Check if it's a letter
#     if (65 <= code <= 90) or (97 <= code <= 122):  # A-Z or a-z
#         # Check vowels by ASCII
#         if code in (65,69,73,79,85,97,101,105,111,117):  # AEIOUaeiou
#             vcnt += 1
#         else:
#             Ccnt += 1
#     # Ignore digits, spaces, punctuation

# print("Vowels:", vcnt)
# print("Consonants:", Ccnt)


#-------------------------------------------------------------------------
#Problem 21 — Character Frequency
# n = input("Enter the string: ")
# counts = {}

# for ch in n:
#     if ch==" ":
#         continue
#     if ch in counts:        
#         counts[ch] += 1     
#     else:                   
#         counts[ch] = 1      

# print(counts)
#----------------------------------------------------------
#Problem 22 — Remove Duplicate Characters
# n = input("Enter the string: ")
# seen = []
# result=''
# for ch in n:
#     if ch==" ":
#         continue
#     if ch in seen:        
#         continue   
#     else:                   
#         seen.append(ch) 

# result="".join(seen)
# print(result)####################################