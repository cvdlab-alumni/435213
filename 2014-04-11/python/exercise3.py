from larcc import *
from pyplasm import *
import exercise2

def rgb2color(rgb):
	r,g,b = rgb
	nr = float(r)/255
	nb = float(b)/255
	ng = float(g)/255
	return [nr,nb,nb]


prato = CUBOID([42.5,50,0.3])
prato = COLOR(GREEN)(prato)
sea = CUBOID([10,50,0.3])
sea = T(1)(42.5)(sea)
sea = COLOR(BLUE)(sea)
base = CUBOID([15,50,1])
base = T([1,3])([20,0.3])(base)
baseSmall = CUBOID([7.5,50,0.5])
baseSmall = T([1,3])([35,0.3])(baseSmall)
house4x4 = exercise2.building
house4x4 = T([1,2,3])([31,17,1.3])(house4x4)

houseCube = CUBOID([4,4,4])
houseBase = CUBOID([4,4,8.7])
houseCube = T([1,2,3])([0.8,-0.8,6.5])(houseCube)
colorhouseGemella = rgb2color([74,78,79])

house4x4gemella = STRUCT([houseBase,houseCube])
#VIEW(house4x4gemella)
house4x4gemella = T([1,2,3])([31,25,1.3])(house4x4gemella)
house4x4gemella = COLOR(colorhouseGemella)(house4x4gemella)

colonna = larRod([0.3,4])([48,2])
colonna = STRUCT(MKPOLS(colonna))
colonneX = STRUCT(NN(2) ([colonna,T(1)(4)]))
colonneX = STRUCT(NN(3) ([colonneX,T(2)(4)]))
colonneY = STRUCT(NN(3) ([colonna,T(2)(4)]))
colonnato = STRUCT([colonneX, colonneY])
colonnato = T(1)(0.5)(colonnato)
V = [[0,0],[5,0],[5,1.6],[3,2],[2.5,5],[2,2],[0,1.6]]
FV = [[0,1,2,3,4,5,6,0]]
tettoContorno = V,FV

V1 = AA(LIST)([0.,10])
C1V = [[0,1]]
tetto = V1,C1V

tetto = larModelProduct([tettoContorno,tetto])
tetto = STRUCT(MKPOLS(tetto))
tetto = R([2,3])(PI/2)(tetto)
#tetto = R([1,2])(PI/2)(tetto)
tetto = T([2,3])([9,3.5])(tetto)
capannone = STRUCT([colonnato,tetto])
capannone = T([1,2])([28,4])(capannone)

houseRed_color = rgb2color([92,58,56])
houseRed = CUBOID([6,4,8])
houseRed = T([1,2])([23,35])(houseRed)
houseRed = COLOR(houseRed_color)(houseRed)

negozio_color = rgb2color([223,110,195])
negozio = CUBOID([10,8,5])
negozio = T([1,2])([23,40])(negozio)
negozio = COLOR(negozio_color)(negozio)

smallBasement = CUBOID([4,3,3])
smallBasement_color = rgb2color([87,99,44])
smallBasement = T([1,2])([30,35])(smallBasement)
smallBasement = COLOR(smallBasement_color)(smallBasement)

baseHouse = STRUCT([base,baseSmall,house4x4,house4x4gemella,capannone,houseRed,negozio,smallBasement])
area = STRUCT([prato,sea,baseHouse])
VIEW(area)