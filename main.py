from Model.database import get_connection
from View.ventana_principal import VentanaPrincipal

if __name__ == "__main__":
    get_connection()
    main_view = VentanaPrincipal()
    main_view.mainloop()