from collections import OrderedDict
import argparse

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
            if line.strip():
                yield line.strip().decode('utf-8')       
                       
def combine_into_dict(lines):
    for lines in zip(*lines):
        target = OrderedDict(number='', time='', lines='')
        if lines[0].isdigit():
            line_number = lines[0]
            target['number'] = line_number
        elif '-->' in lines[0]:
            target['time'] = lines[0]
        else:
            target['lines'] = [line for line in lines]
        yield target
        
def write_combined_file(name, combined_subtitles):
    with open('%s.srt' % name, 'w') as f:
        for item in combined_subtitles:
            f.write(item['number'].encode('utf-8'))
            f.write(item['time'].encode('utf-8'))
            for line in item['lines']:
                f.write(line.encode('utf-8'))
                f.write(u'\n')
            f.write(u'\n') 
    print "===> Combined subtitles into a file named '%s.srt'" % name                   

#actual processing workflow
args = parser.parse_args()
lines = read_files(args.files)
combined_subtitles = combine_into_dict(lines) 
write_combined_file(args.title, combined_subtitles)

            
        
   
            