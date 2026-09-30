import tkinter as tk
from tkinter import messagebox


class LoginView:
    def __init__(
        self,
        contenedor,
        restaurante_servicio,
        mostrar_main
    ):
        self.contenedor = contenedor
        self.restaurante_servicio = restaurante_servicio
        self.mostrar_main = mostrar_main

        self.frame = tk.Frame(self.contenedor)
        self.frame.pack(fill="both", expand=True)

        titulo = tk.Label(
            self.frame,
            text="ACCESO AL RESTAURANTE",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=30)

        tk.Label(
            self.frame,
            text="Usuario:"
        ).pack()

        self.entrada_usuario = tk.Entry(
            self.frame,
            width=30
        )
        self.entrada_usuario.pack(pady=8)

        tk.Label(
            self.frame,
            text="Contraseña:"
        ).pack()

        self.entrada_contrasena = tk.Entry(
            self.frame,
            width=30,
            show="*"
        )
        self.entrada_contrasena.pack(pady=8)

        boton_ingresar = tk.Button(
            self.frame,
            text="Ingresar",
            width=20,
            command=self.validar_acceso
        )
        boton_ingresar.pack(pady=20)

    def validar_acceso(self):
        usuario = self.entrada_usuario.get().strip()
        contrasena = self.entrada_contrasena.get().strip()

        if not usuario or not contrasena:
            messagebox.showwarning(
                "Aviso",
                "Complete usuario y contraseña."
            )
            return

        usuario_autenticado = (
            self.restaurante_servicio.validar_acceso(
                usuario,
                contrasena
            )
        )

        if usuario_autenticado is not None:
            messagebox.showinfo(
                "Acceso",
                "Ingreso correcto."
            )

            self.mostrar_main(
                usuario_autenticado
            )

        else:
            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos."
            )

    def destruir(self):
        self.frame.destroy()