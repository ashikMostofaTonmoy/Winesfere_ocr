
# In[]:
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
from dotenv import load_dotenv
print(platform.python_version())
print(sys.path)

# get_ipython().system('which python')


# In[]:
load_dotenv('../env/.env')

# %%

df = pd.read_excel('../data/colas_sharing_form_display.xlsx', index_col=0)
# %%
