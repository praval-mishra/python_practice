#understanding simple methods 
name='Albert das'
print(name)
print(len(name))#10
print(name[5])#t
print(name[:8])#Albert d
#need to learn more about slicing 
print(name.upper())
print(name.count('das'))#1 Also remember you should give the steing inside '' as a parameter i count method 
print(name.count('a'))#1 its case sensitive 
#replace method 
new_name=name.replace('das','dan')
print(new_name)#Albert dan


phone = "(555) 123-4567"
clean_phone = phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
print(clean_phone) 
# Output: "5551234567"
#Method Chaining: As shown in the phone number example,
#  you can chain multiple .replace() calls together
#  because each call returns a new string.


