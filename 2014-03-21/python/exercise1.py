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

verts_wall_sx = [[0,3.5],[0.25,3.5],[0,0.7],[0.25,0.7]]
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

verts_wall_T = [[0.75,0.25],[0.9,0.25],[0.75,0.75],[0.9,0.75]]
cells_wall_T = [[1,2,3,4]]
pols = None
wall_T =MKPOL([verts_wall_T,cells_wall_T,pols])
#VIEW(wall_down_dx)


floor0 = STRUCT([floor0_sx,ups,wall_sx,wall_up_dx,wall_rect_sx,wall_down_dx,wall_T])

VIEW(((floor0)))

floors = STRUCT([basement,floor0])
VIEW(SKELETON(1)(floors))

