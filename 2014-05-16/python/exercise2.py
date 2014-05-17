from larcc import *
from scipy import *
import exercise1
from pyplasm import *

def createUpstairs(width,number):
	element = CUBOID([6,0.5,2])
	column = STRUCT( CAT(N(10)([element, T([2,3])([1,1.5])])))
	return column



# DRAW = COMP([VIEW,STRUCT,MKPOLS])
# master = assemblyDiagramInit([1,4,4])([[12.3],[3,12.9,3,12.9],[3.5,3.5,3.5,0.3]])
# V,CV = master
# d = exercise1.apartment

# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
# VIEW(hpc)

# toMerge = 4
# cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
# master = diagram2cell(d,master,toMerge)

# toMerge = 4
# cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
# master = diagram2cell(d,master,toMerge)

# toMerge = 4
# cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
# master = diagram2cell(d,master,toMerge)

# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
# VIEW(hpc)

# toMerge = 9
# cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
# master = diagram2cell(d,master,toMerge)

# toMerge = 9
# cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
# master = diagram2cell(d,master,toMerge)

# toMerge = 9
# cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
# master = diagram2cell(d,master,toMerge)

# DRAW(master)


DRAW = COMP([VIEW,STRUCT,MKPOLS])
master = assemblyDiagramInit([1,3,4])([[12.3],[12.9,3,12.9],[3.5,3.5,3.5,0.3]])
V,CV = master
d = exercise1.apartment


hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)

toRemove = [4,5,6]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#DRAW(master)

dS = larApply(s(1,-1,1))(d)

toMerge = 0
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
master = diagram2cell(dS,master,toMerge)
toMerge = 0
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
master = diagram2cell(dS,master,toMerge)

toMerge = 0
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
master = diagram2cell(dS,master,toMerge)
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)

toMerge = 2
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
master = diagram2cell(d,master,toMerge)
toMerge = 2
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
master = diagram2cell(d,master,toMerge)
toMerge = 2
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
master = diagram2cell(d,master,toMerge)
#DRAW(master)

element = CUBOID([1.61,0.4,0.1])
column = STRUCT( CAT(N(10)([element, T([2,3])([0.3,0.2])])))
column = R([1,2])(PI/2)(column)
column = T([1,2])([6,12.8])(column)
column2 = T(3)(3.7)(column)
column3 = T([1,2,3])([8.9,28.8,1.8])(R([1,2])(PI)(column))
column4 = T(3)(3.7)(column3)
floor05 = CUBOID([3.2,3.5,0.1])
floor05 = T([2,3])([12.7,1.8])(floor05)
floor15 = T(3)(3.7)(floor05)

floor25 = CUBOID([6.3,3.5,0.1])
floor25 = T([1,2,3])([6,12.8,3.8])(floor25)
floor35 = T(3)(3.5)(floor25)
master = STRUCT(MKPOLS(master))
VIEW(STRUCT([master,column,column2,column3,column4,floor05,floor15,floor25,floor35]))