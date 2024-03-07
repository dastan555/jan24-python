def checkEven(num):
    if num % 2==0:
        return "this is even"
    else:
        return "this is odd"

even = 7
print(checkEven(even))

def numbers(lst):
    return lst[::2]                       #string slicing 
lst = [2, 4, 5, 6, 8, 9, 10, 11]           
num = numbers(lst)
print(num)

def oddlist(par):
    odd_list =[]
    for i in par:
        if i % 2 == 1:
            odd_list.append(i)
    return odd_list 

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(oddlist(lst))


def checker (lst, char):
    word_lst =[]
    for word in lst:
        if char in word:
            word_lst.append(word)
    return word_lst

print(checker(['banana', 'apple', 'cherry' ], "a")) 
 

def add(inp1, inp2):
    return inp1 + inp2
inp1 = 20
inp2 = 30
print (add(inp1, inp2)) 

def check(word, char):
    return word, char 
var = "hello"
character = "e"
print (check(var, character))

def check(word, char):
    if char in word:
        return "inside"
    else:
        return "outside"
print(check("salam", "gg"))
print(check("salam", "a"))

