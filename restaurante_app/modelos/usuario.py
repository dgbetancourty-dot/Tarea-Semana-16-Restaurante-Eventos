class Usuario:
    ROLES_VALIDOS = (
        "Administrador",
        "Empleado",
        "Cliente"
    )

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str,
        usuario: str,
        rol: str
    ) -> None:

        if not identificacion.strip():
            raise ValueError(
                "La identificación no puede estar vacía."
            )

        if not nombre.strip():
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        if not correo.strip():
            raise ValueError(
                "El correo no puede estar vacío."
            )

        if "@" not in correo:
            raise ValueError(
                "El correo electrónico no es válido."
            )

        if not usuario.strip():
            raise ValueError(
                "El usuario no puede estar vacío."
            )

        if rol not in self.ROLES_VALIDOS:
            raise ValueError(
                "El rol seleccionado no es válido."
            )

        self._identificacion = identificacion.strip()
        self._nombre = nombre.strip()
        self._correo = correo.strip()
        self._usuario = usuario.strip()
        self._rol = rol

    @property
    def identificacion(self) -> str:
        return self._identificacion

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def correo(self) -> str:
        return self._correo

    @property
    def usuario(self) -> str:
        return self._usuario

    @property
    def rol(self) -> str:
        return self._rol

    def a_diccionario(self) -> dict:
        return {
            "identificacion": self._identificacion,
            "nombre": self._nombre,
            "correo": self._correo,
            "usuario": self._usuario,
            "rol": self._rol
        }

    def mostrar_informacion(self) -> None:
        print(
            f"Identificación: {self._identificacion}"
        )
        print(f"Nombre: {self._nombre}")
        print(f"Correo: {self._correo}")
        print(f"Usuario: {self._usuario}")
        print(f"Rol: {self._rol}")