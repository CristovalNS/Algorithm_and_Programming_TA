# With
with open("Jabberwocky.txt", "r") as jabber:
    for line in jabber:
        print(line.rstrip())

# Readlines
with open("Jabberwocky.txt", "r") as jabber:
    lines = jabber.readlines()

print(lines)
print(lines[-1:])

for line in reversed(lines):
    print(line.rstrip())

# Read

with open("Jabberwocky.txt", "r") as jabber:
    text = jabber.read()

print(text)

for character in reversed(text):
    print(character, end="")

# Readline

with open("Jabberwocky.txt") as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break

# Equivalent code
with open("Jabberwocky.txt") as jabber:
    for line in jabber:
        print(line.rstrip())
        if 'jubjub' in line.casefold():
            break