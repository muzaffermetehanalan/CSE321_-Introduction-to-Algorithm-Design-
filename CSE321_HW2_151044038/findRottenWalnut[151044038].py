def compareScales (leftScaleList, rightScaleList): 
	result = sum(leftScaleList) - sum(rightScaleList) 
	if result < 0:
		return 1 
	elif result > 0:
		return -1
	else: 
		return 0



def findRottenWalnut(walnuts):

	halfWalnuts = (int) (len(walnuts)/2)

	if(len(walnuts)%2== 0):
		leftSList = walnuts[:halfWalnuts]
		rightSList = walnuts[halfWalnuts:]
		result = compareScales(leftSList,rightSList)

	else:
		leftSList = walnuts[:halfWalnuts]
		rightSList = walnuts[(halfWalnuts+1):]
		result = compareScales(leftSList,rightSList)
		if(result == 0):
			return halfWalnuts

	if (len(walnuts)==1):
		return 0

	if result == 1:
		return  findRottenWalnut(leftSList)

	elif result == -1:
		if(len(walnuts)%2 == 1):
			halfWalnuts = halfWalnuts+1
			return  halfWalnuts + findRottenWalnut(rightSList)

		else:
			return halfWalnuts + findRottenWalnut(rightSList)



print (findRottenWalnut([1,1,1,1,0.5,1]))











