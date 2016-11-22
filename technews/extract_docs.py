import json
import re
import os

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
            # print(content)
            fo = open(output_path, 'w')
            fo.write(content)
            fo.close()

if __name__ == '__main__':
    inputfile = 'webcontent.jl'
    outputdir = 'data'

    extract_docs(inputfile, outputdir)
