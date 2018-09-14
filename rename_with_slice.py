import os
import glob
#from sys import argv
#import sys,getopt
import sys

#filedir = ''
#new_file_name = ''
#try:
#   opts, agrs = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
#except getopt.GetoptError:
#   print ''

arglen = len(sys.argv)
if arglen != 4:
	print ' 1-dir,2-old_file_name_suffix,3-new_file_suffix'
	sys.exit(2)

dir = sys.argv[1]
old_file_name_suffix = sys.argv[2]
new_file_name_suffix = sys.argv[3]

if dir.strip()=='':
	print 'dir is null'
	sys.exit(2)
if old_file_name_suffix=='':
	print 'old_file_name_suffix is null'
	sys.exit(2)
if new_file_name_suffix=='':
	print 'new_file_name_suffix is null'
	sys.exit(2)

os.chdir(dir)
for file in glob.glob("*."+old_file_name_suffix):
    file_name = os.path.splitext(file)[0]
    extension = os.path.splitext(file)[1]
    new_file_name = file_name + "."+new_file_name_suffix
    try:
        os.rename(file, new_file_name)
    except OSError as e:
        print(e)
    else:
        print("Renamed {} to {}".format(file, new_file_name))
