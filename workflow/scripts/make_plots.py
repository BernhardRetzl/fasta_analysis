import matplotlib.pyplot as plt


def make_plots(input_file, output_file):
    counts = list()
    occurences = list()
    with open(input_file) as in_file:
        for line in in_file:
            line = line.strip().split('\t')
            counts.append(int(line[-1]))
            occurences.append(int(line[0]))
    plt.scatter(occurences, counts, s=1)
    plt.xlabel('occurrences')
    plt.ylabel('frequency')
    plt.savefig(output_file)


# make_histogram(input_file='/home/b/data/Lexo/results/analyze_frequenzy/frequnzy_length_8.tsv',
#                output_file='/home/b/data/Lexo/results/create_histogramm/test.svg')
make_plots(input_file=snakemake.input[0], output_file=snakemake.output[0])


