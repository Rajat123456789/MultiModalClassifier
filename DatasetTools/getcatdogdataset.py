import tensorflow as tf
import pathlib
import PIL
import PIL.Image
import os

new_dir = os.chdir("/Users/rajatsharma/Documents/Semester 2/Deep Learning/HW2")
print(new_dir)

_URL = 'https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'

new_path = "/Users/rajatsharma/Documents/Semester 2/Deep Learning/HW2"

file_name = _URL.split('/')[-1]

new_zip_path = os.path.join(new_path, file_name)

path_to_zip = tf.keras.utils.get_file(file_name, origin=_URL, extract=True, cache_subdir=new_path)

print(new_path)

PATH = os.path.join(new_path, 'cats_and_dogs_filtered')
train_dir = os.path.join(PATH, 'train')
validation_dir = os.path.join(PATH, 'validation')

train_dir = pathlib.Path(train_dir)
print(train_dir) 
image_count = len(list(train_dir.glob('*/*.jpg')))
print(image_count) #2000
