import vtk

def vtkRtBtnCallback(obj, event):
	print(event)

def annotatePick(object, event):

	global picker #, textActor, textMapper
	print(event)
	if(picker.GetCellId() < 0):
		print('1')
	else:
		print('2')
		
sphere = vtk.vtkSphereSource()
sphereMapper = vtk.vtkPolyDataMapper()
sphereMapper.SetInputConnection(sphere.GetOutputPort())
sphereActor = vtk.vtkActor()
sphereActor.SetMapper(sphereMapper)
sphereActor.SetOrigin(2, 1, 3)
sphereActor.SetPosition(2.25, 0, 0)
sphereActor.GetProperty().SetColor(1, 0, 1)

cube = vtk.vtkCubeSource()
cubeMapper = vtk.vtkPolyDataMapper()
cubeMapper.SetInputConnection(cube.GetOutputPort())
cubeActor = vtk.vtkActor()
cubeActor.SetMapper(cubeMapper)
cubeActor.SetPosition(0.0, 1.25, 0)
cubeActor.GetProperty().SetColor(1, 0, 1)

cone = vtk.vtkConeSource()
coneMapper = vtk.vtkPolyDataMapper()
coneMapper.SetInputConnection(cone.GetOutputPort())
coneActor = vtk.vtkActor()
coneActor.SetMapper(coneMapper)
coneActor.SetPosition(0, 0, 1.25)
coneActor.GetProperty().SetColor(0, 1, 0)

cylinder = vtk.vtkCylinderSource()
cylinderMapper = vtk.vtkPolyDataMapper()
cylinderMapper.SetInputConnection(cylinder.GetOutputPort())
cylinderActor = vtk.vtkActor()
cylinderActor.SetMapper(cylinderMapper)
cylinderActor.GetProperty().SetColor(1, 0, 0)

assembly = vtk.vtkAssembly()
assembly.AddPart(cylinderActor)
assembly.AddPart(cubeActor)
assembly.AddPart(sphereActor)
assembly.AddPart(coneActor)
assembly.AddPosition(5, 0, 0)
assembly.RotateX(15)

picker = vtk.vtkCellPicker()
picker.AddObserver('endPickEvent',annotatePick)

ren1 = vtk.vtkRenderer()
ren1.AddActor(assembly)
ren1.AddActor(coneActor)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(400,400)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
iren.SetPicker(picker)

# The style variable allows for user iteraction - q = quit
style = vtk.vtkInteractorStyleTrackballCamera() 
iren.SetInteractorStyle(style)
iren.AddObserver('RightButtonPressEvent',vtkRtBtnCallback)
iren.Initialize() 

iren.Start()