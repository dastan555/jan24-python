    #    Homework Task 1:
         
kumo ={
    "name": "Kumo",
    "salary": "$1500",
    "age": "23",
    "items": ["car", "tv", "laptop", "monitor"]
}

for info in kumo.items():
    print (info)

mike ={
    "name": "Mike",
    "salary": "$10000",
    "age": "20",
    "items":["car", "PC", "smartwatch", "boat"]
}
print("---------------------------------------------")
for info in mike.items():
    print(info)
            #    Task1 
kumo = ['name:kuma','salary: $1500', '23 years', 'he owns a car,laptop, tv']
print(kumo)
mike =[ 'name:mike','salary: $10000', '20 years', 'he owns a car,pc,smartwatch and boat']
print(mike) 


                #Task 2
numbers = [i for i in range(1, 51)]
print(numbers)

numbers = [i for i in range(1, 51)]
sum_of_evens = sum(num for num in numbers if num % 2 == 0)
print(sum_of_evens)

numbers = [i for i in range(1, 51)]
pro_of_odds = 1  
for num in numbers:
    if num % 2 != 0:  
        pro_of_odds *= num
print(pro_of_odds)

numbers = [i for i in range(1, 51)]
largest_num = max(numbers)
print(largest_num)

print("Sum of all even numbers:", sum_of_evens)
print("Product of odd numbers:", pro_of_odds)
print("Largest number:", largest_num)

            # Task3
animal_list = ['lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'hippopotamus', 'monkey', 'crocodile',
 'bear', 'panda', 'penguin', 'kangaroo', 'lion', 'gazelle', 'parrot',
  'toucan', 'giraffe', 'elephant', 'kangaroo', 'monkey']
listx= {animal: animal_list.count(animal) for animal in set(animal_list)}
print(listx)


#             #Task4
connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
routes_to_rome = 0
total_flight_time = 0

for connection in connections:
    if connection[1] == 'Rome':
        routes_to_rome += 1
        total_flight_time +=200

print("Number of routes that lead to Rome:", routes_to_rome)
print("total flight time: ", total_flight_time)