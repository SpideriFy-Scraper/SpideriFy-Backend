import os
import shutil


load_model = True


def import_tens():
    global tf, hub, text
    tf = __import__('tensorflow')
    hub = __import__('tensorflow_hub')
    text = __import__('tensorflow_text')


def initialize_sentiment():

    global load_model, reloaded_model, saved_model_path
    if load_model:
        load_model = False
        saved_model_path = "/home/tesla/Project/SpideriFy/spiderify-backend/commen/ML-Model"
        reloaded_model = tf.saved_model.load(saved_model_path)
    return


class AmSentiment:
    def __init__(self, saved_model_path):
        if saved_model_path is not None:
            self.saved_model_path = saved_model_path
        import_tens()
        initialize_sentiment()

    def sent_analyz(self, reviews: list):
        reloaded_results = tf.sigmoid(reloaded_model(tf.constant(reviews)))
        return reloaded_results.numpy().tolist()
