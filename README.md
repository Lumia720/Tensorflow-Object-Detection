# Tensorflow-Object-Detection
Object detection for wild life animals monitoring
The objective of the task was to create a program to classify wild-life animals from the
photos taken by hunter cameras. The program (the first version of it) is using a TensorFlowtrained classifier to detection. The model was retrained for the specified task using images
from Loimaa 2017, plus additional data of species called ‘Roe deer’. I have used Single Shot
Multibox Detector (SSD) neural network system.
The results of object detector model are shown in object_detection_methods_4_wl_species_monitoring.pdf. The program draws boxes
around detected animals and identifies species of the animals.
Initial observations show that the part model of identification the species works well,
however, detecting part of model that draws boxes has some room for improvements: in
many cases it fails to detect animals.
Tthe work on describing statistics of the model is not completed. This is some work
for the future.
