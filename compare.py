'''A simple script to compare the files in two directories and move the common ones from one directory to another. Comes in handy when you want to have same files in the corresponding directories'''

import os
import glob
import shutil

###Exisiting labels directory.. Needs to be edited###
image_labels = glob.glob(
    os.path.join('image_2/', '*.' + 'jpg'))


velod_dir = 'label_2/'
save_dir = 'new_labels/'

for index, ilabel in enumerate(image_labels):
    base = (ilabel.split('/')[-1]).split('.')[0]
    name = base+ '.txt'
	
    shutil.move(os.path.join(velod_dir, name), os.path.join(save_dir, name)) 

print(index)

