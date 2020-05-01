'''This script can help you rename files in different directories in a sequential manner. I had the trouble while working with datasets and when I wanted to rename for instance the labels and corresponding images. The trick again is to find the basename from one of the directories and then try to manipulate the other files in other directories'''

import os
import glob
import shutil


###Check these paths before you proceed###
image_labels = glob.glob(
    os.path.join('image_2/', '*.' + 'png'))


image_dir = 'image_2/'
label_dir = 'label_2/'
calib_dir = 'calib/' 
velodyne_dir = 'velodyne/'
i = 0


for aindex, alabel in enumerate(image_labels):
    base_name_images = (alabel.split('/')[-1]).split('.')[0]    
    base_name_labels = base_name_images
    base_name_calib  = base_name_images
    base_name_velodyne = base_name_images        
    
    my_dest_labels ="" + str(i) + ".txt"
    my_dest_images ="" + str(i) + ".png"
    my_dest_calib ="" + str(i) + ".txt"
    my_dest_velodyne ="" + str(i) + ".bin"

    my_source_labels =label_dir + base_name_labels + '.txt'
    my_source_images =image_dir + base_name_images + '.png'
    my_source_calib =calib_dir + base_name_calib + '.txt'
    my_source_velodyne =velodyne_dir + base_name_velodyne + '.bin' 

    my_dest_images =image_dir + my_dest_images
    my_dest_labels =label_dir + my_dest_labels
    my_dest_calib =calib_dir + my_dest_calib
    my_dest_velodyne =velodyne_dir + my_dest_velodyne

    os.rename(my_source_labels, my_dest_labels)
    os.rename(my_source_images, my_dest_images)
    os.rename(my_source_calib, my_dest_calib)
    os.rename(my_source_velodyne, my_dest_velodyne)
            
    i += 1        
    	     

