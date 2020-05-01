'''This script can help you with moving the files having the same name from one directory to another. The trick is to find the base name from one of the directories, in my case I am finding the basename of labels'''

import os
import glob
import shutil


###Check this path before you proceed###
labels = glob.glob(os.path.join('label_2/', '*.' + 'txt'))


image_dir= 'image_2/'
velodyne_dir= 'velodyne/'
calib_dir= 'calib/'
planes_dir= 'planes/'


save_dir_images = 'real_images/'
save_dir_velodyne = 'real_velodyne/'
save_dir_calib = 'real_calib/'
save_dir_planes = 'real_planes/'

for index, ilabel in enumerate(labels):
    basename_labels = (ilabel.split('/')[-1]).split('.')[0]
        
    name_velodyne = basename_labels + '.bin'
    name_images = basename_labels + '.png'
    name_planes = basename_labels + '.txt'
    name_calib = basename_labels + '.txt'
	
    shutil.move(os.path.join(image_dir, name_images), os.path.join(save_dir_images, name_images)) 
    shutil.move(os.path.join(velodyne_dir, name_velodyne), os.path.join(save_dir_velodyne, name_velodyne)) 
    shutil.move(os.path.join(calib_dir, name_calib), os.path.join(save_dir_calib, name_calib)) 
    shutil.move(os.path.join(planes_dir, name_planes), os.path.join(save_dir_planes, name_planes)) 

print(index)


