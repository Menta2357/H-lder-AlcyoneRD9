# EJEMPLOS/gaussian_pi.py
# Modelo simplificado del caso gaussiana (π):
# RD-partition con dos clases: C y R1. Y se anula en R1 (cancelación de modos),
# lo que produce una mejora ~29-30% frente a la cota clásica.

import numpy as np
import os
import matplotlib.pyplot as plt
from src.alcyoneRD import compare_bounds

def gaussian_weights(n, A):
    """Pesos gaussianos w(k) = exp(-k^2/A) normalizados a suma 1."""
    k = np.arange(-n, n+1)
    w = np.exp(-(k**2)/A)
    return k, w/np.sum(w)

if __name__ == "__main__":
    # --- Parámetros del modelo ---
    n = 2000          # soporte simétrico [-n, n]
    A = 5000.0        # anchura gaussiana
    k, prob = gaussian_weights(n, A)        # prob ~ gaussiana
    N = len(k)

    # Partición RD minimal para el modelo: dos clases (C y R1)
    # (No necesitamos mod 9 aquí, solo simulamos dos bloques estructurales)
    C_idx  = (k % 2 == 0)     # clase "C" (pares) como proxy
    R1_idx = ~C_idx           # clase "R1" (impares)
    classes = [np.where(C_idx)[0], np.where(R1_idx)[0]]

    # Señales:
    # X: uniforme (no distingue clases)
    # Y: activa solo en C (anulada en R1) -> simula cancelación de modos
    X = np.ones(N)
    Y = np.zeros(N); Y[C_idx] = 1.0

    # Cotas (p=q=2)
    c_clas, c_alc, mej = compare_bounds(X, Y, classes=[classes[0]], p=2, prob=prob)
    # Nota: AlcyoneRD suma sólo la clase activa (classes[0]=C)

    print(f"Clásico={c_clas:.4f}  AlcyoneRD={c_alc:.4f}  Mejora={mej:.2f}%")

    # Gráfico comparativo
    os.makedirs("figures", exist_ok=True)
    labels = ["Clásico", "AlcyoneRD"]
    values = [c_clas, c_alc]

    plt.figure(figsize=(5.5,3.8))
    bars = plt.bar(labels, values, color=["steelblue", "seagreen"])
    for b,v in zip(bars, values):
        plt.text(b.get_x()+b.get_width()/2, v+0.01, f"{v:.3f}", ha="center", va="bottom", fontsize=10)
    plt.ylabel("Valor de la cota")
    plt.title("Caso gaussiana (modelo simplificado)")
    plt.ylim(0, max(values)*1.15)
    out = "figures/gaussian_compare.png"
    plt.tight_layout(); plt.savefig(out, dpi=160)
    print(f"Gráfico guardado en: {out}")
