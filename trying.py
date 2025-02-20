import os

def find_files(directory, filename):
    total_files = 0
    files_to_search = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == filename:
                files_to_search.append(os.path.join(root, file))
            total_files += 1

    print("Finding...")

    for index, file_path in enumerate(files_to_search, 1):
        print(f"Found: {file_path}")

        try:
            with open(file_path, 'r') as f:
                content = f.read()
                print(f"Content of {file_path}:")
                print(content)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
        
        break  
        
        if index % 10 == 0: 
            print(f"Finding... ({index}/{total_files})")

find_files('C:\\', 'flag')
