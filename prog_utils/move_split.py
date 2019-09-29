# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 10:07:32 2019

@author: 03081182
Open folder with images and xml docs
randomly shuffle them into 20 and 80% into cross-validation/training sets
"""

import os
import shutil
import numpy as np
import tensorflow as tf

def makeFolders(file_dir, dir_tr_te):
    for dir_t in dir_tr_te:    
        direc = file_dir + "/" + dir_t  #+ "/" + dir_t
        if not os.path.exists(direc):
            os.mkdir(direc) 
                        
#Moves file to its proper folder and delete any duplicates
def moveFile(moveFile, file_direc_old, direc):
    srcPath = file_direc_old + "/" + moveFile
    dstPath = file_direc_old + "/" + direc +"/" + moveFile
    if os.path.isfile(srcPath):
        if not os.path.isfile(dstPath):
            shutil.copy2(srcPath, dstPath)

    #If the file doesn't have a duplicate in the new folder, move it
    
    
            #If the file already exists with that name and has the same md5 sum
    
def main():
    flags = tf.app.flags
    flags.DEFINE_string('image_dir', '', 'Path to images')
    FLAGS = flags.FLAGS
    dir_tr_te = {"Train", "Test"}
    makeFolders(FLAGS.image_dir, dir_tr_te)      
  

    # first check if there is a raindeer
    # if it ONE  then split all picture with one reinderr into folders of gender and age
    # esle, send the photo to multiple folder
    # else = If there is  no reindeer, check if the image is empty 5377
    # else if the image is not empty, send the image into a cathegory it belongs to
    summis=0
    for filename in os.listdir(FLAGS.image_dir):
        if np.random.random(1)[0] >= 0.1: 
            direc = "Train" 
        else: 
            direc = "Test"
        if filename.endswith(".JPG"):
            moveFile(filename, FLAGS.image_dir, direc)
            xmlname = filename[:-3] + 'xml'
            if not os.path.isfile(FLAGS.image_dir + "/" + xmlname):
                print("no ", xmlname)
                summis=summis + 1
            moveFile(xmlname, FLAGS.image_dir, direc)
    print("ready ", summis)

main()
