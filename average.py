
average_in_korean = "산술 평균"


def av_2_num(a, b):
    return (a + b) / 2

def av_3_num(a, b, c):
    return (a + b + c) / 3


class AverageCalculator:
    def __init__(self):
        self.result = 0

    def calculate_average(self):

        count = int(input("산술 평균을 구하고자 하는 숫자의 개수를 입력해 주세요: "))
        
        numbers = []
        for i in range(1, count + 1):

            val = float(input(f"{i}번 숫자를 입력하세요: "))
            numbers.append(val)
        

        self.result = sum(numbers) / len(numbers)
        return self.result

    def show_result(self):
        return f"사용자 숫자의 산술 평균: {self.result} 입니다"

calc = AverageCalculator()
calc.calculate_average()
print(calc.show_result())