import re

phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('My number is 415-555-4242.')

print('Phone number found: '+ mo.group())
# print('Phone number found: '+ mo.group(1))
# print('Phone number found: '+ mo.group(2))
areaCode, mainNumber = mo.groups()

print('Phone number found: '+ areaCode)
print('Phone number found: '+ mainNumber)