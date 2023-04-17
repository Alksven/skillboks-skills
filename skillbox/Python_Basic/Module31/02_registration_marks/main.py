import re

numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

car_pattern = r'\b\w{1}\d{3}\w{2}\d{,3}'
taxi_pattern = r'\b\w{2}\d{3}\d{,3}'

num_car = re.findall(car_pattern, numbers)
num_taxi = re.findall(taxi_pattern, numbers)
print(num_car)
print(num_taxi)
