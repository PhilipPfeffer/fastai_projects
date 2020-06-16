##### googleimagesdownload OUT OF DATE ####

#!/usr/bin/python

import sys
from subprocess import call


# Trying to use google_images_download to download images
# googleimagesdownload -k "button-up shirts" -s medium -l 10 -o "data/clothes_classifier" -i "button-up shirts" -cd "~/../../Applications/chromedriver"
project_name = "clothes_classifier/"
search_term = sys.argv[1]
num_imgs = sys.argv[2]
path = "fastai/courses/dl1/data/" + project_name
#path = "~/Documents/fastai_projects/data/" + project_name
dest = "images/" + search_term
chromedriver = "~/../../Applications/chromedriver"

call(["googleimagesdownload", "-k", search_term, "-s", "medium", "-l", num_imgs, "-o", path, "-i", dest, "-cd", chromedriver])
