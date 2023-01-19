import re



texto = "The winners are: User9, UserN, User8,UserÑ,User@,User!"

expresion = r'User\w'
regex = r'User[!@0-9]'

password = "el texto password1234"

print(re.findall(expresion, texto))
print(re.findall(regex, texto))