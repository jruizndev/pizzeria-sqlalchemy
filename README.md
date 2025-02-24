# 🍕 Pizzeria SQL Lite con SQLAlchemy

Este es un proyecto formativo que implementa un **CRUD** (Crear, Leer, Actualizar y Eliminar) con **SQLite y SQLAlchemy** en Python.  
El objetivo es gestionar una base de datos de platos y sus ingredientes en una pizzería.

## 🛠️ Tecnologías utilizadas
- Python 3.x
- SQLite (Base de datos ligera)
- SQLAlchemy (ORM para interactuar con la BD)

---

## 🚀 Instalación

1️⃣ **Clona este repositorio**:
```bash
git clone https://github.com/tu-usuario/pizzeria_sql_lite.git
cd pizzeria_sql_lite
```

2️⃣ **Crea y activa un entorno virtual** (recomendado):
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
# En Windows usa:
# .venv\Scripts\activate
```

3️⃣ **Instala las dependencias**:
```bash
pip install sqlalchemy
```

---

## 📌 Uso del CRUD

### 1️⃣ Ejecutar el script
Para probar el CRUD, simplemente ejecuta el archivo principal:
```bash
python main.py
```

---

### 2️⃣ Funciones disponibles

| Función               | Descripción |
|----------------------|-------------|
| `crear_plato(nombre, ingredientes)` | Añade un nuevo plato con ingredientes. |
| `leer_platos()` | Lista todos los platos y sus ingredientes. |
| `actualizar_plato(id, nuevo_nombre)` | Cambia el nombre de un plato por su ID. |
| `eliminar_plato(id)` | Borra un plato y sus ingredientes asociados. |

---

## 🔥 Ejemplo de ejecución

Después de ejecutar el código, verás una salida similar a esta:

```
✅ Plato 'Pizza Margarita' creado con ingredientes: ['Tomate', 'Queso', 'Albahaca']
✅ Plato 'Spaghetti Carbonara' creado con ingredientes: ['Pasta', 'Huevo', 'Queso', 'Panceta']

📜 Listado de Platos:
🍽️ Pizza Margarita
   🥗 Tomate
   🥗 Queso
   🥗 Albahaca
🍽️ Spaghetti Carbonara
   🥗 Pasta
   🥗 Huevo
   🥗 Queso
   🥗 Panceta

✅ Plato actualizado a 'Pizza Napolitana'.

📜 Platos después de la actualización:
🍽️ Pizza Napolitana
   🥗 Tomate
   🥗 Queso
   🥗 Albahaca

❌ Plato 'Spaghetti Carbonara' eliminado.

📜 Platos después de la eliminación:
🍽️ Pizza Napolitana
   🥗 Tomate
   🥗 Queso
   🥗 Albahaca
```

