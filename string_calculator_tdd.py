'''Give class calculate sum of numbers from the given string'''
class StringCalculator:
    def __init__(self):
        self.delimiter = ','

    def add(self, numbers: str) -> int:
        #Return 0 if string is empty
        if not numbers:
            return 0
        # If the input string has a custom delimiter at the start
        nums = numbers
        if numbers.startswith('//'):
            delimiter, nums = numbers[2:].split('\n', 1)
            # Use the custom delimiter instead of hardcoding a comma
            nums = nums.replace('\n', delimiter)
            nums = nums.replace(delimiter, ',')
        else:
            nums = nums.replace('\n', ',')
        # Split string and convert into integers
        integers = [int(n) for n in nums.split(',')]
        # neagtive numbers are not allowed
        negatives = [n for n in integers if n < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")
        # Return the sum of integers
        return sum(integers)
