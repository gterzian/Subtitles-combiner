
import argparse
from itertools import izip

#setting up the command line parser
parser = argparse.ArgumentParser(description='Process some subtitles.')
parser.add_argument('--files', type=str, metavar='Names', nargs='+', 
                       help='the name of the subtitle files, without comma separation but within single brackets')
parser.add_argument('--title', type=str, metavar='Title', nargs='?', 
                       help='the title of movie within single brackets, used for the name of the generated file')   

def read_files(names):
    for name in names:
        yield read_subs(name)

def read_subs(sub_file):
    with open(sub_file, 'rt') as f: 
        for line in f:
            striped = line.strip()
            if striped:
                yield striped.decode('utf-8')     
                        
def combine(lines):
    for lines in izip(*lines):
        if lines[0].isdigit():
            yield lines[0]
        elif '-->' in lines[0]:
            yield lines[0]
        else:
            for line in lines:
                yield line
          
def write_combined_file(name, combined_subtitles):
    with open('%s.srt' % name, 'w') as f:
        for line in combined_subtitles:
            f.write(line.encode('utf-8'))
            f.write(u'\n') 
                       

#actual processing workflow
args = parser.parse_args()
readers = read_files(args.files)
combined_subtitles = combine(readers) 
write_combined_file(args.title, combined_subtitles)
print "===> Combined subtitles into a file named '%s.srt'" % args.title



            
        
   
            