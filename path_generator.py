# The time library is needed to measure execution time
# PIL library to manipulate images (python imaging library)
# colorsys library to manipulate colors
# cv2 library to manipulate images (opencv)
# operator library to sort the values of the array in the fastest way
import os
import sys
import time
import cv2
from artist import *
from painter import *
from explorer import *

start_time = time.time()
# script_dir = os.path.dirname(__file__) # the absolute path of the script
script_dir = os.path.dirname(os.path.abspath(__file__))     # the absolute path of the script
print(script_dir)


def run(fileinput):
    """
    This is the main function calling all the other methods.
    :param fileinput: the file to be taken as input
    :param userchoice: the algorithm that has to be executed
    :return:
    """

    explorer = Explorer()
    painter = Painter()
    sorter = Sorter()

    # Open the file, get the content and the size
    oldimg, oldimgcontent = explorer.imgopen(fileinput)
    size = painter.getsize(oldimg)
    width = size[1]
    height = size[2]

    # We store the pixel values of the original image in an array
    pixvalues = painter.getpixels(oldimgcontent, width, height)

    algostarttime = time.time()

    print("--- algorithm execution time: %s s--" % (time.time() - algostarttime))

    newimg, newimgcontent = explorer.imgcreate(width, height)

    # Write the content of the image
    painter.fill_horizontal(sortedvalues, newimgcontent, width, height)

    # Save the image
    output_name = "img-output.jpg"
    output_path = os.path.join(script_dir, 'output', output_name)
    explorer.saveimg(newimg, output_path)

    print("\nOutput file: /output/img-output.jpg\n")
    return


# Let the user choose the options

# Choose the file
print("\n\n-------------------------------------------------")
print("Insert the name of the image you want to sort")
print("PLEASE NOTE: the image should be in the \"input\" folder.")
print("Insert the name WITHOUT the folder path (example: image.jpg)\n")
fileinput = input("Leave blank if you want to use the default image (img-input-small.jpg): ")
if fileinput == "":
    fileinput = "img-input-small.jpg"
input_path = os.path.join(script_dir, 'input', fileinput)


print("-- total exec time: %s seconds --" % (time.time() - start_time))
