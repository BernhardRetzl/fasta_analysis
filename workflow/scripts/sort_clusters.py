import glob
import os


class Cluster:
    def __init__(self, occurences, rest):
        self.occurences = occurences
        self.rest = rest

    def __lt__(self, other):
        return self.occurences < other.occurences

    def __eq__(self, other):
        return self.occurences == other.occurences

    def __repr__(self):
        return str(self.occurences) + '\n'+''.join(self.rest)


def sort_clusters(input_path, output_path):
    cluster_list = list()

    with open(input_path) as in_file:
        cluster = list()
        for line in in_file:
            cluster.append(line)
            if line.startswith('-'):
                occurences = int(cluster[0].split('\t')[-1])
                rest = cluster[1::]
                cluster_list.append(Cluster(occurences, rest))
                cluster = list()

    cluster_list.sort(reverse=True)
    counter = 0
    with open(output_path, 'wt') as out_file:
        for i in cluster_list:
            counter += 1
            out_file.write('>sequence_cluster '+str(counter)+'\n'+str(i))


if not os.path.exists('./../../results/sorted_clusters'):
    os.mkdir('./../../results/sorted_clusters')
file_list = glob.glob('./../../results/find_clusters/*')
file_list = [i for i in file_list if os.path.getsize(i) != 0]
for file in file_list:
    number = file.split('/')[-1]
    sort_clusters(input_path=file, output_path='./../../results/sorted_clusters/'+number)
