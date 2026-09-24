##Problem 1 — Swap Two Numbers Without Using a Temporary Variable
# a=10
# b=20
# print('before swap',a,b)
# a,b=b,a
# print("after swap",a,b)

#Problem 2 — Even or Odd
# x=int(input("please enter the no :"))
# if x%2==0:
#     print(x,"is even number ")
# else :
#     print(x,"is not a even number")

#Problem 3 — Largest of Three Numbers
a,b,c=[int(x) for x in (input("enter the three no.s")).split()]
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c :
    print(b)
else :
    print(c)