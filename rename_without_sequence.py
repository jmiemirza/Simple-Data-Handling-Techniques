'''This script can be useful to rename all files in a directory in a series, for my case I wanted them to start from 0'''

import os

def rename():
   i = 0
   
   ####Check this path before proceeding###
   path="/mnt/data2/Customdataset_with_labels_rain/75mm/"
   for filename in os.listdir(path):
      my_dest ="" + str(i) + ".txt"
      my_source =path + filename
      my_dest =path + my_dest
      # rename() function will
      # rename all the files
      os.rename(my_source, my_dest)
      i += 1
# Driver Code
if __name__ == '__main__':
	rename()
