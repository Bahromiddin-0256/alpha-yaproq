import cv2 as cv
import dill

# import fastai
from fastai.vision.all import *


def process_image(image_path):
    learner = load_learner("data_models/yaproq_2.pkl", pickle_module=dill)
    img = cv.imread(image_path)
    bigger = cv.resize(img, (224, 224))

    image = cv.cvtColor(bigger, cv.COLOR_BGR2RGB)
    pred, _, prob = learner.predict(image)
    return pred, prob * 100
