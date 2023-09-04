
import cv2

vendor = {
    "position": {
        "x": 1121,
        "y": 157,
        "width": 67,
        "height": 45
    }
}

image = cv2.imread("input/image.jpg")

position = vendor.get("position")
x = position.get("x")
y = position.get("y")
width = position.get("width")
height = position.get("height")

target = image[y:y+height, x:x+width]

filename = f'out/vendor.jpg'
cv2.imwrite(filename, target)