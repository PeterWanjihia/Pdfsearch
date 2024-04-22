import os

def crawl_directories(root_dir, log_file):
    total_size = 0
    with open(log_file, 'w') as log:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith('.pdf') or filename.endswith('.epub'):
                    file_path = os.path.join(dirpath, filename)
                    file_size = os.path.getsize(file_path)
                    log.write(f"{file_path} ({file_size} bytes)\n")
                    total_size += file_size

    print(f"Total space occupied by PDF and EPUB files: {total_size} bytes")

if __name__ == '__main__':
    root_directory = '/home/moringa'
    log_filename = 'file_log.txt'
    crawl_directories(root_directory, log_filename)