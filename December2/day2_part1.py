from utilsDay2 import determine_safety_of_list, check_if_list_is_sorted

def main():
    file_name = "AdventOfCode2024/December2/day2_input.txt"
    result_list = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                if(determine_safety_of_list(line.strip()) == True and check_if_list_is_sorted(line.strip()) == True):
                    print(line.strip())
                    result_list.append(1)
                else:
                    result_list.append(0)
    except Exception as e:
        print(f"An error occurred: {e}")
    print(sum(result_list))

if __name__ == "__main__":
    main()