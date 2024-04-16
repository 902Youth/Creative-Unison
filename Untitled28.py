#!/usr/bin/env python
# coding: utf-8

# In[13]:


#pip install bcrypt
#pip install flask-cors
#pip install python-dotenv
#pip install flask
#pip install pyjwt
#pip install mysql-connector-python

#pip install pymysql
#pip install watchdog
get_ipython().system('pip freeze > requirements.txt')


# In[2]:


get_ipython().system('pip install PyJWT bcrypt')


# In[3]:


import bcrypt

def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')


# In[4]:


import jwt
import datetime

def generate_jwt(username, hashed_password):
    payload = {
        'username': username,
        'password': hashed_password,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  
    }
    jwt_token = jwt.encode(payload, 'your_secret_key', algorithm='HS256')
    return jwt_token


# In[ ]:




