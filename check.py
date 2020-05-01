'''This is for a very specific application. Where I wanted to check for the empty labels which were present in my labels folder. After checking the empty labels I wanted to remove the corresponding files in the other directories as well.'''


import glob  
import os
import shutil
import sys

###Give the exisiting labels directory###
labels= glob.glob(os.path.join('label_2/', '*.' + 'txt'))

###Change this to your own directory###
dest = 'empty_labels/'

print(len(labels))
i=0
for label,alabels in enumerate(labels):
    labels[label] = (alabels.split('/')[-1]).split('.')[0]
    if os.stat(alabels).st_size == 0:
        print(labels)
        os.remove('label_2/'+labels[label]+'.txt')
        os.remove('image_2/'+labels[label]+'.png')
        os.remove('calib/'+labels[label]+'.txt')
        os.remove('velodyne/'+labels[label]+'.bin')
