from functions import deep_fryer, add_text, meme_generator

##
##

assert callable (deep_fryer)
assert deep_fryer() is deep_fryer(folder = 'Documents', filename = 'idk') 
"""These tests assert that the same values are being changed for two different images in two different directories."""

assert callable (add_text)
assert add_text() is add_text(folder = 'Documents')

"""Similar to above, this test asserts that both images behave 
the same when put through the add_text function, even when directory changes."""

assert callable (meme_generator)