import time 
import vtk

class MyCallback(object): 

	def __init__(self, ren):
		self.ren = ren
	
	def __call__(self, caller, ev):
		pos = self.ren.GetActiveCamera().GetPosition() 
		print(', '.join('{0:0.6g}'.format(i) for i in pos))
		
class vtkTimerCallback():
	def __init__(self,ren,renwin):
		self.timer_count = 0
		self.ren = ren
		self.renwin = renwin

	def execute(self,obj,event):
		print(self.timer_count)
		self.ren.GetActiveCamera().Azimuth(1) # Rotate 1 degree from current angle
		self.renwin.Render()
		self.timer_count += 1

colors = vtk.vtkNamedColors()
# Create the pipeline
cone = vtk.vtkConeSource()
cone.SetHeight(3.0)
cone.SetRadius(1.0)
cone.SetResolution(10)
	
coneMapper = vtk.vtkPolyDataMapper() 
coneMapper.SetInputConnection(cone.GetOutputPort())
coneActor = vtk.vtkActor()
coneActor.SetMapper(coneMapper) 
coneActor.GetProperty().SetColor(colors.GetColor3d("Banana"))
	
ren1 = vtk.vtkRenderer() 
ren1.AddActor(coneActor)
ren1.SetBackground(colors.GetColor3d('MidnightBlue')) 
# Add the observer here 
#ren1.AddObserver("StartEvent", MyCallback(ren1)) 
renWin = vtk.vtkRenderWindow() 
renWin.AddRenderer(ren1)
renWin.SetSize(300, 300)

iren = vtk.vtkRenderWindowInteractor() 
iren.SetRenderWindow(renWin)

#style = vtk.vtkInteractorStyleTrackballCamera() 
#iren.SetInteractorStyle(style)
iren.Initialize() 

# Sign up to receive TimerEvent
cb = vtkTimerCallback(ren1,renWin)
cb.actor = coneActor
iren.AddObserver('TimerEvent', cb.execute)
timerId = iren.CreateRepeatingTimer(100);
   
iren.Start()	
		
#if __name__ == '__main__': main()