#EAST
vertsEAST_base = [[0.85,0],[4.85,0],[4.85,8.7],[0.85,8.7]]
cellsEAST_base = [[1,2,3,4]]
pols = None 
EAST_base = MKPOL([vertsEAST_base,cellsEAST_base,pols])
EAST_base = COLOR(GRAY)(EAST_base)
#VIEW(EAST_base)

vertsEAST_cube = [[0,6.25],[4,6.25],[0,10.45],[4,10.45]]
cellsEAST_cube = [[1,2,3,4]]
pols = None 
EAST_cube = MKPOL([vertsEAST_cube,cellsEAST_cube,pols])
EAST_cube = COLOR(GRAY)(EAST_cube)
#VIEW(EAST_cube)

window_down = CUBOID([0.4,1.4])
window_down = T([1,2])([1.35,1.3])(window_down)
window_down = COLOR(BLUE)(window_down)

window_sq1 = CUBOID([0.7,0.75])
window_sq1 = T([1,2])([2.4,3])(window_sq1)
window_sq1 = COLOR(BLUE)(window_sq1)

window_sq2 = CUBOID([0.7,0.75])
window_sq2 = T([1,2])([2.4,4.4])(window_sq2)
window_sq2 = COLOR(BLUE)(window_sq2)

window_sq3 = CUBOID([0.7,0.75])
window_sq3 = T([1,2])([1.7,7.9])(window_sq3)
window_sq3 = COLOR(BLUE)(window_sq3)
EAST = STRUCT([EAST_base,EAST_cube,window_down,window_sq1,window_sq2,window_sq3])
#VIEW(EAST)

#NORTH
vertsNORTH_base = [[0.85,0],[4.85,0],[4.85,8.7],[0.85,8.7]]
cellsNORTH_base = [[1,2,3,4]]
pols = None 
NORTH_base = MKPOL([vertsNORTH_base,cellsNORTH_base,pols])
NORTH_base = COLOR(GRAY)(NORTH_base)
#VIEW(NORTH_base)

vertsNORTH_cube = [[0,6.25],[4,6.25],[0,10.45],[4,10.45]]
cellsNORTH_cube = [[1,2,3,4]]
pols = None 
NORTH_cube = MKPOL([vertsNORTH_cube,cellsNORTH_cube,pols])
NORTH_cube = COLOR(GRAY)(NORTH_cube)
#VIEW(EAST_cube)

window_Base = CUBOID([0.67,1])
window_Base = T([1,2])([2.6,4.85])(window_Base)
window_Base = COLOR(BLUE)(window_Base)

window_cube_rect = CUBOID([0.6,2.15])
window_cube_rect = T([1,2])([0.25,6.45])(window_cube_rect)
window_cube_rect = COLOR(YELLOW)(window_cube_rect)

window_cube = CUBOID([3.35,1.5])
window_cube = T([1,2])([0.25,8.6])(window_cube)
window_cube = COLOR(BLUE)(window_cube)

NORTH = STRUCT([NORTH_base,NORTH_cube,window_Base,door,window_cube_rect,window_cube])
VIEW(NORTH)

#WEST
vertsWEST_base = [[0,0],[4,0],[4,8.7],[0,8.7]]
cellsWEST_base = [[1,2,3,4]]
pols = None 
WEST_base = MKPOL([vertsWEST_base,cellsWEST_base,pols])
WEST_base = COLOR(GRAY)(WEST_base)
#VIEW(NORTH_base)

vertsWEST_cube = [[0.8,6.25],[4.8,6.25],[0.8,10.45],[4.8,10.45]]
cellsWEST_cube = [[1,2,3,4]]
pols = None 
WEST_cube = MKPOL([vertsWEST_cube,cellsWEST_cube,pols])
WEST_cube = COLOR(GRAY)(WEST_cube)
#VIEW(EAST_cube)

window_big0 = CUBOID([0.3,0.86])
window_big0 = T([1,2])([0.25,0])(window_big0)
window_big0 = COLOR(BLUE)(window_big0)

window_big1 = CUBOID([0.3,2])
window_big1 = T([1,2])([0.25,1.27])(window_big1)
window_big1 = COLOR(BLUE)(window_big1)

window_big2 = CUBOID([0.3,2])
window_big2 = T([1,2])([0.25,3.36])(window_big2)
window_big2 = COLOR(BLUE)(window_big2)

window_big3 = CUBOID([0.3,2])
window_big3 = T([1,2])([0.25,5.53])(window_big3)
window_big3 = COLOR(BLUE)(window_big3)

window_WEST_sq0 = CUBOID([0.3,0.3])
window_WEST_sq0 = T([1,2])([3.25,0])(window_WEST_sq0)
window_WEST_sq0 = COLOR(BLUE)(window_WEST_sq0)

window_WEST_sq1 = CUBOID([0.3,0.3])
window_WEST_sq1 = T([1,2])([3.25,2.2])(window_WEST_sq1)
window_WEST_sq1 = COLOR(BLUE)(window_WEST_sq1)

window_WEST_sq2 = CUBOID([0.3,0.3])
window_WEST_sq2 = T([1,2])([3.25,4.37])(window_WEST_sq2)
window_WEST_sq2 = COLOR(BLUE)(window_WEST_sq2)

rect1 = CUBOID([0.08,6.25])
rect1 = T([1,2])([1.8,0])(rect1)
rect1 = COLOR(YELLOW)(rect1)

rect2 = CUBOID([0.08,6.25])
rect2 = T([1,2])([2,0])(rect2)
rect2 = COLOR(YELLOW)(rect2)

rect3 = CUBOID([0.08,2.10])
rect3 = T([1,2])([2.61,8.35])(rect3)
rect3 = COLOR(YELLOW)(rect3)

rect4 = CUBOID([0.08,2.10])
rect4 = T([1,2])([2.81,8.35])(rect4)
rect4 = COLOR(YELLOW)(rect4)
WEST = STRUCT([WEST_base,WEST_cube,window_big0,window_big1,window_big2,window_big3,window_WEST_sq0,window_WEST_sq0,window_WEST_sq1,window_WEST_sq2,rect1,rect2,rect3,rect4])
VIEW(WEST)

