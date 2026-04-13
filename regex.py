import re

text = "My 32 phone number is 08152583387"
new_text = "Call me on 08152593387 or 07040574820 or just come to block 5"
new_text2 = "My email is alameenabiola3@gmail.com and my old one is abiolaalameen1@gmail.com"
new_text3 = """
Contact John at john@gmail.com or call 08152593387.
You can also reach Amina at amina@yahoo.com or 09087654321.
Office number is 5.
"""
new_text4a = "08031234567 is my phone number"
new_text4b = "my number is 08031234567"

new_text5 = "Reach Emeka at emeka@gmail.com or 08031234567, and Ngozi at ngozi@yahoo.com or 09054321876"

'''
Three functions that is mostly used in regex are:
re.search() # finds a match of anywhere in the string and returns a match object if found, else returns None
re.match() # checks for a match only at the beginning of the string and returns a match object if found, else returns None
re.findall() # returns All matches as a list

# \d - matches any single digit
# \d+ - one ore more digits in a row
# \d{11} - matches exactly 11 digits in a row

\w+   →  one or more word characters (the username part)
@     →  the literal @ symbol
\w+   →  one or more word characters (the domain name)
\.    →  a literal dot (the . in .com)
\w+   →  one or more word characters (com, net, org etc)


These characters have special meaning in regex and need \ to be treated literally:
.  ^  $  *  +  ?  {  }  [  ]  \  |  (  )


Two new special characters: ^ and $
These are called anchors. They don't match characters — they match a position in the text.

^ — means "start of the string" - must appear at the start
$ — means "end of the string" - must appear at the end
'''

# result = re.search(r'\d+', text)
# print(result.group())

# result = re.search(r'\d+', new_text)
# print(result.group())

# result = re.findall(r'\d{11}', new_text) #this matches exactly two digits in a row
# print(result)
 
# result = re.findall(r'\w+@\w+\.\w+', new_text2)
# print(result)


# emails = re.findall(r'\w+@\w+\.\w+', new_text3)
# phones = re.findall(r'\d{11}', new_text3)

# print("Emails:", emails)
# print("Phones:", phones)

# print(re.search(r'^\d{11}', new_text4a)) # matches because the string starts with 11 digits
# print(re.search(r'^\d{11}', new_text4b)) # does not match because the string does not start with 11 digits

# print(re.search(r'\d{11}$', new_text4a)) # does not match because the string does not end with 11 digits
# print(re.search(r'\d{11}$', new_text4b)) # matches because the string ends with 11 digits

# Extracts all emails
result = re.findall(r'\w+@\w+\.\w+', new_text5)
# Extracts all phone numbers
result1 = re.findall(r'\d{11}', new_text5)

print(result)
print(result1)