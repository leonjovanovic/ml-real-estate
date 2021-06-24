import json

files = ['nekretnine_kuce.json', 'nekretnine_stanovi.json', '4zida_all.json']

def merge_JsonFiles(filename):
    result = list()
    for f1 in filename:
        with open(f1, 'r') as infile:
            result.extend(json.load(infile))
            print(infile)

    with open('merged.json', 'w') as output_file:
        output_file.write(
        '[' +
        ',\n'.join(json.dumps(i) for i in result) +
        ']\n')

merge_JsonFiles(files)