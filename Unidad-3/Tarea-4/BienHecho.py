import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Clase para almacenar reglas
class Regla:
    def __init__(self, id_regla, sintomas, diagnostico):
        self.id = id_regla
        self.sintomas = sintomas
        self.diagnostico = diagnostico

# Lista con todas las reglas
reglas = [
    Regla(1, ["motor_no_gira", "girar_llave"], "batería descargada"),
    Regla(2, ["motor_inicia", "no_arranca"], "falla en el sistema de combustible o encendido"),
    Regla(3, ["girar_llave", "sin_luces_tablero"], "batería desconectada o totalmente descargada"),
    Regla(4, ["pierde_potencia_electrica"], "falla en el alternador"),
    Regla(5, ["arranca_y_se_apaga"], "falla del sistema antirrobo o sensor de cigüeñal"),
    Regla(6, ["clic_motor_arranque"], "falla del solenoide o batería débil"),
    Regla(7, ["se_apaga_en_marcha"], "alternador o sistema de alimentación fallando"),
    Regla(8, ["faros_se_atenuan_con_accesorios"], "problema con el alternador"),
    Regla(9, ["claxon_no_suena"], "revisar fusible, relé o conexión"),
    Regla(10,["tablero_parpadea"], "revisar conexiones eléctricas principales o alternador"),

    Regla(11, ["motor_tarda_en_encender"], "filtro de gasolina obstruido"),
    Regla(12, ["falla_al_acelerar"], "inyector sucio o bomba débil"),
    Regla(13, ["olor_gasolina_al_encender"], "fuga en líneas o inyectores"),
    Regla(14, ["pierde_potencia_en_pendientes"], "filtro de aire sucio o falla de bomba"),
    Regla(15, ["zumbido_en_tanque_al_encender"], "la bomba de gasolina está trabajando"),
    Regla(16, ["olor_constante_a_gasolina"], "revisar sellos del tanque"),
    Regla(17, ["se_apaga_en_caliente"], "falla en la bomba de gasolina"),
    Regla(18, ["consumo_combustible_alto"], "revisar mezcla aire-combustible"),
    Regla(19, ["vibra_al_encender"], "bujía o inyector defectuoso"),
    Regla(20, ["humo_negro_escape"], "mezcla rica en combustible"),

    Regla(21, ["aguja_temperatura_sube_rapido"], "fuga o falta de refrigerante"),
    Regla(22, ["vapor_del_capo"], "motor sobrecalentado"),
    Regla(23, ["electroventilador_no_enciende"], "revisar el sensor de temperatura o el relé"),
    Regla(24, ["refrigerante_marron"], "mezcla con aceite"),
    Regla(25, ["olor_dulce_en_el_auto"], "fuga del radiador interno"),
    Regla(26, ["presion_excesiva_en_mangueras"], "termostato trabado"),
    Regla(27, ["nivel_refrigerante_baja_constante"], "posibles fugas"),
    Regla(28, ["burbujas_en_deposito"], "daño en la junta de culata"),
    Regla(29, ["motor_tarda_en_calentar"], "termostato abierto"),
    Regla(30, ["sobrecalentamiento_con_ac"], "revisar ventiladores o radiador"),

    Regla(31, ["pedal_se_hunde_demasiado"], "fuga o falta de líquido de frenos"),
    Regla(32, ["coche_se_va_de_lado_al_frenar"], "frenos desiguales o pinzas trabadas"),
    Regla(33, ["se_escucha_chirrido_al_frenar"], "pastillas de freno desgastadas"),
    Regla(34, ["pedal_vibra_al_frenar"], "discos de freno deformados"),
    Regla(35, ["luz_freno_tablero_encendida"], "revisar nivel de líquido o pastillas"),
    Regla(36, ["freno_mano_no_sostiene"], "revisar tensores o balatas traseras"),
    Regla(37, ["olor_quemado_tras_pendientes"], "frenos recalentados"),
    Regla(38, ["zumbido_metalico_al_frenar"], "balatas gastadas al límite"),
    Regla(39, ["pedal_duro_frenar"], "fallo en el servofreno"),
    Regla(40, ["abs_activa_frenadas_suaves"], "revisar sensores o módulo ABS"),

    Regla(41, ["cambio_brusco_marchas"], "revisar aceite de transmisión o sensores"),
    Regla(42, ["no_entra_reversa"], "falla de solenoides"),
    Regla(43, ["se_queda_en_una_velocidad"], "falla en el cuerpo de válvulas"),
    Regla(44, ["fuga_fluido_rojo"], "pérdida de ATF"),
    Regla(45, ["auto_se_sacude_cambio"], "soporte de transmisión"),
    Regla(46, ["palanca_no_se_mueve"], "revisar bloqueo de cambio o freno de pie"),
    Regla(47, ["zumbido_constante"], "revisar rodamientos o nivel de aceite"),
    Regla(48, ["olor_quemado_transmision"], "transmisión sobrecalentada"),
    Regla(49, ["golpeteo_al_acelerar"], "revisar soportes de motor y transmisión"),
    Regla(50, ["patina_al_acelerar"], "discos internos desgastados"),

    Regla(51, ["volante_vibra_en_carretera"], "revisar balanceo o alineación"),
    Regla(52, ["sonido_clac_al_girar"], "revisar juntas homocinéticas"),
    Regla(53, ["auto_rebota_mucho"], "amortiguadores vencidos"),
    Regla(54, ["crujido_en_topes"], "revisar bujes o rótulas"),
    Regla(55, ["volante_torcido_coche_recto"], "revisar alineación"),
    Regla(56, ["coche_se_ladea"], "revisar suspensión trasera"),
    Regla(57, ["vibraciones_al_frenar"], "revisar suspensión delantera"),
    Regla(58, ["hunde_de_un_lado_al_frenar"], "amortiguador o resorte roto"),
    Regla(59, ["volante_duro_girar"], "revisar nivel de aceite de dirección"),
    Regla(60, ["silbido_al_girar"], "posible bomba de dirección dañada"),

    Regla(61, ["humo_azul_escape"], "el motor está quemando aceite"),
    Regla(62, ["humo_blanco_continuo"], "junta de culata dañada"),
    Regla(63, ["olor_fuerte_escape"], "catalizador dañado"),
    Regla(64, ["explosiones_escape"], "inyección fuera de tiempo"),
    Regla(65, ["falla_verificacion_vehicular"], "revisar sensores y catalizador"),
    Regla(66, ["catalizador_caliente"], "mezcla rica en combustible"),
    Regla(67, ["humo_negro_al_arrancar"], "revisar retenes de válvulas"),
    Regla(68, ["escape_suena_fuerte"], "fuga o rotura del silenciador"),
    Regla(69, ["silbido_en_escape"], "revisar junta de múltiple"),
    Regla(70, ["check_engine_encendido"], "problema de emisiones"),

    Regla(71, ["luz_motor_encendida"], "realizar escaneo OBD"),
    Regla(72, ["testigo_bateria_encendido"], "alternador no está cargando"),
    Regla(73, ["testigo_temperatura_encendido"], "nivel de líquido anticongelante bajo, detener y rellenar después de enfriar"),
    Regla(74, ["testigo_abs_encendido"], "revisar sensores de ruedas del ABS"),
    Regla(75, ["testigo_motor_parpadea"], "posible falla grave en el motor"),
    Regla(76, ["testigo_freno_encendido"], "revisar nivel de líquido de frenos o freno de mano"),
    Regla(77, ["testigo_aceite_parpadea"], "apagar motor y revisar nivel de aceite"),
    Regla(78, ["testigo_airbag_encendido"], "revisar sensores o cinturones de seguridad"),
    Regla(79, ["luz_control_traccion_parpadea"], "posible falla de sensor de rueda del control de tracción"),
    Regla(80, ["luces_multiples_encendidas"], "revisar batería y sistema eléctrico"),

    Regla(81, ["aceite_negro"], "cambiar aceite de inmediato"),
    Regla(82, ["filtro_aire_sucio"], "disminución del rendimiento del motor"),
    Regla(83, ["bujias_mas_40000km"], "cambiar bujías"),
    Regla(84, ["refrigerante_mas_2_anos"], "cambiar refrigerante"),
    Regla(85, ["liquido_frenos_viejo"], "posible pérdida de presión en el sistema de frenos"),
    Regla(86, ["correa_distribucion_nunca_cambiada"], "riesgo de ruptura de la correa de distribución"),
    Regla(87, ["filtro_cabina_sucio"], "disminución del flujo de aire del A/C"),
    Regla(88, ["banda_serpentina_agrietada"], "cambiar para evitar daños mayores"),
    Regla(89, ["limpiaparabrisas_ruido"], "cambiar plumas del limpiaparabrisas"),
    Regla(90, ["faros_opacos"], "pulir o reemplazar faros"),

    Regla(91, ["ruido_metalico_marcha"], "freno rozando"),
    Regla(92, ["coche_tiembla_ralenti"], "revisar soportes del motor"),
    Regla(93, ["se_apaga_al_frenar"], "revisar sensor de ralentí o vacío"),
    Regla(94, ["zumbido_acelerar_frio"], "revisar banda o poleas"),
    Regla(95, ["llave_no_gira"], "revisar cilindro o batería del control remoto"),
    Regla(96, ["faros_empanados_interior"], "humedad en la carcasa de los faros"),
    Regla(97, ["agua_interiores"], "revisar sellos de puertas o parabrisas"),
    Regla(98, ["polvo_interior"], "revisar el filtro de cabina"),
    Regla(99, ["espejos_vibran"], "revisar anclajes de los espejos"),
    Regla(100, ["vibracion_acelerar"], "revisar ejes o balanceo")
]

class DiagnosticoVentana:
    def __init__(self, root):
        self.root = root
        # nombre de la ventana
        self.root.title("Diagnóstico Vehicular")
        self.check_vars = []

        frame_principal = ttk.Frame(root)
        frame_principal.pack(fill="both", expand=True)

        # Área de búsqueda
        frame_busqueda = ttk.Frame(frame_principal)
        frame_busqueda.pack(fill="x", padx=5, pady=5)

        ttk.Label(frame_busqueda, text="Buscar por síntoma:").pack(side="left")
        self.entry_busqueda = ttk.Entry(frame_busqueda)
        self.entry_busqueda.pack(side="left", fill="x", expand=True, padx=5)
        ttk.Button(frame_busqueda, text="Buscar", command=self.buscar_por_sintoma).pack(side="left")

        # Botón para agregar regla
        ttk.Button(frame_busqueda, text="Agregar regla", command=self.abrir_ventana_agregar).pack(side="left", padx=5)

        # Scroll para reglas
        frame_scroll = ttk.Frame(frame_principal)
        frame_scroll.pack(side="top", fill="both", expand=True)

        self.canvas = tk.Canvas(frame_scroll)
        self.scrollbar = ttk.Scrollbar(frame_scroll, orient="vertical", command=self.canvas.yview)
        self.rules_frame = ttk.Frame(self.canvas)

        self.rules_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.rules_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Diagnóstico
        ttk.Label(frame_principal, text="Diagnóstico:", font=("Segoe UI", 10)).pack(anchor="w", padx=5)
        self.txt_conclusiones = tk.Text(frame_principal, height=6, wrap="word")
        self.txt_conclusiones.pack(fill="x", padx=5, pady=5)

        self.cargar_reglas(reglas)

    # metodo encargado de quitar y mostrar la lista de todas las reglas del arreglo "reglas"
    def cargar_reglas(self, lista_reglas):
        for widget in self.rules_frame.winfo_children():
            widget.destroy()
        self.check_vars.clear()

        for regla in lista_reglas:
            var = tk.BooleanVar()
            chk = ttk.Checkbutton(
                self.rules_frame,
                text=f"Síntoma {regla.id}: {regla.sintomas}",
                variable=var,
                command=self.actualizar_conclusiones
            )
            chk.pack(anchor="w", padx=5, pady=2)
            self.check_vars.append((var, regla))

    # cada que se selecciona un síntoma se actualiza la lista de conclusiones
    def actualizar_conclusiones(self):
        self.txt_conclusiones.delete(1.0, tk.END)
        for var, regla in self.check_vars:
            if var.get():
                self.txt_conclusiones.insert(tk.END, f"Conclusión de la regla {regla.id}: {regla.diagnostico}\n")

    # dependiendo la palabras se actualiza la lista con los sintomas filtrados
    def buscar_por_sintoma(self):
        sintoma = self.entry_busqueda.get().strip().lower()
        if not sintoma:
            self.cargar_reglas(reglas)
            return
        filtradas = [r for r in reglas if any(sintoma in s.lower() for s in r.sintomas)]
        self.cargar_reglas(filtradas)

    # sencillo no necesita explicaciones 
    def abrir_ventana_agregar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar nueva regla")
        ventana.geometry("400x200")

        # parte para agregar síntoma
        ttk.Label(ventana, text="Síntoma o síntomas:").pack(pady=5)
        entry_sintomas = ttk.Entry(ventana, width=50)
        entry_sintomas.pack()

        # parte para agregar diagnostico perteneciente a el sintoma de la seccion superior
        ttk.Label(ventana, text="Diagnóstico:").pack(pady=5)
        entry_diagnostico = ttk.Entry(ventana, width=50)
        entry_diagnostico.pack()

        def guardar_nueva_regla():
            sintomas = [s.strip() for s in entry_sintomas.get().split(",") if s.strip()]
            diagnostico = entry_diagnostico.get().strip()
            if not sintomas or not diagnostico:
                messagebox.showerror("Error", "Debe ingresar al menos un síntoma y un diagnóstico.")
                return
            #agrega la regla
            reglas.append(Regla([max(r.id for r in reglas) + 1], sintomas, diagnostico))
            self.cargar_reglas(reglas) # recarga las reglas con la nueva
            ventana.destroy() # cierra la ventana

        # boton para guardar la regla y quitar la ventana
        ttk.Button(ventana, text="Guardar", command=guardar_nueva_regla).pack(pady=10)

# Ejecutar app
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x500")
    app = DiagnosticoVentana(root)
    root.mainloop()
