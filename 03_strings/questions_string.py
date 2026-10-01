#str var text with your full text
# print first character

# text = "yogesh"
# print(text[0])
# print(text[-1])
# print(text[0:6])
# print(text[::-1])
# print(len(text))

# concatebate string hello and world w space in them
# str1 = "hello"
# str2 = "world"
# print(str1 + str2)
# print(str1,str2)


# string slicing

# "Python Programming"
# print first and last 6 letter

# text = "python Programming"
# print(text[0:6])
# print(text[:-7:-1])
# print(text[::-1])
# print(text[-6:])
# print(text[0::2])
# print(text[::-1])

# take the string " i love p programming "
# 1remove xtra space and change to title case and count no of times o

text = " i love p programming "
print(text.strip())
print(text.title())
print(text.lower())
print(text.upper())


print(text.count("o"))

text1 = "123abc"
print(text1.isalnum())

# string formatting and fstring
# fstring answer
name = "lucky"
age = 20
print (f"my name is {name} and my age is {age}")

print()
# by string format
name = "lucky"
age = 20
print ("my name is {} and my age is {}".format(name,age))
print()
print()
# Given Sentence
# "Coding in Python is fun' , replace "fun" with
# "awesome" and print it.
sentence = "Coding in Python is fun"
new = sentence.replace("fun","awesome")
print(new)
print(sentence.replace("fun","awesome"))
index = sentence.index("Python")
print(index)
print(sentence.index("Python"))
up = sentence.upper()
print(up)


# count vowels in string
for char in sentence:
    print(char)
    