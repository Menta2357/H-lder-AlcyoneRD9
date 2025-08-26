# EXAMPLES/cuadrados_mod9.py
# Ejemplo reproducible: Hölder (clásico) vs AlcyoneRD9 en mod 9
# Genera además un gráfico comparativo (figures/comparativa.png)

import numpy as np
import os
import matplotlib.pyplot as plt

def holder_classic_bound(X, Y, p=2, prob=None):
    X = np.asarray(X, float); Y = np.asarray(Y, float)
    n = len(X)
    if prob is None: prob = np.ones(n)/n
    q = p/(p-1)
    norm_X = (np.sum((np.abs(X)**p)*prob))**(1/p)
    norm_Y = (np.sum((np.abs(Y)**q)*prob))**(1/q)
    return norm_X * norm_Y

def alcyone_rd_bound(X, Y, classes, p=2, prob=None):
    X = np.asarray(X, float); Y = np.asarray(Y, float)
    n = len(X)
    if prob is None: prob = np.ones(n)/n
    q = p/(p-1)
    total = 0.0
    for c in classes:
        mask = np.zeros(n, dtype=bool); mask[c] = True
        if not mask.any(): 
            continue
        nx = (np.sum((np.abs(X[mask])**p)*prob[mask]))**(1/p)
        ny = (np.sum((np.abs(Y[mask])**q)*prob[mask]))**(1/q)
        total += nx*ny
    return total

def compare_bounds(X, Y, classes, p=2, prob=None):
    c_clas = holder_classic_bound(X, Y, p=p, prob=prob)
    c_alcy = alcyone_rd_bound(X, Y, classes, p=p, prob=prob)
    mejora = (c_clas - c_alcy)/c_clas*100 if c_clas>0 else 0.0
    return c_clas, c_alcy, mejora

if __name__ == "__main__":
    N = 9
    prob = np.ones(N)/N
    C_R1 = [0,1,4,7]            # clases cuadráticas activas
    classes = [C_R1]

    # -------- Caso A: X uniforme, Y filtrado (mejora ~33.33%) --------
    X = np.ones(N)
    Y = np.array([1 if i in C_R1 else 0 for i in range(N)])
    c1A, c2A, gA = compare_bounds(X, Y, classes, p=2, prob=prob)
    print(f"[Caso A] Clásico={c1A:.4f}  AlcyoneRD={c2A:.4f}  Mejora={gA:.2f}%")

    # -------- Caso B: X e Y uniformes (mejora ~55.56%) ---------------
    X2 = np.ones(N); Y2 = np.ones(N)
    c1B, c2B, gB = compare_bounds(X2, Y2, classes, p=2, prob=prob)
    print(f"[Caso B] Clásico={c1B:.4f}  AlcyoneRD={c2B:.4f}  Mejora={gB:.2f}%")

    # Gráfico comparativo
    os.makedirs("figures", exist_ok=True)
    labels = ["Sin estructura", "Caso A", "Caso B"]
    clasico = [1.0, c1A, c1B]
    alcyone = [1.0, c2A, c2B]

    x = np.arange(len(labels))
    plt.figure(figsize=(6.5,4))
    plt.bar(x-0.20, clasico, width=0.4, label="Clásico", color="steelblue")
    plt.bar(x+0.20, alcyone, width=0.4, label="AlcyoneRD", color="seagreen")
    plt.xticks(x, labels)
    plt.ylabel("Valor de la cota")
    plt.title("Hölder clásico vs AlcyoneRD9 (mod 9)")
    plt.ylim(0,1.1)
    plt.legend()
    out = "figures/comparativa.png"
    plt.tight_layout(); plt.savefig(out, dpi=160)
    print(f"Gráfico guardado en: {out}")
