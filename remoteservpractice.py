# Practice python script for remote jobs

import time
import os
print('starting')
time.sleep(30)
if os.path.exists('62979.pdf'):
  os.remove('62979.pdf')
else:
  print('The file does not exist')
print('done')