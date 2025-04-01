# Cars API

API REST para gestión de vehículos y marcas, construida con Flask y MongoDB.

## 🚀 Estructura del Proyecto

```
cars_api/
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
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
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
- `GET /api/v1/get_cars` - Listar vehículos (paginable)
- `GET /api/v1/get_cars/car_details` - Búsqueda avanzada
- `POST /api/v1/create_car` - Crear nuevo vehículo

### Marcas
- `GET /api/v1/get_brands` - Listar marcas
- `POST /api/v1/create_brand` - Crear nueva marca

## 🔧 Uso con Postman

### Ejemplo GET (Listar vehículos)
```
GET http://localhost:8020/api/v1/get_cars?page=1&limit=5
```

### Ejemplo POST (Crear marca):
```json
{
    "name": "Toyota"
}
```

## 🐧 Uso con cURL

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

### Dependencias faltantes
```bash
pip freeze > requirements.txt  # Regenerar si es necesario
pip install -r requirements.txt --force-reinstall
```

### Puerto en uso
```bash
# Linux/Mac
sudo lsof -i :8020
kill -9 <PID>

# Windows
netstat -ano | findstr :8020
taskkill /PID <PID> /F
```

## 📄 Notas Adicionales
- Los datos se almacenan en formato UUID
- CORS habilitado para todos los dominios
- Logs de acceso en consola para `/api/v1/get_cars`


