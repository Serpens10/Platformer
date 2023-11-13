level_map = [
'                            ',    
'                            ', 
'                            ',   
'XX     XXX            XX    ', 
'XX                          ',    
'XXXX          XX         XX ', 
'XXXX        XX              ',     
'XX     X  XXXX    XX  XX    ',    
'       X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']

TILESIZE = 64
screen_width = 1200
screen_height = len(level_map) * TILESIZE
# make height relative to the level map. rows*tilesize 11*64
