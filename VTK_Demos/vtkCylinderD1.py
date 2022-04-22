import vtk

cylinder = vtk.vtkCylinderSource()
cylinder.SetResolution( 8 )

cylinderMapper = vtk.vtkPolyDataMapper()
cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

cylinderActor = vtk.vtkActor()
cylinderActor.SetMapper(cylinderMapper)
cylinderActor.GetProperty().SetColor(1.0, 0.3882, 0.2784)
cylinderActor.RotateX(30.0)
cylinderActor.RotateY(-45.0)

ren1 = vtk.vtkRenderer()
ren1.AddActor(cylinderActor)
ren1.SetBackground(0.1, 0.2, 0.4)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(400,400)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# The style variable allows for user iteraction - q = quit
style = vtk.vtkInteractorStyleTrackballCamera() 
iren.SetInteractorStyle(style)
iren.Initialize() 
iren.Start()