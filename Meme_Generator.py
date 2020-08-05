#!/usr/bin/env python
# coding: utf-8

# # Meme Generator
# 
# ## Intro
# 
# #### The purpose of this project is to generate memes, of course. A modern meme consists of a heavily edited or distorted image, typically accompanied by some sort of caption. My code aims to generate memes based on user-inputted images by adjusting color and contrast, and by adding text.

# In[1]:


from PIL import Image, ImageFilter, ImageEnhance, ImageFont, ImageDraw
import os, random
import textwrap


# ## ImportCell
# 
# #### The prior cell imported a couple modules that I will be using.
# 
# 
# 
# 
# ## Deep Fryer
# 
# #### This next cell is the "Deep fryer" of my code. This function will take an inputted image from a specified directory. The default for this code is of course set to my computer, but it is designed to be able to reach any destination you specify (as long as it fits within the parameters). This function is compatible with all image filetypes.

# In[35]:


def deep_fryer(address = 'C:\\Users\\BALTHASAR - 02\\Downloads\\', filename = 'untitled.jpg'):
    
    """ 
    Accesses an image in a specified directory, and modifies contrast and color values.

    -------------
    PARAMETERS:
    -------------
        address  | file directory minus the file name.
        
        filename | the name of the image file you wish to access. include filetype (.png, .png, etc).
        
        """
    
    directory = (address + filename)
    
    
    untitled = Image.open(directory)
    
    #Splits the color bands of the image, allowing for each band to be modified independetly
    source = untitled.split()


    ##Modifies each individual band
    R, G, B = 0, 1, 2

    mask = source[R].point(lambda i: i < 115 and 255)

    out = source[G].point(lambda i: i * 0.3)

    source[B].paste(out, None, mask)

    ##Recombines the bands into one image
    img = Image.merge(untitled.mode, source)

    ##retrieves the image and assigns it to the Contrast fucntion, which allows me to adjust the contrast
    fried = ImageEnhance.Contrast(img)

    #enhance now knows to take from the contrast function, the value in parentheses is the value by which the
    #contrast of the image will be raised by a factor of 8.5
    fried = fried.enhance(8.5)
    
    ##Presents the image, after all modifications have been done
    return fried


# In[39]:


assert callable (deep_fryer)


# #### Here, I run the previously defined function, generating a new image. This image is placed within the same directory the user has specified. Additionally, the image is converted into a .jpg (to make it a little uglier and more compressed in case a .png was uploaded). Lastly, the image is assigned the name "fried" in order for the following function to find the image.

# In[37]:


def add_text(img, caption = '', caption_2 = '', font_ = 'Impact.ttf', save_to = False):
    
    """ 
    Adds text to an inputted image and displays it.
    
    --------------
    PARAMETERS:
    --------------
        img       | image of type PIL.image.image, or a directory that leads to an image.
        
        caption   | (optional) a custom caption to be placed on the upper half of the image
        
        caption_2 | (optional) a second custom caption to be placed on the lower half of the image
        
        font_     | (optional) Truetype font for the text. Fonts must be available under the Windows /fonts directory.
                    Will return an OSerror if the font is not installed.
                        
        save_to   | (optional) directory for which to save the image. Must include filename and filetype as well.
        
        """
    
    if type(img) == str:
        image = Image.open(address)
        
    else:
        image = img
    
    #resisizing image
    image = image.resize((600,500))
        
    #retrieves the font I will be using for the image
    font = ImageFont.truetype(font_, 30)

    #coordinates for the text, x2 and y2 being the coordinates for the second text
    #ratios used in order to be compatible with varying image dimensions
    (x, y) = (50, 40)
    (x2, y2) = (50, 550)
    
    #creates a variable allowing me to edit the image
    draw = ImageDraw.Draw(image)
    
    #list of possible jokes
    jokes = ['I am guilty of 12 counts of \nhome invasion in the state of Lousiana \nfrom the years 2008 - 2012',
             
    'PLEASE GIVE ME AN A',
             
    'my drunk *** lookin at the \nmcdonalds menu at 3:32am:',
             
    '(slow heavy metal music playing)',
             
    'the screen at the bowling \nalley when you get a strike:',
             
    'we live in a society',
             
    'how the mcdonalds manager \nrolls up when there\'s a problem',
             
    'Me: *Turns off AdBlocker* \nHot local singles in my area:',
             
    'Nobody: \nGeorge Lopez at 3AM:',
             
    '10 year old me explaining why I need a \nclub penguin membership to have different colored \nigloos and puffins']

    
    if len(caption) > 0:
        text = caption
        
    else:
        
        #randomly assigns a value from the list
        text = random.choice(jokes)
    
    #colors that will be used for the images, 1 for text, and 2 for text2
    fill_1 = 'rgb(255,255,255)'
    fill_2 = 'rgb(255,255,255)'
    outline_1 = 'rgb(0,0,0)'
    outline_2 = 'rgb(0,0,0)'
    
    #gives the text to be put on the image a border, to be more clearly visible
    #SOURCE : https://mail.python.org/pipermail/image-sig/2009-May/005681.html
    draw.text((x-1, y-1), text, font=font, fill = outline_1)
    draw.text((x+1, y-1), text, font=font, fill = outline_1)
    draw.text((x-1, y+1), text, font=font, fill = outline_1)
    draw.text((x+1, y+1), text, font=font, fill = outline_1)
    
    #applies the fill color of the generated text to the image
    meme = draw.text((x, y), text, fill = fill_1, font = font)
    
    #generates a random float between 0 and 1
    chance = random.random()
    
    
    #sets a condition that if true, will generate another value from the 
    #list and assign it to a new variable, text2   
    if len(caption_2) > 0:
        text2 = caption_2
        
        #text2 is given a border and fill, then applied to the image
        #SOURCE: https://mail.python.org/pipermail/image-sig/2009-May/005681.html
        draw.text((x2-1, y2-1), text2, font=font, fill = outline_2)
        draw.text((x2+1, y2-1), text2, font=font, fill = outline_2)
        draw.text((x2-1, y2+1), text2, font=font, fill = outline_2)
        draw.text((x2+1, y2+1), text2, font=font, fill = outline_2)
        
        meme_2 = draw.text((x2, y2), text2, fill = fill_2, font = font)
        
        #fin_meme is the final output of all added text if this condition is filled
        #will show the final image
        fin_meme = image.show(meme_2)
        
        
    elif chance >= 0.75 and len(caption) == 0:
        
        text2 = random.choice(jokes)
        
        #text2 is given a border and fill, then applied to the image
        #SOURCE: https://mail.python.org/pipermail/image-sig/2009-May/005681.html
        draw.text((x2-1, y2-1), text2, font=font, fill = outline_2)
        draw.text((x2+1, y2-1), text2, font=font, fill = outline_2)
        draw.text((x2-1, y2+1), text2, font=font, fill = outline_2)
        draw.text((x2+1, y2+1), text2, font=font, fill = outline_2)
        
        meme_2 = draw.text((x2, y2), text2, fill = fill_2, font = font)
        
        #fin_meme is the final output of all added text if this condition is filled
        #will show the final image
        fin_meme = image.show(meme_2)
        
    else:
        
        #in this case, text2 is not assigned a value
        #fin_meme becomes the output of only the original text variable being put on the image
        #will show the final image
        fin_meme = image.show(meme)

        
    if save_to:
        
        fin_meme.save(save_to)
    
    return fin_meme

# In[41]:


assert callable (add_text)


# #### Running add_text returns the final image.

# In[92]:


add_text()

