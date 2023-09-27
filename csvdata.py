import random
import csv

mhighWeightList = [3.9, 5.1, 6.3, 7.2, 7.9, 8.4, 8.9, 9.3, 9.6, 10.0, 10.3, 10.5, 10.8, 11.1, 11.3, 11.6, 11.8, 12.0, 12.3, 12.5, 12.7, 13.0, 13.2, 13.4, 13.7]
mlowWeightList = [2.9, 3.9, 4.9, 5.6, 6.2, 6.7, 7.1, 7.4, 7.7, 7.9, 8.2, 8.4, 8.6, 8.8, 9.0, 9.2, 9.4, 9.6, 9.7, 9.9, 10.1, 10.3, 10.5, 10.6, 10.8]
fhighWeightList = [3.7, 4.8, 5.9, 6.7, 7.3, 7.8, 8.3, 8.7, 9.0, 9.3, 9.6, 9.9, 10.2, 10.4, 10.7, 10.9, 11.2, 11.4, 11.6, 11.9, 12.1, 12.4, 12.6, 12.8, 13.1]
flowWeightList = [2.9, 3.6, 4.5, 5.1, 5.6, 6.1, 6.4, 6.7, 7.0, 7.3, 7.5, 7.7, 7.9, 8.1, 8.3, 8.5, 8.7, 8.8, 9.0, 9.2, 9.4, 9.6, 9.8, 9.9, 10.1]

# Create and open a CSV file for writing the main data
data_file_name = "x_data.csv"
with open(data_file_name, mode='w', newline='') as data_csv_file:
    # Create a CSV writer for the main data file
    data_csv_writer = csv.writer(data_csv_file)

    # Write the header row to the main data CSV file
    data_csv_writer.writerow(["Age", "Weight", "Virion Count", "Gender"])

    # Create separate CSV files for the severity data with variance and without variance
    severity_file_name_variance = "y_data_variance.csv"
    severity_file_name_precise = "y_data_precise.csv"
    
    with open(severity_file_name_variance, mode='w', newline='') as severity_csv_file_variance, \
         open(severity_file_name_precise, mode='w', newline='') as severity_csv_file_precise:
        
        # Create CSV writers for both severity data files
        severity_csv_writer_variance = csv.writer(severity_csv_file_variance)
        severity_csv_writer_precise = csv.writer(severity_csv_file_precise)

        # Write the header row to both severity data CSV files
        severity_csv_writer_variance.writerow(["Severity"])
        severity_csv_writer_precise.writerow(["Severity"])

        # Generate data and write it to the main data and severity data CSV files
        for i in range(10000000):
            age = random.randint(0, 24)
            virionCount = random.randint(1, int(1e10))
            gender = random.randint(0, 1)
            if gender == 0:
                weight = random.uniform(0, mhighWeightList[age] + mlowWeightList[age])
                acceptableWeight = (mhighWeightList[age] + mlowWeightList[age]) / 2
            else:
                weight = random.uniform(0, fhighWeightList[age] + flowWeightList[age])
                acceptableWeight = (fhighWeightList[age] + flowWeightList[age]) / 2

            

            severity = (1 - age / 24) * (virionCount) + abs((acceptableWeight - weight) / acceptableWeight) ** 2
            # Add 0.01% variance to the severity by multiplying it with a random factor
            variance_factor = 1 + random.uniform(-0.0001, 0.0001)
            severity_with_variance = severity * variance_factor

            # Write the data to the main data CSV file
            data_csv_writer.writerow([age, weight, virionCount, gender])

            # Write the severity data with variance to the severity data CSV file
            severity_csv_writer_variance.writerow([severity_with_variance])

            # Write the precise severity data (without variance) to the other severity data CSV file
            severity_csv_writer_precise.writerow([severity])

    print(f"Main data CSV file '{data_file_name}' has been created.")
    print(f"Severity data CSV file '{severity_file_name_variance}' with 0.1% variance has been created.")
    print(f"Precise Severity data CSV file '{severity_file_name_precise}' without variance has been created.")