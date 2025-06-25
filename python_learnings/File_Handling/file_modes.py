def read_file(file_name):
    with open(file_name,'r')as file:
        content=file.read()
    return content
data=read_file('sample_file.txt')
print(data)