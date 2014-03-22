#Floor0
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

verts0_T = [[1.15,0.3],[1.3,0.3],[1.15,1.2],[1.3,1.2],[1.15,1.2],[0.8,1.3],[0.95,1.2]]
cells0_T = [[1,2,3,4]]
wall_T = MKPOL([verts0_T,cells0_T,pols])
#VIEW(wall_T)
floor0 = STRUCT([wall0_rect_sx,wall0_down_sx,wall0_up,wall0_upstairs,wall0_down_dx,wall0_up_dx,wall_T])
VIEW(floor0)





verts0_ext = [[0,4],[1.65,4],[1.65,1.9],[1.5,1.9],[1.5,3.75],[0,3.75]]
cells0_ext = [[1,2,5,6],[2,3,4,5]]
pols = None
floor0_sx = MKPOL([verts0_ext, cells0_ext, pols])
#VIEW(floor0_sx)

vert0_ups = [[0.8,1.9],[0.9,1.9],[0.8,3.15],[0.9,3.15]]
cells0_ups = [[1,2,3,4]]
pols = None
ups = MKPOL([vert0_ups,cells0_ups,pols])

verts_wall_sx = [[0,3],[0.25,3],[0,0.7],[0.25,0.7]]
cells_wall_sx = [[1,2,3,4]]
pols = None
wall_sx = MKPOL([verts_wall_sx,cells_wall_sx,pols])


verts_wall_down_sx = [[0,0],[1.65,0],[1.65,0.25],[0.25,0.25],[0.25,0.4],[0,0.4]]
cells_wall_down_sx = [[1,2,3,4],[4,5,6,1]]
pols = None
wall_sx = MKPOL([verts_wall_down_sx,cells_wall_down_sx,pols])
#VIEW(wall_sx)

verts_wall_up_dx = [[4,4],[4,0.65],[3.75,0.65],[3.75,3.75],[2.35,3.75],[2.35,2.6],[2.15,2.6],[2.15,4]]
cells_wall_up_dx = [[1,2,3,4],[1,4,5,8],[5,6,7,8]] 
pols = None
wall_up_dx = MKPOL([verts_wall_up_dx,cells_wall_up_dx,pols])
#VIEW(wall_up_dx)

verts_wall_rect_sx = [[0,0.65],[0.25,0.65],[0,3],[0.25,3]]
cells_wall_rect_sx = [[1,2,3,4]]
pols = None
wall_rect_sx = MKPOL([verts_wall_rect_sx,cells_wall_rect_sx,pols])
#VIEW(wall_rect_sx)


verts_wall_down_dx = [[2.15,1.85],[2.35,1.85],[2.35,0.3],[2.15,0],[4,0],[4,0.4],[3.75,0.4],[3.75,0.3]]
cells_wall_down_dx = [[1,2,3,4],[3,4,5,8],[5,6,7,8]]
pols = None
wall_down_dx =MKPOL([verts_wall_down_dx,cells_wall_down_dx,pols])
#VIEW(wall_down_dx)

verts_wall_T = [[0.75,0.3],[0.85,0.3],[0.75,0.8],[0.85,0.8],[0.8,1.3],[1,1.1],[1.65,1.3],[1.65,1.1],[0.8,0.9],[1,0.9],[0.8,1.1],[0.75,1.3]]
cells_wall_T = [[1,2,3,4],[10,7,3,10],[5,9,6,7],[5,6,9,10]]
pols = None
wall_T =MKPOL([verts_wall_T,cells_wall_T,pols])
VIEW((wall_T))

floor0 = STRUCT([floor0_sx,ups,wall_sx,wall_up_dx,wall_rect_sx,wall_down_dx,wall_T])
VIEW(((floor0)))



#Floor1
verts_wall_rect_sx = [[0,0.65],[0.25,0.65],[0,3],[0.25,3]]
cells_wall_rect_sx = [[1,2,3,4]]
pols = None
wall_rect_sx = MKPOL([verts_wall_rect_sx,cells_wall_rect_sx,pols])

verts_wall_down_sx = [[0,0],[1.65,0],[1.65,0.3],[0.25,0.3],[0.25,0.4],[0,0.4]]
cells_wall_down_sx = [[1,2,3,4],[4,5,6,1]]
pols = None
wall_sx = MKPOL([verts_wall_down_sx,cells_wall_down_sx,pols])


verts_wall_up = [[0,4],[0,3.75],[3.75,3.75],[4,4],[4,2.35],[3.75,2.35]]
cells_wall_up = [[1,2,3,4],[4,5,6,3]]
pols = None
wall_up = MKPOL([verts_wall_up,cells_wall_up,pols])
#VIEW(wall_up)

verts_wall_down = [[2.35,0],[4,0],[3.75,0.35],[2.35,0.35],[4,2],[3.75,2]]
cells_wall_down = [[1,2,3,4],[2,5,6,3]]
pols = None
wall_down = MKPOL([verts_wall_down,cells_wall_down,pols])
#VIEW(wall_down)

verts_int_wall = [[1.5,3.75],[1.6,3.75],[1.5,0.7],[1.6,0.7]]
cells_int_wall = [[1,2,3,4]]
pols = None
int_wall = MKPOL([verts_int_wall,cells_int_wall,pols])
#VIEW(int_wall)


verts_upstairs = [[0.8,1.8],[0.95,1.8],[0.95,3.1],[0.8,3.1]]
cells_upstairs = [[1,2,3,4]]
pols = None
wall_upstairs = MKPOL([verts_upstairs,cells_upstairs,pols])
#VIEW(wall_upstairs)

floor1 = STRUCT([wall_rect_sx,wall_sx,wall_up,wall_down,int_wall,wall_upstairs])
VIEW(floor1)


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
VIEW(floor2)


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
VIEW(wall3_ext_down)
floor3 = STRUCT([wall3_down,wall3_rect_sx,wall3_up,wall3_up_dx,wall3_ext_up,wall3_ext_down])
VIEW(floor3)

floors = STRUCT([basement,floor0])
VIEW(SKELETON(1)(floors))

