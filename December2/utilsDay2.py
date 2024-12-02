def check_range_of_numbers(first_number, second_number):
    if(abs(first_number - second_number) >= 1 and abs(first_number - second_number) <= 3):
        #print(f"First number : {first_number} Second number : {second_number} abs = {abs(first_number - second_number)}")
        return True
    return False


def determine_safety_of_list(number_string):
    number_list = number_string.split()
    for i in range(len(number_list) - 1):
        if(check_range_of_numbers(int(number_list[i]), int(number_list[i + 1])) == False):
            return False
    return True

def check_if_list_is_sorted(number_string):
    number_list = number_string.split()
    int_number_list = []
    for i in range(len(number_list)):
        int_number_list.append(int(number_list[i]))
    if int_number_list == sorted(int_number_list) or int_number_list == sorted(int_number_list, reverse=True):
        return True
    return False