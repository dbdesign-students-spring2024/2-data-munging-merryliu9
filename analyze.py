# Place code below to do the analysis part of the assignment.

import csv

def read_clean_data(file_name):
    data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            data.append(row)
    return data

def calculate_decade_average(data):
    decades = {}
    for row in data:
        year = int(row[0])
        anomaly = float(row[1])
        decade = (year // 10) * 10
        if decade in decades:
            decades[decade].append(anomaly)
        else:
            decades[decade] = [anomaly]

    decade_average = {}
    for decade, anomalies in decades.items():
        decade_average[decade] = sum(anomalies) / len(anomalies)

    return decade_average

def print_results(averages):
    for decade, average in sorted(averages.items()):
        print(f"Decade {decade}-{decade + 9}: Average anomaly {average:.2f} °F")

def main():
    filename = 'data/clean_data.csv'
    data = read_clean_data(filename)
    decade_averages = calculate_decade_average(data)
    print_results(decade_averages)

if __name__ == "__main__":
    main()
