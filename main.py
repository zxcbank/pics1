import matplotlib.pyplot as plt
from PIL import Image


def show(img, title=None):
    plt.figure(figsize=(6, 6))
    plt.imshow(img)
    if title is not None:
        plt.title(title)
    plt.axis('off')

def to_black(img):
    return img.convert('L')


img = Image.open(r"наполеон.jpg")
show(img)
(to_black(img)).show()
