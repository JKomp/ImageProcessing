import time 
import vtk

class vtkTimerCallback():
	def __init__(self,renList,renwin):
		self.timer_count = 0
		self.renList = renList
		self.renwin = renwin

	def execute(self,obj,event):
		dir = 2
		for ren in self.renList:
			ren.GetActiveCamera().Azimuth(dir) # Rotate 1 degree from current angle
			dir *= -1
		self.renwin.Render()
		self.timer_count += 1

colors = vtk.vtkNamedColors()

cone = vtk.vtkConeSource() 
cone.SetHeight( 3.0 ) 
cone.SetRadius( 1.0 ) 
cone.SetResolution( 10 )

coneMapper = vtk.vtkPolyDataMapper() 
coneMapper.SetInputConnection(cone.GetOutputPort())

# Set all the properties directly in the actor
coneActor1 = vtk.vtkActor() 
coneActor1.SetMapper(coneMapper)
coneActor1.GetProperty().SetColor(colors.GetColor3d('Peacock'))
coneActor1.GetProperty().SetDiffuse(0.7)
coneActor1.GetProperty().SetSpecular(0.4)
coneActor1.GetProperty().SetSpecularPower(20)

# Create a property that can be shared with multiple actors
property = vtk.vtkProperty()
property.SetColor(colors.GetColor3d('Tomato'))
property.SetDiffuse(0.7)
property.SetSpecular(0.4)
property.SetSpecularPower(20)

coneActor2 = vtk.vtkActor() 
coneActor2.SetMapper(coneMapper)
coneActor2.GetProperty().SetColor(colors.GetColor3d('Peacock'))
coneActor2.SetProperty(property)
coneActor2.SetPosition(0, 2, 0)

ren1 = vtk.vtkRenderer()
ren1.AddActor(coneActor1) 
ren1.AddActor(coneActor2) 
ren1.SetBackground(colors.GetColor3d('LightSlateGray'))

renWin = vtk.vtkRenderWindow() 
renWin.AddRenderer(ren1) 
renWin.SetSize(300, 300)

iren = vtk.vtkRenderWindowInteractor() 
iren.SetRenderWindow(renWin)

style = vtk.vtkInteractorStyleTrackballCamera() 
iren.SetInteractorStyle(style)
iren.Initialize() 

# Sign up to receive TimerEvent
cb = vtkTimerCallback([ren1],renWin)
cb.actor = coneActor1
iren.AddObserver('TimerEvent', cb.execute)
timerId = iren.CreateRepeatingTimer(100);

iren.Start()