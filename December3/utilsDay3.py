import re

class instruction:
    def __init__(self, instruction, value):
        self.instruction = instruction
        self.indexInText = value

def find_instructions(text):
    pattern = r"mul\((\d+),(\d+)\)"
    instructions = re.finditer(pattern, text)
    return instructions

def find_commands(text):
    find_do_commands = r"do\(\)"
    find_dont_commands = r"don't\(\)"
    do_commands = re.finditer(find_do_commands, text)
    dont_commands = re.finditer(find_dont_commands, text)
    return do_commands, dont_commands

def construct_command_list(do_commands, dont_commands):
    do_next = next(do_commands)
    dont_next = next(dont_commands)
    command_list = []
    while do_next is not None or dont_next is not None:
        if do_next is not None and (dont_next is None or do_next.start() <= dont_next.start()):
            command_list.append(instruction("do", do_next.start()))
            try:
                do_next = next(do_commands)  # Advance the 'do' iterator
            except StopIteration:
                do_next = None
        elif dont_next is not None:
            command_list.append(instruction("dont" ,dont_next.start()))
            try:
                dont_next = next(dont_commands) 
            except StopIteration:
                dont_next = None
    return command_list

def exctract_number_from_instruction(instruction):
    clean_instruction = instruction.replace("mul(", "").replace(")", "")
    num1, num2 = map(int, clean_instruction.split(","))
    print(num1, num2)
    return num1 * num2



