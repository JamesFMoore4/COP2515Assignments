# File writer program

# Prompt for file name
name = input('What file would you like to write? ')

with open(name, mode='w') as file:
  line = input('Type a line for the file: ')
  while line != '':
    # Prompt for line
    file.write(line + '\n')
    line = input('Type a line for the file: ')
  # Repeat until empty string ('')

