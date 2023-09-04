import cv2
import json

from ocr import extract_text_from_region ,extract_value_from_region
from data import info

image = cv2.imread("input/image.jpg")

result = []

for item in info:
    id = item.get("id")
    position = item.get("position")
    x = position.get("x")
    y = position.get("y")
    width = position.get("width")
    height = position.get("height")
    is_value = item.get("is_value")

    extracted = extract_text_from_region(id, image, x, y, width, height)
    
    cur = item.copy()
    cur["result"] = extracted.replace("\n", "")
    result.append(cur)

with open("out/info.json", "w") as json_file:
    json.dump(result, json_file)