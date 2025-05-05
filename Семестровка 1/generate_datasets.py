import numpy as np

def generate_datasets():
    sizes = np.linspace(100, 10000, num=50, dtype=int)
    datasets = []
    for size in sizes:
        random_data = np.random.randint(0, 100000, size).tolist()
        almost_sorted = sorted(random_data)
        almost_sorted[:10] = np.random.randint(0, 100000, 10).tolist()  # Добавляем шум
        reversed_data = sorted(random_data, reverse=True)
        datasets.append((size, random_data, almost_sorted, reversed_data))
    return datasets