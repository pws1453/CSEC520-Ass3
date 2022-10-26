import csv
import os
import random

os.mkdir('malware_vectors')
with open("sha256_family.csv") as csvfile:
    feature_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in feature_reader:
        hash = row[0].split(',')[0]
        if hash != "sha256":
            os.rename(f'feature_vectors/{hash}', f'malware_vectors/{hash}')


os.mkdir('benign_vectors')
list_of_benign = os.listdir('feature_vectors')
randints = random.sample(range(len(list_of_benign)),3000)
for num in randints:
    hash = list_of_benign[num]
    os.rename(f'feature_vectors/{hash}', f'benign_vectors/{hash}')
