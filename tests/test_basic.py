from src.alcyoneRD import compare_bounds
import numpy as np

def test_caseB():
    """
    Caso B: X e Y uniformes sobre 9 clases, 
    AlcyoneRD apaga 5 clases inactivas -> mejora 55.6%
    """
    N=9; prob=np.ones(N)/N
    X=Y=np.ones(N)
    C_R1=[0,1,4,7]
    c_clas, c_alc, mej = compare_bounds(X,Y,[C_R1],p=2,prob=prob)
    assert round(mej,1) == 55.6
