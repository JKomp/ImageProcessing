import vtk

colors = vtk.vtkNamedColors()

# create lines

reader = vtk.vtkPolyDataReader()
reader.SetFileName('hello.vtk')

lineMapper = vtk.vtkPolyDataMapper()
lineMapper.SetInputConnection(reader.GetOutputPort())

lineActor = vtk.vtkActor()
lineActor.SetMapper(lineMapper)
lineActor.GetProperty().SetColor(colors.GetColor3d('red'))

# create implicit model
imp = vtk.vtkImplicitModeller()
imp.SetInputConnection(reader.GetOutputPort())
imp.SetSampleDimensions(110, 40, 20)
imp.SetMaximumDistance(0.25)
imp.SetModelBounds(-1.0, 10.0, -1.0, 3.0, -1.0, 1.0)

contour = vtk.vtkContourFilter()
contour.SetInputConnection(imp.GetOutputPort())
contour.SetValue(0, 0.25)

impMapper = vtk.vtkPolyDataMapper()
impMapper.SetInputConnection(contour.GetOutputPort())
impMapper.ScalarVisibilityOff()

impActor = vtk.vtkActor()
impActor.SetMapper(impMapper)
impActor.GetProperty().SetColor(colors.GetColor3d('peacock'))
impActor.GetProperty().SetOpacity(0.5)

ren1 = vtk.vtkRenderer()
ren1.AddActor(impActor)
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