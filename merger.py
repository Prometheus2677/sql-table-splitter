import os

def merge_files_by_size(directory, output_file_size_limit):
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    files.sort(key=lambda x: os.path.getsize(x))

    merged_files = []
    current_size = 0
    current_files = []

    for file in files:
        file_size = os.path.getsize(file)
        if current_size + file_size <= output_file_size_limit:
            current_files.append(file)
            current_size += file_size
        else:
            # Merge current files into a new file
            with open('merged_file_{}.sql'.format(len(merged_files)), 'wb') as output_file:
                for f in current_files:
                    with open(f, 'rb') as input_file:
                        output_file.write(input_file.read())
                merged_files.append('merged_file_{}.sql'.format(len(merged_files)))
            current_files = [file]
            current_size = file_size

    # Merge any remaining files
    if current_files:
        with open('merged_file_{}.sql'.format(len(merged_files)), 'wb') as output_file:
            for f in current_files:
                with open(f, 'rb') as input_file:
                    output_file.write(input_file.read())
            merged_files.append('merged_file_{}.sql'.format(len(merged_files)))

    return merged_files

directory = "db"
output_file_size_limit = 40 * 1024 * 1024  # 40 MB in bytes

merged_files = merge_files_by_size(directory, output_file_size_limit)
print("Merged files:", merged_files)