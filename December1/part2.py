from utilsDay1 import split_numbers, how_many_times_number_appears_in_list, multiply_occurances_in_list

def main():
    file_name = "AdventOfCode2024/December1/part1_input.txt"
    left_list = []
    right_list = []
    similarity_list = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                left, right = split_numbers(line.strip())
                left_list.append(left)
                right_list.append(right)
    except Exception as e:
        print(f"An error occurred: {e}")
    for i in range(len(left_list)):
        similarity_list.append(how_many_times_number_appears_in_list(left_list[i], right_list))
    print(multiply_occurances_in_list(similarity_list, left_list))
if __name__ == "__main__":
    main()