import numpy as np
import glob
import pandas as pd


def calculate_mean_and_std(input_file, output_file):
    occurrences = list()
    with open(input_file) as in_file:
        for line in in_file:
            line = line.strip().split('\t')
            occurrences += [int(line[0])]*int(line[1])
    occurrences_array = np.array(occurrences)
    mean = occurrences_array.mean()
    std = occurrences_array.std()
    mean_and_std_df = pd.DataFrame({'mean': [mean], 'std': [std]})
    mean_and_std_df.to_csv(output_file)


# file = '/home/b/data/Lexo/results/analyze_frequenzy/frequnzy_length_15.tsv'
# calculate_mean_and_std()

calculate_mean_and_std(input_file=snakemake.input[0], output_file=snakemake.output[0])




#%%
