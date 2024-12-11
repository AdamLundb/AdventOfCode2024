def coordinate_differences(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    delta_x = x2 - x1
    delta_y = y2 - y1

    return delta_x, delta_y

class frequency:
    def __init__ (self, symbol):
        self.antennaSymbol = symbol
        self.locationOfSymbols = []
        self.numberOfAntiNodesCreatedBySymbols = 0
        self.coordinatesOfAntiNodes = []

    def add_coordinate_to_symbol(self, coordainte):
        self.locationOfSymbols.append(coordainte)
    
    def place_anti_node(self, delta_x, delta_y, first_coord, second_coord):
        first_anti_node_coord = (first_coord[0] - delta_x, first_coord[1] - delta_y)
        second_anti_node_coord = (second_coord[0] + delta_x, second_coord[1] + delta_y)
        self.coordinatesOfAntiNodes.append(first_anti_node_coord)
        self.coordinatesOfAntiNodes.append(second_anti_node_coord)

    def place_all_anti_node(self, delta_x, delta_y, first_coord, second_coord, map):
        first_x_coord = first_coord[0]
        first_y_coord = first_coord[1]
        map_x_size = len(map[0]) 
        map_y_size = len(map)
        self.coordinatesOfAntiNodes.append(first_coord)
        self.coordinatesOfAntiNodes.append(second_coord)
        while(first_x_coord > 0 and first_y_coord > 0 and first_x_coord < map_x_size and first_y_coord < map_y_size):
            first_x_coord = first_x_coord - delta_x
            first_y_coord = first_y_coord - delta_y
            print(first_x_coord, first_y_coord)
            first_anti_node_coord = (first_x_coord, first_y_coord)
            self.coordinatesOfAntiNodes.append(first_anti_node_coord)
        second_x_coord = second_coord[0]
        second_y_coord = second_coord[1]
        while(second_x_coord < map_x_size and second_y_coord < map_y_size and second_x_coord < 0 and second_y_coord < 0):
            second_x_coord = second_x_coord + delta_x
            second_y_coord = second_y_coord + delta_y
            second_anti_node_coord = (second_x_coord, second_y_coord)
            self.coordinatesOfAntiNodes.append(second_anti_node_coord)

        #print(f"antennas : {first_coord}, {second_coord} anti nodes: {first_anti_node_coord}, {second_anti_node_coord}")
    def find_anti_node_for_frequency(self, setting, map):
        for i in range(len(self.locationOfSymbols)):
            current_coordinate = self.locationOfSymbols[i]
            for j in range(len(self.locationOfSymbols)):
                if i != j:
                    coordinate_to_check_against = self.locationOfSymbols[j]
                    delta_x, delta_y = coordinate_differences(current_coordinate, coordinate_to_check_against)
                    if(setting == 'part1'):
                        self.place_anti_node(delta_x, delta_y, current_coordinate, coordinate_to_check_against)
                    if(setting == 'part2'):
                        self.place_all_anti_node(delta_x, delta_y, current_coordinate, coordinate_to_check_against, map)
