# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 02:33:22 2021

@author: DiiCo
"""

import numpy as np

m = []

def matrix_create(n):
    global m
    #N bu N matrix creation (w/ zeros)
    m = np.zeros((n,n))
    n_row_index = -1
    n_column_index = 0 
    step_count = 0
    #N by N matrix modification (every element is 1 higher than the one before)
    for i in range ((n)*(n)):
        step_count += 1
        if step_count % n == 1:
            n_row_index += 1
            n_column_index = -1
        n_column_index += 1
        m[n_row_index][n_column_index] = i+1
    print('Matrix Creation')
    print(m)

def matrix_rotate_clockwise_90 ():
    global m
    placeholder = np.zeros((len(m),len(m)))
    test_list = []
    count_internal = len(m) - 1
    for i in range(len(m)):
        for k in m[i]:
            test_list.append(k)
        for i in range(len(test_list)):
            placeholder[i][count_internal] = test_list[i]
            if i >= 1:
                if i % (len(m)) == len(m)-1:
                    count_internal -= 1
        test_list.clear()  
    m = placeholder
    print('Matrix Rotation 90 Degrees Clockwise')
    print(m)
    

matrix_create(int(input('Enter the n number from which a matrix of n by n will be created\nand rotated 90 degrees clockwise 4 times (n can not be 1): ')))
print('\nFirst Rotation (90)')
matrix_rotate_clockwise_90()
print('\nSecond Rotation (180)')
matrix_rotate_clockwise_90()
print('\nThird Rotation (270)')
matrix_rotate_clockwise_90()
print('\nFourth Rotation (360)')
matrix_rotate_clockwise_90()