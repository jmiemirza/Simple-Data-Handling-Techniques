'''This simple script will simply check the empty labels files in the label directory and then move those particular files to another directory'''

import glob  
import os
import shutil

###Give your labels directory###
labels= glob.glob('label_2/*.txt')

###Give the directory where you would like to move the empty files###
dest = 'empty_labels/'

print(len(labels))
i=0
for label,alabels in enumerate(labels):
    if os.stat(alabels).st_size == 0:
        shutil.move(alabels,dest)
        

