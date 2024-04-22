import os
import math

def split_log_file(log_file, output_files):
    with open(log_file, 'r') as log:
        file_paths = log.readlines()

    num_files = len(file_paths)
    chunk_size = math.ceil(num_files / 4)

    for i in range(4):
        start = i * chunk_size
        end = start + chunk_size
        chunk = file_paths[start:end]
        with open(output_files[i], 'w') as out_file:
            out_file.writelines(chunk)

if __name__ == '__main__':
    log_file = 'file_log.txt'
    output_files = ['log1.txt', 'log2.txt', 'log3.txt', 'log4.txt']
    split_log_file(log_file, output_files)