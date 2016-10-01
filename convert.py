from PySide import QtCore
import Part, Mesh
import os
import fnmatch

dirs = []

for root, dirnames, filenames in os.walk('Vex'):
    dirs.append(root)

for thisdir in dirs:

    d=QtCore.QDir(thisdir)
    d.setNameFilters(["*.step", "*.stp"])
    files = d.entryInfoList()

    for i in files:
        shape = Part.Shape()
        shape.read(i.absoluteFilePath())
        mesh = Mesh.Mesh()
        mesh.addFacets(shape.tessellate(0.01))
        dirname = i.absolutePath()
        dirname = dirname.replace("STEP", "OBJ")
        if(not os.path.exists(dirname)):
            os.makedirs(dirname)
        mesh.write(dirname+"/"+i.baseName()+".obj")
