'''In autonomous driving the Kitti dataset is perhaps the most famous dataset available. I recently ran in to trouble with renaming one of my directories to the kitti format in a sequential manner so that the labels and images will correspond to the same thing.'''

import os
import glob
import shutil


###Check these paths before you proceed###
image_labels = glob.glob(
    os.path.join('image_2/', '*.' + 'png'))

image_dir = 'image_2/'
planes_dir = 'planes_2/'

i = 0

for aindex, alabel in enumerate(image_labels):
    base_name_images = (alabel.split('/')[-1]).split('.')[0]    

    my_dest_planes ="" + str(i).zfill(6) + ".txt"


    my_source_planes =label_dir + base_name_labels + '.txt'


    my_dest_images =image_dir + my_dest_images

    os.rename(my_source_labels, my_dest_labels)

            
    i += 1        
    	     

