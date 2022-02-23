# Problem Statement 
This should be a brief description of the domain of your dataset (e.g. if it is the Titanic Dataset then write about the ship, the incident that happened, what you're trying to do with the data).
## Dataset

The dataset used is the [Name of the Dataset](Download link) from (source of download e.g Kaggle). If the task is a classification task, then you must specify the number of classes and give a 1 line description of each class as follows(example of Iris Dataset). 

The 3 class labels are:
<br>

**1. Iris Setosa:** Given iris flower belongs to the Setosa species
<br>
**2. Iris Virginica:** Given iris flower belongs to the Virginica species
<br>
**3. Iris Versicolor:** Given iris flower belongs to the Versicolor species

If the task is a regression task, then explain the target variable and give brief statistics.(e.g. Housing Prices)

**Target Variable: SalePrice**
<br>
<br>
Sale Price refers to the selling price of the house.
<br>
**Mean Selling Price:** 121,000$
<br>
**Max Selling Price:** 1,000,000$
<br>
**Min Selling Price:** 45,000$


## Model(s) Used

This needs to be a description of the model used and a brief overview of how it works in theory (e.g taken of a CNN Model): 

The network architecture used was a basic CNN model, with Max Pooling and ReLU Activation functions. Input images are resized to an optimal size and then fed into the **Convolutional layer**. These images are converted to their pixel values, which can be imagined as a three-dimensional matrix for the purpose of visualization. The **Convolutional layer** has a kernel. This kernel is generally a small matrix of specified kernel size mxnx3 (3 for RGB images). 
<br>

**Rectified Linear Unit (ReLU)** is the activation layer used in CNNs.The activation function is applied to increase non-linearity in the CNN. Images are made of different objects that are not linear to each other.


**Max Pooling:** A limitation of the feature map output of Convolutional Layers is that they record the precise position of features in the input. This means that small movements in the position of the feature in the input image will result in a different feature map. This can happen with re-cropping, rotation, shifting, and other minor changes to the input image. A common approach to addressing this problem from signal processing is called down sampling. This is where a lower resolution version of an input signal is created that still contains the large or important structural elements, without the fine detail that may not be as useful to the task.

## Future Work
Good ideas or strategies that you were not able to implement which you think can help  improve performance.
