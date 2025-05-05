import csv
from generate_datasets import generate_datasets
from introsort import measure_introsort

def run_benchmarks():
    datasets = generate_datasets()
    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Size', 'Data Type', 'Time (s)', 'Iterations'])
        for size, random_data, almost_sorted, reversed_data in datasets:
            for data, dtype in zip([random_data, almost_sorted, reversed_data], 
                                    ['random', 'almost_sorted', 'reversed']):
                time_taken, iterations = measure_introsort(data)
                writer.writerow([size, dtype, time_taken, iterations])

if __name__ == '__main__':
    run_benchmarks()