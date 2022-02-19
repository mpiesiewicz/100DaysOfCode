
# during this day we will mainly use the methods above to add high score system to snake game

# read from file
with open('newfile.txt', 'w') as file:
    file.write('Some text inside the document')

with open('newfile.txt', 'r') as file:
    text = file.read()
    print(text)

with open('newfile.txt', 'a') as file:
    file.write('\nadd another line to text')

with open('newfile.txt', 'r') as file:
    text = file.read()
    print(text)


