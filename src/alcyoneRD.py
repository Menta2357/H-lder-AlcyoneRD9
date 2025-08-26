import numpy as np

def holder_classic_bound(X, Y, p=2, prob=None):
    """Cota clásica de Hölder: ||X||_p * ||Y||_q con 1/p+1/q=1"""
    X = np.asarray(X,float); Y = np.asarray(Y,float)
    n = len(X)
    if prob is None:
        prob = np.ones(n)/n
    q = p/(p-1)
    norm_X = (np.sum((np.abs(X)**p)*prob))**(1/p)
    norm_Y = (np.sum((np.abs(Y)**q)*prob))**(1/q)
    return norm_X * norm_Y

def alcyone_rd_bound(X, Y, classes, p=2, prob=None):
    """Cota AlcyoneRD: suma por bloques de clases"""
    X = np.asarray(X,float); Y = np.asarray(Y,float)
    n = len(X)
    if prob is None:
        prob = np.ones(n)/n
    q = p/(p-1)
    total = 0.0
    for c in classes:
        mask = np.zeros(n,bool); mask[c]=True
        if not mask.any():
            continue
        nx = (np.sum((np.abs(X[mask])**p)*prob[mask]))**(1/p)
        ny = (np.sum((np.abs(Y[mask])**q)*prob[mask]))**(1/q)
        total += nx*ny
    return total

def compare_bounds(X, Y, classes, p=2, prob=None):
    """Devuelve (cota_clásica, cota_AlcyoneRD, mejora %)"""
    c_clas = holder_classic_bound(X, Y, p=p, prob=prob)
    c_alc  = alcyone_rd_bound(X, Y, classes, p=p, prob=prob)
    mejora = (c_clas - c_alc)/c_clas*100 if c_clas>0 else 0.0
    return c_clas, c_alc, mejora
