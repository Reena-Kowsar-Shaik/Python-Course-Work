#match
'''
import re  
#pattern = r'code'
#pattern = r'[A-Za-z]'
pattern = r'[0-9]'
text='codegnan'
res = re.match(pattern,text)
print(res.group() if res else "Pattern not found")
'''
#search
'''
import re  
pattern = r'[0-9]'
text='codegnan2026'
res = re.search(pattern,text)
print(res.group() if res else "Pattern not found")
'''
#findall-see all the patterns
'''
import re  

pattern = r'[a-z]' #r'[0-9]'
text='codegnan 2026 python version 3.14'
res = re.findall(pattern,text)
print(res)
'''

#finditer-use for index 
'''
import re
#pattern = r'[0-9]'
pattern = r'[a-z]'
text = 'codegnan 2026 python version 3.14'
res = re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())
'''
#fullmatch-only what we want [exactly match] validation 
'''
import re
pattern = r'[0-9]{10}' #{2} - pattern not found
text = '9876543210'
res = re.fullmatch(pattern,text)
print(res.group() if res else "Pattern not found")
'''
#split-split according to the pattern
'''
import re
pattern = r'[,(#]'
text = 'java,python(html#css)' 
res = re.split(pattern,text)
print(res) 
'''
#sub- used to replace function
'''
import re
pattern = r'[0-9]' 
text = 'python version 3.14, batch-63'
res = re.sub(pattern,'*',text)
print(res)
'''
# dot(.)
'''
import re 
pattern = r'e.t'
text = 'e@t eaat eat eet ett ect Egfjlh hfrtyuij'
res = re.findall(pattern,text)
print(res)
'''
# ^ cap-starting with
'''
import re 
pattern = r'^(91)'
text = '91987654320'
res = re.findall(pattern,text)
print(res)
'''
#$-ending with
'''
import re 
pattern = r'0$'
text = '9198765210'
res = re.findall(pattern,text)
print(res)
'''
# * - 0 or more occurance
'''
import re 
pattern = r'to*'
text = 'to t too tooo tooooooo'
res = re.findall(pattern,text)
print(res)
'''
'''
import re 
pattern = r'ab*'
text = 'ab abbb a abbbbbb abbbbbb'
res = re.findall(pattern,text)
print(res)
'''
# + -> atleast one one occurance
'''
import re 
pattern = r'to+'
text = 'to tdghjy too tooo toooooo'
res = re.findall(pattern,text)
print(res)
'''
# ? --> zero or one occurance
import re 
pattern = r'91|0'
text = '08763'
res = re.findall(pattern,text)
print(res)