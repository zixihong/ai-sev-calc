import random


mhighWeightList = [3.9, 5.1, 6.3, 7.2, 7.9, 8.4, 8.9, 9.3, 9.6, 10.0, 10.3, 10.5, 10.8, 11.1, 11.3, 11.6, 11.8, 12.0, 12.3, 12.5, 12.7, 13.0, 13.2, 13.4, 13.7]
mlowWeightList = [2.9, 3.9, 4.9, 5.6, 6.2, 6.7, 7.1, 7.4, 7.7, 7.9, 8.2, 8.4, 8.6, 8.8, 9.0, 9.2, 9.4, 9.6, 9.7, 9.9, 10.1, 10.3, 10.5, 10.6, 10.8]
fhighWeightList = [3.7, 4.8, 5.9, 6.7, 7.3, 7.8, 8.3, 8.7, 9.0, 9.3, 9.6, 9.9, 10.2, 10.4, 10.7, 10.9, 11.2, 11.4, 11.6, 11.9, 12.1, 12.4, 12.6, 12.8, 13.1]
flowWeightList = [2.9, 3.6, 4.5, 5.1, 5.6, 6.1, 6.4, 6.7, 7.0, 7.3, 7.5, 7.7, 7.9, 8.1, 8.3, 8.5, 8.7, 8.8, 9.0, 9.2, 9.4, 9.6, 9.8, 9.9, 10.1]

# 0 is male, 1 is female
virionCount = 1e8  # Replace with the actual virioncount value
weight = 1.2         # Replace with the actual weight value
age = 4            # Replace with the actual age value
gender = 0       # Replace with the actual gender value

if gender == 0:
                weight = random.uniform(0, mhighWeightList[age] + mlowWeightList[age])
                acceptableWeight = (mhighWeightList[age] + mlowWeightList[age]) / 2
else:
                weight = random.uniform(0, fhighWeightList[age] + flowWeightList[age])
                acceptableWeight = (fhighWeightList[age] + flowWeightList[age]) / 2
        

severity = (1 - age / 24) * (virionCount) + abs((acceptableWeight - weight) / acceptableWeight)*((virionCount) ** 2)
print(severity)
