from x_class import x_class

def identify_letter_position(puzzle_input, letter):
    all_X_in_puzzle_input = []
    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input[i])):
            if(puzzle_input[i][j] == letter):
                x_found = x_class(j,i)
                all_X_in_puzzle_input.append(x_found)
    return all_X_in_puzzle_input