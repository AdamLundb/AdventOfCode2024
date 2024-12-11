from arrowClass import arrow
from utilsDay6 import find_arrow_location, calculate_steps

def main():
    file_name = "AdventOfCode2024/December6/day6_input.txt"
    game_map = []
    with open(file_name, "r") as file:
        for line in file:
                game_map.append(line.strip())
    arrow_x, arrow_y = find_arrow_location(game_map)
    gaurd = arrow(arrow_x, arrow_y)
    print(calculate_steps(gaurd, game_map))
if __name__ == "__main__":
    main()