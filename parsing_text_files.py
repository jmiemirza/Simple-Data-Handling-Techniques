'''This script gives you an example of parsing .txt files and then changing a specific entry from float to int. This is again very problem specific but can give you a reasonable starting point'''


import os
import glob 


###Check these paths before you proceed###
save_path = '/mnt/data2/pointpillars/second.pytorch/second/data/astar_3d_night/training/labels_2/'

file_paths = glob.glob('/mnt/data2/pointpillars/second.pytorch/second/data/astar_3d_night/training/wrong_labels/*.txt')



for filename in file_paths:
    
    base_name = filename.split('/')[-1]
    save_name = save_path+ base_name 
    label_original = open(filename, 'r')
    
    f =  open(save_name, 'wb')

    for line in label_original:
        line = line.strip()
        l = line.split(' ')
        l[2] = int(float(l[2]))
        l = [str(x) + ' '  for x in l]

        s = "".join(l)
        f.write(s.encode('utf-8'))  
        f.write('\n'.encode('utf-8'))


    f.close()
    label_original.close()


