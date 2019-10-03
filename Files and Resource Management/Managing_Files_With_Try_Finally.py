import sys
from itertools import count, islice

def sequence():
    seen = set()
    a=0
    for n in count(1):
        yield a
        seen.add(a)
        c=a-n
        if c < 0 or c in seen:
            c=a+n
        a=c

def write_sequence(filename, num):
    f=open(file=filename, mode='wt',encoding='utf-8')
    f.write('Starting \n')
    f.writelines("{0} \n".format (r) for  r in islice(sequence (), int(num) +1 ))
    f.write('Finished \n')
    f.close()

if __name__=='__main__':
    write_sequence(filename=sys.argv[1],num=sys.argv[2])