import os
import shutil

import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text
from official.nlp import optimization  # to create AdamW optmizer


class AmSentiment:
    # saved_model_path
    reloaded_model = tf.saved_model.load(saved_model_path)

    def __init__(self, saved_model_path):
        if saved_model_path is not None:
            self.saved_model_path = saved_model_path

    def sent_analyz(self, reviews: list):
        reloaded_results = tf.sigmoid(reloaded_model(tf.constant(reviews)))
        return reloaded_results.tolist()


# def print_my_examples(inputs, results):
#   result_for_printing = \
#     [f'inut: p{inputs[i]:<30} : score: {results[i][0]:.6f}'
#                          for i in range(len(inputs))]
#   print(*result_for_printing, sep='\n')
#   print()
