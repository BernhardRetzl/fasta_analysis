import pandas as pd


def filter_data(input_file, mean_and_std_df, output_file):
    mean_and_std_df = pd.read_csv(mean_and_std_df, index_col=0)
    cut_off = round(mean_and_std_df['mean'][0]+9*mean_and_std_df['std'][0])
    with open(input_file) as in_file:
        with open(output_file, 'wt') as out_file:
            for line in in_file:
                occurrences = int(line.strip().split('\t')[-1])
                if occurrences >= cut_off:
                    out_file.write(line)


def test():
    input_file = '/home/b/data/Lexo/results/count_parts/length_8.tsv'
    mean_and_std_df = '/home/b/data/Lexo/results/mean_and_std/mean_and_std_8.csv'
    output_file = '/home/b/data/Lexo/test/filter_data/filtered_data.tsv'
    filter_data(input_file=input_file, mean_and_std_df=mean_and_std_df, output_file=output_file)


filter_data(input_file=snakemake.input[0], mean_and_std_df=snakemake.input[1], output_file=snakemake.output[0])
