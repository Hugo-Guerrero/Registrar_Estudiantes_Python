# Registrar Estudiantes API

API REST construida con **Flask** y **Supabase** para registrar y consultar estudiantes.  
Este proyecto sirve como ejemplo académico y práctico de integración entre Python y Supabase.

---

## 🚀 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/Hugo-Guerrero/Registrar_Estudiantes_Python.git
cd Registrar_Estudiantes_Python
```

2. Crea y activa un entorno virtual:

```bash
python -m venv mi_ambiente
mi_ambiente\Scripts\activate
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuración del entorno

El archivo `.env` **no se incluye en el repositorio** por seguridad.  
Debes crearlo en la raíz del proyecto a partir de `example.env`:

```env
SUPABASE_URL=https://TU_PROYECTO.supabase.co
SUPABASE_KEY=sb_secret_xxxxxxxxxxxxxxxxxxxxx
```

⚠️ Usa tu **secret key** o **service_role key** de Supabase.  
El archivo `.env` está en `.gitignore` para proteger tus credenciales.

---

## ▶️ Uso

Ejecuta la API con:

```bash
python app.py
```

La API estará disponible en:

```
http://127.0.0.1:5000
```

---

# 📌 Endpoints

## POST /estudiantes
Agrega un nuevo estudiante.

### Ejemplo de cuerpo JSON

```json
{
  "nombre": "Ana Pérez",
  "carrera": "Ingeniería en TI",
  "semestre": 3
}
```

### Respuesta

```json
{
  "mensaje": "Estudiante agregado exitosamente"
}
```

### 📷 Prueba del endpoint POST en Postman

![POST Estudiantes](img/Captura%20de%20pantalla%202026-03-11%20151915.png)

---

## GET /estudiantes
Obtiene todos los estudiantes registrados.

### Respuesta

```json
[
  {
    "id": 1,
    "nombre": "Ana Pérez",
    "carrera": "Ingeniería en TI",
    "semestre": 3
  }
]
```

### 📷 Prueba del endpoint GET en Postman

![GET Estudiantes](img/Captura%20de%20pantalla%202026-03-11%20151926.png)

---

# 🧪 Pruebas rápidas

## Con Postman

- **POST** → `http://127.0.0.1:5000/estudiantes`
- **GET** → `http://127.0.0.1:5000/estudiantes`

## Con curl

```bash
curl -X POST http://127.0.0.1:5000/estudiantes \
-H "Content-Type: application/json" \
-d "{\"nombre\":\"Juan López\",\"carrera\":\"Sistemas\",\"semestre\":5}"

curl http://127.0.0.1:5000/estudiantes
```

---

# 📂 Estructura del proyecto

```
Registrar_Estudiantes_Python/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── example.env
│
└── img/
    ├── Captura de pantalla 2026-03-11 151915.png
    └── Captura de pantalla 2026-03-11 151926.png
```

---

# ✨ Notas finales

- Este proyecto es académico y no debe usarse en producción sin ajustes de seguridad.
- Mantén tus claves fuera del repositorio.
- Puedes extender la API agregando más endpoints como:
  - **PUT /estudiantes** (actualizar)
  - **DELETE /estudiantes** (eliminar)

---

# 👨‍💻 Autor

Proyecto desarrollado por **Hugo Guerrero** como práctica de desarrollo de **APIs con Flask y Supabase**.
