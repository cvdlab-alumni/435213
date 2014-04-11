from pyplasm import *
from numpy import *
#Floor0

verts = [[0,0],[0,4],[4,4],[4,0]]
cells = [[1,2,3,4]]
pols = None
base = MKPOL([verts,cells,pols])

verts0_wall_rect_sx = [[0,0.65],[0.25,0.65],[0,3],[0.25,3]]
cells0_wall_rect_sx = [[1,2,3,4]]
pols = None
wall0_rect_sx = MKPOL([verts0_wall_rect_sx,cells0_wall_rect_sx,pols])
#VIEW(wall_rect_sx)

verts0_wall_down_sx = [[0,0],[1.65,0],[1.65,0.3],[0.25,0.3],[0.25,0.4],[0,0.4]]
cells0_wall_down_sx = [[1,2,3,4],[4,5,6,1]]
pols = None
wall0_down_sx = MKPOL([verts0_wall_down_sx,cells0_wall_down_sx,pols])
#VIEW(wall0_down_sx)

verts0_upstairs = [[0.8,1.8],[0.95,1.8],[0.95,3.1],[0.8,3.1]]
cells0_upstairs = [[1,2,3,4]]
pols = None
wall0_upstairs = MKPOL([verts0_upstairs,cells0_upstairs,pols])
#VIEW(wall_upstairs)

verts0_wall_up = [[0,4],[0,3.75],[1.5,3.75],[1.8,4],[1.8,1.8],[1.5,1.8]]
cells0_wall_up = [[1,2,3,4],[3,4,5,6]]
pols = None
wall0_up = MKPOL([verts0_wall_up,cells0_wall_up,pols])
#VIEW(wall0_up)

verts0_wall_down_dx = [[3.75,0.4],[4,0.4],[4,0],[3.75,0.3],[2.35,0],[2.45,0.3],[2.35,1.85],[2.45,1.85]]
cells0_wall_down_dx =[[1,2,3,4],[3,5,6,4],[5,8,7,6]]
pols = None
wall0_down_dx = MKPOL([verts0_wall_down_dx,cells0_wall_down_dx,pols])
#VIEW(wall_down_dx)


verts0_wall_up_dx = [[2.3,2.5],[2.4,2.5],[2.3,4],[2.4,3.75],[4,4],[3.75,3.75],[3.75,0.65],[4,0.65]]
cells0_wall_up_dx =[[1,2,3,4],[5,6,3,4],[5,6,7,8]]
pols = None
wall0_up_dx = MKPOL([verts0_wall_up_dx,cells0_wall_up_dx,pols])
#VIEW(wall0_up_dx)

verts0_T = [[1.15,0.3],[1.3,0.3],[1.15,1.2],[1.3,1.2],[1.65,1.15],[1.65,1.3],[0.85,1.3],[0.85,1.15],[1,1.15],[0.85,0.9],[1,0.9]]
cells0_T = [[1,2,3,4],[5,6,7,8],[8,9,10,11]]
wall_T = MKPOL([verts0_T,cells0_T,pols])
#VIEW(wall_T)
floor0 = STRUCT([wall0_rect_sx,wall0_down_sx,wall0_up,wall0_upstairs,wall0_down_dx,wall0_up_dx,wall_T])
#VIEW(floor0)




#Floor1
verts1_wall_rect_sx = [[0,0.65],[0.25,0.65],[0,3],[0.25,3]]
cells1_wall_rect_sx = [[1,2,3,4]]
pols = None
wall1_rect_sx = MKPOL([verts1_wall_rect_sx,cells1_wall_rect_sx,pols])
#VIEW(wall1_rect_sx)

verts1_wall_down_sx = [[0,0],[1.65,0],[1.65,0.3],[0.25,0.3],[0.25,0.4],[0,0.4]]
cells1_wall_down_sx = [[1,2,3,4],[4,5,6,1]]
pols = None
wall1_sx = MKPOL([verts1_wall_down_sx,cells1_wall_down_sx,pols])
#VIEW(wall1_sx)

verts1_wall_up = [[0,4],[0,3.75],[3.75,3.75],[4,4],[4,2.35],[3.75,2.35]]
cells1_wall_up = [[1,2,3,4],[4,5,6,3]]
pols = None
wall1_up = MKPOL([verts1_wall_up,cells1_wall_up,pols])
#VIEW(wall1_up)

verts1_wall_down = [[2.35,0],[4,0],[3.75,0.35],[2.35,0.35],[4,2],[3.75,2]]
cells1_wall_down = [[1,2,3,4],[2,5,6,3]]
pols = None
wall1_down = MKPOL([verts1_wall_down,cells1_wall_down,pols])
#VIEW(wall1_down)

verts1_int_wall = [[1.5,3.75],[1.6,3.75],[1.5,0.7],[1.6,0.7]]
cells1_int_wall = [[1,2,3,4]]
pols = None
int1_wall = MKPOL([verts1_int_wall,cells1_int_wall,pols])
#VIEW(int1_wall)


verts1_upstairs = [[0.8,1.8],[0.95,1.8],[0.95,3.1],[0.8,3.1]]
cells1_upstairs = [[1,2,3,4]]
pols = None
wall1_upstairs = MKPOL([verts1_upstairs,cells1_upstairs,pols])
#VIEW(wall1_upstairs)

floor1 = STRUCT([wall1_rect_sx,wall1_sx,wall1_up,wall1_down,int1_wall,wall1_upstairs])
#VIEW(floor1)


#Floor2
verts2_upstairs = [[0.8,1.8],[0.95,1.8],[0.95,3.1],[0.8,3.1]]
cells2_upstairs = [[1,2,3,4]]
pols = None
wall2_upstairs = MKPOL([verts2_upstairs,cells2_upstairs,pols])
#VIEW(wall_upstairs)

verts2_wall_up = [[0,4],[0,3.75],[1.5,3.75],[1.65,4],[1.65,1],[1.5,1]]
cells2_wall_up = [[1,2,3,4],[3,4,5,6]]
pols = None
wall2_up = MKPOL([verts2_wall_up,cells2_wall_up,pols])
#VIEW(wall_up)

verts2_wall_rect_sx = [[0,0.65],[0.25,0.65],[0,3],[0.25,3]]
cells2_wall_rect_sx = [[1,2,3,4]]
pols = None
wall2_rect_sx = MKPOL([verts2_wall_rect_sx,cells2_wall_rect_sx,pols])
#VIEW(wall_rect_sx)

verts2_wall_down = [[0,0],[0.25,0],[0.25,0.37],[0,0.37]]
cells2_wall_down = [[1,2,3,4]]
pols = None
wall2_down = MKPOL([verts2_wall_down,cells2_wall_down,pols])
#VIEW(wall_down)

verts2_wall_down_dx = [[4,0],[4,2],[3.75,2],[3.75,0]]
cells2_wall_down_dx = [[1,2,3,4]]
pols = None
wall2_down_dx = MKPOL([verts2_wall_down_dx,cells2_wall_down_dx,pols])
#VIEW(wall_down_dx)

verts2_wall_up_dx = [[2.35,4],[2.35,3.75],[4,4],[3.75,3.75],[4,2.75],[3.75,2.75]]
cells2_wall_up_dx = [[1,2,3,4],[3,4,6,5]]
pols = None
wall2_up_dx = MKPOL([verts2_wall_up_dx,cells2_wall_up_dx,pols])
#VIEW(wall2_up_dx)

floor2 = STRUCT([wall2_upstairs,wall2_up,wall2_rect_sx,wall2_down,wall2_down_dx,wall2_up_dx])
#VIEW(floor2)


#floor3
verts3_wall_down = [[0,0],[0.25,0],[0.25,0.37],[0,0.37]]
cells3_wall_down = [[1,2,3,4]]
pols = None
wall3_down = MKPOL([verts3_wall_down,cells3_wall_down,pols])
#VIEW(wall3_down)

verts3_wall_rect_sx = [[0,0.65],[0.25,0.65],[0,3],[0.25,3]]
cells3_wall_rect_sx = [[1,2,3,4]]
pols = None
wall3_rect_sx = MKPOL([verts3_wall_rect_sx,cells3_wall_rect_sx,pols])
#VIEW(wall3_rect_sx)

verts3_wall_up = [[0,4],[0,3.75],[1.5,3.75],[1.65,4],[1.65,1],[1.5,1]]
cells3_wall_up = [[1,2,3,4],[3,4,5,6]]
pols = None
wall3_up = MKPOL([verts3_wall_up,cells3_wall_up,pols])
#VIEW(wall3_up)

verts3_wall_up_dx = [[2.35,4],[2.35,3.75],[3.75,3.75],[4,4],[4,3],[3.75,3]]
cells3_wall_up_dx = [[1,2,3,4],[3,4,5,6]]
pols = None
wall3_up_dx = MKPOL([verts3_wall_up_dx,cells3_wall_up_dx,pols])
#VIEW(wall3_up_dx)

verts3_wall_ext_up = [[4.45,3.25],[4.8,3.25],[4.8,2],[4.45,2]]
cells3_wall_ext_up = [[1,2,3,4]]
pols = None
wall3_ext_up = MKPOL([verts3_wall_ext_up,cells3_wall_ext_up,pols])
#VIEW(wall3_ext_up)

verts3_wall_ext_down = [[4.45,1.2],[4.8,1.2],[4.8,-0.75],[4.45,-0.75]]
cells3_wall_ext_down = [[1,2,3,4]]
pols = None
wall3_ext_down = MKPOL([verts3_wall_ext_down,cells3_wall_ext_down,pols])
#VIEW(wall3_ext_down)


floor3 = STRUCT([wall3_down,wall3_rect_sx,wall3_up,wall3_up_dx,wall3_ext_up,wall3_ext_down])

#VIEW(floor3)

f0Color = COLOR(RED)(floor0)
f1Color = COLOR(BLUE)(floor2)
f2Color = COLOR(GREEN)(floor2)
f3Color = COLOR(YELLOW)(floor3)
f0 = STRUCT([f0Color,base])
f1 = STRUCT([f1Color,base])
f2 = STRUCT([f2Color,base])
f3 = STRUCT([f3Color,base])
building = STRUCT([f0,f1,f2,f3])
f1t = T(3)(1)(f1)
f2t = T(3)(2)(f2)
f3t = T(3)(3)(f3)
building = STRUCT([f0,f1t,f2t,f3t])
VIEW(building)
