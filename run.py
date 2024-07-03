import sys
import ui.ui as ui
import terminal.menu as menu
import terminal.usuario as usuario

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        if usuario.valida_usuario():
            menu.iniciar()
    else:
        app = ui.MainWindow()
        app.mainloop()
