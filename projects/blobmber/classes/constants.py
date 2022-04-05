

class Constants():

    DEBUG_PHYSICS = False

    KEYBOARD_CTRLID1 = 1000000
    KEYBOARD_CTRLID2 = 2000000

    NB_CELLS_X = 18
    NB_CELLS_Y = 14

    SELECT_RATIO = 4.5

    BLOB_ALPHA = 220
    BLOB_COLORS = [(128,255,128,220),(128,128,255,220)]
    BLOB_POS = [
        (1,1),
        (NB_CELLS_X-1,NB_CELLS_Y-1),
        (NB_CELLS_X-1, 1),
        (1, NB_CELLS_Y-1),
        (NB_CELLS_X//2,NB_CELLS_Y-1),
        (NB_CELLS_X // 2, 1),
        (3, NB_CELLS_Y // 2),
        (NB_CELLS_X-3, NB_CELLS_Y // 2),

    ]
    BLOB_HW_RATIO = 1.0
    BLOB_MOVE_SPEED  = 150   # pix per sec
    BLOB_FRAME_SPEED = 1/35  # sec per frame
    BLOB_SIZE_COEF   = 2.0
    BLOB_REDUCE_FACTOR = 4
    BLOB_Y_OFFSET      = 12

    BLOCKS_REDUCE_FACTOR = 1.2

    BUBBLE_FRAME_SPEED = 1/7
    BUBBLE_SIZE_COEF = 1
    BUBBLE_COLL_SIZE_COEF = 0.9