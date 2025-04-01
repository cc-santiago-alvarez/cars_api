# Cars API - Santiago Álvarez

API REST para gestión de vehículos y marcas, construida con Flask y MongoDB.

## 🚀 Estructura del Proyecto

```
cc-santiago-alvarez-cars_api/
├── app.py
├── db.py
├── requirements.txt
├── utils.py
├── controllers/
│   ├── brands.py
│   └── cars.py
└── models/
    ├── brands.py
    └── cars.py
```

## 📋 Prerrequisitos

- Python 3.8+
- pip
- Acceso a MongoDB (local o remoto)
- Postman o herramienta similar (para pruebas API)

## ⚙️ Instalación

1. Clonar repositorio
2. Crear entorno virtual:
   
   # Windows
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
   # Linux/Mac
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   si no funciona intentar con:
   ```bash
   . .venv/bin/activate
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Ejecutar el Servidor

```bash
python app.py
```
El servidor iniciará en `http://0.0.0.0:8020`

## 📡 Endpoints de la API

### Vehículos
- `GET /api/v1/get_cars` - Listar vehículos con filtros básicos (paginable)
- `GET /api/v1/get_cars/car_details` - Búsqueda avanzada con múltiples filtros
- `POST /api/v1/create_car` - Crear nuevo vehículo

### Marcas
- `GET /api/v1/get_brands` - Listar marcas
- `POST /api/v1/create_brand` - Crear nueva marca

## 🔧 Uso con Postman

### Filtros y Paginación (Query Parameters)
| Parámetro    | Descripción                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `brand`      | Filtrar por nombre de marca (ej: Toyota)                                    |
| `model`      | Filtrar por modelo de auto (solo en `/car_details`, ej: Corolla)            |
| `price`      | Filtrar por precio exacto (ej: 25000)                                       |
| `kilometers` | Filtrar por kilometraje exacto (ej: 15000)                                  |
| `page`       | Número de página para paginación (ej: 2)                                    |
| `limit`      | Cantidad de resultados por página (ej: 10)                                  |

**Ejemplo con múltiples filtros:**
```
GET http://localhost:8020/api/v1/get_cars/car_details?brand=Toyota&model=Corolla&page=1&limit=5
```

### Ejemplo GET (Listar vehículos paginados)
```
GET http://localhost:8020/api/v1/get_cars?page=1&limit=5&brand=Ford
```

### Ejemplo POST (Crear marca):
```json
{
    "name": "Toyota"
}
```

## 🐧 Uso con cURL

### Listar vehículos con filtros:
```bash
curl -X GET "http://localhost:8020/api/v1/get_cars/car_details?brand=Toyota&model=Corolla&price=25000&page=1&limit=5"
```

### Listar marcas:
```bash
curl -X GET "http://localhost:8020/api/v1/get_brands"
```

### Crear vehículo:
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
    "model": "Corolla",
    "price": 25000,
    "kilometers": 15000,
    "brandId": "UUID_DE_LA_MARCA"
}' \
http://localhost:8020/api/v1/create_car
```

## 🚨 Manejo de Errores

La API devuelve respuestas estandarizadas:
```json
{
    "data": null,
    "status": 400,
    "message": "Invalid fields"
}
```

Códigos comunes:
- 400: Campos inválidos
- 404: Recurso no encontrado
- 500: Error interno

## 🛠️ Solución de Problemas

### Error de conexión a MongoDB
1. Verificar cadena de conexión en `db.py`
2. Asegurar acceso a internet si usa MongoDB Atlas
3. Validar credenciales

### Filtros no funcionan
- Usar nombres exactos de parámetros (case-sensitive)
- Para búsquedas parciales usar formato: `brand=Toyo*` (autocompletado con wildcards)
- Valores numéricos sin comillas

### Dependencias faltantes
```bash
pip freeze > requirements.txt  # Regenerar si es necesario
pip install -r requirements.txt --force-reinstall
```

## 📄 Notas Adicionales
- Los filtros pueden combinarse según necesidades
- Paginación opcional: si no se envían `page` y `limit` muestra todos los resultados
- Los UUID de marcas se obtienen del endpoint `get_brands`
- CORS habilitado para todos los dominios
