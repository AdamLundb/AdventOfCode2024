from utilsDay1 import split_numbers, compare_lists

def main():
    file_name = "AdventOfCode2024/December1/part1_input.txt"
    left_list = []
    right_list = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                left, right = split_numbers(line.strip())
                left_list.append(left)
                right_list.append(right)
            left_list.sort()
            right_list.sort()
    except Exception as e:
        print(f"An error occurred: {e}")
    print(compare_lists(left_list, right_list))

if __name__ == "__main__":
    main()