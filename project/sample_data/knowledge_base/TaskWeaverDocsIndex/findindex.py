import os

# Assuming the TaskWeaverDocsIndex directory is within the current working directory or a known parent directory 
# Replace 'your_known_directory' with the directory you expect to contain the TaskWeaverDocsIndex
known_directory = 'Knowledge_base'
index_directory_name = 'TaskWeaverDocsIndex'

# Search for the index directory
for root, dirs, files in os.walk(known_directory):
    if index_directory_name in dirs:
        index_directory_path = os.path.join(root, index_directory_name)
        break
else:
    index_directory_path = 'Index directory not found'

print(index_directory_path)
