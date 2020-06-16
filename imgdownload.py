#!/usr/bin/python

import sys
from subprocess import call

project_name = "clothes_classifier"
search_term = sys.argv[1]
num_imgs = sys.argv[2]
path = "fastai/courses/dl1/data/" + project_name
dest = "images/" + search_term
chromedriver = "~/../../Applications/chromedriver"

call(["googleimagesdownload", "-k", search_term, "-s", "medium", "-l", num_imgs, "-o", path, "-i", dest, "-cd", chromedriver])
