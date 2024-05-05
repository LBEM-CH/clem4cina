# CLEM4CINA
Simple GUI tool based on tkinter to enable coordinate transformation between TEM and LM images. It allows to open an image from light microscopy (LM), identify coordinates of landmarks such as corners of a section in the LM image with a mouse click, navigate to the same locations in the electron microscope (EM), note the stage coordinates from those same locations, and enter LM and EM coordinate pairs into the GUI. This has to be done for at least three pairs of coordinates. The GUI then calculates the transformation matrix between coordinates in the LM image and the EM image. 
After the transformation matrix has been created, one can click on points of interest in the LM image and receive the coordinates to where the stage of the EM should drive to find the same object in the EM.  

## Dependencies

* Python
* NumPy
* tkinter

## Usage
In a shell terminal, type:

```bash
./clem4cina
```

## Interface

The GUI looks like this:

![CLEM4CINA GUI](clem4cina_gui.png "CLEM4CINA GUI")
