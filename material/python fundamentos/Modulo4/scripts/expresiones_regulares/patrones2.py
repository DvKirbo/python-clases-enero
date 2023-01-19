import re

password = "el texto password1234 password15 password1 password145 password178923"


regex = r'password[0-9]{2,4}'

print(re.findall(regex, password))