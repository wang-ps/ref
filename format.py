import sys

filename = sys.argv[1] if len(sys.argv) > 1 else 'reference.bib'

with open(filename, 'r', encoding='UTF-8') as fid:
  lines = fid.readlines()

output = []
for line in lines:
  if line == '\n':
    continue
  elif line.startswith('@') and not line.startswith('@String'):
    output.append('\n')
    output.append(line)
  else:
    output.append(line)

with open(filename, 'w', encoding='UTF-8') as fid:
  fid.writelines(output)
