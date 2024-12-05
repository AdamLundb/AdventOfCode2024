import reportsClass

def main():
    file_name = "AdventOfCode2024/December2/day2_input.txt"
    result_list = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                new_repport = reportsClass.Report(line.strip())
                if(new_repport.return_safety_rating() == "safe"):
                    result_list.append(1)
                else:
                    result_list.append(0)
            print(sum(result_list))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()