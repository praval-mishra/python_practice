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
# print(result)

#-----------------------------------------
# problem 23 Anagram check 
# s1=input("enter the frist string:").lower().replace(' ','')
# s2=input("enter the frist string:").lower().replace(' ','')
# if len(s1)!=len(s2):
#   print("not an anagram")
# else :
#   freq1={}
#   for ch in s1 :
#     freq1[ch]=freq1.get(ch,0)+1
#   freq2={}
#   for ch in s2:
#     freq2[ch]=freq2.get(ch,0)+1



# print(freq1,freq2)
# if freq1==freq2:
#   print("Its an anagram ")
# else : print("Not an anagram ")
#################################
#method 2 
# s1=input("enter the frist string:").lower().replace(' ','')
# s2=input("enter the frist string:").lower().replace(' ','')
# if sorted(s1)==sorted(s2):
#     print("its an anagram")
# else : print("its not an anagram")
#------------------------------------------------------------------


#Problem 24: Capitalize Each Word
# s1=input("enter the frist string:")
# result=[]
# for ch in s1.split():
#    ch=ch[0].upper()+ch[1:] 
#    result.append(ch)
# output=" ".join (result)
# print(output)
#----------------------------------------------------------------------
##Problem 25: Count Words in a Sentence
# s1=input("enter the frist string:")
# count =0
# for ch in s1.split():
#   if ch.isalpha():
#     count+=1
# print(count)  
#-------------------------------------------------------------------
#Problem 26: Most Frequent Character
# s1=input("enter the frist string:")
# count={}
# for ch in s1.lower():
#   if ch==" ":
#     continue 
#   elif ch in count:
#     count[ch]+=1
#   else :
#     count[ch]=1
# print([k for k,v in count.items() if v==max(count.values())])
# print(f"the max count is ",max(count.values()))
#-------------------------------------------------------------------------
#Problem 27: Find the Largest and Smallest Elements in a List
# lst=[]
# for i in range(5):
#   val=int(input("enter the values : "))
#   lst.append(val)
# maxi=lst[0]
# mini=lst[0]

# for i in lst :
#   if i>maxi:
#     maxi=i
#   if i<mini:\
#     mini=i
# print("maximum",maxi)
# print("minimum",mini)
#-------------------------------------------------------------------------
#problem 28 to find the second largest 
