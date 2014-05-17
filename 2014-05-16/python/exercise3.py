from larcc import *
 
DRAW = COMP([VIEW,STRUCT,MKPOLS])

# def automatizeMultipleDiagram2cell(masterDiagram,subDiagram,toMergeList,toRemoveList,):
# 	subDiagram = subDiagram[0],[cell for k,cell in enumerate(subDiagram[1]) if not (k in toRemoveList)]
# 	for i in range(len(list(sort(toMergeList)))):
# 		masterDiagram = diagram2cell(subDiagram,masterDiagram,toMergeList[i]-i)
# 	return masterDiagram
def automatizeMultipleDiagram2cell(masterDiagram,subDiagram,toMergeList,toRemoveList):
	subDiagram = subDiagram[0],[cell for k,cell in enumerate(subDiagram[1]) if not (k in toRemoveList)]
	toMergeList = list(sort(toMergeList))
	for i in range(len(list(sort(toMergeList)))):
		numCell = toMergeList[i]-i
		masterDiagram = diagram2cell(subDiagram,masterDiagram,numCell)
	return masterDiagram

shape = [5,5,1]
sizePatterns = [[.5,5,.5,5,.5],[.5,5,.5,5,.5],[3]]
master = assemblyDiagramInit(shape)(sizePatterns)
toRemove = [6,8,16,18]
master = master[0],[cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
mV,mCV = master
mVV = [[i] for i in range(len(mV))]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering ((mV,mCV),hpc)(range(len(mCV)),CYAN,5)
hpc = cellNumbering ((mV,mVV),hpc)(range(len(mVV)),GREEN,1)
VIEW(hpc)
DRAW(master)

#Rispetto alla coordinata X
subShape = [5,1,3]
subSizePatterns = [[1.5,2,1.5,2,1.5],[.5],[1,1,1]]
subDiagram = assemblyDiagramInit(subShape)(subSizePatterns)
subV,subCV = subDiagram
subVV = [[i] for i in range(len(subV))]

subhpc = SKEL_1(STRUCT(MKPOLS(subDiagram)))
subhpc = cellNumbering ((subV,subCV),subhpc)(range(len(subCV)),CYAN,5)
subhpc = cellNumbering ((subV,subVV),subhpc)(range(len(subVV)),GREEN,1)
VIEW(subhpc)


master = automatizeMultipleDiagram2cell(master,subDiagram,[7,15,6,14,5,13],[4,10])
mV,mCV = master
mVV = [[i] for i in range(len(mV))]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering ((mV,mCV),hpc)(range(len(mCV)),CYAN,5)
hpc = cellNumbering ((mV,mVV),hpc)(range(len(mVV)),GREEN,1)
VIEW(hpc)
DRAW(master)

#Rispetto alla coordinata Y
subShape = [1,5,3]
subSizePatterns = [[.5],[1.5,2,1.5,2,1.5],[1,1,1]]
subDiagram = assemblyDiagramInit(subShape)(subSizePatterns)
subV,subCV = subDiagram
subVV = [[i] for i in range(len(subV))]

subhpc = SKEL_1(STRUCT(MKPOLS(subDiagram)))
subhpc = cellNumbering ((subV,subCV),subhpc)(range(len(subCV)),CYAN,5)
subhpc = cellNumbering ((subV,subVV),subhpc)(range(len(subVV)),GREEN,1)
VIEW(subhpc)


master = automatizeMultipleDiagram2cell(master,subDiagram,[3,8,13,1,6,11],[4,10])
mV,mCV = master
mVV = [[i] for i in range(len(mV))]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering ((mV,mCV),hpc)(range(len(mCV)),CYAN,5)
hpc = cellNumbering ((mV,mVV),hpc)(range(len(mVV)),GREEN,1)
VIEW(hpc)
DRAW(master)