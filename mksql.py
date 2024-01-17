
"""
Convert a C-expression of a string concatenation to APL
"""
import re
import sys

with open(sys.argv[1]) as f:
    lines = [line.strip() for line in f]
 
p = re.compile(r'.*?([a-z]+)\s+=\s+\"(.*)\"')
m = p.match(lines[0])

if m:
    name = m.group(1)
    line1 = m.group(2).replace("'", '"')

    print(f"{name}  ← '{line1}'")

    for line in lines[1:]:
        d = line[1:-1].replace("'", '"')
        print(f"{name} ,← '{d}'")
