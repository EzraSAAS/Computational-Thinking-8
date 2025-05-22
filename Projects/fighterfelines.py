# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(imagefile, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, imagefile)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
# TODO - create your player character
# TODO - set your background
# TODO - set the starting value for your variable
s1 = create_sprite("r-cat")
set_background("map")
s1.direction = "right"

s2 = create_sprite("rat")
# Section 3: Controls
# TODO - define your controls
def move_up():
	s1.setheading(90)
	s1.forward(10)
   	 
def move_down():
	s1.setheading(270)
	s1.forward(10)
    
def move_left():
	s1.setheading(180)
	s1.forward(10)
	if s1.direction == "right":
		set_image(s1, "l-cat")
		s1.direction = "left"
def move_right():    
	s1.setheading(0)
	s1.forward(10)
	if s1.direction == "left":
		set_image(s1, "r-cat")
		s1.direction = "right"

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")
# TODO - pick keys for each control

# Section 4: Game Loop
window.listen()
timer = 0
obstacles = []
while True:
	time.sleep(0.01)
	timer += 1  
	
	if timer % 100 == 0:
		y_position = random.randint(-250, 250)
		x_position = random.randint(-250, 250)
		s2 = create_sprite("rat")
		s2.setheading(random.randint)(0, 360)
		obstacles.append(s2)
    
	for s2 in obstacles:
		s2.forward(10)
		if get_distance(s1,s2) < 10:
			score += 1
			s2.hideturtle()
			obstacles.remove(s2)
 	# TODO - code for automatic actions
	# create mice every 10 sec



	# interact wth mice





	window.update()

	# if :
	# 	break
	

print("Game Over")
