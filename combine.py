
from collections import OrderedDict
import argparse

#setting up the command line parser
parser = argparse.ArgumentParser(description='Process some subtitles.')
parser.add_argument('--files', type=str, metavar='Names', nargs='+', 
                       help='the name of the subtitle files, without comma separation but within single brackets')
parser.add_argument('--title', type=str, metavar='Title', nargs='?', 
                       help='the title of movie within single brackets, used for the name of the generated file')   

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
            line_number = lines[0]
            subs[line_number] = {}
            subs[line_number]['number'] = line_number
        elif '-->' in lines[0]:
            subs[line_number]['time'] = lines[0]
        else:
            subs[line_number]['lines'] = [ line for line in lines]
    for item in subs.items():
        yield item[1]
        
def write_combined_file(name, combined_subtitles):
    with open('%s.srt' % name, 'w') as f:
        for item in combined_subtitles:
            f.write(item['number'].encode('utf-8'))
            f.write(u'\n')
            f.write(item['time'].encode('utf-8'))
            f.write(u'\n')
            for line in item['lines']:
                f.write(line.encode('utf-8'))
                f.write(u'\n')
            f.write(u'\n')                    

#actual processing workflow
args = parser.parse_args()
file_names = process_filenames(args.files)
files = read_file(file_names)
combined_subtitles = combine(files) 
write_combined_file(args.title, combined_subtitles)

            
        
   
            