
# In[]:
from dotenv import load_dotenv
from multiprocessing.pool import ThreadPool
from time import time
from clint.textui import progress
import requests
import json
import os
import pandas as pd
import sys
import platform
import uuid
print(platform.python_version())
print(sys.path)

# get_ipython().system('which python')


# In[]:
load_dotenv('../env/.env')

# In[]:


destination = os.path.join('../data', 'downloaded_all_same')
print(destination)
try:
    os.makedirs(destination, exist_ok=True)
    # print("Directory doesn't exist. \nCreating Directory...")
except OSError as error:
    print(error)

# In[]:
df = pd.read_excel('../data/colas_sharing_form_display.xlsx', index_col=0)


# In[ ]:


urlHead = os.environ.get("urlHead")
for entry in df.index:
    id = str(uuid.uuid4())
    # dest = os.path.join(destination, str(entry))  # destination path

    if pd.isna(entry) == False:
        img_data = json.loads(df.loc[entry, 'img_data'])
        # if os.path.exists(dest) == False:
        #     try:
        #         os.makedirs(dest, exist_ok=True)
        #         print(f"Directory doesn't exist. \nCreating Directory: {dest} ")
        #     except OSError as error:
        #         print(error)

        for images in img_data:
            start = time()

            # actual url of image
            url = os.path.join(urlHead, images['img'])

            # get the image name
            head_tail = os.path.split(url)
            frame_name = os.path.join(destination, str(entry)+'_'+head_tail[1])

            # download the file
            r = requests.get(url, stream=True)

            # save the file
            with open(frame_name, "wb") as f:
                total_length = int(r.headers.get('content-length'))

                # for progresss bar in terminal
                for chunk in progress.bar(r.iter_content(chunk_size=2391975), expected_size=(total_length/1024) + 1):
                    if chunk:
                        f.write(chunk)
            print(f"{frame_name}: took time: {time() - start :.3f}s")

# In[ ]:
# %%
