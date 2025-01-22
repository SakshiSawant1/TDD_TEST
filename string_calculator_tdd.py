class StringCalculator:
    def __init__(self):
        self.delimiter = ','
    
    
    def add(self, numbers: str) -> int:
        #Return 0 if string is empty
        if not numbers:
            return 0