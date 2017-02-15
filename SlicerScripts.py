import vtk, qt, ctk, slicer


#Jan 19
def buttonClicked():
    print "Button clicked"

button = qt.QPushButton('Button')
button.connect('clicked()', buttonClicked)
button.show()


#Jan 24
#This will create a linear transform node
modelToRas = slicer.vtkMRMLLinearTransformNode()
modelToRas.SetName('ModelToRas')
slicer.mrmlScene.AddNode(modelToRas)

modelToRasTransform = vtk.vtkTransform()
modelToRasTransform.PreMultiply() 
modelToRasTransform.Update()

modelToRas.SetAndObserveTransformToParent(modelToRasTransform)

