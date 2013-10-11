
from collections import OrderedDict

def read_subs(sub_file):
    with open(sub_file, 'rt') as f: 
        for line in f:
            if line.strip():
                yield line.strip().decode('utf-8')
                
def combine_in_dict(pinyin=None, traditional=None):
    subs = OrderedDict()
    line_number = None
    for lines in zip(pinyin, traditional):
        if lines[0].isdigit():
            subs[lines[0]] = {}
            line_number = lines[0]
        elif '-->' in lines[0]:
            subs[line_number]['time'] = lines[0]
        else:
            subs[line_number]['pinyin'] = lines[0]
            subs[line_number]['traditional'] = lines[1]
    return subs
                
            
if __name__ == '__main__':
    print 'reading'
    traditional = read_subs('Crouching Tiger Hidden Dragon.srt')
    pinyin = read_subs('Crouching_Tiger_Hidden_Dragon.Pinyin.srt')
    subs = combine_in_dict(pinyin=pinyin, traditional=traditional) 
    with open('combined.srt', 'w') as f:
        for item in subs.items():
            f.write(item[0])
            f.write('\n')
            f.write(item[1]['time'].encode('utf-8'))
            f.write('\n')
            f.write(item[1]['traditional'].encode('utf-8'))
            f.write('\n')
            f.write(item[1]['pinyin'].encode('utf-8'))
            f.write('\n')
            f.write('\n')
            
        
   
            