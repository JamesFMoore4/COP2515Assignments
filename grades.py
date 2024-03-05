# Open grades.csv
with open('grades.csv') as grades:
  # Read file contents
  lines = grades.readlines()

  # Read in column headings
  heading = []
  entries = lines[0].rstrip().split(',')
  for e in entries:
    heading.append(e)

  avgs = [0 for i in heading]
  for row in range(1, len(lines)):  # skip first row
    entries = lines[row].split(sep=',')
    for col in range(2, len(entries)): # skip first 2 columns
      avgs[col] += int(entries[col])

  # Output all grade averages to 2 decimal places
  numrows = len(lines) - 1
  numcols = len(heading)
  for i in range(2, numcols):
    print(f'{heading[i]}:  {avgs[i] / numrows:.2f}')

#Closes file automatically!
