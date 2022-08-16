import numpy as np
import cv2 as cv
import random

class Graph:
    def __init__(self, adj_mat):
        self.matrix = adj_mat
        self.img = img = cv.imread("White.png", 1)
        self.s = int((adj_mat.size)**(1/2))
    
    def visualize(self):
        l = []
        font = cv.FONT_HERSHEY_SIMPLEX
        for i in range(self.s):
            rc = (random.randint(10, 700), random.randint(10, 490))
            l.append(rc)
            cv.circle(self.img, rc, 3, 0, 6)
            cv.putText(self.img, str(i+1), rc, font, 1, (255, 0, 0), 1)
        edges = []
        for a in range(self.s):
            for b in range(self.s):
                if A[a][b] == 1:
                    edges.append([a,b])
        for i in edges:
            cv.line(self.img, l[i[0]], l[i[1]], (23, 200 , 75), thickness = 2) 

        cv.imshow("Test", self.img)
        cv.waitKey()

A = np.array([[0,0,0,1,0,1,0],
[0,0,0,1,1,0,1],
[0,0,0,0,0,1,1],
[1,1,0,0,1,0,1],
[0,1,0,0,0,1,0],
[0,1,1,1,0,0,1],
[0,1,0,1,0,1,0]])

graph = Graph(A)
graph.visualize()
