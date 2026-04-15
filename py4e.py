# Chapters Covered 

# Chapter 4: function
# Chapter 5: Loop and Iteration
            #Loop Idioms
            #more loopp pattern

    # check on how to get the smallest value within a range on numbers
    # parsing and extracting

# Chapter 6: Strings : 02:59:00
            # looping through strings
            # string operation: slicing
            # Using in as a logical operator
            # string comparison
            # String Library ==> string methods
# Chapter 7: Reading Files : 03:27:00
            # http://www.py4e.com/code3/mbox-short.txt
            # open a file ==> open() function
            # newline character (\n)
            # Reading files: 03:35:28
            # Reading the whole file
            # Searching through a file
# Chapter 8: Data Structures
            # List ==> list are mutable
            # using len(), range()
            # loop operations
            # list methods ==> building a list from scratch,
            # strings vs list ==> using split to convert strings to list
            # The double split pattern ==> splitting an item twice
# Chapter 9: Dictionaries : 04:29:09
            # comparing lists and dictionaries  
            # counting
            # counting words in text
            # using get() method
# Chapter 10: Tuples : 05:23:00
            # sorting list of tuples 
# Chapter 11: Regular Expressions
# Chapter 12: Networked Programs 06:23:00
            # socket programming
            # web browsing in python





x = 90

# if x < 2 :
#     print('Below 2')
# elif x >= 2 :
#     print('Two or more')
# else :
#     print('Something else') #this will never print, regardless of the value of x

# if x < 2:
#     print('Below 2')
# elif x < 20 :
#     print('Below 20')
# elif x < 10 :
#     print('Below 10') #It will never run this
# else :
#     print('Something else')

# astr = 'Hello Bob'
# try:
#     istr = int(astr)
# except:
#     istr = -1

# print('First', istr)

# astr = '123'
# try:
#     istr = int(astr)
# except:
#     istr = -1

# print('Second', istr)

# rawstr = input('Enter a number: ')
# try:
#     ival = int(rawstr)
# except:
#     ival = -1

# if ival > 0 :
#     print('Nice work')
# else:
#     print('Not a number')
#     print(rawstr) 
    #****
    # Quick question, 
    # how do i loop this to ask the user to input new number
    # how do i strip spaces inbetween numbers


# try:
#     check = max ("Hellow", "cope", "padd", 89)
# except:
#     check = max (7,8,65)
# print(check)

# while x > 20:
#     print("are you there?")
#     print("yes sir")
#     x = x - 15
# print("no days off")

# for i in [9,7,6,5,4,3,2,1] :
#     print(i)
# print("Voila!")


# Checking for the largest Number
# numbers = [19.233, 19.2333, 19.23333]

# largest_num = 0

# for number in numbers :
#     if number > largest_num:
#         largest_num = number

# print(f"the largest number is {largest_num}")

# counting in a loop
# count = 0
# print('Before', count)
# for thing in (9, 41, 12, 3, 74, 15) :
#     count = count + 1
#     print(count, thing)
# print("After", count)

# find the smallest number
# numbers = [2.33,3,6,2.333,8,9]
# check = numbers[0]
# for number in numbers :
#    if number < check:
#         check = number
# print(type(check))


# string comparison
# word ='banana'
# if word == 'banana' :
#     print('All right, banana.')

# print(dir(str))

# Use open()
# handle = open(filename, mode)
# fhand = open('generated_text.txt', 'r')
# print(fhand)

# File Handle as a sequence ==> Read texts in a file ==> count number of lines
# xfile = open('generated_text.txt')
# count = 0
# for cheese in xfile:
#     print(f'{count} ==> {cheese}')
#     count += 1
# print(count)

# # Read the whole file
# fhand =  ('generated_text.txt')
# read = fhand.read()
# print(len(read))
# print(read[:])

# search through a file
# fhand = open('generated_text.txt')
# for line in fhand:
#     # line = line.rstrip()
#     if line.startswith('Py'):
#         continue
#     print(line)

# Currently at 03:49:02

# use split()
# t = "i am not my circumstances"
# new = t.split()
# print(new)

# Currently at 04:16:58
# Currently at 04:24:52

# han = open('randomtext.txt')

# for line in han:
#     line = line.rstrip()
#     print('Line:',line)
#     wds = line.split()
#     print('Words:',wds)
#     if wds[0] != 'We' :
#         print('Ignore')
#         continue
#     print(wds[2])


# Dictionaries
# diced = {}
# diced["one"] = 1
# diced["two"] = 2
# diced["three"] = 3
# # diced[input("your words")] = input("your response")
# print(len(diced))
# print(diced)

# diced["three"] = diced["two"]*50
# print(diced)


# counts = {}
# text = '''Writing programs or programming is a very creative and rewarding activity.
# You can write programs for many reasons ranging from making your living to solving a difficult data analysis problem to having fun to helping someone else solve a problem.
# This book assumes that everyone needs to know how to program and that once you know how to program, you will figure out what you want to do with your newfound skills.
# We are surrounded in our daily lives with computers ranging from laptops to cell phones.
# We can think of these computers as our personal assistants who can take care of many things on our behalf.
# The hardware in our current-day computers is essentially built to continuously ask us the question: What would you like me to do next?
# Programmers add an operating system and a set of applications to the hardware and we end up with a Personal Digital Assistant that is quite helpful and capable of helping many different things.'''

# text_to_list = text.split()


# for word in text_to_list:
#     if word not in counts:
#         counts[word] = 1
#     else:
#         counts[word] += 1

# print(len(counts))
# fig = 0
# for word, count in counts.items():
#     print(f"{word} ==> {count}")
#     fig += 1
# print(f"Total number of unique words is {fig}")

# counts = {}
# names = ['carl', 'alan', 'cart', 'alank', 'carl', 'alan', 'alank']
# for name in names:
#     counts[name] = counts.get(name,0) + 1
# print(counts)


# name = input('Enter file: ')
# handle = open(name)

# counts = {}
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[words] = counts.get(word, 0) + 1

# bigcount = None
# bigword = None
# for word,count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count

# print(bigword, bigcount)

# 04:53:58
# di={"one": 1, "two":2}
# for a in di:
#     print(a)
# # print(di.get("one", 3))

# Stopped at 05:23:07

# Tuples

# tu = (1, 2, 3, 4)
# tu[3] = 56
# print(tu[2])


# d = dict()
# d['csev'] = 2
# d['cwen'] = 4

# for (k,v) in d.items():
#     print(k, v)

# tups = d.items()
# print(tups)


# Currently at 06:21:00 

# web browsing in python
# Stopped at 06:43:35

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) # opened a connection to a server
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # asked for a file, and the server sent back information about the file
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
