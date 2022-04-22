import vtk
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

ren1.GetActiveCamera().Azimuth(45)

iren = vtk.vtkRenderWindowInteractor() 
iren.SetRenderWindow(renWin)

style = vtk.vtkInteractorStyleTrackballCamera() 
iren.SetInteractorStyle(style)
iren.Initialize() 
iren.Start()