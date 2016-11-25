import os
import sys
import re
from os import listdir
from os.path import isfile
from nltk import word_tokenize

def clean(w):
    match = re.search(r'^[\.,;\(\)\*\#\$!&\'\"%\+-]*(.+)[\.,;\(\)\*\#\$!&\'\"%\+-]*$', w)
    if match:
        return match.group(1)
    return w

def is_bad(w):
    if re.search(r'^[\.,;\(\)\*\#\$!&\'\"%\+-]*$',w):
        return True
    if re.search(r'^[^a-zA-Z_]*$', w):
        return True
    return False

def extract_vocab(input_dir, output_file):
    onlyfiles = [f for f in listdir(input_dir) if isfile(os.path.join(input_dir, f))]
    vocab = {}
    for filename in onlyfiles:
        path = os.path.join(input_dir, filename)
        with open(path, 'r') as f:
            for line in f:
                line = line.strip()
                if line == '':
                    continue
                words = word_tokenize(line)
                for w in words:
                    w = clean(w)
                    if not is_bad(w):
                        vocab[w.lower()] = 1
    # print out vocabulary
    fo = open(output_file, 'w')
    for w in sorted( vocab.keys() ):
        fo.write('%s\n' % w)
    fo.close()


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 2:
        print('Usage: python %s <input_dir>  <output_vocab>' % sys.argv[0])
        sys.exit(1)

    input_dir   = args[0]
    output_file = args[1]
    extract_vocab(input_dir, output_file)
