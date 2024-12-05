class Report:
    def __init__(self, string_reportCode):
        number_list = string_reportCode.split()
        self.reportCode = []
        self.safetyRating = ""
        self.permutations = []
        for i in range(len(number_list)):
            self.reportCode.append(int(number_list[i]))
        self.determine_report_list_order()
        self.check_report_safety()

    def determine_report_list_order(self):
        increasing = 0
        decreasing = 0
        for i in range(len(self.reportCode) - 1):
            if(self.reportCode[i] > self.reportCode[i + 1]):
                decreasing += 1
            elif(self.reportCode[i] < self.reportCode[i + 1]):
                increasing += 1
            else:
                self.safetyRating = "Unsafe"
        if(decreasing > increasing):
            self.listOrder = "decreasing"
        else:
            self.listOrder = "increasing"

    def check_range_of_numbers(self, first_number, second_number):
        if(abs(first_number - second_number) >= 1 and abs(first_number - second_number) <= 3):
            return True
        return False


    def determine_safety_of_list_range(self):
        for i in range(len(self.reportCode) - 1):
            if(self.check_range_of_numbers(self.reportCode[i], self.reportCode[i + 1]) == False):
                return False
        return True
    
    def check_if_list_sorted(self, status):
        if(self.listOrder == "decreasing"):
            if(self.reportCode == sorted(self.reportCode, reverse=True)):
                return True
            else:
                return False
        else:
            if(self.reportCode == sorted(self.reportCode)):
                return True
            else:
                return False
            
    def find_code_permutations(self):
        for i in range(len(self.reportCode)):
            temp_removed_index = self.reportCode.pop(i)
            permutation = self.reportCode[:]
            self.permutations.append(permutation)
            self.reportCode.insert(i, temp_removed_index)

    def check_for_safe_permutation(self):
        for i in range(len(self.permutations)):
            originalReportCode = self.reportCode
            self.reportCode = self.permutations[i]
            if(self.determine_safety_of_list_range() == True and self.check_if_list_sorted(True) == True):
                return True
            self.reportCode = originalReportCode
        return False
    
    def check_report_safety(self):
        if(self.determine_safety_of_list_range() == True and self.check_if_list_sorted(True) == True):
            self.safetyRating = "safe"
        else:
            self.find_code_permutations()
            if(self.check_for_safe_permutation() == True):
                self.safetyRating = "safe"
            else:
                self.safetyRating = "unsafe"
    def return_safety_rating(self):
        return self.safetyRating