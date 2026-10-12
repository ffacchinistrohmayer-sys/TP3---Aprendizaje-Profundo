# TP3 - Aprendizaje Profundo (Co26) - Clasificador de emociones

**Universidad de Buenos Aires - Aprendizaje Profundo, Cohorte 26, 4to bimestre 2026**
Grupo: Victoria Baiardo, Yonatan Aguirre, Francisco Facchini

CNN en PyTorch, entrenada desde cero, que clasifica 7 emociones faciales
(alegría, disgusto, enojo, miedo, seriedad, sorpresa, tristeza).

## Contenido
- `Baiardo-Aguirre-Facchini-TP3-Co26-CV.ipynb`: notebook completo, con todas las salidas guardadas.
- `entorno/`: instalación del entorno local (VS Code / Jupyter) en Mac.
- `datos/LEEME.md`: cómo obtener los datos (no se incluyen en el repo).

## Resultados principales (validación)
- Accuracy 82,0 % y F1 macro 0,744 (mejor época: 79 de 80).
- Imágenes nuevas: 17,6 % sin recorte y 58,8 % con detección y recorte de rostro (17 imágenes).

## Cómo correrlo
**Local:** seguir `entorno/LEEME.md` y colocar los datos como indica `datos/LEEME.md`.
**Colab:** subir el notebook; descarga el dataset con `gdown` y pide subir las imágenes nuevas.

## Entrega
Solo por el Google Forms de la cátedra (link a un notebook de Colab compartido con
gvilcamiza.ext@fi.uba.ar con comentarios habilitados). Fecha límite: miércoles 21/10, 23:59 (Argentina).
