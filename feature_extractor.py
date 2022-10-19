DATA_DIRECTORY = 'feature_vectors/'


import os

# Get list of files to read
files_list = os.listdir(DATA_DIRECTORY)
files_list.sort()

count = 0

features = set()

for file in files_list:
    if count % 5000 == 0:
        print('.', end='', flush=True)
    with open('{}{}'.format(DATA_DIRECTORY, file), 'r') as infile:
        lines = (infile.read().strip().split('\n'))
        features.update(lines)
    count += 1

print()
print(len(features))