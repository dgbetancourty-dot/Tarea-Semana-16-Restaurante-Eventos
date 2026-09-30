from datetime import datetime

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class RestauranteServicio:
    def __init__(
        self,
        productos_datos,
        usuarios_datos,
        ventas_datos,
        archivo_servicio
    ):
        self.productos = []
        self.usuarios = []
        self.ventas = []
        self.archivo_servicio = archivo_servicio

        self.cargar_productos(productos_datos)
        self.cargar_usuarios(usuarios_datos)
        self.cargar_ventas(ventas_datos)

    # ---------------------------------------------------------
    # CARGA DE DATOS
    # ---------------------------------------------------------

    def cargar_productos(self, productos_datos):
        for dato in productos_datos:
            producto = Producto(
                dato["codigo"],
                dato["nombre"],
                dato["precio"],
                dato["categoria"],
                dato["stock"]
            )

            self.productos.append(producto)

    def cargar_usuarios(self, usuarios_datos):
        for dato in usuarios_datos:
            usuario = Usuario(
                dato["identificacion"],
                dato["nombre"],
                dato["correo"],
                dato["usuario"],
                dato["rol"]
            )

            self.usuarios.append(usuario)

    def cargar_ventas(self, ventas_datos):
        for dato in ventas_datos:
            venta = Venta(
                dato["usuario"],
                dato["producto"],
                dato["fecha"]
            )

            self.ventas.append(venta)

    # ---------------------------------------------------------
    # ACCESO
    # ---------------------------------------------------------

    def validar_acceso(self, usuario, contrasena):
        for usuario_registrado in self.usuarios:
            if (
                usuario_registrado.usuario.lower()
                == usuario.strip().lower()
                and contrasena == "1234"
            ):
                return usuario_registrado

        return None

    # ---------------------------------------------------------
    # LISTADOS
    # ---------------------------------------------------------

    def listar_productos(self):
        return self.productos

    def listar_usuarios(self):
        return self.usuarios

    def listar_ventas(self):
        return self.ventas

    # ---------------------------------------------------------
    # BÚSQUEDAS
    # ---------------------------------------------------------

    def buscar_producto(self, codigo):
        codigo_buscado = codigo.strip().lower()

        for producto in self.productos:
            if producto.codigo.lower() == codigo_buscado:
                return producto

        return None

    def buscar_usuario(self, identificacion):
        identificacion_buscada = identificacion.strip()

        for usuario in self.usuarios:
            if (
                usuario.identificacion
                == identificacion_buscada
            ):
                return usuario

        return None

    def buscar_usuario_por_nombre_usuario(
        self,
        nombre_usuario
    ):
        nombre_buscado = (
            nombre_usuario.strip().lower()
        )

        for usuario in self.usuarios:
            if usuario.usuario.lower() == nombre_buscado:
                return usuario

        return None

    # ---------------------------------------------------------
    # PRODUCTOS
    # ---------------------------------------------------------

    def registrar_producto(
        self,
        codigo,
        nombre,
        precio,
        categoria,
        stock
    ):
        if self.buscar_producto(codigo) is not None:
            raise ValueError(
                "Ya existe un producto con ese código."
            )

        try:
            precio_convertido = float(precio)
        except ValueError:
            raise ValueError(
                "El precio debe ser un número válido."
            )

        try:
            stock_convertido = int(stock)
        except ValueError:
            raise ValueError(
                "El stock debe ser un número entero."
            )

        producto = Producto(
            codigo,
            nombre,
            precio_convertido,
            categoria,
            stock_convertido
        )

        self.productos.append(producto)
        self.guardar_productos()

        return producto

    def actualizar_producto(
        self,
        codigo,
        nombre,
        precio,
        categoria,
        stock
    ):
        producto_encontrado = (
            self.buscar_producto(codigo)
        )

        if producto_encontrado is None:
            raise ValueError(
                "No existe un producto con ese código."
            )

        try:
            precio_convertido = float(precio)
        except ValueError:
            raise ValueError(
                "El precio debe ser un número válido."
            )

        try:
            stock_convertido = int(stock)
        except ValueError:
            raise ValueError(
                "El stock debe ser un número entero."
            )

        producto_actualizado = Producto(
            producto_encontrado.codigo,
            nombre,
            precio_convertido,
            categoria,
            stock_convertido
        )

        posicion = self.productos.index(
            producto_encontrado
        )

        self.productos[posicion] = producto_actualizado
        self.guardar_productos()

        return producto_actualizado

    def eliminar_producto(self, codigo):
        producto = self.buscar_producto(codigo)

        if producto is None:
            raise ValueError(
                "No existe un producto con ese código."
            )

        self.productos.remove(producto)
        self.guardar_productos()

    def guardar_productos(self):
        self.archivo_servicio.guardar_productos(
            self.productos
        )

    # ---------------------------------------------------------
    # USUARIOS - SEMANA 16
    # ---------------------------------------------------------

    def registrar_usuario(
        self,
        identificacion,
        nombre,
        correo,
        nombre_usuario,
        rol
    ):
        identificacion = identificacion.strip()
        nombre_usuario = nombre_usuario.strip()

        if self.buscar_usuario(identificacion) is not None:
            raise ValueError(
                "Ya existe un usuario con esa identificación."
            )

        if (
            self.buscar_usuario_por_nombre_usuario(
                nombre_usuario
            )
            is not None
        ):
            raise ValueError(
                "El nombre de usuario ya está registrado."
            )

        usuario = Usuario(
            identificacion,
            nombre,
            correo,
            nombre_usuario,
            rol
        )

        self.usuarios.append(usuario)
        self.guardar_usuarios()

        return usuario

    def actualizar_usuario(
        self,
        identificacion,
        nombre,
        correo,
        nombre_usuario,
        rol
    ):
        usuario_encontrado = (
            self.buscar_usuario(identificacion)
        )

        if usuario_encontrado is None:
            raise ValueError(
                "No existe un usuario con esa identificación."
            )

        usuario_mismo_nombre = (
            self.buscar_usuario_por_nombre_usuario(
                nombre_usuario
            )
        )

        if (
            usuario_mismo_nombre is not None
            and usuario_mismo_nombre.identificacion
            != usuario_encontrado.identificacion
        ):
            raise ValueError(
                "El nombre de usuario ya está registrado."
            )

        usuario_actualizado = Usuario(
            usuario_encontrado.identificacion,
            nombre,
            correo,
            nombre_usuario,
            rol
        )

        posicion = self.usuarios.index(
            usuario_encontrado
        )

        self.usuarios[posicion] = usuario_actualizado
        self.guardar_usuarios()

        return usuario_actualizado

    def eliminar_usuario(
        self,
        identificacion,
        identificacion_autenticada=None
    ):
        usuario = self.buscar_usuario(
            identificacion
        )

        if usuario is None:
            raise ValueError(
                "No existe un usuario con esa identificación."
            )

        if (
            identificacion_autenticada is not None
            and usuario.identificacion
            == identificacion_autenticada
        ):
            raise ValueError(
                "No puede eliminar la cuenta "
                "administrativa actualmente autenticada."
            )

        self.usuarios.remove(usuario)
        self.guardar_usuarios()

    def guardar_usuarios(self):
        self.archivo_servicio.guardar_usuarios(
            self.usuarios
        )

    # ---------------------------------------------------------
    # VENTAS
    # ---------------------------------------------------------

    def registrar_venta(
        self,
        identificacion_usuario,
        codigo_producto
    ):
        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        if usuario is None:
            raise ValueError(
                "El usuario seleccionado no existe."
            )

        producto = self.buscar_producto(
            codigo_producto
        )

        if producto is None:
            raise ValueError(
                "El producto seleccionado no existe."
            )

        fecha = datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )

        venta = Venta(
            usuario.nombre,
            producto.nombre,
            fecha
        )

        self.ventas.append(venta)
        self.guardar_ventas()

        return venta

    def guardar_ventas(self):
        self.archivo_servicio.guardar_ventas(
            self.ventas
        )

    # ---------------------------------------------------------
    # CONTADORES
    # ---------------------------------------------------------

    def cantidad_productos(self):
        return len(self.productos)

    def cantidad_usuarios(self):
        return len(self.usuarios)