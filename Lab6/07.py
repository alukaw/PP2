source_file = r"source.txt"
destination_file = r"destination.txt"

with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
    dest.write(src.read())
