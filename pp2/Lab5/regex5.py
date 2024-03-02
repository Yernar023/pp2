import re
txt=input()
word=re.findall(r'%s', txt)
print(word)