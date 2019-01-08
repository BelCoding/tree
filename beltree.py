import turtle
import numpy as np


def angleMeth():
	return np.random.uniform(10,50)

def ArrAur(array, branchLen):
	Aur=1.618
	
	i=1
	array.append(Aur*i)
	while Aur*(i+1) < branchLen:
		array.append(Aur*(i+1))
		i=i+1

	return i-1


def tree(branchLen,t, ram):
	
	array=[]
	len = ArrAur(array, branchLen) # Forma un array de numeros aureos
	#print(array)
	# Variables len, para escojer entre un rango de indices segun el tamanio que queramos, depende del orden ram.
	lenlimit = ram*ram+1 # el maximo ira creciendo (num mas grandes, ramas mas peq). 
	# Cuanto mas ramificaciones haya mas ramas pequenias ( el array va dividiendo a la branchLen)

	# Llamo a random desde 0 al maximo varias veces, para dar mas probabilidades a los numeros pequenios.
	# Asi el arbol tendra mas ramas.
	ind=0
	if lenlimit >= len: #limitamos el maximo a len, para que no haya overflow.
		lenlimit=len
	if lenlimit > 0: # Siempre con cuidado de no llamar a random en 0,0
		ind = np.random.randint(0, lenlimit)
	if ind > 0:		
		ind = np.random.randint(0, ind)
	if ind > 0:
		ind = np.random.randint(0, ind)

	#print(lenlimit, len, ram)
	#print(ind, array[ind], branchLen/array[ind])
	#print('\n')
	ram=ram+1
	
	wid=branchLen/13
	t.width(wid)

	if branchLen < 17: # SIN TERMINAR. Si es la ultima rama, la ponemos verde
		t.color("#006600") #Verde
	else:
		t.color("#331900") #Marron
	
	if branchLen > 3: # las menores de 1 no las pintamos
		t.down()
		t.forward(branchLen)
		tree( branchLen/array[ind],t, ram)
		anr = angleMeth()
		anl = angleMeth()
		t.right(anr)
		tree(branchLen/array[ind],t, ram)
		t.left(2*anl)
		tree(branchLen/array[ind],t, ram)
		t.right(2*anl - anr)
		t.up()

		# Si no son las ultimas ramas, va marron, para que no pinte encima verde al volver
		#	t.color("#331900") #Marron		
		t.backward(branchLen)
			
	
def main():

	LONGINI=161
	ram=0
	t = turtle.Turtle()
	t.color("#331900")
	myWin=turtle.Screen()
	myWin.bgcolor("#060614")
	t.speed(0)
	t.width(1)
	t.left(90)
	t.up()
	t.backward(200)
	t.down()
	tree(LONGINI,t,ram) #long inicial 161 y ram=0 (orden de la ramificacion)
	t.up()
	t.left(90)
	t.forward(250)
	t.down()
	t.backward(500)
	t.up()
	t.forward(250)
	t.right(90)
	myWin.exitonclick()
main()
