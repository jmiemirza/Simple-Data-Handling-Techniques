# Simple-Data-Handling-Techniques
I will be sharing some simple data handling techniques in this repository. However, these scripts are very problem specific. Still they can be extended and can give you a headstart in adopting them to your own problems.

Just a brief description about each file: 

<b>1. check.py:</b> This is for a very specific application. Where I wanted to check for the empty labels which were present in my labels folder. After checking the empty labels I wanted to remove the corresponding files in the other directories as well.

<b>2. splitting_labels.py:</b> Helpful script to generate the train and validation splits.

<b>3. rename_with_sequence.py:</b> This script can help you rename files in different directories in a sequential manner. I had the trouble while working with datasets and when I wanted to rename for instance the labels and corresponding images. The trick again is to find the basename from one of the directories and then try to manipulate the other files in other directories.

<b>4. rename_without_sequence.py:</b> This script can be useful to rename all files in a directory in a series, for my case I wanted them to start from 0.

<b>5. parsing_text_files.py:</b> This script gives you an example of parsing .txt files and then changing a specific entry from float to int. This is again very problem specific but can give you a reasonable starting point.

<b>6. kitti_style_renaming.py:</b> In autonomous driving the Kitti dataset is perhaps the most famous dataset available. I recently ran in to trouble with renaming one of my directories to the kitti format in a sequential manner so that the labels and images will correspond to the same thing.

<b>7. moving_files.py:</b> This script can help you with moving the files having the same name from one directory to another. The trick is to find the base name from one of the directories, in my case I am finding the basename of labels.

<b>8. compare.py:</b> A simple script to compare the files in two directories and move the common ones from one directory to another. Comes in handy when you want to have same files in the corresponding directories.

<b>9. check_empty_files.py:</b> This simple script will simply check the empty labels files in the label directory and then move those particular files to another directory
