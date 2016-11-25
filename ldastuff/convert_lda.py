import os
import sys
from os import listdir
from os.path import isfile
from nltk import word_tokenize
from make_vocab import clean, is_bad
from collections import defaultdict

def load_vocab(filename):
    vocab = {}
    i = 0
    with open(filename, 'r') as f:
        for w in f:
            w = w.strip()
            if w == '':
                continue
            vocab[w] = i
            i += 1
    return vocab

def convert_lda(input_dir, output_file, vocab):
    vocab_dict = load_vocab(vocab)
    #print(vocab_dict)

    onlyfiles = [f for f in listdir(input_dir) if isfile(os.path.join(input_dir, f))]
    
    fo = open(output_file, 'w')
    for filename in onlyfiles:
        print(filename)
        freq = defaultdict(int)
        path = os.path.join(input_dir, filename)
        with open(path, 'r') as f:
            for line in f:
                line = line.strip()
                if line == '':
                    continue
                words = word_tokenize(line)
                for w in words:
                    w = clean(w)
                    if w in vocab_dict:
                        freq[vocab_dict[w]] += 1
            uniq_words = len(freq.keys())
            fo.write('%d ' % uniq_words)
            for idx, ff in freq.items():
                fo.write('%d:%d ' %(idx, ff))
            fo.write('\n')
    fo.close()

if __name__ == '__main__':
    INPUT_DIR   = './data'
    OUTPUT_FILE = './technews.dat'
    VOCAB       = 'vocab.txt'
    convert_lda(INPUT_DIR, OUTPUT_FILE, VOCAB)
