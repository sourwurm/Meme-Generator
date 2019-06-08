from PIL import Image, ImageFilter, ImageEnhance, ImageFont, ImageDraw
import os, random
import textwrap






"""A collection of function for doing my project."""

def deep_fryer(root = 'C', root_dir = 'Users', sub_dir = 'BALTHASAR - 02', 
               folder = 'Downloads', filename = 'untitled', filetype = 'jpg'):
    
    """ Accesses an image in a specified directory, and modifies contrast and color values.
    
    PARAMETERS:
    
        root | string, root of ones directory (such as E, D, or C)
        
        root_dir | string, the root folder of the directory to be used (i.e. Program Files, Users, etc.)
        
        sub_dir | string, the sub directory within the root directory. Will vary depending on the root folder
                selected (i.e. if root_dir is Users: sub_dir may be the username such as John or DavidsPC)
                
        folder | the folder within the sub directory that you wish to access (i.e. Documents, Pictures, Downloads)
        
        filename | the name of the file you wish to access
        
        filetype | the image type of the file you are accessing. DO NOT include any periods. (i.e. jpg, png, etc.)"""
    
    directory = (root + ':\\' + root_dir + '\\' + sub_dir + '\\' + folder + '\\' + filename + '.' + filetype)
    
    
    untitled = Image.open(directory)
    
    #Splits the color bands of the image, allowing for each band to be modified independetly
    source = untitled.split()


    ##Modifies each individual band
    R, G, B = 0, 1, 2

    mask = source[R].point(lambda i: i < 115 and 255)

    out = source[G].point(lambda i: i * 0.3)

    source[B].paste(out, None, mask)

    ##Recombines the bands into one image
    im = Image.merge(untitled.mode, source)

    ##retrieves the image and assigns it to the Contrast fucntion, which allows me to adjust the contrast
    get_fry = ImageEnhance.Contrast(im)

    #enhance now knows to take from the contrast function, the value in parentheses is the value by which the
    #contrast of the image will be raised
    # 8.5 = 750% increase in contrast

    fried = get_fry.enhance(8.5)
    
    dir_no_file = (root + ':\\' + root_dir + '\\' + sub_dir + '\\' + folder + '\\')
    
    fry_out = fried.save(dir_no_file + 'fried.jpg')

    ##Presents the image, after all modifications have been done
    return fry_out

def add_text(root = 'C', root_dir = 'Users', sub_dir = 'BALTHASAR - 02', 
               folder = 'Downloads'):
    
    """ Accesses the image created by the function deep_fryer() and adds text to it.
        Additionally, can be used to add text to any image, as long as the image is named fried.jpg.
        
        This function works best with images that are 500x500 pixels, as some text strings will not
        properly fit on the page.
    
    
    PARAMETERS:
    
        root | string, root of ones directory (such as E, D, or C)
        
        root_dir | string, the root folder of the directory to be used (i.e. Program Files, Users, etc.)
        
        sub_dir | string, the sub directory within the root directory. Will vary depending on the root folder
                selected (i.e. if root_dir is Users: sub_dir may be the username such as John or DavidsPC)
                
        folder | the folder within the sub directory that you wish to access (i.e. Documents, Pictures, Downloads)
        
        ENSURE THESE INPUTS MATCH THE ONES USED IN deep_fryer()"""
    
    
    directory = (root + ':\\' + root_dir + '\\' + sub_dir + '\\' + folder + '\\' + 'fried.jpg')
    
    
    #opens the image
    image = Image.open(directory)
    
    #creates a variable allowing me to edit the image
    draw = ImageDraw.Draw(image)
    
    #retrieves the font I will be using for the image
    font = ImageFont.truetype('impact.ttf', size = 40)
    
    #coordinates for the text, x2 and y2 being the coordinates for the second text
    (x, y) = (50,40)
    (x2, y2) = (50, 550)
    
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
    if chance >= 0.75:
        
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
    
    return fin_meme


def meme_generator(root = 'C', root_dir = 'Users', sub_dir = 'BALTHASAR - 02', folder = 'Downloads',
                  filename = 'untitled', filetype = 'jpg'):
    
    
    deep_fryer(root, root_dir, sub_dir, folder, filename, filetype )
    
    
    
    add_text(root, root_dir, sub_dir, folder)