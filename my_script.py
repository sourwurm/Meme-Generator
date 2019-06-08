"""Script to run some part of my project."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

# Imports
Import from PIL import Image, ImageFilter, ImageEnhance, ImageFont, ImageDraw
import os, random
import textwrap

from my_module.functions import deep_fryer, add_text, meme_generator

###
###

# PYTHON SCRIPT HERE
meme_generator()

    
