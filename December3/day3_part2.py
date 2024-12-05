from utilsDay3 import find_instructions, exctract_number_from_instruction, find_commands, construct_command_list, instruction

def main():
    file_name = "C:\school\AdventOfCode2024\AdventOfCode2024\December3\day3_input.txt"
    puzzle_input = ""
    result_from_instructions = 0
    instruction_index = 0
    current_instruction = "do"
    with open(file_name, "r") as file:
        for line in file:
            puzzle_input += line.strip()
    instructions = find_instructions(puzzle_input)
    do_instruction, dont_instruction = find_commands(puzzle_input)
    command_list = construct_command_list(do_instruction, dont_instruction)
    for instruction in instructions:
        try:
            list_insturction = command_list[instruction_index]
        except IndexError:
            list_insturction = command_list[len(command_list)-1]
        if(instruction.start() > list_insturction.indexInText):
            current_instruction = list_insturction.instruction
            instruction_index += 1
        if(current_instruction == "do"):
            result_from_instructions += exctract_number_from_instruction(instruction.group())
        else:
            continue
    print(result_from_instructions)
if __name__ == "__main__":
    main()