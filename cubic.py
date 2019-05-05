'''
Arlan Vincent Uy
2015-09385
CS 131 THU
'''

'''
Juico, Jules Gerard E.
2014-40314
CS 131 THU
'''

import math

def main():
     file_object = open("input2.txt", "r")
     outputfile_object = open("output2.txt", "w")
     counter = 0
     num_rows = 0

     x_row_vector = []
     y_row_vector = []
     for line in file_object:
        line_counter = 0
        if counter == 0:
            while line[line_counter] != '\n':
                num_rows = num_rows + (ord(line[line_counter]) - ord('0'))
                num_rows *= 10
                line_counter += 1
            num_rows /= 10
            num_rows = int(num_rows)
        elif counter == 1:
            array_of_coeffs = line.split(',' , num_rows + 1)
            array_of_coeffs[-1] = array_of_coeffs[-1][:-1]

            for coeff in array_of_coeffs:
                x_row_vector.append(float(coeff))


        elif counter == 2:
            array_of_coeffs = line.split(',' , num_rows + 1)
            array_of_coeffs[-1] = array_of_coeffs[-1][:-1]

            for coeff in array_of_coeffs:
                y_row_vector.append(float(coeff))



        counter += 1
     matrix_counter = 4
     a_coeffs_matrix = []
     while matrix_counter <= num_rows:
         matrix = []
         constructPowerSeriesFittingMatrix(matrix, x_row_vector, y_row_vector, matrix_counter - 4)
         GaussianElim(matrix, 4)
         #print(matrix)
         #finding out the coefficient of the interpolants:
         a_row_vector = []
         for i in range(0, 4):
             a_row_vector.append(matrix[i][4])
         #print("a_row_vector is ")
         #print(a_row_vector)
         a_coeffs_matrix.append(a_row_vector)
         matrix_counter += 1
     outputfile_object.write("[")
     for j in range(0, num_rows - 3):
         for i in range(0, 4):
             outputfile_object.write(str(a_coeffs_matrix[j][i]) + " ")
         outputfile_object.write("\n")
     outputfile_object.write("]")
      #print(a_coeffs_matrix)
'''
Input: x_row_vector: contains the x-coordinates of the data points
y_row_vector: contains the y-coordinates of the data points
num_rows: size of matrix
'''
def constructPowerSeriesFittingMatrix(matrix, x_row_vector, y_row_vector, iteration):
    row_index = 0
    #print(x_row_vector)
    #print(y_row_vector)
    while row_index <  4:
        coeffs = []
        column_index = 0
        while column_index <  5:
            if column_index == 0:
                coeffs.append(1)
            elif column_index == 4:
                coeffs.append(y_row_vector[row_index + iteration])
                #print("entry is 4 " + str(y_row_vector[row_index + iteration]) + " row_index is " + str(row_index + iteration))
            else:
                entry = math.pow(x_row_vector[row_index + iteration],  column_index)
                #print("entry is " + str(entry) + " row_index is " + str(row_index + iteration))
                coeffs.append(entry)
            column_index += 1
        matrix.append(coeffs)
        row_index += 1
    #print(matrix)
'''
Input: matrix: the matrix from the GaussianElim method
row: the current row to be scaled
pivot_index: the row index associated with the pivot being used at the moment
multiplier: The number that will be multiplied on all of the coefficients in the current row
num_rows: size of matrix
Method: Scales the current row in order to zero out an element in the current row
'''
def scaleRow(matrix, row, pivot_index, multiplier, num_rows):
    counter = pivot_index
    while counter <= num_rows:
        row[counter] = (row[counter] * multiplier) + matrix[pivot_index][counter]
        counter += 1

'''
Input: matrix from the main method
num_rows: size of the matrix
Method: Uses all of the steps associated with the Gaussian Elimination method
'''
def GaussianElim(matrix, num_rows):

    row_counter = 0
    while row_counter < num_rows:
        column_counter  = 0
        while column_counter < row_counter:
            pivot = matrix[column_counter][column_counter]
            current = matrix[row_counter][column_counter]
            if current != 0:
                multiplier = (pivot / current) * -1
                scaleRow(matrix, matrix[row_counter], column_counter, multiplier, num_rows)
            column_counter += 1
        row_counter += 1

main( )
