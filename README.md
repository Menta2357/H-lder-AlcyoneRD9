# Hölder-AlcyoneRD9
Refinamiento modular de la desigualdad de Hölder que apaga clases inactivas y logra mejoras del 25–55% en escenarios con estructura (como residuos cuadráticos mod 9 o sumas gaussianas).

## Uso como librería

```python
from src.alcyoneRD import compare_bounds
import numpy as np

N=9; prob=np.ones(N)/N
X=Y=np.ones(N)
C_R1=[0,1,4,7]

c_clas, c_alc, mej = compare_bounds(X,Y,[C_R1],p=2,prob=prob)
print(c_clas, c_alc, mej)  
# Esperado: 1.0, 0.4444, 55.56%
