import os
from keywords import words

dir = 'C:\\Users\\Public\\Documents\\dev\\git\\'
extension = '.js'
print('Scanning directory:' + dir)
print('Scanning files with extension:' + extension)

for root, _, files in os.walk(dir):
    for path in filter(lambda p: p.endswith(extension), files):
        with open(os.path.join(root, path), encoding="utf8") as f:
            for i, line in enumerate(f.readlines()):
                for word in filter(lambda w: w in line, words):
                    #print(f'{path}, {i+1}, {word}')
                    print(f'{path}, {i+1}, {word}, {line.strip()}')