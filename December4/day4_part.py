from utilsDay4 import identify_letter_position

def main():
    file_name = "AdventOfCode2024/December4/day4_input.txt"
    puzzle_data = []
    result = 0
    with open(file_name, "r") as file:
        for line in file:
                puzzle_data.append(line.strip())
    x_poses = identify_letter_position(puzzle_data, 'X')
    for i in range(len(x_poses)):
         x_poses[i].investigate_X(puzzle_data)
         result += x_poses[i].score
    print(result)
if __name__ == "__main__":
    main()