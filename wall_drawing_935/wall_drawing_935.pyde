move = 0    # counts the amount of times the colours move along the stripes in each box, no movement unless mouse is pressed, then the colours move along by one with each press
tinySquare = 1      # size of each tiny square that makes up the diagonal lines in bottom two sections

#set the canvas size once
def setup():
    size(1200, 800)
    noLoop()       # stops Processing from continuously executing this code within draw()

def draw():           #  draw() usually repeats but noLoop() in setup makes it run the code just once
    background(0) # black background like LeWitt's wall drawings that this piece is inspired by 
    noStroke()     # no outline 

    # colour set as list [], mostly pastel shades and using pinks rather than red
    # written in a compressed structure rather than rewriting lines of code for colour over and over again
    # 11 colours total that each box section moves through with the interaction by pressing the mouse
    colors = [
        color(247, 167, 191),  # pastel pink
        color(209, 160, 227),  # pastel purple
        color(159, 220, 250),  # pastel blue
        color(250, 241, 159),  # yellow
        color(199, 250, 159),  # pastel green
        color(250, 166, 81),   # orange
        color(81, 158, 250),   # royal blue
        color(252, 120, 146),  # pink
        color(194, 252, 240),  # teal
        color(166, 198, 138),  # olive green
        color(255, 255, 188)   # pastel yellow
    ]

    # top left box with vertical stripes 
    # loop drawing 11 rectangles within box parameters 
    for s in range(11):
        fill(colors[(s + move) % 11])
      # rect(x, y, width, height) - the x,y coordinates are always the top left corner of a rectangle
      # X = 25 + s * 50, Y = 25, width = 50 (thickness of each stripe), height = 350 (height of the box)
      # 11 stripes multiplied by 50 (width) equates to 550, filling the width of the box 
        rect(25 + s * 50, 25, 50, 350)

    # top right box with horizontal stripes 
    # loop drawing 7 rectangles within box parameters 
    for s in range(7):
        fill(colors[(s + move) % 11])
        # same concept as the vertical stripes but now s * 50 is part of the Y coordinate moving down rather than across
        # X = 620, Y = 25 + s * 50, width = 550 (width of the box), height = 50 (thickness of each stripe)
        # 7 stripes multiplied by 50 (height) equates to 350, filling the height of the box
        rect(620, 25 + s * 50, 550, 50)

    # bottom left box with diagonal stripes going positive angle (a + b)
    # 13 stripes (bottom right stripe is not fully visible)
    # a and b are the positions within the box parameters 
    # using a nested loop so that the inner loop runs completely from start to finish for every single iteration of the outer loop
    for a in range(0, 550, tinySquare):               # outer loop that moves across the box following x-axis
        for b in range(0, 350, tinySquare):               # inner loop that moves down the box following y-axis
        # brackets read from inside out - colour is determined by the final number from brackets inside
        # (a + b) is the same for each tinySquare along the diagonal stripe - when a goes up, b goes down by the same amount
        # colour is picked based on a + b position
        # the // operator used for floor division, drops the fraction and always rounds down to whole number
        # '70' controls the diagonal stripe thickness moving as 70 steps along the a + b direction - every 70 steps is a new diagonal stripe
        # '% 11' goes back to start of colour list when it runs out
            fill(colors[((a + b) // 70 + move) % 11]) 
            # square(a, b, extent) 
            # a = 25 + a, y = 420 + b, extent = tinySquare variable set at start (=1)
            # draws one tiny square repeatedly within the loops for every position within the ranges 
            # 30 and 420 are the X,Y coordinates that set the box parameters starting from top left corner    
            square(25 + a, 420 + b, tinySquare)

    # bottom right box with diagonal stripes going negative angle ( a - b)
    # 13 stripes (bottom left stripe is not fully visible)
    # same nested loop as bottom left box
    for a in range(0, 550, tinySquare):           # outer loop that moves across the box
        for b in range(0, 350, tinySquare):         # inner loop that moves down the box
            # subtracting b from a creates the opposite diagonal stripes
            # colour determined same as in bottom left box but going opposite angle
            fill(colors[((a - b) // 70 + move) % 11])
            # square() same method as bottom left box
            # 620 and 420 are the X,Y coordinates that set the box parameters starting from top left corner
            square(620 + a, 420 + b, tinySquare)

# one press on the mouse to action the move in colours once - each individual mouse-press actions one move of colours 
def mousePressed():
    global move
    move = move + 1    # move variable set at start as 0, only moves +1 when mouse is pressed 
    redraw()             # need redraw to enable the mousePressed function to work and change the screen since noLoop() was used in setup
                         # goes back to the draw() function and re-draws all the rectangles and tiny squares each time the colours move with the mouse press
