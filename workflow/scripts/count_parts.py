def count_parts(input_file, output_file):
    """counts sequences of length n (n specified by name of output file)"""
    length = int(output_file.split('length_')[-1].split('.tsv')[0])
    part_dict = dict()
    with open(input_file) as in_file:
        for line in in_file:
            if not line.startswith('>'):
                line = line.strip()
                for i in range(len(line)-length+1):
                    part = line[i:i+length]
                    if part in part_dict:
                        part_dict[part] += 1
                    else:
                        part_dict[part] = 1
    with open(output_file, 'wt') as out_file:
        for i in part_dict:
            out_file.write(i+'\t'+str(part_dict[i])+'\n')


def test():
    count_parts('./../../resources/data.fa', './../../test/count_parts/length_1.tsv')


count_parts(snakemake.input[0], snakemake.output[0])
