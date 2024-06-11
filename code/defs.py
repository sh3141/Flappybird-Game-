###### IMAGES FILE PATH #########
BG_IMAGE_FILEPATH = '../BG.png'
PIPE_IMAGE_FILEPATH = '../Pipe.png'
BIRD_IMAGE_FILEPATH = '../bird6.png'
COIN_GOLD1_IMG_FILEPATH = '../coin_gold1.png'
COIN_GOLD2_IMG_FILEPATH = '../coin_gold2.png'
COIN_GOLD3_IMG_FILEPATH = '../coin_gold3.png'
COIN_GOLD4_IMG_FILEPATH = '../coin_gold4.png'
COIN_GOLD5_IMG_FILEPATH = '../coin_gold5.png'
COIN_GOLD6_IMG_FILEPATH = '../coin_gold6.png'
### TUTORIAL TEXT FILE ########
TUTORIAL_TEXT_FILEPATH = '../tutorial.txt'

##### SCREEN FOR GAME DISPLAY ######
DISPLAY_WIDTH = 960
DISPLAY_HEIGHT = 540
FPS = 30

#### PAUSE SCREEN #####
LABEL_OFFSET = 30
LABEL_DATA_OFFSET = 15

### STATE ###
PAUSE = 0
LOST = 1
### MODE ####
MANUAL = 0
AI =1
### PAUSE STATUS RETURN PARAMETERS ###
QUIT = 0
RETURN_TO_MAIN_MENU = 1
RESTART = 2
RESUME = 3 
#### QUIT #####
QUIT_DISPLAY_WIDTH = 200
QUIT_DISPLAY_HEIGHT =100

##### MAIN MENU ######
MAIN_MENU_FONT_TYPE = "arialblack"
MAIN_MENU_FONT_SIZE = 40
MAIN_MENU_FONT_COLOUR = (0,150,0)

###### PIPE PARAMETERS #######
PIPE_VELOCITY= -70/1000
PIPE_UPPER = 1
PIPE_LOWER = 0 
PIPE_MOVING =1
PIPE_OUT = 0

##### PIPE SPACING PARAMETERS #####
PIPE_SPACING_X = 160
INITAL_PIPE_POS_X = 440
PIPE_GAP_MIN = 140
PIPE_GAP_MAX = 180
PIPE_GAP = 160
PIPE_MIN_Y = 75
PIPE_MAX_Y = 480 - PIPE_GAP_MAX

###COIN DISTANCE###
COIN_CLEARANCE = 20
SKEW = 0.1 #Alters probability of finding a coin

### SINGLE BIRD ###
ALIVE = 1
DEAD = 0
BIRD_SPEED_Y = -0.32 #inital velocity given to bird when it jumps
BIRD_INIT_POS_X = 200
BIRD_INIT_POS_Y = 200
g = 10/10000 #gravational acceleration

### BIRD GENETATION ###
GENERATION_SIZE = 60

### NEURAL NET PARAMETERS ###
HIDDEN_LAYERS = 1
NEURONS_PER_HIDDEN_LAYER = 5
NUM_OF_INPUTS = 3
NUM_OF_OUTPUTS = 1

nnet_input = 3
nnet_hidden = 5
nnet_output = 1

#### DESICION PARAMETERS ###
DO_JUMP = 0.5 # minimum neural network output at which the bird should jump 
COIN_WEIGHT = 0.35
SCORE_FACTOR = 5.0 #to make score as significant as distance to pipe gap
PENALTY_FACTOR = 1 # to reduce significance of distance penality
COINS_FACTOR = 80
### INPUT NORMALISATION ###
Y_MAX = DISPLAY_HEIGHT - PIPE_MIN_Y - PIPE_GAP_MIN /2
Y_MIN = PIPE_MAX_Y + PIPE_GAP_MAX/2
Y_SHIFT = abs(Y_MIN)
Y_NORMALISER = Y_SHIFT + Y_MAX  

max_y_dif = DISPLAY_HEIGHT - PIPE_GAP/2 - PIPE_MIN_Y
min_y_dif = PIPE_GAP/2 + PIPE_MAX_Y
y_shift = abs(min_y_dif)
normaliser = y_shift + max_y_dif


COIN_SHIFT = PIPE_MAX_Y + PIPE_GAP_MAX - COIN_CLEARANCE
COIN_NORMALISER = COIN_SHIFT + DISPLAY_HEIGHT - PIPE_MIN_Y - COIN_CLEARANCE

### SELECTION AND MUTATION PARAMETERS ####
mutation_array_mix_perc = 0.5
MAX_MIXING_PERCENTAGE =mutation_array_mix_perc

mutation_weight_modify_chance = 0.2
MUTATION_RATIO = mutation_weight_modify_chance 


mutation_cut_off = 0.4
GOOD_PERCENTAGE = mutation_cut_off


mutation_bad_to_keep = 0.2
BAD_BUT_KEEP = mutation_bad_to_keep

mutation_modify_chance_limit = 0.4
MUTATION_CHANCE = mutation_modify_chance_limit
