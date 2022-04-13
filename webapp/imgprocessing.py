from skimage.io import imread, imshow
from skimage import transform
from skimage import color
import numpy as np
import pandas as pd

def getPixelAsRowVector():
    img = imread(r"C:\Users\mitug\Pneumonia-Detection-System\webapp\static\images\xray.jpg")
    img = transform.resize(img,(50,50))
    img = np.reshape(img,(1,-1))
    print(np.shape(img))
    return pd.DataFrame(img)

