from glob import glob;from os import getcwd,remove
def incept(a):return sum([sorted(glob(i+'._*'))+incept(sorted(glob(i+'*\\')))for i in a],[])
for i in incept([getcwd()]):print(i,remove(i))
