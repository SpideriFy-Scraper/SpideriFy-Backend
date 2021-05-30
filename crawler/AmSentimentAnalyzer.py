import os
import shutil
import httpx
import asyncio
import json

load_model = True


def import_tens():
    global tf, hub, text
    tf = __import__("tensorflow")
    hub = __import__("tensorflow_hub")
    text = __import__("tensorflow_text")


def initialize_sentiment():
    global load_model, reloaded_model, saved_model_path
    if load_model:
        load_model = False
        saved_model_path = "./common/sentiment_model/1"
        reloaded_model = tf.saved_model.load(saved_model_path)


class AmSentiment:
    def __init__(self, saved_model_path):
        if saved_model_path is not None:
            self.saved_model_path = saved_model_path
        # import_tens()
        # initialize_sentiment()

    def sent_analyz(self, reviews: list):
        # reloaded_results = tf.sigmoid(reloaded_model(tf.constant(reviews)))
        reloaded_results = asyncio.run(self.request_tf_serve(reviews=reviews))
        return reloaded_results

    async def request_tf_serve(self, reviews: list):
        async with httpx.AsyncClient() as requester:
            content = {}
            content["signature_name"] = "serving_default"
            content["instances"] = reviews
            response = await requester.post(
                url="http://sentiment:8501/v1/models/sentiment:predict",
                data=json.dumps(content),
                timeout=None,
            )
            result = json.loads(response.text)
            return result["predictions"]
