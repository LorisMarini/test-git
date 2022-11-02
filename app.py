#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from IPython.core.interactiveshell import InteractiveShell
import warnings
from IPython.core.display import display, HTML

import seaborn as sns 
import plotly.express as px

get_ipython().run_line_magic('matplotlib', 'inline')
warnings.filterwarnings('ignore')
display(HTML("<style>.container { width:85% !important; }</style>"))
InteractiveShell.ast_node_interactivity = "all"

pd.set_option('max_colwidth', 100)
pd.set_option("display.max_columns", 200)
pd.set_option("display.max_rows", 1000)

# pd.reset_option('display.float_format')
pd.set_option('display.float_format', lambda x: '%.3f' % x)

get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")


# In[3]:


df = pd.read_csv("./sprout-data.csv")


# In[4]:


df


# In[ ]:




