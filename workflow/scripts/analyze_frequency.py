def analyze_frequency(input_file, output_file):
    frequency_dict = dict()
    with open(input_file) as in_file:
        for line in in_file:
            line = line.strip().split('\t')
            counts = line[1]
            if counts in frequency_dict:
                frequency_dict[counts] += 1
            else:
                frequency_dict[counts] = 1
    items = list(frequency_dict.items())
    items.sort(key=lambda x: (x[1], x[0]), reverse=True)
    with open(output_file, 'wt') as out_file:
        for i in items:
            out_file.write(i[0]+'\t'+str(i[1])+'\n')


def test():
    analyze_frequency('./../../test/count_parts/length_1.tsv', './../../test/analyze_frequncy/frequnzy_length_1.tsv')


analyze_frequency(snakemake.input[0], snakemake.output[0])
