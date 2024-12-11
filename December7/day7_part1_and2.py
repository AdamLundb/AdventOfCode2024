from utilsDay7 import split_into_numbers_and_answer, find_possible_answer_combinations

def main():
    file_name = "AdventOfCode2024/December7/day7_input.txt"
    result = 0
    with open(file_name, "r") as file:
        for line in file:
                answer, numbers = split_into_numbers_and_answer(line.strip())
                result += find_possible_answer_combinations(numbers, answer)
    print(result)
if __name__ == "__main__":
    main()