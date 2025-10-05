def show_menu():
    print("options\n"
          "1)Enter your number:\n"
          "2)Enter your name:\n"
          "3)show the list numbers:\n"
          "4)show the list names:\n"
          "5)show the result of numbers:\n"
          "6)remove item:\n"
          "7)exit")
    option = int(input("Enter your option: "))
    return option

list_of_numbers = []
list_of_names = []

def add_number():
    number = int(input("Enter your number: "))
    list_of_numbers.append(number)
    return number
def add_name():
    name = input("Enter your name: ")
    list_of_names.append(name)
    return name
def show_the_list_of_numbers():
    print("your list of numbers",list_of_numbers)
def show_the_result_of_numbers():
    result = sum(list_of_numbers)/len(list_of_numbers)
    print("your result is",result)
    return result
def show_the_list_of_names():
    print("your list of names",list_of_names)
def remove_item():
    choose =(input("input which list do you want to remove from(name , number): "))
    if choose == "number":
        remove_the_item = int(input("Enter the number you want to remove: "))
        list_of_numbers.remove(remove_the_item)
    elif choose == "name":
        remove_the_name = input("Enter the name you want to remove: ")
        list_of_names.remove(remove_the_name)
    else:
        print("invalid choice")

