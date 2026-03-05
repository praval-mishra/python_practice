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

