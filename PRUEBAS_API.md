# Documento de Pruebas para API REST de Videos

### Nombre del Endpoint: GET
(Obtener la lista de videos de la base de datos.)

- **Método HTTP:** GET
- **Ruta:** `/api/videos`
- **Descripción:** Devuelve la lista de los videos registrados en el servidor.

#### Ejemplo de Petición
```sh
GET "http://localhost:5000/api/videos"
```
#### Ejemplo de Peticion cambio de pagina
```sh
GET "http://localhost:5000/api/videos?page=2&per_page=2
```
- **page=2:** Indica que quieres la segunda pagina
- **per_page=10:** Indica que quieres 10 videos por pagina

#### Respuesta Esperada
```sh
{
  "total": 1,
  "page": 1,
  "per_page": 10 
  "videos": [
    {
      "id": 1,
      "name": "Video de ejemplo",
      "views": 100,
      "likes": 10
    }
     {
      "id": 2,
      "name": "Video de ejemplo",
      "views": 100,
      "likes": 10
    }
     {
      "id": 3,
      "name": "Video de ejemplo",
      "views": 100,
      "likes": 10
    }
     {
      "id": 4,
      "name": "Video de ejemplo",
      "views": 100,
      "likes": 10
    }
  ],
}
```
- **Respuesta Esperada:** OK
- **Observaciones:** La respuesta contiene los datos esperados.


### Nombre del Endpoint: PUT
(Crear un nuevo video.)

- **Método HTTP:** PUT
- **Ruta:** `/api/videos/30`
- **Descripción:** Crear un nuevo video con un ID especificado.

#### Ejemplo de Petición
```sh
PUT "http://localhost:5000/api/videos/30"
```
#### Cuerpo de la peticion
```sh
{
  "likes": 200,
  "name": "Prueba",
  "views": 2500
}
```
#### Respuesta Esperada
```sh
{
  "id" 30
  "likes": 200,
  "name": "Prueba",
  "views": 2500
}
```

- **Respuesta Esperada:** OK
- **Observaciones:** El video fue creado correctamente.

### Nombre del Endpoint: PATCH
(Actualizar un videos existente.)

- **Método HTTP:** PATCH
- **Ruta:** `/api/videos/30`
- **Descripción:** Actualiza los datos de un video existente.

#### Ejemplo de Petición
```sh
PATCH "http://localhost:5000/api/videos/30"
```

#### Cuerpo de la peticion
```sh
{
  "likes": 250,
  "name": "Prueba",
  "views": 2600
}
```
#### Respuesta Esperada
```sh
{
"id": 30,
"name": "Prueba",
"views": 2600,
"likes": 250
}
```

- **Respuesta Esperada:** OK
- **Observaciones:** El video es actualizado correctamente.

### Nombre del Endpoint: DELETE
(Eliminar un video existente.)

- **Método HTTP:** DELETE
- **Ruta:** `/api/videos/30`
- **Descripción:** Elimina el video con el ID especificado.
#### Ejemplo de Petición
```sh
DELETE "http://localhost:5000/api/videos/30"
```

#### Respuesta Esperada
```sh
  1
```
- **Cuerpo de la Respuesta:** Vacio
- **Respuesta Esperada:** OK
- **Observaciones:** El video fue eliminado correctamente.