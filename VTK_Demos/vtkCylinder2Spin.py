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

coneActor = vtk.vtkActor() 
coneActor.SetMapper(coneMapper)

ren1 = vtk.vtkRenderer()
ren1.AddActor(coneActor) 
ren1.SetBackground(colors.GetColor3d('MidnightBlue'))
ren1.SetViewport(0.0, 0.0, 0.5, 1.0)

ren2 = vtk.vtkRenderer()
ren2.AddActor(coneActor) 
ren2.SetBackground(colors.GetColor3d('SlateGray'))
ren2.SetViewport(0.5, 0.0, 1.0, 1.0)

renWin = vtk.vtkRenderWindow() 
renWin.AddRenderer(ren1) 
renWin.AddRenderer(ren2) 
renWin.SetSize(600, 300)

iren = vtk.vtkRenderWindowInteractor() 
iren.SetRenderWindow(renWin)

#style = vtk.vtkInteractorStyleTrackballCamera() 
#iren.SetInteractorStyle(style)
iren.Initialize() 

# Sign up to receive TimerEvent
cb = vtkTimerCallback([ren1, ren2],renWin)
cb.actor = coneActor
iren.AddObserver('TimerEvent', cb.execute)
timerId = iren.CreateRepeatingTimer(100);

iren.Start()