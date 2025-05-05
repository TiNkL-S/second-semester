import pandas as pd
import matplotlib.pyplot as plt

def plot_results():
    df = pd.read_csv('results.csv')
    plt.figure(figsize=(12, 6))
    for dtype in df['Data Type'].unique():
        subset = df[df['Data Type'] == dtype]
        plt.plot(subset['Size'], subset['Time (s)'], label=f'{dtype} time')
    plt.xlabel('Размер данных')
    plt.ylabel('Время (сек)')
    plt.legend()
    plt.savefig('time_vs_size.png')
    plt.show()

if __name__ == '__main__':
    plot_results()