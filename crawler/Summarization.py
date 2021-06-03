import asyncio
import httpx
import json
import os.path
from logger.corelogger import Logger
from inspect import currentframe


class Summarization:

    REVIEWS = None
    SUMMARIZED = None

    def __init__(self, reviews):
        self.REVIEWS = reviews

    def call_summarization_service(self):
        logger = Logger(
            os.path.basename(__file__),
            currentframe().f_lineno,
            "Connenting to Summarization service...",
            "info",
        )
        self.SUMMARIZED = asyncio.run(self.request_summarization_service())
        return self.SUMMARIZED

    async def request_summarization_service(self):
        summarized_data = {}
        for review in self.REVIEWS.keys():
            async with httpx.AsyncClient() as requester:
                response = await requester.post(
                    url="http://summarization-api:8000/predict",
                    data=json.dumps({"text": self.REVIEWS[review]}),
                    timeout=None,
                )
            if response.status_code != httpx.codes.OK:
                logger = Logger(
                    os.path.basename(__file__),
                    currentframe().f_lineno,
                    "Failed to establish a connection to Summarization service...",
                    "error",
                )
                return None
            else:
                summar = json.loads(response.text)
                summarized_data[review] = summar["summarized_text"]
        return summarized_data

    def clean_attributes(self):
        self.REVIEWS = None
        self.SUMMARIZED = None
