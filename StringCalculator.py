import re

class StringCalculator:
    def add(self, string):
        array = re.findall(r"[\w']+", string)
        array_len = len(array)
        if array_len == 0:
            return 0
        elif array_len == 1:
            return int(string)
        else:
            sum = 0
            for number in array:
                sum += int(number)
            return sum
