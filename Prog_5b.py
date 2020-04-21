#Given a path, traverse the path and display all files and subdirectories in each level till the deepest level.
# Also display total number of files and subdirectories.

import os

# Set the directory to start from
print("Enter path to traverse :", end="")
rootDir = input()
if (os.path.exists(rootDir)):
    dir_count = 0
    file_count = 0
    for dirName, subdirList, fileList in os.walk(rootDir):
        print('Found directory: %s' % dirName)
        # check to ignore starting directory while taking directory count
        # normpath returns the normalized path eliminating double slashes etc.
        if os.path.normpath(rootDir) != os.path.normpath(dirName):
            dir_count += 1
        for fname in fileList:
            file_count += 1
            print('\t%s' % fname)

    print("No: of subdirectories :", dir_count, end="")
    print("\nNo: of files :", file_count, end="")
else:
    print("Entered path doesn't exist")
