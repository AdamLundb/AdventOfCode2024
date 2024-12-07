class x_class:
    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate
        self.score = 0
    def check_if_letter(self, x, y, puzzle_input, letter):
        if(x < 0 or y < 0):
            return False
        try:
            if(puzzle_input[y][x] == letter):
                return True
            else:
                return False
        except IndexError:
            return False

    def investigate_left_side(self, puzzle_input):
        if(self.check_if_letter(self.x + 1, self.y, puzzle_input, 'M') == True):
            if(self.check_if_letter(self.x + 2, self.y, puzzle_input, 'A') == True):
                if(self.check_if_letter(self.x+ 3, self.y, puzzle_input, 'S') == True):
                    print(f"LEFT X FOUND : x pos : {self.x} y pos : {self.y}")
                    self.score += 1
    def investigate_right_side(self, puzzle_input):
        if(self.check_if_letter(self.x - 1, self.y, puzzle_input, 'M') == True):
            if(self.check_if_letter(self.x - 2, self.y, puzzle_input, 'A') == True):
                if(self.check_if_letter(self.x - 3, self.y, puzzle_input, 'S') == True):
                    print(f"RIGHT X FOUND : x pos : {self.x} y pos : {self.y}")
                    self.score += 1
    def investigate_above(self, puzzle_input):
        if(self.check_if_letter(self.x, self.y - 1, puzzle_input, 'M') == True):
            if(self.check_if_letter(self.x, self.y - 2, puzzle_input, 'A') == True):
                if(self.check_if_letter(self.x, self.y - 3, puzzle_input, 'S') == True):
                    print(f"ABOVE X FOUND : x pos : {self.x} y pos : {self.y}")
                    self.score += 1
    def investigate_below(self, puzzle_input):
        if(self.check_if_letter(self.x, self.y + 1, puzzle_input, 'M') == True):
            if(self.check_if_letter(self.x, self.y + 2, puzzle_input, 'A') == True):
                if(self.check_if_letter(self.x, self.y + 3, puzzle_input, 'S') == True):
                    print(f"BELOW X FOUND : x pos : {self.x} y pos : {self.y}")
                    self.score += 1
    def investigate_NE(self, puzzle_input):
        if(self.check_if_letter(self.x + 1, self.y - 1, puzzle_input, 'M') == True):
            if(self.check_if_letter(self.x + 2, self.y - 2, puzzle_input, 'A') == True):
                if(self.check_if_letter(self.x + 3, self.y - 3, puzzle_input, 'S') == True):
                    print(f"NE X FOUND : x pos : {self.x} y pos : {self.y}")
                    self.score += 1
    def investigate_SE(self, puzzle_input):
        if(self.check_if_letter(self.x + 1, self.y + 1, puzzle_input, 'M') == True):
            if(self.check_if_letter(self.x + 2, self.y + 2, puzzle_input, 'A') == True):
                if(self.check_if_letter(self.x + 3, self.y + 3, puzzle_input, 'S') == True):
                    print(f"SE X FOUND : x pos : {self.x} y pos : {self.y}")
                    self.score += 1
    def investigate_SW(self, puzzle_input):
        if(self.check_if_letter(self.x - 1, self.y + 1, puzzle_input, 'M') == True):
            if(self.check_if_letter(self.x - 2, self.y + 2, puzzle_input, 'A') == True):
                if(self.check_if_letter(self.x - 3, self.y + 3, puzzle_input, 'S') == True):
                    print(f"SW X FOUND : x pos : {self.x} y pos : {self.y}")
                    self.score += 1
    def investigate_NW(self, puzzle_input):
        if(self.check_if_letter(self.x - 1, self.y - 1, puzzle_input, 'M') == True):
            if(self.check_if_letter(self.x - 2, self.y - 2, puzzle_input, 'A') == True):
                if(self.check_if_letter(self.x - 3, self.y - 3, puzzle_input, 'S') == True):
                    print(f"NW X FOUND : x pos : {self.x} y pos : {self.y}")
                    self.score += 1
    def investigate_X(self, puzzle_input):
        self.investigate_above(puzzle_input)
        self.investigate_below(puzzle_input)
        self.investigate_left_side(puzzle_input)
        self.investigate_right_side(puzzle_input)
        self.investigate_NE(puzzle_input)
        self.investigate_NW(puzzle_input)
        self.investigate_SE(puzzle_input)
        self.investigate_SW(puzzle_input)
    def check_NW_M(self, puzzle_input):
        if(self.check_if_letter(self.x - 1, self.y -1, puzzle_input, 'M') == True):
            return True
    def check_NW_S(self, puzzle_input):
        if(self.check_if_letter(self.x - 1, self.y -1, puzzle_input, 'S') == True):
            return True
    def check_SW_M(self, puzzle_input):
        if(self.check_if_letter(self.x - 1, self.y + 1, puzzle_input, 'M') == True):
            return True
    def check_SW_S(self, puzzle_input):
        if(self.check_if_letter(self.x - 1, self.y + 1, puzzle_input, 'S') == True):
            return True
    def check_SE_M(self, puzzle_input):
        if(self.check_if_letter(self.x + 1, self.y + 1, puzzle_input, 'M') == True):
            return True
    def check_SE_S(self, puzzle_input):
        if(self.check_if_letter(self.x + 1, self.y + 1, puzzle_input, 'S') == True):
            return True
    def check_NE_M(self, puzzle_input):
        if(self.check_if_letter(self.x + 1, self.y - 1, puzzle_input, 'M') == True):
            return True
    def check_NE_S(self, puzzle_input):
        if(self.check_if_letter(self.x + 1, self.y - 1, puzzle_input, 'S') == True):
            return True
        
    def investigate_A(self, puzzle_input):
        if(self.check_NE_M(puzzle_input) == True and self.check_SW_S(puzzle_input) == True):
            self.score += 1
        if(self.check_NE_S(puzzle_input) == True and self.check_SW_M(puzzle_input) == True):
            self.score += 1
        if(self.check_NW_M(puzzle_input) == True and self.check_SE_S(puzzle_input) == True):
            self.score += 1
        if(self.check_NW_S(puzzle_input) == True and self.check_SE_M(puzzle_input) == True):
            self.score += 1
    


