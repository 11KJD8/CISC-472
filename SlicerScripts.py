from __main__ import vtk, qt, ctk, slicer

#
# Button
#

class SlicerScripts:
  def __init__(self, parent):
    parent.title = "Button click"
    parent.categories = ["Examples"]
    parent.dependencies = []
    parent.contributors = ["Kyle"]
    parent.helpText = ""
    parent.acknowledgementText = ""
    self.parent = parent

#
# SlicerScriptsWidget
#

class SlicerScriptsWidget:
  def __init__(self, parent = None):
    if not parent:
      self.parent = slicer.qMRMLWidget()
      self.parent.setLayout(qt.QVBoxLayout())
      self.parent.setMRMLScene(slicer.mrmlScene)
    else:
      self.parent = parent
    self.layout = self.parent.layout()
    if not parent:
      self.setup()
      self.parent.show()

  def setup(self):
    # Instantiate and connect widgets ...

    # Collapsible button
    sampleCollapsibleButton = ctk.ctkCollapsibleButton()
    sampleCollapsibleButton.text = "A collapsible button"
    self.layout.addWidget(sampleCollapsibleButton)

    # Layout within the sample collapsible button
    sampleFormLayout = qt.QFormLayout(sampleCollapsibleButton)

    ########################
    # Button
    clickButton = qt.QPushButton("Button")
    clickButton.toolTip = "Print 'Button clicked' in standard ouput."
    sampleFormLayout.addWidget(clickButton)
    clickButton.connect('clicked(bool)', self.buttonClicked)
    ########################
    
    # Add vertical spacer
    self.layout.addStretch(1)

    # Set local var as instance attribute
    self.clickButton = clickButton

  def buttonClicked(self):
    print "Button clicked"
    #qt.QMessageBox.information(slicer.util.mainWindow(),'SlicerPython','HelloWorld!')
    

