import turtle
import numpy as np


def angleMeth(): # In the future could give an Aur angle, random
	return np.random.uniform(20,90)

def ArrAur(array, branchLen): # ArrAur creates an array of Aur proportions for a given lengh
	#Aur=1.6180339887
	auxlong = branchLen
	Aur=1.600 + np.random.uniform(0,0.036)
	array.append(auxlong)
	i=1
	while auxlong > 3:
		auxlong=auxlong/Aur
		array.append(auxlong)
		i=i+1
	return i

def CreateBranchRight(branchLen,t, ram):
	if ram < 3:
		anr = angleMeth() # Angle to right
		t.right(anr)
		ramaux=ram
		Branches(branchLen,t, ramaux)
		t.left(anr)

def CreateBranchLeft(branchLen,t, ram):
	if ram < 3:
		anl = angleMeth() # Angle to left
		t.left(anl)
		ramaux=ram
		Branches(branchLen,t, ramaux)
		t.right(anl)

def SetWidColor(t, branchLen):
	wid=branchLen/13
	t.width(wid)

	if branchLen < 17: # Set the colour, depend on the long branch
		t.color("#006600") #Green
	else:
		t.color("#331900") #Brown
	return wid

def Branches(branchLen,t, ram):

	ram = ram+1
	array=[]
	len = ArrAur(array, branchLen)
	#print(array)
	#t.forward(branchLen)
	
	Total=0
	i = 1
	while i < len:

		SetWidColor(t, branchLen)
		t.down()
		t.forward(array[i])
		CreateBranchRight(array[i],t, ram)
		CreateBranchLeft(array[i],t, ram)
		t.up()
		t.backward(array[i])
		i=i+1

	#t.backward(branchLen)

def tree(branchLen,t, ram):

	ram = ram+1
	array=[]
	len = ArrAur(array, branchLen)
	print(array)
	#t.forward(branchLen)
	
	Total=0
	i = 1
	while i < len:

		SetWidColor(t, branchLen)
		t.down()	
		t.forward(array[i])
		CreateBranchRight(array[i],t, ram)
		CreateBranchLeft(array[i],t, ram)
		Total = Total+array[i]
		i=i+1
	# We create new branches-trees on the right side
	#CreateBranchRight(branchLen,t, ram)

	# We create new branches-trees on the left side
	#CreateBranchLeft(branchLen,t, ram)

	t.up()
	t.backward(Total)
	#t.backward(branchLen)
	
def main():

	LONGINI=165
	ram=0
	t = turtle.Turtle()
	t.color("#331900")
	myWin=turtle.Screen()
	myWin.bgcolor("#060614")
	t.speed(0)
	t.width(1)
	# Turtle starts in (0,0), in the midle-centre of the screen
	t.left(90)
	t.up()
	t.backward(200)
	t.down() # located now in the midle-down

	tree(LONGINI,t,ram) #long inicial 161 y ram=0 (orden de la ramificacion)
	
	t.up()
	t.left(90)
	t.forward(250)
	t.down()
	t.width(3)
	t.color("#006600") #Green, ground
	t.backward(500)
	t.up()
	t.forward(250)
	t.right(90)
	myWin.exitonclick()
main()
