import re

helloRegex = re.compile(r'Batman|Tina Fey')

mo1 = helloRegex.search('Batman and Tina Fey.')

print('Test 1 ' + mo1.group())

mo2 = helloRegex.search('Tina Fey and Batman.')

print('Test 2 ' + mo2.group())

