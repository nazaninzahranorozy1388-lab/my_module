from my_module import *
while True:
    attempt=show_menu()
    if attempt==1:
        first_performance=add_number()
        print(first_performance)
        print("*" * 30)
    elif attempt==2:
        second_performance=add_name()
        print(second_performance)
        print("*" * 30)
    elif attempt==3:
        show_the_list_of_numbers()
        print("*" * 30)
    elif attempt==4:
        show_the_list_of_names()
        print("*" * 30)
    elif attempt==5:
        show_the_result_of_numbers()
        print("*" * 30)
    elif attempt==6:
        remove_item()
        print("*" * 30)
    elif attempt==7:
        print("bye")
        break
    else:
        print("invalid number")