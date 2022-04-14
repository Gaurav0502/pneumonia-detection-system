# Problem Statement 
Medical Image Analysis is used to process medical images like X-rays(here),CT Scans etc. Here, we will classify whether or not that person suffers from a disease or not.
Moreover, it can also be used for plant disease prediction as well.
## Dataset

The dataset used is the Chest X-Ray Images (Pneumonia)(https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia) from Kaggle.

Task : Classification

The 2 class labels are:
<br>

**1. Pneumonia:** Given X-Ray is of a person suffering from Pneumonia.
<br>

**2. Normal:** Given X-Ray is of a normal person.

## Model(s) Used

Various models were trained with the grayscale X-Rays like :

1. Binary Logistic Regression.
2. K- Nearest Neighbours (KNN).
3. Support Vector Machines (SVM).
4. Multilayer Perceptron (MLP).
5. Neural Network.

<br>

**Binary Logistic Regression** is a Supervised Learning model in which the sigmoid function is used to predict a categorical dependent variable (here, X-Ray type) based on a given set of independent variables.


**K-Nearest Neighbours** is a Supervised Learing model in which is used for both classification and regression tasks. Here, we use KNN for classifying the type of Lung X-Ray. This algorithm classifies test values based k-nearest train values usually based on <i>Euclidean distance</i> metric.

**Support Vector Machines** is a Supervised Learning model which can be used for both classification and regression problems. The main idea behind this algorithm is estimate the best possible decision boundary to segreggate a n-dimensional space called <i>hyperplanes</i>. For a new set of independent variables it classifies the dependent variable based on the distance boundary or hyperplane.

**Multilayer Perceptron** is a Supervised Learning model which is majorly used for classification tasks. It is type <i>feedforward Artificial Neural Network</i> that generates a set of outputs from a set of inputs. Diagrammatically, it is a directed graph with the outermost layers as the input and output layers and the intermediate layers referred to as inner layers. The model is trained using <i>back propagation technique</i>.

# Blog Link

The project is documented as a [medium article].(https://medium.com/@prasham1515/pneumonia-detection-system-ea42928b938a)


## Future Work
To apply much better image processing techniques and training deep learning models.
