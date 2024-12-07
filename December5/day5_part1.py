from utilsDay5 import indentify_rules, indentify_codes, init_numbers, identify_next_number, constuct_rules_list, get_correctly_ordered_updates, calculate_score

def main():
    file_name = "AdventOfCode2024/December5/day5_input.txt"
    rules = []
    update_codes = []
    with open(file_name, "r") as file:
        for line in file:
                if(indentify_rules(line.strip()) == True):
                     rules.append(line.strip())
                     continue
                else:
                    if indentify_codes(line.strip()) == True:
                        update_codes.append(line.strip())
                         
    print(rules)
    print(update_codes)
    print(calculate_score(update_codes, rules))

if __name__ == "__main__":
    main()