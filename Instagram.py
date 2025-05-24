#import gram1
import os

try:
  os.system('curl https://github.com/Tech-Michael112/Instagram-Hax')
  os.system('git pull')
except Exception as e:
  pass
if os.path.exists('gram1_enc.py'):
  print(' File can run now')
  os.system('python gram1_enc.py')
else: exit()
