cources=['cse','csd','cs','ece','aiml','AiDs']
print(len(cources))
cources.append('eee')
print(cources)
cources.insert(5,'ds')
print(cources)
cources2=['mec','civil','automob']
cources.insert(0,cources2)
print(cources)
cources.extend(cources2)
print(cources)
# to remove lists item
cources.remove('mec')
print(cources)
cources.pop()# pops the last element form the list 

# to reverse the list 
cources2.reverse()
print(cources2)

# sorting in the alphebatical order
cources2.sort()
num=[1,2,3,5,6,8,4]

print(sorted(num))
num.sort(reverse=True)
print(num)
print(min(num))
print(max(num))
print(sum(num))
# we ccan get the index nos by enterring thelist item 
print(num.index(8))
print(cources.index('ece'))
# aso we can check if the item exixt in the list or not 
print("mec" in cources)#if no returns False 


#for index,cources in enumerate(cources):
   # print(index,cources)

for index,cources in enumerate(cources, start=1):
    print(index,cources)


# to get in csv format 
cources_csv=','.join(cources2)
print(cources_csv) 

# split function 
split_cource=cources_csv.split(' ')
print(split_cource)

###tuples cannot be modified. immutable collection of elements.
#They are defined using parentheses () and can store mixed data types.Allows duplicates.

# Basic tuple
tup1 = ("apple", "banana", "cherry")

# Mixed data types
tup2 = (5, "Welcome", 7.5, True)

# Empty tuple
tup3 = ()

# Single-element tuple (note the comma!)
tup4 = ("apple",)

# Using tuple() constructor
tup5 = tuple([1, 2, 3, 4])

# for rpetation 
tup5=('hi')
print(tup5*3)

tup1 = (5)
print(type(tup1))   # <class 'int'>   ❌ Not a tuple

tup2 = (5,)
print(type(tup2))   # <class 'tuple'> ✅ Correct



# packing and un packing 
tup = ("CSE", "ECE", "AIML")
(branch1, branch2, branch3) = tup
print(branch1)  # CSE




# sets 
# Basic set
s1 = {1, 2, 3, 4}

# Mixed data types
s2 = {"apple", 42, (1,2)}

# Empty set (must use set(), not {})
s3 = set()   # {} creates a dictionary



# common  operations 
s = {1, 2, 3}

# Add elements
s.add(4)          # {1,2,3,4}

# Remove elements
s.remove(2)       # {1,3,4}
s.discard(5)      # no error if element not found

# Membership test
print(3 in s)     # True

# Length
print(len(s))     # 3



# set algebra 

a = {1,2,3,4}
b = {3,4,5,6}

print(a.union(b))        # {1,2,3,4,5,6}
print(a.intersection(b)) # {3,4}
print(a.difference(b))   # {1,2}
print(a.symmetric_difference(b)) # {1,2,5,6}

nums = [1,2,2,3,4,4,5]
unique = set(nums)
print(unique)   # {1,2,3,4,5}

