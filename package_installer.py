# This program installs packages, which are listed in
# requirements.txt file. Be careful with outdated packages 
# and packages, that aren't recommended to be upgraded

import os
os.system("pip freeze > requirements.txt")
os.system("pip install -r requirements.txt")
os.system("pip list --outdated")