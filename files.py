"""
Examples with text files
"""

f = open("models.txt", 'w')
f.write('asdf')

data = ['1\n', '2\n', '3']
f.writelines(data)
f.close()

# with open('models.txt', 'w') as f:
#     f.write('asdf')

"""
reading file
"""
with open('models.txt', 'r') as f:
    result = f.readline()
    print(result)
    result = f.readline()
    print(result)

with open('models.txt', 'r') as f:
    for line in f:
        result = line
        print(result)
