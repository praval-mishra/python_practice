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
    raise_amt=1.10
    def __init__(self, first, last, pay,progLang):
        super().__init__(first, last, pay)
        self.progLang=progLang
        
emp1=Developers('raghu','kumar',600000,'python')
emp2=Developers('ganesh','kumar',900000,'Java')
print(emp1.FullName())
#The help() method is a built-in Python function
#  used to access documentation for modules, classes,
#  methods, and variables directly from your terminal
#  or script. It is like having a built-in manual for
#  the entire Python language.
# print(help(Developers))
print(emp2.progLang)

class manager(Employee):
    pass
