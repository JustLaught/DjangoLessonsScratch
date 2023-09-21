import time
import json
from PIL import Image, ImageFilter
import concurrent.futures


# for img_name in file_names:
def process_img(img_name):
    img = Image.open(f"images/{img_name}")
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail((1200, 1200))
    img.save(f"processed/{img_name}")
    print(f"image {img_name} was processed")

if __name__ == "__main__":
    t1 = time.time()
    with open("file_names.txt", "r") as f:
        file_names = json.load(f)

    with concurrent.futures.ProcessPoolExecutor() as co:
        co.map(process_img, file_names)

    t2 = time.time()
    print(f"Time used {round(t2 - t1, 2)} sec.")


 