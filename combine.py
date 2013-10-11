
from collections import OrderedDict
import argparse


def process_filenames(filenames_list):
    for name in filenames_list:
        yield name
        
def read_file(names):
    for name in names:
        yield read_subs(name)

def read_subs(sub_file):
    with open(sub_file, 'rt') as f: 
        for line in f:
            if line.strip():
                yield line.strip().decode('utf-8')
                
def combine(files):
    subs = OrderedDict()
    line_number = None
    for lines in zip(*files):
        if lines[0].isdigit():
            subs[lines[0]] = {}
            line_number = lines[0]
        elif '-->' in lines[0]:
            subs[line_number]['time'] = lines[0]
        else:
            subs[line_number]['lines'] = [ line for line in lines]
    for item in subs.items():
        yield item
        
def create_combined_file(name, combined_subtitles):
    with open('%s.srt' % name, 'w') as f:
        for item in combined_subtitles:
            f.write(item[0])
            f.write('\n')
            f.write(item[1]['time'].encode('utf-8'))
            f.write('\n')
            for line in item[1]['lines']:
                f.write(line.encode('utf-8'))
                f.write('\n')
            f.write('\n')
    

parser = argparse.ArgumentParser(description='Process some subtitles.')
parser.add_argument('--files', type=str, metavar='Names', nargs='+', 
                       help='the name of the subtitle files, without comma separation but within single brackets')
parser.add_argument('--title', type=str, metavar='Title', nargs='?', 
                       help='the title of movie within single brackets, used for the name of the generated file')                       

args = parser.parse_args()
file_names = process_filenames(args.files)
files = read_file(file_names)
combined_subtitles = combine(files) 
create_combined_file(args.title, combined_subtitles)

            
        
   
            