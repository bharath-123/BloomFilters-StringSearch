import timeit
from filter_col import *
import matplotlib.pyplot as plt
import numpy as np

def plot_results(benchmarks):
        bar_labels = ['Naive', 'Naive with BlF(Serial)', 'Naive with BlF(Parallel)']
        '''
        We are using three algorithms. Naive, Naive with bloom filter
        and parallelized version of Naive with bloom filter.
        '''
        fig = plt.figure(figsize=(10,8))

        # plot bars
        y_pos = np.arange(len(benchmarks))#No of grids to plot
        plt.yticks(y_pos, bar_labels, fontsize=16) # labelling the grids
        bars = plt.barh(y_pos, benchmarks,
                 align='center',  color='g') # drawing the bars on the figure

        plt.xlabel('time in seconds', fontsize=14) #x axis
        plt.ylabel('Algorithms used', fontsize=14) #y axis
        t = plt.title('Performance Comparison', fontsize=18) #title of the plot
        plt.grid()
        plt.show()


if __name__ == '__main__'  :

    benchmarks = create_DNA_collection_and_search('Human','Mouse',1)[1]

    print(benchmarks)


    plot_results(benchmarks)
