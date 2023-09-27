import numpy as np
import matplotlib
import random


class DeJongN5:
    name = "De Jong N. 5"
    latex_formula = r"f(x, y)= \left ( 0.002 + \sum_{i=1}^{25} \frac{1}{i+(x - a_{1, i})^6+(x - a_{2, ij})^6}  \right)^{-1}"
    latex_formula_dimension = r"d=2"
    latex_formula_input_domain = r"x \in [-65.536, 65.536], y \in [-65.536, 65.536]"
    latex_formula_global_minimum = r"f(-32, -32)\approx-0.998003838818649"
    continuous = True
    convex = False
    separable = False
    differentiable = True
    mutimodal = True
    randomized_term = False
    parametric = True

    @classmethod
    def is_dim_compatible(cls, d):
        assert (d is None) or (
            isinstance(d, int) and (not d < 0)
        ), "The dimension d must be None or a positive integer"
        return d == 2

    def __init__(self, d, a=None):
        self.d = d
        self.input_domain = np.array([[-65.536, 65.536], [-65.536, 65.536]])
        if a is None:
            l = [-32, -16, 0, 16, 32]
            self.a = np.array([[x, y] for x in l for y in l])
        else:
            self.a = a

    def get_param(self):
        return {"a": self.a}

    def get_global_minimum(self, d):
        X = self.a[0]
        return (X, self(X))
    def function_return(self):
        latex_formula = r"f(x, y)= \left ( 0.002 + \sum_{i=1}^{25} \frac{1}{i+(x - a_{1, i})^6+(x - a_{2, ij})^6}  \right)^{-1}"
        return latex_formula
    def __call__(self, X):
        x, y = X
        res = (
            0.002
            + np.sum(
                [
                    1 / ((i + 1) + (x - a1) ** 6 + (y - a2) ** 6)
                    for i, (a1, a2) in enumerate(self.a)
                ]
            )
        ) ** -1
        return res
    
