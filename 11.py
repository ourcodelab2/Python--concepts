file1 = 'file1.txt'
file2 = 'file2.txt'
file3 = 'merged_file.txt'
with open(file1, 'r') as f1, open(file2, 'r') as f2, open(file3, 'w') as f3:
f3.write(f1.read())
f3.write("\n") # Optional: Adding a newline between the contents
f3.write(f2.read())
print("Files merged successfully.")