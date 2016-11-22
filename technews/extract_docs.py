import json
import re
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

english_stops = set(stopwords.words('english'))

def extract_docs(filename, output_dir):
    """
    filename: input json file
    outputdir: output directory to store docs
    """

    with open(filename, 'r') as f:
        i = 0
        for line in f:
            line = line.strip()
            if line == '':
                continue
            i += 1
            output_path = os.path.join(output_dir, 'doc' + str(i) + '.txt' )
            fields = json.loads(line)
            content = fields['content']
            re.sub(r'\n', ' ', content)
            content = content.strip()
            words = word_tokenize(content)
            words = [w for w in words if w not in english_stops]
            content = ' '.join(words)
            # print(content)
            fo = open(output_path, 'w')
            fo.write(content)
            fo.close()

if __name__ == '__main__':
    inputfile = 'webcontent.jl'
    outputdir = 'data'

    extract_docs(inputfile, outputdir)
