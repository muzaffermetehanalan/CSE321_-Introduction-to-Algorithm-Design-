def TOHtime(fromP,toP,withP):
	height = int(input("Input size is "))
	liste = []
	for i in range(0,(height)):
		liste.append(0)

	movingTower(height,fromP,toP,withP,liste)


	for i in range(0,height):
		print ("Elasped time for disk  " + str(i+1) + ":" + str(liste[i]))


def movingTower(height,fromP, toP, withP,liste):
    if height >= 1:
        movingTower(height-1,fromP,withP,toP,liste)
        movingDisk(height,fromP,toP,liste)
        movingTower(height-1,withP,toP,fromP,liste)

def movingDisk(height,fp,tp,liste):
    print("disk " + str(height) + ":" + fp + " to " + tp)

    if( (fp == "SRC" and tp == "DST") or (fp == "DST" and tp == "SRC")):
    	value = 2*height
    else:
    	value = height


    liste[height-1]+= value



TOHtime("SRC","DST","AUX")