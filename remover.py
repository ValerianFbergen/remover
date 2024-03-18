#! /usr/bin/env python3
from argparse import ArgumentParser
from sys import argv
arg=ArgumentParser(description='''
Recursively search and optionally delete files using built-in or user-specified wildcards.
Useful for removing hidden temp files files placed by Mac OS (._* and .DS_STORE) and MS Office (~$*)\n
''',epilog='at least one of -w, -mac, -ds, -mso, -tmp arguments/flags must be specified')
arg.version=1.0
#arg.add_argument('-v','-version',action='version')
arg.add_argument('-mac',action='store_true',dest='mac',help='Cleanup ._* files')
arg.add_argument('-ds',action='store_true',dest='ds',help='Cleanup .DS_STORE')
arg.add_argument('-mso',action='store_true',dest='mso',help='Cleanup ~$*')
arg.add_argument('-tmp',action='store_true',dest='tmp',help='Cleanup *.tmp')
arg.add_argument('-w','-wildcard',dest='wildcard',metavar='TEXT',help='Input custom wildcard')
arg.add_argument('-r','-remove',dest='rm',action='store_true',help='Remove found files. Disabled by default.')
arg.add_argument('-s','-stat',dest='stat',action='store_true',help='Show statistics instead of filenames.')
arg.add_argument('-q','-quiet',dest='quiet',action='store_true',help='Quiet mode - suppress output')
arg.add_argument('filepath',nargs='+',help='Specify one or more filepaths for cleanup')
if len(argv)==1:arg.print_help();exit()
args=arg.parse_args()
code={'.DS_STORE':args.ds,'._*':args.mac,'~$*':args.mso,'*.tmp':args.tmp}
wild=([args.wildcard]if args.wildcard else[])+[i for i in code if code[i]]
if not any(wild):arg.print_help();exit()
if any((i in'C:/')for i in args.filepath) and args.rm:
    if '*'in wild:print('What do you think you are doing!?');exit()
    if input('One or more filepaths specified contains system root (C: or /)!\nProceed with EXTREME CAUTION!\nAre you sure whatever you are doing is worth it?\n(Y/N):').upper()[0]!='Y':exit()
    if input('Are you sure?\n(Y/N):').upper()[0]!='Y':exit()
    print('Prepare for unforeseen consequences...')
from glob import glob;from os import getcwd,remove,sep
print(wild,args.filepath)
def incept(a,w):return sum([sorted(glob(i+w))+incept(sorted(glob(i+'*'+sep)),w)for i in a],[])
if args.quiet:print=lambda*a,**kw:None
total=d=0
for i in wild:
    lst=incept(args.filepath,i)
    total+=len(lst)
    for j in lst:
        if args.rm:
            try:remove(i);d+=1
            except:continue
        if not args.stat:print('\n'.join(lst))
if args.stat:
    print('Total:',total)
    if args.rm:print('Deleted:',d)
