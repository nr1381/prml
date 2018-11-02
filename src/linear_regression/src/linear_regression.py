import numpy as np

class LinearRegression(object):


    def __init__(self, dimension):
        self.dimension = dimension


    def phi(self, x, j):
        return x**j


    def train(self, x, y):
        matrix_tmp = []
        for x_elms in x.tolist():
            row = []
            for j in range(self.dimension):
                row.append(self.phi(x_elms, j))
            matrix_tmp.append(row)
        matrix = np.array(matrix_tmp)
        return (np.linalg.inv(matrix.T @ matrix)) @ (matrix.T @ y)


    def predict(self, x, w):
        y = []
        for x_elms in x.tolist():
            list_phi = []
            for j in range(self.dimension):
                list_phi.append(self.phi(x_elms, j))
            nd_phi = np.array(list_phi)
            y.append(np.dot(w, nd_phi))
        return y
