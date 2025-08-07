import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
from datetime import datetime

class CalculadoraNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Notas Universitarias")
        self.root.geometry("500x450")
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(False, False)
        
        # Guardar tamaño original
        self.original_geometry = "500x450"
        
        # Archivo de historial
        self.historial_file = "historial_notas.json"
        
        # Configurar estilo
        style = ttk.Style()
        style.theme_use('clam')
        
        self.crear_interfaz()
    
    def crear_menu(self):
        """Crea la barra de menú"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menú Archivo
        archivo_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)
        archivo_menu.add_command(label="Guardar Resultado", command=self.guardar_resultado)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Ver Historial", command=self.mostrar_historial)
        archivo_menu.add_command(label="Exportar Historial", command=self.exportar_historial)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.root.quit)
        
        # Menú Herramientas
        herramientas_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Herramientas", menu=herramientas_menu)
        herramientas_menu.add_command(label="Predictor de Notas", command=self.mostrar_predictor)
        
        # Menú Ayuda
        ayuda_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=ayuda_menu)
        ayuda_menu.add_command(label="Acerca de", command=self.mostrar_acerca_de)
        
    def crear_interfaz(self):
        # Crear menú
        self.crear_menu()
        
        # Título principal
        titulo = tk.Label(
            self.root, 
            text="📚 Calculadora de Notas Universitarias", 
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50"
        )
        titulo.pack(pady=20)
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(padx=30, pady=10, fill="both", expand=True)
        
        # Configurar grid para 3 columnas
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)  
        main_frame.grid_columnconfigure(2, weight=1)
        
        # Primer Examen
        self.crear_campo(main_frame, "Primer Examen (0-100):", "primer_examen", 0)
        
        # Segundo Examen
        self.crear_campo(main_frame, "Segundo Examen (0-100):", "segundo_examen", 1)
        
        # Nota Práctica
        self.crear_campo(main_frame, "Nota Práctica (0-100):", "nota_practica", 2)
        
        # Examen Final
        self.crear_campo(main_frame, "Examen Final (0-100):", "examen_final", 3)
        
        # Botón calcular
        btn_calcular = tk.Button(
            main_frame,
            text="🧮 Calcular Promedio",
            command=self.calcular_promedio,
            font=("Arial", 12, "bold"),
            bg="#3498db",
            fg="white",
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        btn_calcular.grid(row=4, column=0, columnspan=2, pady=(20, 10))
        
        # Botón predictor
        btn_predictor = tk.Button(
            main_frame,
            text="🎯 ¿Qué necesito para aprobar?",
            command=self.mostrar_predictor,
            font=("Arial", 10, "bold"),
            bg="#e67e22",
            fg="white",
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2"
        )
        btn_predictor.grid(row=4, column=2, columnspan=1, pady=(20, 10), padx=(10, 0))
        
        # Resultado
        self.resultado_frame = tk.Frame(main_frame, bg="#f0f0f0")
        self.resultado_frame.grid(row=5, column=0, columnspan=3, pady=10)
        
        # Botón limpiar
        btn_limpiar = tk.Button(
            main_frame,
            text="🗑️ Limpiar",
            command=self.limpiar_campos,
            font=("Arial", 10),
            bg="#95a5a6",
            fg="white",
            relief="flat",
            padx=15,
            pady=5,
            cursor="hand2"
        )
        btn_limpiar.grid(row=6, column=0, columnspan=3, pady=10)
        
    def crear_campo(self, parent, texto, atributo, fila):
        # Label
        label = tk.Label(
            parent, 
            text=texto, 
            font=("Arial", 11),
            bg="#f0f0f0",
            fg="#34495e"
        )
        label.grid(row=fila, column=0, sticky="w", pady=8, padx=(0, 10))
        
        # Entry
        entry = tk.Entry(
            parent, 
            font=("Arial", 11),
            width=12,
            relief="solid",
            borderwidth=1,
            justify="center"
        )
        entry.grid(row=fila, column=1, sticky="w", pady=8)
        
        # Guardar referencia al entry
        setattr(self, atributo, entry)
        
    def validar_nota(self, nota_str, nombre_campo):
        try:
            nota = float(nota_str)
            if nota < 0 or nota > 100:
                messagebox.showerror("Error", f"{nombre_campo} debe estar entre 0 y 100")
                return None
            return nota
        except ValueError:
            messagebox.showerror("Error", f"{nombre_campo} debe ser un número válido")
            return None
    
    def calcular_promedio(self):
        # Obtener valores
        primer_examen_str = self.primer_examen.get().strip()
        segundo_examen_str = self.segundo_examen.get().strip()
        nota_practica_str = self.nota_practica.get().strip()
        examen_final_str = self.examen_final.get().strip()
        
        # Validar que todos los campos estén llenos
        if not all([primer_examen_str, segundo_examen_str, nota_practica_str, examen_final_str]):
            messagebox.showerror("Error", "Por favor, complete todos los campos")
            return
        
        # Validar y convertir notas
        primer_examen = self.validar_nota(primer_examen_str, "Primer Examen")
        segundo_examen = self.validar_nota(segundo_examen_str, "Segundo Examen")
        nota_practica = self.validar_nota(nota_practica_str, "Nota Práctica")
        examen_final = self.validar_nota(examen_final_str, "Examen Final")
        
        if None in [primer_examen, segundo_examen, nota_practica, examen_final]:
            return
        
        # Cálculo según la fórmula especificada:
        # 1. Promedio de primer y segundo examen
        promedio_examenes = (primer_examen + segundo_examen) / 2
        
        # 2. Promedio final: (promedio_examenes + nota_practica + examen_final) / 3
        nota_final = (promedio_examenes + nota_practica + examen_final) / 3
        
        # Determinar letra de calificación
        letra_calificacion = self.obtener_letra_calificacion(nota_final)
        color_letra = self.obtener_color_letra(letra_calificacion)
        
        # Mostrar resultado
        self.mostrar_resultado(primer_examen, segundo_examen, nota_practica, examen_final, promedio_examenes, nota_final, letra_calificacion, color_letra)
        
        # Guardar resultado para posible guardado
        self.ultimo_resultado = {
            "primer_examen": primer_examen,
            "segundo_examen": segundo_examen,
            "nota_practica": nota_practica,
            "examen_final": examen_final,
            "promedio_examenes": promedio_examenes,
            "nota_final": nota_final,
            "letra": letra_calificacion
        }
    
    def obtener_letra_calificacion(self, nota):
        if nota >= 90:
            return "A"
        elif nota >= 80:
            return "B"
        elif nota >= 70:
            return "C"
        else:
            return "F"
    
    def obtener_color_letra(self, letra):
        colores = {
            "A": "#27ae60",  # Verde
            "B": "#f39c12",  # Naranja
            "C": "#e67e22",  # Naranja oscuro
            "F": "#e74c3c"   # Rojo
        }
        return colores.get(letra, "#34495e")
    
    def mostrar_resultado(self, primer_examen, segundo_examen, nota_practica, examen_final, promedio_examenes, nota_final, letra, color):
        # Limpiar resultado anterior
        for widget in self.resultado_frame.winfo_children():
            widget.destroy()
        
        # Aumentar el tamaño de la ventana para el nuevo contenido
        self.root.geometry("500x600")

        # Frame del resultado
        resultado_container = tk.Frame(self.resultado_frame, bg="#ecf0f1", relief="solid", borderwidth=1)
        resultado_container.pack(pady=10, padx=20, fill="x")
        
        # Título del resultado
        titulo_resultado = tk.Label(
            resultado_container,
            text="📊 RESULTADO DETALLADO",
            font=("Arial", 12, "bold"),
            bg="#ecf0f1",
            fg="#2c3e50"
        )
        titulo_resultado.pack(pady=(10, 5))

        # Formula
        formula_label = tk.Label(
            resultado_container,
            text="Fórmula: ((P1 + P2) / 2 + Práctica + Final) / 3",
            font=("Arial", 9, "italic"),
            bg="#ecf0f1",
            fg="#34495e"
        )
        formula_label.pack(pady=(5, 2))

        # Detalle del cálculo
        detalle_calculo_str = f"Cálculo: (({primer_examen:.2f} + {segundo_examen:.2f}) / 2 + {nota_practica:.2f} + {examen_final:.2f}) / 3"
        detalle_label = tk.Label(
            resultado_container,
            text=detalle_calculo_str,
            font=("Arial", 9),
            bg="#ecf0f1",
            fg="#34495e"
        )
        detalle_label.pack(pady=2)
        
        # Promedio de exámenes
        promedio_label = tk.Label(
            resultado_container,
            text=f"Paso 1 - Promedio Exámenes: {promedio_examenes:.2f}",
            font=("Arial", 10),
            bg="#ecf0f1",
            fg="#34495e"
        )
        promedio_label.pack(pady=5)
        
        # Nota final
        nota_final_label = tk.Label(
            resultado_container,
            text=f"Paso 2 - Nota Final: {nota_final:.2f}",
            font=("Arial", 12, "bold"),
            bg="#ecf0f1",
            fg="#2c3e50"
        )
        nota_final_label.pack(pady=5)
        
        # Calificación con letra
        if letra == "F":
            mensaje = f"¡Te quemaste! 🔥 Calificación: {letra}"
        else:
            mensaje = f"¡Pasaste! 🎉 Calificación: {letra}"
            
        calificacion_label = tk.Label(
            resultado_container,
            text=mensaje,
            font=("Arial", 14, "bold"),
            bg="#ecf0f1",
            fg=color
        )
        calificacion_label.pack(pady=(5, 15))
        
        # Descripción de la calificación
        descripciones = {
            "A": "Excelente (90-100)",
            "B": "Bueno (80-89)",
            "C": "Regular (70-79)",
            "F": "Reprobado (0-69)"
        }
        
        descripcion_label = tk.Label(
            resultado_container,
            text=descripciones[letra],
            font=("Arial", 9),
            bg="#ecf0f1",
            fg="#7f8c8d"
        )
        descripcion_label.pack(pady=(0, 10))
    
    def limpiar_campos(self):
        self.primer_examen.delete(0, tk.END)
        self.segundo_examen.delete(0, tk.END)
        self.nota_practica.delete(0, tk.END)
        self.examen_final.delete(0, tk.END)
        
        # Limpiar resultado y restaurar tamaño
        for widget in self.resultado_frame.winfo_children():
            widget.destroy()
        self.root.geometry(self.original_geometry)
    
    def mostrar_predictor(self):
        """Muestra una ventana para predecir qué nota se necesita en el examen final"""
        predictor_window = tk.Toplevel(self.root)
        predictor_window.title("🎯 Predictor de Notas")
        predictor_window.geometry("450x350")
        predictor_window.configure(bg="#f0f0f0")
        predictor_window.resizable(False, False)
        
        # Centrar ventana
        predictor_window.transient(self.root)
        predictor_window.grab_set()
        
        # Título
        titulo = tk.Label(
            predictor_window,
            text="🎯 ¿Qué necesito para aprobar?",
            font=("Arial", 14, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50"
        )
        titulo.pack(pady=20)
        
        # Frame principal
        frame = tk.Frame(predictor_window, bg="#f0f0f0")
        frame.pack(padx=30, pady=10)
        
        # Campos de entrada
        self.crear_campo_predictor(frame, "Primer Examen:", "pred_primer_examen", 0)
        self.crear_campo_predictor(frame, "Segundo Examen:", "pred_segundo_examen", 1)
        self.crear_campo_predictor(frame, "Nota Práctica:", "pred_nota_practica", 2)
        
        # Nota objetivo
        tk.Label(
            frame,
            text="Nota objetivo:",
            font=("Arial", 11),
            bg="#f0f0f0",
            fg="#34495e"
        ).grid(row=3, column=0, sticky="w", pady=8, padx=(0, 10))
        
        self.objetivo_var = tk.StringVar(value="70")
        objetivo_combo = ttk.Combobox(
            frame,
            textvariable=self.objetivo_var,
            values=["60", "70", "80", "90"],
            width=10,
            state="readonly"
        )
        objetivo_combo.grid(row=3, column=1, sticky="w", pady=8)
        
        # Botón calcular
        btn_calcular_pred = tk.Button(
            frame,
            text="🧮 Calcular",
            command=lambda: self.calcular_prediccion(predictor_window),
            font=("Arial", 12, "bold"),
            bg="#27ae60",
            fg="white",
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        btn_calcular_pred.grid(row=4, column=0, columnspan=2, pady=20)
        
        # Frame para resultado
        self.pred_resultado_frame = tk.Frame(frame, bg="#f0f0f0")
        self.pred_resultado_frame.grid(row=5, column=0, columnspan=2, pady=10)
    
    def crear_campo_predictor(self, parent, texto, atributo, fila):
        """Crea un campo de entrada para el predictor"""
        label = tk.Label(
            parent,
            text=texto,
            font=("Arial", 11),
            bg="#f0f0f0",
            fg="#34495e"
        )
        label.grid(row=fila, column=0, sticky="w", pady=8, padx=(0, 10))
        
        entry = tk.Entry(
            parent,
            font=("Arial", 11),
            width=12,
            relief="solid",
            borderwidth=1,
            justify="center"
        )
        entry.grid(row=fila, column=1, sticky="w", pady=8)
        
        setattr(self, atributo, entry)
    
    def calcular_prediccion(self, ventana):
        """Calcula qué nota se necesita en el examen final para alcanzar el objetivo"""
        try:
            # Obtener valores
            primer_examen = float(self.pred_primer_examen.get().strip())
            segundo_examen = float(self.pred_segundo_examen.get().strip())
            nota_practica = float(self.pred_nota_practica.get().strip())
            objetivo = float(self.objetivo_var.get())
            
            # Validar notas
            if not all(0 <= nota <= 100 for nota in [primer_examen, segundo_examen, nota_practica]):
                messagebox.showerror("Error", "Las notas deben estar entre 0 y 100")
                return
                
            if not (0 <= objetivo <= 100):
                messagebox.showerror("Error", "El objetivo debe estar entre 0 y 100")
                return
            
            # Calcular promedio de exámenes
            promedio_examenes = (primer_examen + segundo_examen) / 2
            
            # Calcular nota necesaria en examen final
            # Fórmula: (promedio_examenes + nota_practica + examen_final) / 3 = objetivo
            # Despejando: examen_final = (objetivo * 3) - promedio_examenes - nota_practica
            nota_necesaria = (objetivo * 3) - promedio_examenes - nota_practica
            
            # Limpiar resultado anterior
            for widget in self.pred_resultado_frame.winfo_children():
                widget.destroy()
            
            # Mostrar resultado
            resultado_container = tk.Frame(self.pred_resultado_frame, bg="#ecf0f1", relief="solid", borderwidth=1)
            resultado_container.pack(pady=10, padx=10, fill="x")
            
            # Determinar color y mensaje según si es posible
            if nota_necesaria <= 100:
                if nota_necesaria < 0:
                    color = "#27ae60"
                    mensaje = "¡Ya tienes la nota asegurada! 🎉"
                    detalle = f"Con {nota_necesaria:.1f} puntos ya pasas"
                else:
                    color = "#f39c12" if nota_necesaria <= 85 else "#e74c3c"
                    mensaje = f"Necesitas {nota_necesaria:.1f} en el examen final"
                    if nota_necesaria <= 60:
                        detalle = "¡Muy alcanzable! 💪"
                    elif nota_necesaria <= 80:
                        detalle = "¡Puedes hacerlo! 📚"
                    elif nota_necesaria <= 95:
                        detalle = "¡Requiere esfuerzo extra! 🔥"
                    else:
                        detalle = "¡Necesitas excelencia total! ⭐"
            else:
                color = "#e74c3c"
                mensaje = f"Necesitas {nota_necesaria:.1f} (>100)"
                detalle = "Imposible alcanzar este objetivo 😞"
            
            # Mostrar mensaje principal
            mensaje_label = tk.Label(
                resultado_container,
                text=mensaje,
                font=("Arial", 12, "bold"),
                bg="#ecf0f1",
                fg=color
            )
            mensaje_label.pack(pady=10)
            
            # Mostrar detalle
            detalle_label = tk.Label(
                resultado_container,
                text=detalle,
                font=("Arial", 10),
                bg="#ecf0f1",
                fg="#34495e"
            )
            detalle_label.pack(pady=(0, 10))
            
            # Mostrar cálculo
            calculo_label = tk.Label(
                resultado_container,
                text=f"Promedio actual sin final: {((promedio_examenes + nota_practica) / 2):.1f}",
                font=("Arial", 9),
                bg="#ecf0f1",
                fg="#7f8c8d"
            )
            calculo_label.pack(pady=(0, 10))
            
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")
    
    def guardar_resultado(self):
        """Guarda el resultado actual en el historial"""
        try:
            # Verificar que hay un resultado calculado
            if not hasattr(self, 'ultimo_resultado'):
                messagebox.showwarning("Aviso", "Primero calcula una nota para poder guardarla")
                return
            
            # Pedir nombre de la materia
            nombre_materia = self.pedir_nombre_materia()
            if not nombre_materia:
                return
            
            # Cargar historial existente
            historial = self.cargar_historial()
            
            # Agregar nuevo resultado
            nuevo_resultado = {
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "materia": nombre_materia,
                **self.ultimo_resultado
            }
            
            historial.append(nuevo_resultado)
            
            # Guardar historial
            with open(self.historial_file, 'w', encoding='utf-8') as f:
                json.dump(historial, f, indent=2, ensure_ascii=False)
            
            messagebox.showinfo("Éxito", f"Resultado guardado para {nombre_materia}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar: {str(e)}")
    
    def pedir_nombre_materia(self):
        """Solicita el nombre de la materia al usuario"""
        ventana = tk.Toplevel(self.root)
        ventana.title("Nombre de la Materia")
        ventana.geometry("300x150")
        ventana.configure(bg="#f0f0f0")
        ventana.resizable(False, False)
        ventana.transient(self.root)
        ventana.grab_set()
        
        # Centrar ventana
        ventana.geometry("+%d+%d" % (
            self.root.winfo_rootx() + 100,
            self.root.winfo_rooty() + 100
        ))
        
        tk.Label(
            ventana,
            text="Nombre de la materia:",
            font=("Arial", 11),
            bg="#f0f0f0"
        ).pack(pady=20)
        
        entrada = tk.Entry(ventana, font=("Arial", 11), width=25)
        entrada.pack(pady=10)
        entrada.focus()
        
        resultado = [None]  # Lista para poder modificar desde la función interna
        
        def confirmar():
            nombre = entrada.get().strip()
            if nombre:
                resultado[0] = nombre
                ventana.destroy()
            else:
                messagebox.showwarning("Aviso", "Por favor ingresa un nombre")
        
        def cancelar():
            ventana.destroy()
        
        frame_botones = tk.Frame(ventana, bg="#f0f0f0")
        frame_botones.pack(pady=10)
        
        tk.Button(
            frame_botones,
            text="Confirmar",
            command=confirmar,
            bg="#27ae60",
            fg="white",
            padx=15
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            frame_botones,
            text="Cancelar", 
            command=cancelar,
            bg="#95a5a6",
            fg="white",
            padx=15
        ).pack(side=tk.LEFT, padx=5)
        
        # Bind Enter key
        entrada.bind('<Return>', lambda e: confirmar())
        ventana.bind('<Escape>', lambda e: cancelar())
        
        ventana.wait_window()
        return resultado[0]
    
    def cargar_historial(self):
        """Carga el historial desde el archivo JSON"""
        try:
            if os.path.exists(self.historial_file):
                with open(self.historial_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return []
        except Exception:
            return []
    
    def mostrar_historial(self):
        """Muestra el historial de notas en una nueva ventana"""
        historial = self.cargar_historial()
        
        if not historial:
            messagebox.showinfo("Historial", "No hay registros guardados")
            return
        
        # Crear ventana del historial
        hist_window = tk.Toplevel(self.root)
        hist_window.title("📚 Historial de Notas")
        hist_window.geometry("600x400")
        hist_window.configure(bg="#f0f0f0")
        
        # Frame con scrollbar
        frame_container = tk.Frame(hist_window, bg="#f0f0f0")
        frame_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        canvas = tk.Canvas(frame_container, bg="#f0f0f0")
        scrollbar = ttk.Scrollbar(frame_container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Título
        titulo = tk.Label(
            scrollable_frame,
            text="📚 Historial de Calificaciones",
            font=("Arial", 14, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50"
        )
        titulo.pack(pady=10)
        
        # Mostrar registros
        for i, registro in enumerate(reversed(historial)):  # Más recientes primero
            frame_registro = tk.Frame(scrollable_frame, bg="#ecf0f1", relief="solid", borderwidth=1)
            frame_registro.pack(fill=tk.X, padx=10, pady=5)
            
            # Información del registro
            info_texto = (f"📅 {registro['fecha']} | 📖 {registro['materia']}\n"
                         f"📊 Nota Final: {registro['nota_final']:.2f} | "
                         f"📝 Calificación: {registro['letra']} | "
                         f"✅ {'Aprobado' if registro['nota_final'] >= 70 else 'Reprobado'}")
            
            tk.Label(
                frame_registro,
                text=info_texto,
                font=("Arial", 10),
                bg="#ecf0f1",
                fg="#2c3e50",
                justify=tk.LEFT
            ).pack(anchor="w", padx=10, pady=5)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def exportar_historial(self):
        """Exporta el historial a un archivo CSV"""
        historial = self.cargar_historial()
        
        if not historial:
            messagebox.showinfo("Exportar", "No hay registros para exportar")
            return
        
        try:
            archivo = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                title="Guardar historial como..."
            )
            
            if archivo:
                with open(archivo, 'w', encoding='utf-8') as f:
                    # Encabezados
                    f.write("Fecha,Materia,Primer Examen,Segundo Examen,Nota Práctica,Examen Final,Nota Final,Calificación\n")
                    
                    # Datos
                    for registro in historial:
                        f.write(f"{registro['fecha']},{registro['materia']},{registro['primer_examen']:.2f},"
                               f"{registro['segundo_examen']:.2f},{registro['nota_practica']:.2f},"
                               f"{registro['examen_final']:.2f},{registro['nota_final']:.2f},{registro['letra']}\n")
                
                messagebox.showinfo("Éxito", f"Historial exportado a {archivo}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al exportar: {str(e)}")
    
    def mostrar_acerca_de(self):
        """Muestra información acerca de la aplicación"""
        acerca_texto = """
📚 Calculadora de Notas Universitarias
Versión 2.0

🎯 Características:
• Cálculo de promedios universitarios
• Predictor de notas necesarias
• Historial de calificaciones
• Exportación de datos

👨‍💻 Desarrollado por: Jose Mencia
📅 Año: 2024
🎓 Para estudiantes universitarios dominicanos

¡Buena suerte en tus estudios! 🌟
        """
        
        messagebox.showinfo("Acerca de", acerca_texto.strip())

def main():
    root = tk.Tk()
    app = CalculadoraNotas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
