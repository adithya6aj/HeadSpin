
#matrix = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]] 
#matrix = [[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5]]
# matrix = [[1,2,3,4,5],[2,3,4,5,1],[3,4,5,1,2],[4,5,1,2,3],[5,1,2,3,4]] 

def main():
    solution = True
    matrix = []
    for i in range(5):   
        a =[] 
        for j in range(5):
             a.append(int(input())) 
        matrix.append(a) 
    #To display the sudoku
    for i in range(5):
    	for j in range(5):
    		print(matrix[i][j], end = "")
		print()
    #Check whether sum of each row = 15 otherwise exit the program and return False
    total = 0
    for row in matrix:
        total = 0
        for m in range(5):
            total = total + row[m]
        if total != 15:
        	solution = False
        	total = 0
        	break
    # #Check whether sum of each column = 15 otherwise exit the program and return False
    if solution:
        for i in range(0,len(matrix)):
            total = 0
            total = matrix[0][i]
            for j in range(1,len(matrix)):
                total = total +matrix[j][i]
            if total != 15:
                solution = False
                total = 0
                break

    if solution:
        rowRepetition = checkRow(matrix)
        columnRepetition = checkColumn(matrix)
        if not rowRepetition and columnRepetition:
	        solution = True
        else:
        	False
    print(solution)
    return solution
#To check whether thers is a repeating element in the row
def checkRow(matrix):
    repetition = False
    for row in matrix:
        for m in range(5):
            k = m+1
            for j in range(k,len(matrix)-1):
                if row[m] == row[j]:
                    repetition = True
    return repetition

#To check whether thers is a repeating element in the column
def checkColumn(matrix):
    colRepetition = False
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            k = j+1
            for m in range(k,len(matrix)):
                if matrix[j][i] == matrix[m][i]:
                    colRepetition = True
                    break
    return colRepetition

if __name__ == "__main__":
    main()

