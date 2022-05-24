from crawler import AmScrapper
import requests
import json
ams = AmScrapper.AmScrapper(
    all_review_url="https://www.amazon.com/HP-Business-Dual-core-Bluetooth-Legendary/product-reviews/B07VMDCLXV/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
    product_url="https://www.amazon.com/HP-Business-Dual-core-Bluetooth-Legendary/dp/B07VMDCLXV",
    headers=None,
)
params = {
    'api_key': '9EC4C8D2370341CB8E75130DC75E35E1',
    'type': 'reviews',
    'amazon_domain': 'amazon.com',
    'asin': 'B073JYC4XM'
}

result = ams.scrap(asin="B07VMDCLXV", export_type="dict")
print(json.dumps(result))

# a = {
#   "asdf":"asdf",
#   "adf":"1",
#   "v":{
#     "a":"s",
#     "f":{
#       "d":"d"
#     }
#   }
# }
# v = {}
# if "x" in  a["v"]["f"].keys() : v["asdfa"] =  a["v"]["f"]["x"]

