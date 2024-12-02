def split_numbers(number_string):
    parts = number_string.split()

    left_part = int(parts[0])
    right_part = int(parts[1])

    return left_part, right_part

def compare_lists(right_list, left_list):
    sum = 0
    for x in range(len(right_list)):
        sum += abs(right_list[x] - left_list[x])
    return sum

def how_many_times_number_appears_in_list(number, list):
    times_number_appeared = 0
    for i in range(len(list)):
        if(list[i] == number):
            times_number_appeared += 1
    return times_number_appeared

def multiply_occurances_in_list(sim_list, list):
    sum = 0
    for i in range(len(sim_list)):
        sum += sim_list[i] * list[i]
    return sum