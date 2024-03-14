#Task
def merge_and_sort(list1, list2):
    merg_list = list1 + list2
    sort_list = sorted(merg_list)
    return sort_list

list1 = [2, 6, 1, 9]
list2 = [3, 7, 4, 8]
result = merge_and_sort(list1, list2)
print(result)



#Task2
def calculator():
    print("Welcome to the calculator program!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero!")
            return
        else:
            result = num1 / num2
    else:
        print("Invalid operation!")
        return

    print("Result:", result)

calculator()

        #Task3
def average(*args):
    if not args:
        return none
    total = sum(args)
    count = len(args)
    avg = total / count


    return avg

print(average(1,2,3,4,5,6))
print(average(5,10,15,20,30))
print(average(23,33,43,53,63))


