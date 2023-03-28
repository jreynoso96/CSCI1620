'''with open('files/input.txt', 'r') as file:
    print(file.read())'''

x = open('files/input.txt', 'r')
print(x.readline())
content = x.readline()
x.close()
print(content)
print(x.readline())