import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *

def buttonClicked():
    print "Button clicked"

    
button = qt.QPushButton('Button')
button.connect('clicked()', buttonClicked)
button.show()
