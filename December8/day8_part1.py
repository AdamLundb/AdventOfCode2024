from utilsDay8 import locate_symbols, print_symbol_list, place_and_calculate_anti_nodes, print_map

def main():
    file_name = "AdventOfCode2024/December8/day8_input.txt"
    data = []
    symbols = []
    with open(file_name, "r") as file:
        for line in file:
            data.append(list(line.strip()))
    symbol_list = locate_symbols(data, symbols)
    print(len(list(dict.fromkeys(place_and_calculate_anti_nodes(symbol_list, data)))))
    print_map(data)
    
if __name__ == "__main__":
    main()