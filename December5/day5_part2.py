from utilsDay5 import indentify_rules, indentify_codes, calculate_score_of_incorrect_codes, calculate_score

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
    print(calculate_score_of_incorrect_codes(update_codes, rules))

if __name__ == "__main__":
    main()