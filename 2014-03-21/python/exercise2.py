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
VIEW(EAST)

#NORTH
vertsNORTH_base = [[0.85,0],[4.85,0],[4.85,8.7],[0.85,8.7]]
cellsNORTH_base = [[1,2,3,4]]
pols = None 
NORTH_base = MKPOL([vertsNORTH_base,cellsNORTH_base,pols])
NORTH_base = COLOR(GRAY)(NORTH_base)
#VIEW(NORTH_base)

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
VIEW(EAST)

