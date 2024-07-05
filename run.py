import sys
import ui.ui as ui
import terminal.menu as menu
import terminal.usuario as term_usuario
import db.modelos.usuario_mod as class_usu

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        usu = term_usuario.valida_usuario()

        if isinstance(usu, class_usu.Usuario):
            menu.iniciar(usu)
    else:
        app = ui.MainWindow()
        app.mainloop()
