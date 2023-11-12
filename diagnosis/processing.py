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
    return pred


def process_result(weather: list, humidity: list, severity: int):
    with open("data_models/model.pkl", "rb") as f:
        model = pickle.load(f)
        g_c = []
        g = list(zip(weather, humidity))
        print(g)
        for b in g:
            v = list(b)
            v.append(severity)
            g_c.append(v)
        predicted_values = model.predict(g_c)
        threshold = 0.5

        categorical_labels = []
        str_categorical_labels = []
        for prediction in predicted_values:
            if prediction < threshold:
                categorical_labels.append(0)
                str_categorical_labels.append("High")
            elif prediction < 1.5:
                categorical_labels.append(1)
                str_categorical_labels.append("Moderate")
            else:
                str_categorical_labels.append("Low")
                categorical_labels.append(2)
        return str_categorical_labels
