import average as av

print(f"용어 설명: {av.average_in_korean}")

result = av.av_2_num(10, 5)
print(f"두 수(10, 5)의 산술 평균: {result}")

calc = av.AverageCalculator() 
calc.calculate_average()
print(calc.show_result())