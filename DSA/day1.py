##Problem 1 — Swap Two Numbers Without Using a Temporary Variable
# a=10
# b=20
# print('before swap',a,b)
# a,b=b,a
# print("after swap",a,b)
#--------------------------------------------------------------------------
#Problem 2 — Even or Odd
# x=int(input("please enter the no :"))
# if x%2==0:
#     print(x,"is even number ")
# else :
#     print(x,"is not a even number")
#------------------------------------------------
#Problem 3 — Largest of Three Numbers
# a,b,c=[int(x) for x in (input("enter the three no.s")).split()]
# if a>=b and a>=c:
#     print(a)
# elif b>=a and b>=c :
#     print(b)5
# else :
#     print(c)

#---------------------------------------------------------
#Problem 4 — Leap Year
# year=int(input('enter the year :'))
# if (year%400==0) or (year%4==0 and year%100 !=0):
#     print("it is leap year ")
# else :
#     print("not a leap year")
#-------------------------------------------------------------------
#Problem 5 — Factorial Using a Loop
# n=int(input("enter the number :"))
# fact=1
# for i in range(1,n+1):
#     fact=fact *(i)

# print(fact)

#-----------------------------------------
#Problem 6 — First N Fibonacci Numbers
# n=int(input("enter the number :"))
# a=0
# nxt=0
# b=1
# for i in range(0,n):
#     print(a)
#     nxt=a+b
#     a=b
#     b=nxt
# recursive method 
# #def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)

# # Example: print first 10 Fibonacci numbers
# for i in range(10):
#     print(fib(i), end=" ")


#recursive with memoization efficient 
# from functools import lru_cache

# @lru_cache(maxsize=None)
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)

# # Example: print first 10 Fibonacci numbers
# for i in range(10):
#     print(fib(i), end=" ")

#--------------------------------------------------------------------------



#Problem 7 — Sum of Digits
# n= int(input("enter the digits :"))
# Tsum=0
# while n>0 :
#    digit=n%10
#    Tsum=Tsum+digit
#    n=n//10
# print(Tsum)
#---------------------------------------------------------------



#Problem 8 — Reverse a Number
# n=int(input("enter the no:"))
# rev=0
# while n>0 :
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# print(rev)

#-------------------------------------------------------------------

#Problem 9 — Palindrome Number
# n=int(input("enter the no:"))
# ch=n
# rev=0
# while ch>0:
#   digit=ch%10
#   rev=rev*10+ digit
#   ch=ch//10
# #print(rev)
# if n==rev :
#  print('is a palindrome')
# else:
#   print("not a palindrome ")

#--------------------------------------------------------------------------

#Problem 10 — Armstrong Number
# n=int(input("enter the no:"))
# temp=n
# count=0
# while temp>0:
#   count+=1
#   temp//=10
    
# amno=0
# temp=n
# while temp>0:
#   digit=temp%10
#   amno=amno +digit**count
#   temp=temp//10
# if n==amno:
#   print("It is armstrong no.")
# else :
#   print ("not an armstrong no.")

  