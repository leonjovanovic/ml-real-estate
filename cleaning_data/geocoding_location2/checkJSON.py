import json

with open('location2_coords_Belgrade.json', 'r') as infile:
    result = json.load(infile)

with open('location2_coords_.json', 'r') as infile:
    result1 = json.load(infile)

for r, r1 in zip(result, result1):
    li = list(r)
    li1 = list(r1)
    for l, l1 in zip(li, li1):
        if r[l] is None:
            r[l] = r[l1]

with open('location2_coords_result.json', 'w') as output_file:
    output_file.write(
        '[' +
        json.dumps(result, indent=4) +
        ']\n')
