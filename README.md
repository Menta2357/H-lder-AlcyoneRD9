# Hölder–AlcyoneRD9

Refinamiento **modular** de la desigualdad de Hölder que *apaga clases inactivas* y logra **mejoras del 25–55 %** en escenarios con estructura (p. ej., residuos cuadráticos mod 9 o sumas gaussianas).

---

## 1) Idea en 10 s

**Hölder clásico**  
\[
|E[XY]|\le \|X\|_p\,\|Y\|_q,\qquad \tfrac1p+\tfrac1q=1.
\]

**Hölder–AlcyoneRD9 (partición modular)**  
\[
|E[XY]|\;\le\;\sum_{c}\;\|X\cdot \mathbf 1_c\|_p\;\|Y\cdot \mathbf 1_c\|_q,
\]
donde las clases \(c\) son bloques RD (residuos/simetrías).  
- Si todas las clases están activas → **igual** que Hölder.  
- Si hay inactivas/resonancias → **estrictamente más ajustada** (25–55 %).

---

## 2) Instalación rápida / requisitos

- Python 3.9+  
- `numpy`, `matplotlib` (para los ejemplos y gráficos)

```bash
pip install numpy matplotlib

3) Uso como librería
from src.alcyoneRD import compare_bounds
import numpy as np

N = 9
prob = np.ones(N)/N
X = Y = np.ones(N)
C_R1 = [0,1,4,7]  # clases cuadráticas activas mod 9

c_clas, c_alc, mej = compare_bounds(X, Y, [C_R1], p=2, prob=prob)
print(c_clas, c_alc, mej)
# Esperado: 1.0, 0.4444, 55.56

4) Ejemplos reproducibles

4.1 Cuadrados mod 9

Script: EJEMPLOS/cuadrados_mod9.py
Calcula la cota clásica vs AlcyoneRD y genera el gráfico figures/comparativa.png.

Resultados esperados
	•	Caso A (X uniforme, Y filtrado): Clásico = 0.6667, AlcyoneRD = 0.4444, Mejora ≈ 33.3 %
	•	Caso B (X e Y uniformes): Clásico = 1.0000, AlcyoneRD = 0.4444, Mejora ≈ 55.6 %

4.2 Gaussiana (modelo π)

Script: EJEMPLOS/gaussian_pi.py
Media gaussiana sobre ([-n,n]) con dos clases (C y R1). Y se anula en R1 (cancelación de modos).
Clásico ≈ 0.707   AlcyoneRD ≈ 0.500   → Mejora ≈ 29–30 %

5) ¿Por qué mejora?

Si hay (q) clases totales y solo (m) activas (peso uniforme) y tomamos (p=q=2):
[
\text{Clásico}=1,\qquad
\text{AlcyoneRD}=\frac{m}{q},\qquad
\text{Mejora}=\frac{q-m}{q}\times 100%.
]
Ej.: (q=9, m=4 \Rightarrow \text{Mejora}=5/9=55.56%).

⸻

6) Estructura del repositorio
H-lder-AlcyoneRD9/
├── README.md
├── LICENCIA
├── src/
│   └── alcyoneRD.py            # compare_bounds, cota clásica y cota AlcyoneRD
├── EJEMPLOS/
│   ├── cuadrados_mod9.py       # mod 9 (33% y 56% de mejora)
│   └── gaussian_pi.py          # modelo gaussiano (~30% de mejora)
├── tests/
│   └── test_basic.py           # test del caso B (55.6%)
└── figures/
    └── comparativa.png         # se genera al ejecutar ejemplos


⸻

7) Tests

Si tienes pytest:
pip install pytest
pytest
tests/test_basic.py comprueba que el caso B mejora ≈ 55.6 %.

⸻

8) Licencia

Este proyecto está bajo la MIT License (ver LICENCIA).

⸻

9) Cita / referencia

Si usas esta idea o el código, por favor referencia:

Hölder–AlcyoneRD9: a modular refinement of Hölder’s inequality (2024).
Repo: https://github.com/tu-usuario/H-Ider-AlcyoneRD9

⸻

10) Roadmap breve
	•	Añadir ejemplo con mod 27 (cuando sea barato en la rueda).
	•	Notebook con canales de primos (A/B/C) y visualización.
	•	GitHub Actions (CI) para tests automáticos.
	•	Página (GitHub Pages) con el mini–paper y gráficos.

⸻

Contacto

¿Sugerencias o PRs? ¡Bienvenidos! 💡 Abre un issue o un pull request.

⸻

Notas finales
	•	AlcyoneRD nunca es peor que Hölder clásico; es igual sin estructura y estrictamente mejor con ella.
	•	Las mejoras reales en los ejemplos del repo coinciden con la teoría (33–56 %).
---
## Documentos completos

📄 Texto formal (PDF):
- [Español](docs/alcyoneRD9.pdf)
- [English](docs/alcyoneRD9_VE.pdf)


