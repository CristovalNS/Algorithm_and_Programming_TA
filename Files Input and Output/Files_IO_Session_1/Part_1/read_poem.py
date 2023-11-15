poem = open("Jabberwocky.txt", "r")

for line in poem:
    # print(line, end='')
    print(line.rstrip())

poem.close()
