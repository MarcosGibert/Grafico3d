# Generador · Gráfico 3D Incidencias

Frontend estático (GitHub Pages) + backend Flask (Render) para generar gráficos 3D
de incidencias de flota a partir de un archivo `.xlsx`.

---

## Estructura del repositorio

```
/
├── frontend/
│   └── index.html          ← GitHub Pages sirve esto
└── backend/
    ├── app.py              ← Flask API
    ├── template.html       ← Template HTML del gráfico (inyección de payload)
    └── requirements.txt
```

---

## Despliegue del backend en Render

1. Entra en [render.com](https://render.com) y crea un **New Web Service**.
2. Conecta el repositorio de GitHub.
3. Configura:
   - **Root Directory**: `backend`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
4. En el plan **Free**, el servicio se duerme tras 15 min de inactividad.
   El primer request tras el sueño puede tardar ~30-60 s (cold start).
   Usa el botón **"Activar"** del frontend para despertarlo antes de subir el archivo.

---

## Despliegue del frontend en GitHub Pages

1. Ve a **Settings → Pages** del repositorio.
2. Source: **Deploy from a branch** → `main` → carpeta `/frontend`.
3. GitHub Pages servirá `frontend/index.html` como página principal.
4. Una vez desplegado el backend, **edita el campo URL en la interfaz** con la URL
   de tu servicio Render (p. ej. `https://mi-app.onrender.com`).

---

## Formato del archivo .xlsx

El archivo debe contener una hoja llamada **`Unidad_Subsistema_Mes`** con las
siguientes columnas (exactamente con estos nombres):

| Columna | Descripción |
|---|---|
| `Unidad` | Identificador de unidad/locomotora |
| `Mes` | Mes en formato `YYYY-MM` o similar |
| `Organo` | Nivel 1 de la jerarquía |
| `Elemento` | Nivel 2 de la jerarquía |
| `Subsistema` | Nivel 3 de la jerarquía |
| `Incidencias unidad-subsistema por mes` | Número de incidencias |
| `Incidencias P4 (reincidencias mantenimiento)` | Incidencias clasificadas P4 |

---

## Variables configurables en `backend/app.py`

```python
UMBRAL         = 3       # mínimo de incidencias para recibir color propio
HW             = 0.32    # semi-anchura de cada barra 3D
P4_COLOR       = "#E84620"
ORDEN_APILADO  = "desc"  # "asc" | "desc"
```
