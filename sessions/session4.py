cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']
for city in cities:
    print("Current city: ", city)                       # iterating list


turple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0]) 
print(my_tuple[-1]) 

user_data = ('John', 'American', 1964, [77.0, 78.2, 77.5])
user_data[3].append(79.3)
print(user_data)

Answer: ('John', 'American', 1964, [77.0, 78.2, 77.5, 79.3])


         dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}               
print(my_dict)

my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict['name'])


my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
my_dict['age'] = 26
print(my_dict)

movie1 = [
    {
        "name": "Manas",
        "year": "2022",
        "direcotor": "ruslan akun",
        "actor": ["emil", "samat"],
    }
]    
print(movie1)

movie1 ={
    
    "name": "Manas",
    "year": "2022",
    "direcotor": "ruslan akun",
    "actor": ["emil", "samat"],
}
    #.values    #.keys
for info in movie1.items():      
    print(info)         

          #set 
st = {1,1,1,2,2,2,3,3,3,4,"hello", "hello"}
print(st)

my_set = {2, 1, 3, 4, 5,}   #sets - always remove duplicates and sort them
print(my_set)


set_a = {1,2,3,4}
set_b = {4,5,6,7}
union_set = set_a | set_b    # union_set "&" "|"
print(union_set)

comprehansion
lst = []
for num in range(10):
    lst.append(num)
print(lst)

lst = [char for char in "hello" ]   ### [value | for loop]
print(lst)


        #lists --- the list is changable, meaning that we can change,add,remove after it has been created

# cities = ['new york', 'los angeles', 'boston', 'dallas', 'chicago']
# print(cities)
# print(cities[0])            #lists are created using square brackets
# print(cities[-1])
# print(cities[3:])

# cities = ['new york', 'los angeles', 'boston', 'dallas', 'chicago']
# del cities [0]              ##del ---> deleting element in the list 
# print(cities)               

# book_ratings = [1,4,5,6,7,8]
# book_ratings.append(2)           #append ---> adds an element to the end of a list
# print(book_ratings)

# book_ratings = [2,4,6,8]
# book_ratings.insert(4,10)             #insert ---> insert an element at a specific index in a list
# print(book_ratings)


# countries = ['usa', 'china', 'brazil', 'cuba']
# for country in countries:                              # ---> iteratinh
#     print("curent country: ", country)


# cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']
# for index in range(len(cities)):
#     print("current index:", index, '| Current city: ', cities[index])

# thislist = ["apple", "banana", "cherry"]
# print(len(thislist[0]))
