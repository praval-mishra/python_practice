class Employee:
    rais_amt=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first+''+last+'@email.com'
        self.pay=pay

    def FullName(self):
        return f'{self.first} {self.last}'
    def Apply_raise (self):
        pay=int(self.payself.raise_amt)
        
class Developers(Employee):
    pass
emp1=Developers('raghu','kumar',600000)
emp2=Developers('ganesh','kumar',900000)
print(emp1.FullName())