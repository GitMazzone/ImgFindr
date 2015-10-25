# ImgFindr UGA Hacks project by:
# 	Michael Mazzone & Chris Halima

from Tkinter import *
import os
import tkFileDialog

# Getting Clarifai API 
from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi()


# Create the window
root = Tk()

# Application title & size
root.title("ImgFindr")
root.geometry("1000x600")

# Creating frame to add things to
app = Frame(root) 
app.grid() # Adding app frame to grid

# Method that opens file chooser 
# Gets used when button is clicked (command)
def openFileBox():
	directoryPicked = tkFileDialog.askdirectory()
	for filePicked in os.listdir(directoryPicked):
		if filePicked.lower().endswith(".jpg") or filePicked.lower().endswith(".gif") or filePicked.lower().endswith(".png"):
			#set icon label to the current file 
			print(filePicked)


#TODO: add button 'Select Folder'
loaderButton = Button(app)
loaderButton["text"] = "Select Folder"
loaderButton["command"] = openFileBox
loaderButton.grid()

#TODO: add 'Sort' buttons (add functionalty later)
#sortButtonDate
#sortButtonRelevance
#sortButtonImgType
#sortButtonFileSize

#TODO: add 'Save' button

#TODO: add 'Tags' message widget
tagBarLabel = Label(root, text = "Tag:")
tagBarLabel.pack(side = LEFT)
tagBarLabel.grid()

"""
TODO - make for loop to accept tags & populate
			 an array of up to 20 tags that will be:
			 	displayed in a box below
			 	used to apply/narrow filter

for i in range(0, 3):
	print "We're on time"

#tagEntry = 


for i = 0-->19:
	"label" + i = new Label
	add action listener {
		entry[i] = entry
	}
"""

#TODO: add 'Image Field' paned window


# Tells the program to run everything above
root.mainloop()