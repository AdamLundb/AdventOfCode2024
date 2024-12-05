from utilsDay3 import find_instructions, exctract_number_from_instruction

def main():
    file_name = "C:\school\AdventOfCode2024\AdventOfCode2024\December3\day3_input.txt"
    puzzle_input = ""
    result_from_instructions = 0
    with open(file_name, "r") as file:
        for line in file:
            puzzle_input += line.strip()
    instructions = find_instructions(puzzle_input)
    for match_obj in instructions:
         result_from_instructions += exctract_number_from_instruction(match_obj.group())
    print(result_from_instructions)
if __name__ == "__main__":
    main()