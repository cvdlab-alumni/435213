from pyplasm import *
from scipy import *
import os,sys
from larcc import *

#Definisco i muri

DRAW = COMP([VIEW,STRUCT,MKPOLS])
master = assemblyDiagramInit([9,9,2])([[.3,4,.1,2,.1,2,.1,4,.3],[.3,4,.1,1.5,.1,2.5,.1,5,.3],[.3,3.2]])

#PORTA INGRESSO

toMerge = 91
diagram = assemblyDiagramInit([3,1,2])([[.55,.9,.55],[.3],[2.1,1.1]])
master = diagram2cell(diagram,master,toMerge)

toMerge = 163
diagram = assemblyDiagramInit([1,3,1])([[.3],[.3,.9,.3],[2.1]])
master = diagram2cell(diagram,master,toMerge)

#PORTA FEDERICO&FRANCESCO
toMerge = 63
diagram = assemblyDiagramInit([3,1,2])([[.5,.9,.7],[.3],[2.1,1.1]])
master = diagram2cell(diagram,master,toMerge)

toMerge = 170
diagram = assemblyDiagramInit([1,3,1])([[.3],[.03,.03,.03],[2.1]])
master = diagram2cell(diagram,master,toMerge)

#PORTA CUCINA
toMerge = 101
diagram = assemblyDiagramInit([3,1,2])([[.5,.9,.7],[.3],[2.1,1.1]])
master = diagram2cell(diagram,master,toMerge)

toMerge = 177
diagram = assemblyDiagramInit([1,3,1])([[.3],[.03,.03,.03],[2.1]])
master = diagram2cell(diagram,master,toMerge)

#PORTA MIA
toMerge = 66
diagram = assemblyDiagramInit([3,1,2])([[.5,.9,.7],[.3],[2.1,1.1]])
master = diagram2cell(diagram,master,toMerge)

toMerge = 184
diagram = assemblyDiagramInit([1,3,1])([[.3],[.03,.03,.03],[2.1]])
master = diagram2cell(diagram,master,toMerge)

#PORTA BAGNO
toMerge = 47
diagram = assemblyDiagramInit([1,3,2])([[.1],[.7,.9,.5],[2.1,1.1]])
master = diagram2cell(diagram,master,toMerge)

toMerge = 191
diagram = assemblyDiagramInit([3,1,1])([[.03,.01,.03],[.3],[2.1]])
master = diagram2cell(diagram,master,toMerge)

#PORTA JOHN
toMerge = 110
diagram = assemblyDiagramInit([1,3,2])([[.1],[.03,.03,.03],[2.1,1.1]])
master = diagram2cell(diagram,master,toMerge)

toMerge = 198
diagram = assemblyDiagramInit([3,1,1])([[.03,.09,.03],[.3],[2.1]])
master = diagram2cell(diagram,master,toMerge)

#FINESTRA MIA
toMerge = 15
diagram = assemblyDiagramInit([1,3,3])([[.3],[3.5,3,3.5],[1,2,1]])
master = diagram2cell(diagram,master,toMerge)

toMerge = 207
diagram = assemblyDiagramInit([3,6,3])([[.3,.9,.3],[.2,.6,.2,.2,.6,.2],[.6,1.8,.6]])
master = diagram2cell(diagram,master,toMerge)

#FINESTRA CUCINA
toMerge = 152
diagram = assemblyDiagramInit([1,3,2])([[.1],[3.5,3,3.5],[2.5,1]])
master = diagram2cell(diagram,master,toMerge)

toMerge = 266
diagram = assemblyDiagramInit([3,1,1])([[.3,.9,.3],[.3],[2.5]])
master = diagram2cell(diagram,master,toMerge)

#FINESTRA JOHN
toMerge = 148
diagram = assemblyDiagramInit([1,3,3])([[.1],[0.2,1.5,0.2],[1,2,1]])
master = diagram2cell(diagram,master,toMerge)

toMerge = 275
diagram = assemblyDiagramInit([3,6,3])([[.3,.9,.3],[.2,.4,.2,.2,.4,.2],[.6,1.8,.6]])
master = diagram2cell(diagram,master,toMerge)

#FINESTRA FEDERICO&FRANCESCO
toMerge = 7
diagram = assemblyDiagramInit([1,3,2])([[.1],[0.3,1.5,0.3],[2.5,1]])
master = diagram2cell(diagram,master,toMerge)

toMerge = 334
diagram = assemblyDiagramInit([3,1,1])([[.3,.9,.3],[.3],[2.5]])
master = diagram2cell(diagram,master,toMerge)

#FINESTRA BAGNO
toMerge = 10
diagram = assemblyDiagramInit([1,3,3])([[.1],[0.5,1,0.5],[1,2,1]])
master = diagram2cell(diagram,master,toMerge)

toMerge = 343
diagram = assemblyDiagramInit([3,3,3])([[.3,.9,.3],[.2,.8,.2],[.6,2,.6]])
master = diagram2cell(diagram,master,toMerge)


#Definizione muri
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),RED,0.3)
#VIEW(hpc)

toRemoveRoom = [18,22,26,30,38,53,57,60,63,86,90,92,94,97,120,124,128,132]
toRemoveDoor = [156,158,164,166,172,174,180,182,196,198]
toRemoveWall = [20,36,40,47,55,77,88,92,114,122,126]
toRemoveWindows = [266,268,326,290,211,247,220,256,351,369,317,281,336,338]
toRemove = toRemoveRoom + toRemoveDoor + toRemoveWall + toRemoveWindows
master = master[0],[cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
apartment = master
DRAW(apartment)