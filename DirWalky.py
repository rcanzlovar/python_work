#!/usr/bin/env python
#ch  We only need to import this module
import os.path
 
# The top argument for walk. The
# Python27/Lib/site-packages folder in my case
 
topdir = 'mp3s/'
topdir = '/mnt/e/Media/Audio/'
 
# The arg argument for walk, and subsequently ext for step
exten = '.m4a'
 
print (exten)
print (topdir)


def step(ext, dirname):
# def step(ext, dirname, names):
    ext = ext.lower()
 
     # Get the absolute path of the movie_directory parameter
    mydir = os.path.abspath(dirname)
    print ("mydir"+mydir)
 
    # Get a list of files in movie_directory
    names = os.listdir(mydir)

    for name in names:
#    	print ("name "+name)
        if name.lower().endswith(ext):
    	    print ("isname "+name)
            print(os.path.join(dirname, name))
        else:
    	    print ("notname "+name)
            print(os.path.join(name, dirname))

# Start the walk
step(exten,topdir)