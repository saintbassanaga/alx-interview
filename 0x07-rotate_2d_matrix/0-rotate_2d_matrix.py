#!/usr/bin/env python3

C, R=3,3
def reverseColumns(arr):
    for i in range(C):
        j = 0
        k = C-1
        while j < k:
            t = arr[j][i]
            arr[j][i] = arr[k][i]
            arr[k][i] = t
            j += 1
            k -= 1

def transpose(arr):
    for i in range(R):
        for j in range(i, C):
            t = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = t

def rotate_2d_matrix(mat):
    reverseColumns(mat)
    transpose(mat)

    return mat