import numpy as np 
import pandas as pd 
import os 
from PIL import Image

base_path=r'C:\Users\USER\Desktop\Dataset1\labels'
for file in os.listdir(base_path):
    location_of_label=r'C:\Users\USER\Desktop\Dataset1\labels\{}'.format(file)
    location_of_image=r'C:\Users\USER\Desktop\Dataset1\images\{}'.format(file)
    location_of_image=location_of_image[:-4]+'jpg'
    json_file=pd.read_json(location_of_label)
    image=Image.open(location_of_image)
    width,height=image.size
    for index,row in json_file.iterrows():
        sd=str(row['char_id'])+' '+str((row['x']+row['width']/2)/width)+' '+str((row['y']+row['height']/2)/height) +' '+str(row['width']/width) +' '+str(row['height']/height)
        f=open(location_of_label[:-5]+'.txt','a')
        f.write("{}\n".format(sd))
    os.remove(location_of_label)
    f.close()