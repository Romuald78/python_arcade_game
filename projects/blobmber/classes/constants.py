

class Constants():

    DEBUG_PHYSICS = False
    DEBUG_LOW_CRATES = True

    # ==============================================
    # PLAYERS
    # ==============================================
    KEYBOARD_CTRLID1 = 1000000
    KEYBOARD_CTRLID2 = 2000000
    MAX_NB_PLAYERS = 8

    # ==============================================
    # GRID
    # ==============================================
    NB_CELLS_X = 18
    NB_CELLS_Y = 14
    BLOCKS_REDUCE_FACTOR = 1.3

    # ==============================================
    # BLOBS
    # ==============================================
    BLOB_ALPHA = 220
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
    BLOB_HW_RATIO      = 1.0
    BLOB_MOVE_SPEED    = 150   # pix per sec
    BLOB_FRAME_SPEED   = 1/35  # sec per frame
    BLOB_SIZE_COEF     = 2.0
    BLOB_REDUCE_FACTOR = 4
    BLOB_Y_OFFSET      = 3.5

    BUBBLE_FRAME_SPEED = 1/7
    BUBBLE_SIZE_COEF = 1
    BUBBLE_COLL_SIZE_COEF = 0.9
    BUBBLE_COUNTDOWN = 5
    BUBBLE_FADE_TIME = 3
    BUBBLE_POWER = 4
    BUBBLE_PROPAGATION_DELAY = 0.15
    BUBBLE_SHAKE_HALF = 4
    BUBBLE_SHAKE_TIME = 2

    CRATE_DESTROY_TIME = 0.4

    RUNE_OFFSET_KY = 0.225
    RUNE_SIZE_RATIO = 0.9

    SELECT_RATIO = 4.5
