#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://github.com/rvinothrajendran/BotTutorialSample/blob/master/Python_tutorial/22-aihttp_azure/EchoBot/config.py


# In[4]:


import os


class DefaultConfig:
    
    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "e1a03f01-6427-4c38-9a27-fd0e83fcea24")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "xNlTk3E2A8873_IB06jMCAQEOoo~pos-.k" )






