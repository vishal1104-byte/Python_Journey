'''
What is Regex --> Regular Expression 
To use the regular expression firstly we have to import the regular expression using
import re 

A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.

'''

import re 
normal_text = '''
This is some random line that I can add to understand the regex model 
!!!!!!!#$%%%^^^&&&&&&&&&&&&&&&&&****()
We can use any model to start with anything and I am able to understand this all thing in the multiline strings 
'''
sentence = "Start a sentence and then bring it to an end"
pattern = re.compile(r'abc')

matches = pattern.finditer(normal_text)
for match in matches:
    print(match)


