#! /usr/bin/env python
# coding: utf-8
# matrix_calc.py
# 2021-10-05
#

def vec_to_mat(v):
    m = [[v[0]], [v[1]], [v[2]]]
    return m
    
def mat_to_vec(m):
    v = (m[0][0], m[1][0])
    if len(m) > 2:
        v = (m[0][0], m[1][0], m[2][0])
    return v

def matmul(a, b):
    colsA = len(a[0])
    rowsA = len(a)
    colsB = len(b[0])
    rowsB = len(b)
    
    if colsA != rowsB:
        print("Columns of A must match rows of B")
        return
        
    result = [[0 for _ in range(colsB)] for _ in range(rowsA)]
    
    for i in range(rowsA):
        for j in range(colsB):
            sigma = 0
            for k in range(colsA):
                sigma += a[i][k] * b[k][j]
            result[i][j] = sigma
    return mat_to_vec(result)