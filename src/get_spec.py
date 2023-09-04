import cv2
import json

from ocr import extract_text_from_region ,extract_value_from_region
from data import spec

image = cv2.imread("input/image.jpg")

result = {}

item_count: int = spec.get("item_count")
item_height: int = spec.get("item_height")

key_x: int = spec.get("key").get("position").get("x")
key_y: int = spec.get("key").get("position").get("y")
key_width: int = spec.get("key").get("position").get("width")
key_height: int = spec.get("key").get("position").get("height")

value_x: int = spec.get("value").get("position").get("x")
value_y: int = spec.get("value").get("position").get("y")
value_width: int = spec.get("value").get("position").get("width")
value_height: int = spec.get("value").get("position").get("height")

for i in range(item_count):
    key_id = f"spec_{i+1}_key"
    key = extract_text_from_region(key_id, image, key_x, key_y + item_height * i, key_width, key_height).replace("\n", "")

    value_id = f"spec_{i+1}_value"
    value = extract_value_from_region(value_id, image, value_x, value_y + item_height * i, value_width, value_height).replace("\n", "")
    
    if key != "":
        result[key] = value

with open("out/spec.json", "w") as json_file:
    json.dump(result, json_file)