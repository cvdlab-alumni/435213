from larcc import *
from scipy import *
import exercise1
from pyplasm import *

def rgb2color(rgb):
	r,g,b = rgb
	nr = float(r)/255
	nb = float(b)/255
	ng = float(g)/255
	return [nr,nb,nb]
grassColor = rgb2color([4,186,24])
rodTreeColor = rgb2color([76,22,10])
treeChiomaColor = rgb2color([4,186,24])


treeChiomaColor = rgb2color([4,200,24])

def doTree(coords):
	x,y = coords
	def doTree0(dim):
		r,h = dim
		tronco = CYLINDER ([r,h])(50)
		chioma = SPHERE(r*2.5)([32,32])
		tronco = COLOR(rodTreeColor)(STRUCT([tronco]))
		chioma = COLOR(treeChiomaColor)(STRUCT([chioma]))
		return T([1,2])([x,y])(STRUCT([tronco,T(3)(h+r)(chioma)]))
	return doTree0


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


#Scale
gradino = CUBOID([1.61,0.4,0.1])
scala1 = STRUCT( CAT(N(10)([gradino, T([2,3])([0.3,0.2])])))
scala1 = R([1,2])(PI/2)(scala1)
scala1 = T([1,2])([6,12.8])(scala1)
scala2 = T(3)(3.7)(scala1)
scala3 = T([1,2,3])([8.9,28.8,1.8])(R([1,2])(PI)(scala1))
scala4 = T(3)(3.7)(scala3)
floor05 = CUBOID([3.2,3.5,0.1])
floor05 = T([2,3])([12.7,1.8])(floor05)
floor15 = T(3)(3.7)(floor05)

floor25 = CUBOID([6.3,3.5,0.1])
floor25 = T([1,2,3])([6,12.8,3.8])(floor25)
floor3 = T(3)(3.5)(floor25)
upstairs = STRUCT([scala1,scala2,scala3,scala4,floor05,floor15,floor25,floor3])


#Balcone
baseBalcone = CUBOID([1,2,0.2])
palettoRinghiera = CUBOID([0.05,0.05,0.65])
paletti = STRUCT(NN(14)([palettoRinghiera,T(2)(0.15)]))
paletti = T(3)(0.2)(paletti)
palettoRinghieraX = palettoRinghiera
palettoRinghieraX = T([1,2])([1,2])(palettoRinghieraX)
palettiX = STRUCT(NN(7)([palettoRinghiera,T(2)(0.15)]))
palettiX = R([1,2])(PI/2)(palettiX)
palettiX = T([1,3])([1,0.2])(palettiX)
upRinghieraY = CUBOID([0.05,2,0.05])
upRinghieraY = T(3)(0.85)(upRinghieraY)

upRinghieraX = CUBOID([1,0.05,0.05])
upRinghieraX = T(3)(0.85)(upRinghieraX)
upRinghieraX  =STRUCT(NN(2)([upRinghieraX,T(2)(1.95)]))
palettiX = STRUCT(NN(2)([palettiX,T(2)(1.95)]))
upRinghiera = STRUCT([upRinghieraX,upRinghieraY])
balcone = STRUCT([baseBalcone,paletti,upRinghiera,palettiX])

balcone = T([1,2])([-1,7.15])(balcone)
balconiRetro = STRUCT(NN(3)([balcone,T(3)(3.5)]))
balconiRetro = STRUCT(NN(2)([balconiRetro,T(2)(12.5)]))
balconiFronte = STRUCT(NN(3)([balcone,T(3)(3.5)]))
balconiFronte = STRUCT(NN(2)([balconiFronte,T(2)(23.5)]))

tettoRetro= CUBOID([1,2,0.1])
tettoRetro = T([1,2,3])([-1,7.3,10])(tettoRetro)
tettiRetro = STRUCT(NN(2)([tettoRetro,T(2)(12.5)]))

#BalconeFronte
baseBalcone = CUBOID([1.5,3.5,0.2])
palettoRinghiera = CUBOID([0.05,0.05,0.65])
paletti = STRUCT(NN(24)([palettoRinghiera,T(2)(0.15)]))
paletti = T(3)(0.2)(paletti)
palettoRinghieraX = palettoRinghiera
palettoRinghieraX = T([1,2])([1,2])(palettoRinghieraX)
palettiX = STRUCT(NN(10)([palettoRinghiera,T(2)(0.15)]))
palettiX = R([1,2])(PI/2)(palettiX)
palettiX = T([1,3])([1.5,0.2])(palettiX)
upRinghieraY = CUBOID([0.05,3.5,0.05])
upRinghieraY = T(3)(0.85)(upRinghieraY)

upRinghieraX = CUBOID([1.5,0.05,0.05])
upRinghieraX = T(3)(0.85)(upRinghieraX)
upRinghieraX  =STRUCT(NN(2)([upRinghieraX,T(2)(3.45)]))
palettiX = STRUCT(NN(2)([palettiX,T(2)(3.45)]))
upRinghiera = STRUCT([upRinghieraX,upRinghieraY])
balcone = STRUCT([baseBalcone,paletti,upRinghiera,palettiX])

balcone = T([1,2])([-14,-4.5])(balcone)
balcone = R([1,2])(-PI)(balcone)
balconiFronte = STRUCT(NN(3)([balcone,T(3)(3.5)]))
balconiFronte = STRUCT(NN(2)([balconiFronte,T(2)(23.5)]))
tettoFronte = CUBOID([1.5,3.5,0.1])
tettoFronte = T([1,2,3])([12.5,1,10])(tettoFronte)
tettiFronte = STRUCT(NN(2)([tettoFronte,T(2)(23.5)]))

balconi = STRUCT([balconiRetro,balconiFronte,tettiFronte,tettiRetro])

#BASE

domain = larDomain([48,48])
controlPoints1 = [[0, 0,0], [-2, 6.5,0], [0, 13,0]]
controlPoints2 = [[0, 0,1], [-2, 6.5,1], [0, 13,1]]
controlPoints3 = [[0,0,1],[0,6.5,1],[0,13,1]]
controlPoints4 = [[0,0,1],[-2,6.5,1],[0,13,1]]
b1 = BEZIER(S1)(controlPoints1)
b2 = BEZIER(S1)(controlPoints2)
b3 = BEZIER(S1)(controlPoints3)
b4 = BEZIER(S1)(controlPoints4)

mapping = BEZIER(S2)([b1,b2])
mappingBase = BEZIER(S2)([b3,b4])
surface = larMap(mapping)(domain)
surfaceBase = larMap(mappingBase)(domain)

model = STRUCT(MKPOLS(surface))
modelBase = STRUCT(MKPOLS(surfaceBase))

model = STRUCT([model,modelBase])
model2 = T(2)(15.8)(model)

modelRetro = STRUCT([model,model2])

modelFronte = T(1)(12)(modelRetro)
modelFronte = R([1,2])(PI)(modelFronte)
modelFronte = T([1,2])([24,28.5])(modelFronte)

controlPoints5 = [[0, 0,0], [-2, 6.15,0], [0,12.3,0]]
controlPoints6 = [[0, 0,1], [-2, 6.15,1], [0,12.3,1]]
controlPoints7 = [[0,0,1],[0,6.15,1],[0,12.5,1]]
controlPoints8 = [[0,0,1],[-2,6.15,1],[0,12.5,1]]
b5 = BEZIER(S1)(controlPoints5)
b6 = BEZIER(S1)(controlPoints6)
b7 = BEZIER(S1)(controlPoints7)
b8 = BEZIER(S1)(controlPoints8)

mappingLato = BEZIER(S2)([b5,b6])
mappingLatoBase = BEZIER(S2)([b7,b8])
surfaceLato = larMap(mappingLato)(domain)
surfaceLatoBase = larMap(mappingLatoBase)(domain)

modelL = STRUCT(MKPOLS(surfaceLato))
modelBase = STRUCT(MKPOLS(surfaceLatoBase))
modelLato = STRUCT([modelL,modelBase])
modelLato = R([1,2])(PI/2)(modelLato)
modelLato = T(1)(12)(modelLato)

modelLato2 = R([1,2])(PI)(modelLato)
modelLato2 = T([1,2])([11.8,28.8])(modelLato2)

glass = [0.1,0.2,0.47,1,  0,0,0,0.48,  2,2,2,1, 0,0,0,1, 50]
domain = larDomain([48,48])
controlPointsv1 = [[0, 0,0], [-2,1.75,0], [0,3.5,0]]
controlPointsv2 = [[0, 0,9], [-2,1.75,9], [0,3.5,9]]
controlPointsv3 = [[0,0,9],[0,1.75,9],[0,3.5,9]]
controlPointsv4 = [[0,0,9],[-2,1.75,9],[0,3.5,9]]
controlPointsv5 = [[0,0,0],[0,1.75,0],[0,3.5,0]]
controlPointsv6 = [[0,0,0],[-2,1.75,0],[0,3.5,0]]
bv1 = BEZIER(S1)(controlPointsv1)
bv2 = BEZIER(S1)(controlPointsv2)
bv3 = BEZIER(S1)(controlPointsv3)
bv4 = BEZIER(S1)(controlPointsv4)
bv5 = BEZIER(S1)(controlPointsv5)
bv6 = BEZIER(S1)(controlPointsv6)

mappingVetro = BEZIER(S2)([bv1,bv2])
mappingBaseVetro = BEZIER(S2)([bv3,bv4])
mappingBaseVetroInf = BEZIER(S2)([bv5,bv6])
surfaceVetro = larMap(mappingVetro)(domain)
surfaceBaseVetro = larMap(mappingBaseVetro)(domain)
surfaceBaseVetroInf = larMap(mappingBaseVetroInf)(domain)

modelV = STRUCT(MKPOLS(surfaceVetro))
modelBaseV = STRUCT(MKPOLS(surfaceBaseVetro))
modelBaseVInf = STRUCT(MKPOLS(surfaceBaseVetroInf))
modelVetro = STRUCT([modelV,modelBaseV,modelBaseVInf])

modelVetro = T([2,3])([12.6,2.5])(modelVetro)

modelVetro = MATERIAL(glass)(modelVetro)

modelVetro2 = R([1,2])(PI)(modelVetro)
modelVetro2 = T([1,2])([12.4,28.8])(modelVetro2)

street = CUBOID([22,5])
street = T(2)(18)(street)

#Albero
tree = doTree([15.5,17])([0.5,3])
treesX = STRUCT(NN(2)([tree,T(2)(6.8)]))
treesY = STRUCT(NN(3)([treesX,T(1)(2.5)]))

#Disegno finale
master = STRUCT(MKPOLS(master))
building = STRUCT([master,upstairs,balconi])
building = T(3)(1)(building)
bcurve = STRUCT([building,model,modelRetro,modelFronte,modelLato,modelLato2,modelVetro,modelVetro2])
bcurve = T([1,2])([1,6])(bcurve)
base = CUBOID([22,40])
base = COLOR(grassColor)(base)
ambient = STRUCT([bcurve,base,street,treesY])
VIEW(ambient)