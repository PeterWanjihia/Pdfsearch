import os

def crawl_directories(root_dir, log_file):
    total_size = 0
    with open(log_file, 'w') as main_log:
        python_log = open("python.txt", 'w')
        cpp_log = open("cpp.txt", 'w')
        js_log = open("js.txt","w")
        c_log = open("c.txt","w")
        java_log = open("java.txt", 'w')

        for dirpath, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith('.pdf') or filename.endswith('.epub'):
                    file_path = os.path.join(dirpath, filename)
                    file_size = os.path.getsize(file_path)
                    main_log.write(f"{file_path} ({file_size} bytes)\n")
                    total_size += file_size

                    if "python" in filename.lower():
                        python_log.write(f"{file_path} ({file_size} bytes)\n")
                    elif "c++" in filename.lower():
                        cpp_log.write(f"{file_path} ({file_size} bytes)\n")
                    elif " c " in filename.lower():
                        c_log.write(f"{file_path} ({file_size} bytes)\n")
                    elif "javascript" in filename.lower():
                        js_log.write(f"{file_path}  ({file_size}  bytes)\n") 
                    
                    elif "java" in filename.lower():
                        java_log.write(f"{file_path} ({file_size} bytes)\n")

        python_log.close()
        cpp_log.close()
        js_log.close()
        c_log.close()
        java_log.close()

    print(f"Total space occupied by PDF and EPUB files: {total_size} bytes")

if __name__ == '__main__':
    root_directory = '/home/moringa'
    log_filename = 'file_log.txt'
    crawl_directories(root_directory, log_filename)