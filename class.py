class employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    def full_name(self):
         return f'{self.first} {self.last}'
        #old method return '{} {}'.format(self.parametrs)
    def email(self):
        return f'{self.first}@email.com'
    

emp1=employee('raghu','kumar',900000)
print(emp1)
print(emp1.full_name())
print(emp1.email())

class employee :
    num_of_employee=0
    raise_amt=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@gmail.com'
        employee.num_of_employee+=1
    def full_name(self):
        return f'{self.first} {self.last}'
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)
emp1=employee('raghu','kumar',90000)
emp2=employee('pia','singh',100000)
print(employee.raise_amt)
# emp1.raise_amt=1.52
print(emp1.raise_amt)
print(emp2.raise_amt)
# # class variable Example 2
class StreamingUser:
    #class variables (shared by all )
    max_resolution="720p"
    monthly_price=10
    user_count=0
    def __init__(self,email):
        self.email=email
        StreamingUser.user_count+=1
    
    def display_info(self):
        return f'user {self.email} is on the {self.max_resolution} plan at {self.monthly_price}/mo'

user1=StreamingUser("ragnu@email.com")
user2=StreamingUser('kumar@email.com')
print(f'total users created :{StreamingUser.user_count}') 
print(user2.email)
#test ! the global change 
StreamingUser.monthly_price=12
print(user1.display_info())
print(user2.display_info())
# Test 2 the vip overrides 
user1.max_resolution='4k'
print('After VIP Upgrade :')
print(user1.display_info())
print(user2.display_info())

# TEST 3: Look under the hood
print("\nUser1's unique data:", user1.__dict__) 
# You will see 'max_resolution' is now in user1's dictionary

@staticmethod
def is_workday(day):
    if day.weekday() == 5 or   day.weekday()==6:
        return False
    return True

# class methods 

