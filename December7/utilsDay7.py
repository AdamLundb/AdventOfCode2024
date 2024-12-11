def split_into_numbers_and_answer(string_input):
    split = string_input.split(": ")
    answer = split[0]
    numbers = split[1].split()
    return int(answer), list(map(int, numbers))

def concatenate_numbers(num1, num2):
    return int(str(num1) + str(num2))

def find_possible_answer_combinations(number_list, answer):
    first_number = number_list.pop(0)
    possible_answers = [first_number]
    while number_list != []:
        next_number = number_list.pop(0)
        current_size_of_possible_answers = len(possible_answers)
        print(possible_answers)
        for i in range(current_size_of_possible_answers):
            multiply = next_number * possible_answers[0]
            addition = next_number + possible_answers[0]
            concatenate = concatenate_numbers(possible_answers[0], next_number)
            if(multiply == answer):
                return multiply
            if(addition == answer):
                return addition
            if(concatenate == answer):
                return concatenate
            possible_answers.append(multiply)
            possible_answers.append(addition)
            possible_answers.append(concatenate)
            possible_answers.pop(0)
    return 0

