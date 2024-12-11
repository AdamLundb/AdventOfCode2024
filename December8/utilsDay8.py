from frequencyClass import frequency

def print_symbol_list(symbol_list):
    for i in range(len(symbol_list)):
        print(symbol_list[i].antennaSymbol)
        print(symbol_list[i].locationOfSymbols)

def create_new_symbol_and_add_to_list(symbol, coordinate, symbol_list):
    new_frequency = frequency(symbol)
    new_frequency.add_coordinate_to_symbol(coordinate)
    symbol_list.append(new_frequency)

def check_if_spot_is_occupied(coordinate, map):
    if map[coordinate[1]][coordinate[0]] == '.':
        return False
    return True

def check_if_list_contains_symbol(symbol, coordinate, symbol_list):
    if(symbol == '.'):
        return
    for i in range(len(symbol_list)):
        if(symbol == symbol_list[i].antennaSymbol):
            symbol_list[i].add_coordinate_to_symbol(coordinate)
            return
    create_new_symbol_and_add_to_list(symbol, coordinate, symbol_list)

def locate_symbols(map, symbol_list):
    for i in range(len(map)):
        for j in range(len(map[i])):
            check_if_list_contains_symbol(map[i][j], (j, i), symbol_list)
    return symbol_list

def check_if_anti_node_is_valid(anti_node_coord, map):
    try:
        if(anti_node_coord[0] < 0 or anti_node_coord[1] < 0):
            return False
        if(check_if_spot_is_occupied(anti_node_coord, map) == False):
            map[anti_node_coord[1]][anti_node_coord[0]] = '#'
        print(f"Antinode : {anti_node_coord} returned true")
        return True
    except:
        return False
def place_and_calculate_anti_nodes(symbol_list, map):
    list_of_anti_nodes = []
    for i in range(len(symbol_list)):
        symbol_list[i].find_anti_node_for_frequency("part2", map)
        for j in range(len(symbol_list[i].coordinatesOfAntiNodes)):
            if(check_if_anti_node_is_valid(symbol_list[i].coordinatesOfAntiNodes[j], map) == True):
                list_of_anti_nodes.append(symbol_list[i].coordinatesOfAntiNodes[j])
    return list_of_anti_nodes

def print_map(map):
    for i in range(len(map)):
        ''.join(map[i])
        print(map[i])
        map[i] = list(map[i])


        

