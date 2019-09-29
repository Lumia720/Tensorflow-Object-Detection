# This script simply resizes all the images in a folder to one-eigth their
# original size. It's useful for shrinking large cell phone pictures down
# to a size that's more manageable for model training.

# Usage: in anaconda promt call python resizer.py --image_dir="address of the folder with the photos"
# and then run it.
# in the code here we resize all photos which size is larger than 
# thrsize bytes

import numpy as np
import cv2
import os
import tensorflow as tf

#dir_path = os.getcwd()
flags = tf.app.flags
flags.DEFINE_string('image_dir', '', 'Path to images')
FLAGS = flags.FLAGS

thrsize = 302000
for filename in os.listdir(FLAGS.image_dir): 
    # If the images are not .JPG images, change the line below to match the image type.
    if filename.endswith(".JPG"):
        if os.stat(FLAGS.image_dir + "/" + filename).st_size > thrsize:
            print(os.stat(FLAGS.image_dir + "/" + filename).st_size)
            old_size = os.stat(FLAGS.image_dir + "/" + filename).st_size
            image = cv2.imread(FLAGS.image_dir + "/" + filename)
            resized = cv2.resize(image,None,fx = 0.8, fy= 0.8, interpolation=cv2.INTER_AREA)
            #resized = cv2.resize(image,None,fx = thrsize/old_size, fy= thrsize/old_size, interpolation=cv2.INTER_AREA)
            cv2.imwrite(FLAGS.image_dir + "/" + filename,resized)
            print(os.stat(FLAGS.image_dir + "/" + filename).st_size)
            