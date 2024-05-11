# CLEM4CINA
Simple GUI tool based on tkinter to enable coordinate transformation between TEM and LM images. It allows to open an image from light microscopy (LM), identify coordinates of landmarks such as corners of a section in the LM image with a mouse click, navigate to the same locations in the electron microscope (EM), note the stage coordinates from those same locations, and enter LM and EM coordinate pairs into the GUI. This has to be done for at least three pairs of coordinates. The GUI then calculates the transformation matrix between coordinates in the LM image and the EM image. 
After the transformation matrix has been created, one can click on points of interest in the LM image and receive the coordinates to where the stage of the EM should drive to find the same object in the EM.  

## System requirements

* This software has been tested on a Mac with Apple M1 Max processor, running OSX Sonoma 14.4.1. 

## Installation guide

* Download this repository from Github.

In addition, install:
* Python
* NumPy
* tkinter

Typical install time on a desktop computer: 10 minutes.

## Demo

The generation of the correlation matrix works by filling in three X,Y coordinates into the corresponding entry widgets and pressing the ‘Prepare LM2EM’ and/or ‘Prepare EM2LM’ buttons. Any LM or EM X,Y coordinate can then be converted into the other respective coordinate system by filling in the entry widgets in the green frame and pressing the ‘LM->EM’ or ‘LM<-EM’ buttons. 

* Download and install the program
* Run CLEM4CINA from the applications folder, by typing into a terminal window:
```bash
./clem4cina
```
* Click on Load image
* Click the “Control points” button on the pop-up window
* Click on three control points in the LM image (e.g.,ie the corners of the section)
* Drive to the same control points on the TEM
* Enter the XY stage coordinates in the entry widgets for Control Points > EM
* Click Prepare LM2EM
* Click the “5 ROIs” button on the LM image 
* Click on up to 5 ROIs in the LM image
* Click LM->EM in the GUI
* Enter the resulting XY coordinates into the TEM software to drive to that stage position.

Expected run time: 10 minutes.


## Interface

The GUI looks like this:

![CLEM4CINA GUI](clem4cina_gui.png "CLEM4CINA GUI")
