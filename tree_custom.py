import turtle
import numpy as np
AUR=1.6180339887 # AUR is the golden number in Spanish número aúreo
MAX_BRANCH_DEPTH = 5 # as higher MAX_BRANCH_DEPTH, more green detailed branches and more time required.
OMMIT = 2 # as higher OMMIT more probabilities to ommit a branch, values 0 (print all) to 10/MAX_BRANCH_DEPTH (ommit all).

INI_LEN = 100
LEN_MIN = 0.035*INI_LEN # shorter branches won´t be printed under this value

array_golden_angle=[]
arraylengths=[]
len_array_global = 0

def create_array_golden_angle():
    '''
    create an array of golden angles, from 10 to 120 degrees.
    '''
    ang=360
    while ang > 10:
        ang=ang/(AUR)
        if ang < 120:
            array_golden_angle.append(ang)

    
def golden_angle():
    '''
    Return an angle selected randomly in between golden angles.
    '''
    return array_golden_angle[np.random.randint(0, len(array_golden_angle))]

def create_golden_array(branch_len):
    '''
    golden_array creates an array of golden proportions for a given lengh.
    branch_len is gonna be always the longest
    followed by the subsequent shorter lengths in AUR proportions.
    '''
    next_length = branch_len
    arraylengths.append(next_length)
    i=1
    while next_length > LEN_MIN:
        next_length = next_length/(AUR)
        arraylengths.append(next_length)
        i=i+1
    global len_array_global
    len_array_global = i


def create_branch_right(branch_len,t, branch_counter):
    
	if np.random.uniform(0,10) > branch_counter*OMMIT and branch_counter < MAX_BRANCH_DEPTH and branch_len > LEN_MIN:
		deviation = np.random.uniform(0,branch_len/4.2360) # 4.2360 == AUR*AUR*AUR
		t.up()
		t.backward(deviation)
		anr = golden_angle() # Angle to right
		t.right(anr)
		branch_counter_aux = branch_counter
		branches(branch_len,t, branch_counter_aux)
		t.left(anr)
		t.up()
		t.forward(deviation)

def create_branch_left(branch_len,t, branch_counter):
    
	if np.random.uniform(0,10) > branch_counter*OMMIT and branch_counter < MAX_BRANCH_DEPTH and branch_len > LEN_MIN:
		deviation = np.random.uniform(0,branch_len/4.2360)
		t.up()
		t.backward(deviation)
		anl = golden_angle() # Angle to left
		t.left(anl)
		branch_counter_aux = branch_counter
		branches(branch_len,t, branch_counter_aux)
		t.right(anl)
		t.up()
		t.forward(deviation)

def set_branch_color(t, branch_len, banchAlt, branch_counter): 

    # banchAlt pabranch_countereter, is the length of the piece of branch to be painted
	t.width((branch_len/30) + (banchAlt/16))

	if branch_counter > MAX_BRANCH_DEPTH-2: # Set the colour, depend on the long branch
		t.color("#006600") #Green
	else:
		t.color("#341900") #Brown
		if branch_counter==1:
			t.color("#331900") #Brown

def branches(branch_len,t, branch_counter):
    '''
    As tree() does, this function call to create branches on the rigth and left side.
    '''
    branch_counter = branch_counter+1
	#len = golden_array(arraylengths, branch_len)
    i = branch_counter
    while i < len_array_global and arraylengths[i] > LEN_MIN:
        set_branch_color(t, branch_len,arraylengths[i], branch_counter)
        t.down()
        t.forward(arraylengths[i])
        create_branch_right(arraylengths[i],t, branch_counter)
        create_branch_left(arraylengths[i],t, branch_counter)
        create_branch_right(arraylengths[i],t, branch_counter)
        create_branch_left(arraylengths[i],t, branch_counter)
        t.up()
        t.backward(arraylengths[i])
        i=i+1

def tree(branch_len,t, branch_counter):
    '''
    Recurrent main function, in other words this call to create branches right/left, which calls to branche reciprocally
    tree needs the branch_counter pabranch_countereter (starting at 0),
    which is usefull to find a limitation on the depth as well as to paint green the thinnest/last branches.
    branch_len is the lngest branch we want to represent, for instance 265 is good to start.
    This length will be stored in an array, followed by the next smaller longs in Aureal proportions.
    t is the object of the turtle Class
    '''
    branch_counter = branch_counter+1
    Total=0
    t.down()	
    for i in range(len_array_global):
        set_branch_color(t, branch_len, arraylengths[i], branch_counter)
        t.forward(arraylengths[i])
        Total = Total+arraylengths[i]

    t.up()
    t.backward(Total)
    for i in range(len_array_global):
        
        print( i," ", len_array_global)
        print(arraylengths[i])
        #set_branch_color(t, branch_len, arraylengths[i], branch_counter)
        #pause = int(input())
        t.up()
        t.forward(arraylengths[i])
        #pause = int(input())
        #print(pause)
        create_branch_right(arraylengths[i],t, branch_counter)
        create_branch_left(arraylengths[i],t, branch_counter)
        create_branch_right(arraylengths[i],t, branch_counter)
        create_branch_left(arraylengths[i],t, branch_counter)
        
    t.up()
    t.backward(Total)



def main():
    
    Ini_length_branch = INI_LEN
    branch_counter=0
    create_array_golden_angle()
    create_golden_array(Ini_length_branch)

    t = turtle.Turtle()
    t.pencolor("#331900")
    myWin=turtle.Screen()
    myWin.bgcolor("#060614")
    t.speed(0)
    t.width(1)
    # Turtle starts in (0,0), in the midle-centre of the screen
    t.left(90)
    t.up()
    t.backward(200)
    t.down() # located now in the midle-down
    tree(Ini_length_branch,t,branch_counter)
    t.up()
    t.left(90)
    t.forward(250)
    t.down()
    t.width(3)
    t.pencolor("#006600") #Green, ground
    t.backward(500)
    t.up()
    t.forward(250)
    t.right(90)
    myWin.exitonclick()

main()
