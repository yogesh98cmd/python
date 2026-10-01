'''def star(a,b):
    return a*b
star(4,5) #agar yhi se run karoge toh error dega kyuki abhi value store hai for printing ke liye it goes
result = star(4,5)
print(result)
print(star(5,5))
'''

'''square = lambda x :x*x
print(square(4))

def sq(x,y):
    return(x*x,y*y)
print(sq(5,7))'''

# waf that takes string and counts vowels and consonents seprately
'''
def word(userInput):
    
    vowels="aeiouaeiou"
     '''


'''cities = ["del","goa","mum","pune","noida"]
hero = ["thor","spider","monkey","hulk"]
def list_len(list):
    print(len(list))
list_len(cities)
list_len(hero)
'''
 
#  print the elements of string in single line
'''cities = ["del","goa","mum","pune","noida"]
hero = ["thor","spider","monkey","hulk"]


def ltgh(list):
    print(len(list))
def same(list):
    for item in list:
      print(item, end="")
      '''

cities = ["del", "goa", "mum", "pune", "noida"]
hero = ["thor", "spider", "monkey", "hulk"]

def list_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item, end=" ")

list_len(cities)
list_len(hero)

print_list(cities)
print()
print_list(hero)