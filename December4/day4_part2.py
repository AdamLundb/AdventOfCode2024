from utilsDay4 import identify_letter_position

def main():
    file_name = "AdventOfCode2024/December4/day4_input.txt"
    puzzle_data = []
    result = 0
    with open(file_name, "r") as file:
        for line in file:
                puzzle_data.append(line.strip())
    a_poses = identify_letter_position(puzzle_data, 'A')
    for i in range(len(a_poses)):
         a_poses[i].investigate_A(puzzle_data)
         if(a_poses[i].score == 2):
              result += 1
    print(result)
if __name__ == "__main__":
    main()