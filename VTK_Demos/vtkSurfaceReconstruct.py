# This example shows how to construct a surface from a point cloud.
# First we generate a volume using the
# vtkSurfaceReconstructionFilter. The volume values are a distance
# field. Once this is generated, the volume is countoured at a
# distance value of 0.0.

import os
import string
import vtk
import sys

from vtk.util.misc import vtkGetDataRoot

VTK_DATA_ROOT = vtkGetDataRoot()

# Read some points. Use a programmable filter to read them.
pointSource = vtk.vtkProgrammableSource()

def readPoints():
    output = pointSource.GetPolyDataOutput()
    points = vtk.vtkPoints()
    output.SetPoints(points)

#    filename = "cactus.pts"
    filename = "test1068xpd.pts"
    print('start')
    with open(filename) as f:
        for line in enumerate(f):
            index, data = line[0], line[1].split()
            if data[0] == 'p':# and index < 100000: #224000:
                x, y, z = float(data[1]), float(data[2]), float(data[3])
                points.InsertNextPoint(x, y, z)
                    
            if index%1000 == 0:
                sys.stdout.write('[%s]\r' % (index))
                sys.stdout.flush()

    print('\nDone reading input')

pointSource.SetExecuteMethod(readPoints)

# Construct the surface and create isosurface.
surf = vtk.vtkSurfaceReconstructionFilter()
surf.SetInputConnection(pointSource.GetOutputPort())

cf = vtk.vtkContourFilter()
cf.SetInputConnection(surf.GetOutputPort())
cf.SetValue(0, 0.0)

# Sometimes the contouring algorithm can create a volume whose gradient
# vector and ordering of polygon (using the right hand rule) are
# inconsistent. vtkReverseSense cures this problem.
reverse = vtk.vtkReverseSense()
reverse.SetInputConnection(cf.GetOutputPort())
reverse.ReverseCellsOn()
reverse.ReverseNormalsOn()

map = vtk.vtkPolyDataMapper()
map.SetInputConnection(reverse.GetOutputPort())
map.ScalarVisibilityOff()

surfaceActor = vtk.vtkActor()
surfaceActor.SetMapper(map)
surfaceActor.GetProperty().SetDiffuseColor(1.0000, 0.3882, 0.2784)
surfaceActor.GetProperty().SetSpecularColor(1, 1, 1)
surfaceActor.GetProperty().SetSpecular(.4)
surfaceActor.GetProperty().SetSpecularPower(50)

# Create the RenderWindow, Renderer and both Actors
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
style = vtk.vtkInteractorStyleTrackballCamera() 
iren.SetInteractorStyle(style)

# Add the actors to the renderer, set the background and size
ren.AddActor(surfaceActor)
ren.SetBackground(1, 1, 1)
renWin.SetSize(400, 400)
ren.GetActiveCamera().SetFocalPoint(0, 0, 0)
ren.GetActiveCamera().SetPosition(1, 0, 0)
ren.GetActiveCamera().SetViewUp(0, 0, 1)
ren.ResetCamera()
ren.GetActiveCamera().Azimuth(20)
ren.GetActiveCamera().Elevation(30)
ren.GetActiveCamera().Dolly(1.2)
ren.ResetCameraClippingRange()

iren.Initialize()
renWin.Render()
iren.Start()
