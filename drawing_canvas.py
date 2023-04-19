#imports from utils, which imports from setting
from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Program")

def init_grid(rows, cols, color):
    grid = []
    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)
          
    return grid
    # [ 28 rows, 28 columns, tuple with rgb values
    #  [(255,255,255),(255,255,255)],
    #  [(255,255,255),(255,255,255)],
    #  [],
    #  [],
    # ]

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE),
                             (WIDTH, i * PIXEL_SIZE))

        for i in range(COLS + 1):
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0 ),
                             (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))
            

def draw(win, grid):
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)
    pygame.display.update()


def get_row_col_from_pos(pos):
    #decompose the tuple
    x, y = pos
    row = x // PIXEL_SIZE
    col = y // PIXEL_SIZE

    #check we dont click something on the non drawable
    #area

    if row >= ROWS:
        raise IndexError
    
    return row, col
    
def convert_canvas_to_array(canvas):
    array = []
    for i in range(len(canvas)):
        for j in range(len(canvas[i])):
            array.append(255 - canvas[i][j][0])
    return array
 
def sdg_predict(array):
    #time.sleep(1)
    return(sgd_clf.predict([array]))
    
def forest_predict(array):
    return(forest_clf.predict([array]))

def predict_value():
    result = sdg_predict(convert_canvas_to_array(grid))[0]
    buttons[5] = Button(310, button_y, 150, 50, WHITE, f"Value: {result}" , BLACK)
    time.sleep(3000)

def print_test():
    print("print")
    time.sleep(300)


#Event Loop
run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK
value = ""
#Loads ML Models from different file
with open('sgd_model.pkl', 'rb') as f:
    sgd_clf = pickle.load(f)

with open('forest_model.pkl', 'rb') as f:
    forest_clf = pickle.load(f)

button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button(10, button_y, 50, 50, BLACK),
    Button(70, button_y, 50, 50, WHITE, "Erase", BLACK),
    Button(130, button_y, 50, 50, WHITE, "Clear", BLACK),
    Button(190, button_y, 50, 50, WHITE, "SGD", BLACK),
    Button(250, button_y, 90, 50, WHITE, "FOREST", BLACK),
    Button(350, button_y, 150, 50, WHITE, f"Predict Value {value}" , BLACK),
]

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #check if left mouse button is closed 0
    if pygame.mouse.get_pressed()[0]:
        
        #figure out if they pressed pixel, 
        pos = pygame.mouse.get_pos()
        try:
            row, col = get_row_col_from_pos(pos)
            grid[col][row] = drawing_color
            #grid[col][row + 1] = drawing_color
            grid[col][row -1] = drawing_color
            grid[col + 1][row] = drawing_color
            #grid[col - 1][row] = drawing_color
        except IndexError:
            for button in buttons:
                if not button.clicked(pos):
                    continue

                drawing_color = button.color
                if button.text == "Clear":
                    grid = init_grid(ROWS, COLS, BG_COLOR) 
                    result = ""
                    buttons[5] = Button(350, button_y, 150, 50, WHITE, f"Predict Value {result}" , BLACK)
                    drawing_color = BLACK 
                elif button.text == "SGD": 
                    SGD = True
                    FOREST = False
                    drawing_color = BLACK

                elif button.text == "FOREST":
                    FOREST = True
                    SGD = False
                    drawing_color = BLACK 
                
                elif button.text == f"Predict Value {value}":
                    array = convert_canvas_to_array(grid)
                    if SGD:
                        result = sdg_predict(array)[0]
                    elif FOREST:
                        result = forest_predict(array)[0]

                    buttons[5] = Button(350, button_y, 150, 50, WHITE, f"Value: {result}" , BLACK)
                    drawing_color = BLACK
                    print("drawing color", drawing_color)
                
                elif button.text == f"Value: {result}":
                    array = convert_canvas_to_array(grid)
                    if SGD:
                        result = sdg_predict(array)[0]
                    elif FOREST:
                        result = forest_predict(array)[0]

                    buttons[5] = Button(350, button_y, 150, 50, WHITE, f"Value: {result}" , BLACK)
                    drawing_color = BLACK
               
    draw(WIN, grid)

pygame.quit()
