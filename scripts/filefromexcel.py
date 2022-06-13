import os
import requests
# from time import time
from multiprocessing.pool import ThreadPool
from clint.textui import progress

dest = '../data/downloaded/0'
url1 = 'https://img.mediavitis.com/cola_images/Chardonnay_VSR2008.jpg'
url12 = 'https://img.mediavitis.com/cola_images/backlabel.jpg'

head_tail = os.path.split(url12)

head_tail[1]
frame_name = os.path.join(dest, head_tail[1])
print(frame_name)
url = url1
try:
    os.makedirs(dest, exist_ok=True)
#     print("Directory doesn't exist. \nCreating Directory..." )
except OSError as error:
    print(error)

r = requests.get(url, stream=True)
with open(frame_name, "wb") as f:
    total_length = int(r.headers.get('content-length'))
    for chunk in progress.bar(r.iter_content(chunk_size=2391975), expected_size=(total_length/1024) + 1):
        if chunk:
            f.write(chunk)
