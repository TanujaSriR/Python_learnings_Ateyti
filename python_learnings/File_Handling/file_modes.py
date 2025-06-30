def read_file(file_name):
    with open(file_name,'r')as file:
        content=file.read()
    return content
data1=read_file('sample_file.txt')
print(data1)
print("this is original data")
def append_file(file_name):
    with open(file_name,'a')as file:
        file.write('Hy i have written added this line in to the original file, succesfully added this line')
    return "added successfully"
append_file('sample_file.txt')
data2=read_file('sample_file.txt')
print(data2)
print("this is updated data")


