import re
from ruleClass import rule

def indentify_rules(input_string):
    pattern = r"^\d+\|\d+$"
    if re.match(pattern, input_string):
        return True
    else:
        return False

def indentify_codes(input_string):
    pattern = r"^\d+,\d+"
    if re.match(pattern, input_string):
        return True
    else:
        return False
    
def extract_number_from_rule(rule):
    numbers = rule.split("|")
    return int(numbers[0]), int(numbers[1])

def check_if_number_in_list(number, number_list):
    for i in range(len(number_list)):
        if(number == number_list[i].number):
            return i
    return -1

def identify_next_number(number_list):
    current_smallest_dependency = 10**10
    for i in range(len(number_list)):
        if(len(number_list[i].followingList) < current_smallest_dependency):
            current_smallest_dependency = len(number_list[i].followingList)
            index = i
    return index

def remove_number_from_followers(number, number_list):
    for i in range(len(number_list)):
        try:
            number_list[i].followingList.remove(number)
        except:
            continue

def constuct_rules_list(number_list):
    rules_order = []
    while number_list:
        index = identify_next_number(number_list)
        number = number_list[index]
        remove_number_from_followers(number, number_list)
        rules_order.append(number.number)
        del number_list[index]
    return rules_order

def init_numbers(rules_list):
    numbers = []
    for i in range(len(rules_list)):
        dom_number, sub_number = extract_number_from_rule(rules_list[i])
        index_dom_number = check_if_number_in_list(dom_number, numbers)
        if(index_dom_number == -1):
            numbers.append(rule(dom_number))
            numbers[-1].add_follower(sub_number)
        else:
            numbers[index_dom_number].add_follower(sub_number)
        index_sub_number = check_if_number_in_list(sub_number, numbers)
        if(index_sub_number == -1):
            numbers.append(rule(sub_number))
            numbers[-1].start_following(dom_number)
        else:
            numbers[index_sub_number].start_following(dom_number)
    return numbers

def init_update(update):
    update_list = update.split(",")
    return list(map(int, update_list))

def check_if_update_is_in_right_order(ordering_rules, update):
    update_order_indexes = []
    for i in range(len(update)):
        index_in_order_rules = ordering_rules.index(update[i])
        update_order_indexes.append(index_in_order_rules)
    if update_order_indexes == sorted(update_order_indexes):
        return True
    return False

def get_middle_element(code_list):
    middle_index = len(code_list) // 2
    return code_list[middle_index]

def get_correctly_ordered_updates(update_codes, ordering_rules):
    result = 0
    for i in range(len(update_codes)):
        code = init_update(update_codes[i])
        if(check_if_update_is_in_right_order(ordering_rules, code) == True):
            result += get_middle_element(code)
    return result

def check_snippet_against_rules(num1, num2, rules):
    combination_of_numbers = str(num1) + '|' + str(num2)
    for i in range(len(rules)):
        if combination_of_numbers == rules[i]:
            return True
    return False

def check_code(code, rules):
    codes = code.split(",")
    for i in range(len(codes) - 1):
        if(check_snippet_against_rules(codes[i], codes[i + 1], rules) == False):
            return False
    return True

def check_code_2(code, rules):
    for i in range(len(code) - 1):
        if(check_snippet_against_rules(code[i], code[i + 1], rules) == False):
            return False
    return True

def calculate_score(codes, rules):
    score = 0
    for i in range(len(codes)):
        if(check_code(codes[i], rules) == True):
            score += get_middle_element(list(map(int, codes[i].split(","))))
    return score

def fix_incorrect_code(incorrect_code, rules):
    for i in range(len(incorrect_code) - 1):
        if(check_snippet_against_rules(incorrect_code[i], incorrect_code[i + 1], rules) == False):
            incorrect_code[i], incorrect_code[i + 1] = incorrect_code[i + 1], incorrect_code[i]
    if(check_code_2(incorrect_code, rules) == False):
        fix_incorrect_code(incorrect_code, rules)
    return incorrect_code

def calculate_score_of_incorrect_codes(codes, rules):
    incorrect_codes = []
    incorrect_codes_fixed = []
    for i in range(len(codes)):
        if(check_code(codes[i], rules) == False):
            incorrect_codes.append(codes[i])
    for i in range(len(incorrect_codes)):
        new_incorrect_code = incorrect_codes[i].split(",")
        incorrect_codes[i] = fix_incorrect_code(new_incorrect_code, rules)
        incorrect_codes_fixed.append(",".join(incorrect_codes[i]))
        #print(incorrect_codes_fixed)
    return calculate_score(incorrect_codes_fixed, rules)
    
