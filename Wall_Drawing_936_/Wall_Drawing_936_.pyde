# my chosen colour range, using 6 of my favourite colours from the first piece
# colour list starts empty to be filled in setup() once the canvas is made and to be read within curves() later to be drawn
colours = []
# set the canvas
def setup():
    global colours
    size(1200, 800)
    noStroke()
    colours = [
        color(247, 167, 191),  # pastel pink
        color(209, 160, 227),  # pastel purple
        color(159, 220, 250),  # pastel blue
        color(250, 241, 159),  # yellow
        color(199, 250, 159),  # pastel green
        color(250, 166, 81)    # orange
    ]

def draw():
    background(0)
    # stripe refers to the curved stripe made out of overlapping circles (ellipse)
    stripe = 20 + mouseX // 20          # X-coordinate of mouse changes thickness of curved stripes, lower X value = thinner, higher = thicker 
    if mousePressed:
        stripe = stripe * 2               # * is multiplication, pressing the mouse makes curved stripes 2X thicker while held down
    move = mouseY // 40              # Y-coordinate of the mouse moves the colours of curved stripes 

    # curves(boxX, boxY, boxWidth, boxHeight, centreX, centreY, stripe, move)
    # boxX, boxY, boxWidth, boxHeight sets the parameters of the four boxes with curved stripes drawn in
    # centreX, centreY is referring to the centre of each circle (ellipse) that overlap to form the appearance of curved stripes
    curves(30, 30, 550, 350, 30, 380, stripe, move)      # top left box, centre of circles is bottom left corner
    curves(620, 30, 550, 350, 620, 30, stripe, move)     # top right box, centre of circles is top left corner
    curves(30, 420, 550, 350, 580, 770, stripe, move)    # bottom left box, centre of circles is bottom right corner
    curves(620, 420, 550, 350, 1170, 420, stripe, move)  # bottom right box, centre of circles is top right corner

def curves(boxX, boxY, boxW, boxH, centreX, centreY, stripe, move):
    clip(boxX, boxY, boxW, boxH)      # stops the circles from being drawn/displayed outside the box 
    # range(start, stop, step)
    for c in range(40, -1, -1):       # biggest circle first which is '40 * stripe' from the centre to fill the designated box section
                # fill the circles using colour-list variable, adds colour move along the circles, cycles back to start of the colour list when it runs out
        fill(colours[(c + move) % len(colours)])                    # len() = length: returns the number of items in the colour list
        # ellipse(centre X, centre Y, width, height) - width and height are the same to make a circle
        # c * stripe is the distance from the centre to the edge, * 2 gives the width across the whole circle
        ellipse(centreX, centreY, c * stripe * 2, c * stripe * 2)

    noClip()                          # closes the clip before the next box 
