# Tarea Semana 16 - Manejo de eventos en restaurante_app

## Descripción

En esta tarea de la Semana 16 continué trabajando en el Sistema de Restaurante que he venido desarrollando durante las semanas anteriores.

Para esta semana el objetivo principal fue ampliar el manejo de eventos utilizando Tkinter y aplicarlo especialmente en la gestión de usuarios. Para realizar la actividad continué trabajando sobre el mismo proyecto, conservando el inicio de sesión, la gestión de productos, la sección de ventas, la persistencia mediante archivos JSON y la organización modular de la aplicación.

La sección de Usuarios, que anteriormente permitía principalmente consultar los usuarios registrados, fue ampliada para permitir registrar, seleccionar, actualizar y eliminar usuarios. También se incorporaron los roles Administrador, Empleado y Cliente.

No realicé un proyecto nuevo desde cero. Continué evolucionando la aplicación desarrollada anteriormente y mantuve las funcionalidades que ya se encontraban operativas.

## Evolución del proyecto

En la versión anterior del sistema ya tenía implementado el inicio de sesión, la gestión de productos, la consulta de usuarios y la sección de ventas.

Para la Semana 16 continué trabajando sobre esta base y amplié principalmente la gestión de usuarios.

Los principales cambios realizados fueron:

- Incorporación del atributo `rol` en el modelo Usuario.
- Incorporación de un nombre de usuario para el acceso.
- Implementación de los roles Administrador, Empleado y Cliente.
- Registro de nuevos usuarios.
- Actualización de usuarios existentes.
- Eliminación de usuarios con confirmación.
- Uso de un Treeview para visualizar los usuarios registrados.
- Selección de usuarios directamente desde el Treeview.
- Uso de un Combobox para seleccionar el rol.
- Uso de `<<TreeviewSelect>>`.
- Uso de `<<ComboboxSelected>>`.
- Uso de la tecla Enter mediante `<Return>`.
- Uso de la tecla Escape mediante `<Escape>`.
- Uso de `command=` en los botones.
- Persistencia de los usuarios mediante `usuarios.json`.
- Restricción de la gestión de usuarios al rol Administrador.
- Protección para evitar que el administrador autenticado elimine accidentalmente su propia cuenta.

Las funcionalidades anteriores de Productos y Ventas se conservaron durante esta evolución del proyecto.

## Estructura del proyecto

El proyecto mantiene una estructura modular para separar las diferentes responsabilidades del sistema.

```text
restaurante_app/
│
├── assets/
│   ├── logo.png
│   ├── logo_app.png
│   ├── productos.png
│   ├── productos_icon.png
│   ├── usuarios.png
│   ├── usuarios_icon.png
│   ├── ventas.png
│   └── ventas_icon.png
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
└── main.py
```

La carpeta `datos` contiene los archivos JSON utilizados para guardar la información del sistema.

En `modelos` se encuentran las clases principales: Producto, Usuario y Venta.

En `servicios` se encuentra la lógica utilizada para realizar las operaciones y trabajar con los datos.

En `ui` se encuentran las vistas y los componentes gráficos desarrollados con Tkinter.

La carpeta `assets` contiene el logo y los íconos utilizados en la interfaz.

Finalmente, `main.py` es el punto de entrada utilizado para iniciar la aplicación.

## Gestión de usuarios

Para esta semana amplié la sección de Usuarios para permitir una gestión más completa.

Cada usuario contiene:

- Identificación.
- Nombre.
- Correo.
- Usuario.
- Rol.

Desde la interfaz se pueden realizar las siguientes operaciones:

- Registrar.
- Seleccionar.
- Actualizar.
- Eliminar.
- Limpiar el formulario.

Los usuarios registrados se muestran en un Treeview con información como identificación, nombre, usuario y rol.

Cuando se selecciona una fila del Treeview, la aplicación obtiene la identificación del usuario y utiliza `RestauranteServicio` para recuperar el objeto correspondiente. Después los datos se cargan en el formulario para poder actualizarlos o eliminarlos.

La interfaz no realiza directamente las operaciones sobre `usuarios.json`. Estas acciones se delegan a los servicios del sistema.

## Roles de usuario

Para esta actividad incorporé tres roles:

- Administrador.
- Empleado.
- Cliente.

El usuario con rol Administrador puede acceder a la sección de gestión de usuarios.

Los usuarios con rol Empleado o Cliente pueden ingresar al sistema, pero no tienen disponible la misma gestión administrativa de usuarios.

También se agregó una validación para evitar que el administrador que se encuentra autenticado pueda eliminar accidentalmente su propia cuenta.

Esta validación se realiza desde la lógica del servicio antes de eliminar el usuario.

## Manejo de eventos

En esta actividad utilicé diferentes eventos de Tkinter para responder a las acciones realizadas en la interfaz.

### Evento TreeviewSelect

En la tabla de usuarios se utiliza:

```text
<<TreeviewSelect>>
```

Este evento se ejecuta cuando se selecciona una fila del Treeview.

Al seleccionar un usuario se obtiene su identificación y se utiliza `RestauranteServicio` para buscar el objeto Usuario correspondiente.

Después sus datos se cargan en el formulario.

De esta forma puedo seleccionar un usuario directamente desde la tabla y preparar sus datos para actualizarlo o eliminarlo.

### Evento ComboboxSelected

Para seleccionar el rol se utiliza un Combobox con el evento:

```text
<<ComboboxSelected>>
```

Este evento permite detectar cuando se selecciona un rol.

Los roles disponibles son:

```text
Administrador
Empleado
Cliente
```

Al cambiar el rol, la interfaz muestra el rol que fue seleccionado.

### Evento Return

También se utiliza:

```text
<Return>
```

Este evento permite utilizar la tecla Enter para registrar un usuario.

El evento llama al mismo método utilizado por el botón Registrar, evitando duplicar la lógica de la operación.

### Evento Escape

Se utiliza:

```text
<Escape>
```

Al presionar la tecla Escape se limpia el formulario de usuarios y se cancela la selección actual.

Esto permite utilizar el teclado como una forma adicional de interacción con la aplicación.

## Uso de command y bind

Durante esta actividad utilicé tanto `command=` como `bind()`.

`command=` se utiliza principalmente en los botones de la interfaz.

Por ejemplo:

```python
command=self.registrar_usuario
```

De esta manera, cuando se presiona el botón Registrar se ejecuta directamente el método correspondiente.

También se utiliza `command=` en botones como:

- Registrar.
- Actualizar.
- Eliminar.
- Limpiar.
- Registrar venta.
- Cerrar sesión.

Por otra parte, `bind()` permite asociar un evento específico con un callback.

En esta actividad se utiliza para:

```text
<<TreeviewSelect>>
<<ComboboxSelected>>
<Return>
<Escape>
```

Los callbacks reciben el evento generado en la interfaz y después llaman a los métodos correspondientes.

Un ejemplo del flujo utilizado es:

```text
Usuario realiza una acción
        ↓
Se genera un evento
        ↓
bind() o command=
        ↓
Callback
        ↓
Método de la aplicación
        ↓
RestauranteServicio
        ↓
Persistencia
        ↓
Actualización de la interfaz
```

De esta manera la interfaz se encarga principalmente de recibir las acciones del usuario, mientras que la lógica de las operaciones se mantiene en el servicio.

## Persistencia de usuarios

Los usuarios se almacenan en:

```text
restaurante_app/datos/usuarios.json
```

En este archivo se guardan datos como:

- Identificación.
- Nombre.
- Correo.
- Usuario.
- Rol.

La interfaz gráfica no lee ni escribe directamente el archivo JSON.

La lectura y escritura se realiza mediante `ArchivoServicio`, mientras que las operaciones de registro, búsqueda, actualización y eliminación se manejan desde `RestauranteServicio`.

Después de registrar o modificar un usuario, los cambios quedan almacenados en `usuarios.json`.

Al cerrar completamente el programa y volver a ejecutarlo, los usuarios guardados se cargan nuevamente.

## Gestión de productos y ventas

Las funcionalidades desarrolladas anteriormente se mantuvieron operativas.

La sección de Productos continúa permitiendo registrar, cargar, actualizar y eliminar productos.

La sección de Ventas permite seleccionar un usuario y un producto registrados para generar una venta.

Al presionar el botón **Registrar venta**, se utiliza `command=` para ejecutar el callback correspondiente.

Las ventas continúan almacenándose en:

```text
restaurante_app/datos/ventas.json
```

De esta manera la incorporación de los nuevos eventos y la gestión de usuarios no eliminó las funcionalidades que ya se habían desarrollado.

## Interfaz gráfica

La aplicación utiliza Tkinter y ttk para construir la interfaz gráfica.

Actualmente se mantienen las secciones:

- Productos.
- Usuarios.
- Ventas.

También se mantiene la carpeta `assets`, donde se encuentran los recursos visuales utilizados por la aplicación:

- Logo del Sistema de Restaurante.
- Ícono de Productos.
- Ícono de Usuarios.
- Ícono de Ventas.

En la parte superior de la aplicación se muestra el nombre del usuario autenticado y su rol.

Por ejemplo:

```text
Dennis - Administrador
```

Esto permite identificar con qué tipo de usuario se inició sesión.

## Acceso a la aplicación

Para facilitar la revisión y prueba del proyecto por parte del docente, se pueden utilizar las siguientes credenciales:

```text
Usuario: Dennis
Contraseña: 1234
Rol: Administrador
```

Esta cuenta permite ingresar a la aplicación y acceder a:

- Productos.
- Usuarios.
- Ventas.

La cuenta de Administrador es la recomendada para revisar todas las funcionalidades desarrolladas en esta actividad, especialmente el CRUD y los eventos de la sección Usuarios.

Para esta práctica se mantiene la contraseña `1234`, debido a que el objetivo de la actividad está centrado en el manejo de eventos, callbacks, roles y gestión de usuarios.

## Ejecución del programa

Para ejecutar el proyecto se debe tener instalado Python 3.

Primero se debe abrir una terminal en la carpeta principal del repositorio:

```text
Tarea-Semana-16-Restaurante-Eventos
```

Desde esa ubicación se puede ejecutar directamente:

```powershell
python restaurante_app/main.py
```

Al ejecutar `main.py` se abrirá la pantalla de acceso del Sistema de Restaurante.

Para realizar una revisión completa se recomienda utilizar:

```text
Usuario: Dennis
Contraseña: 1234
```

Después del inicio de sesión se podrá navegar por las secciones disponibles de acuerdo con el rol del usuario.

## Pruebas realizadas

Para comprobar el funcionamiento del proyecto realicé diferentes pruebas.

Se verificó:

- Ejecución correcta de `main.py`.
- Inicio de sesión con la cuenta Administrador.
- Navegación entre Productos, Usuarios y Ventas.
- Funcionamiento de las opciones anteriores de Productos.
- Funcionamiento de la sección de Ventas.
- Registro de un nuevo usuario.
- Visualización inmediata del usuario en el Treeview.
- Selección de un usuario mediante `<<TreeviewSelect>>`.
- Carga automática de los datos seleccionados en el formulario.
- Actualización de un usuario.
- Selección de roles mediante el Combobox.
- Respuesta del evento `<<ComboboxSelected>>`.
- Registro mediante la tecla Enter.
- Limpieza del formulario mediante la tecla Escape.
- Eliminación de usuarios con confirmación.
- Validación para evitar que el administrador autenticado elimine su propia cuenta.
- Inicio de sesión con un usuario de rol Empleado.
- Comprobación de que el Empleado no tiene disponible la sección administrativa de Usuarios.
- Cierre completo de la aplicación.
- Nueva ejecución de la aplicación.
- Comprobación de que los usuarios registrados y actualizados permanecen almacenados en `usuarios.json`.
- Visualización correcta del logo y los íconos almacenados en `assets`.

Estas pruebas me permitieron comprobar que los eventos incorporados funcionan correctamente y que las funciones desarrolladas anteriormente continúan operativas.

## Conclusión

Con esta actividad pude comprender de una manera más práctica cómo se pueden manejar diferentes eventos dentro de una interfaz gráfica desarrollada con Tkinter.

Durante la Semana 16 amplié la gestión de usuarios utilizando eventos como `<<TreeviewSelect>>`, `<<ComboboxSelected>>`, `<Return>` y `<Escape>`. También continué utilizando `command=` en los botones para ejecutar los métodos correspondientes.

La incorporación de roles me permitió diferenciar el acceso a la gestión de usuarios entre un Administrador y los demás tipos de usuario.

Finalmente, pude mantener la información almacenada mediante archivos JSON y conservar la separación entre la interfaz, la lógica del sistema y la persistencia de datos.

Esta práctica me ayudó a comprender mejor cómo los eventos y callbacks permiten que una aplicación gráfica responda a las acciones realizadas por el usuario sin colocar toda la lógica directamente dentro de la interfaz.