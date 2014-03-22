#Floor -0
verts_basement_ext = [[0,0],[4,0],[4,4],[0,4]]
cells_basement_ext = [[1,2,3,4]]
pols = None
floor_ext = MKPOL([verts_basement_ext, cells_basement_ext, pols])
verts_basement_int = [[0.25,0.25],[3.75,0.25],[0.25,3.75],[3.75,3.75]]
cells_basement_int = [[1,2,3,4]]
floor_int = MKPOL([verts_basement_int, cells_basement_int, pols])
#VIEW(SKELETON(1)(floor_int))

verts_basement_wall = [[1.5,3.75],[1.65,3.75],[1.5,1.9],[1.65,1.7],[0.8,1.7],[0.9,1.9],[0.8,3.15],[0.9,3.15]]
cells_basement_wall = [[1,2,3,4],[3,4,5,6],[5,6,7,8]]
wall_int = MKPOL([verts_basement_wall, cells_basement_wall, pols])
#VIEW(wall_int)
basement = STRUCT([floor_int,floor_ext,wall_int])
#VIEW((basement))

#Floor0
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
VIEW(wall2_up_dx)

floor2 = STRUCT([wall2_upstairs,wall2_up,wall2_rect_sx,wall2_down,wall2_down_dx,wall2_up_dx])
VIEW(floor2)

floors = STRUCT([basement,floor0])
VIEW(SKELETON(1)(floors))

