import os
import glob


class Sequence:
    def __init__(self, sequence, occurences):
        self.sequence = sequence
        self.occurences = occurences
        self.children = list()
        self.already_used = False

    def __lt__(self, other):
        return len(self.sequence) < len(other.sequence)

    def __repr__(self):
        return self.sequence + '\t' + str(self.occurences)


class Cluster():
    def __init__(self, sequence_list):
        self.sequence_list = sequence_list
        self.total_occurences = sum([i.occurences for i in self.sequence_list])

    def __repr__(self):
        blank_spaces = [self.sequence_list[0].sequence.index(i.sequence)*' ' for i in self.sequence_list]
        blank_spaces_and_sequences = list(zip(blank_spaces, self.sequence_list))
        blank_spaces_and_sequences = [i[0] + str(i[1]) for i in blank_spaces_and_sequences]
        blank_spaces_and_sequences = '\n'.join(blank_spaces_and_sequences)
        return '>sequence_clutser'+'\t'+str(self.total_occurences)+'\n'\
               + blank_spaces_and_sequences+'\n'+'----------'+'\n'


def read_data(input_path):
    sequence_dict = dict()
    for i in range(1, 16):
        my_dict = dict()
        if os.path.getsize(input_path+'/length_'+str(i)+'.tsv') != 0:
            with open(input_path+'/length_'+str(i)+'.tsv') as in_file:
                for line in in_file:
                    line = line.strip().split('\t')
                    sequence = line[0]
                    occurences = int(line[1])
                    my_dict[sequence] = Sequence(sequence, occurences)
            sequence_dict['length_'+str(i)] = my_dict
    length_list = sorted([int(i.split('_')[-1]) for i in list(sequence_dict.keys())], reverse=True)
    return sequence_dict, length_list


def create_connections(length_list, sequence_dict):
    for u in length_list[:-1]:
        for i in sequence_dict['length_'+str(u)]:
            part_1 = i[0:-1]
            part_2 = i[1::]
            if part_1 in sequence_dict['length_'+str(u-1)]:
                sequence_dict['length_'+str(u)][i].children.append(part_1)
            if part_2 in sequence_dict['length_'+str(u-1)]:
                sequence_dict['length_'+str(u)][i].children.append(part_2)


def find_all_paths(sequence, sequence_dict):
    found = list()
    dictionary_of_interest = sequence_dict['length_' + str(len(sequence))]
    found.append(dictionary_of_interest[sequence])
    dictionary_of_interest[sequence].already_used = True
    if not dictionary_of_interest[sequence].children:
        return list(set(found))
    else:
        for i in dictionary_of_interest[sequence].children:
            found += find_all_paths(i, sequence_dict)
        return list(set(found))


def find_clusters(input_path, output_path):
    sequence_dict, length_list = read_data(input_path=input_path)
    create_connections(length_list=length_list, sequence_dict=sequence_dict)
    for i in length_list:
        with open(output_path+'/'+str(i), 'wt') as out_file:
            for k in sequence_dict['length_'+str(i)]:
                if not sequence_dict['length_' + str(i)][k].already_used:
                    out_file.write(str(Cluster(sorted(find_all_paths(sequence=k, sequence_dict=sequence_dict), reverse=True))))

if not os.path.exists('./../../results/find_clusters'):
    os.mkdir('./../../results/find_clusters')
find_clusters(input_path='./../../results/filtered_data', output_path='./../../results/find_clusters')
