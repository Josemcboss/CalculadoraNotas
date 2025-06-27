import tkinter as tk
from tkinter import ttk, messagebox

class CalculadoraNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Notas Universitarias")
        self.root.geometry("500x450")
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(False, False)
        
        # Guardar tamaño original
        self.original_geometry = "500x450"
        
        # Configurar estilo
        style = ttk.Style()
        style.theme_use('clam')
        
        self.crear_interfaz()
        
    def crear_interfaz(self):
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
        btn_calcular.grid(row=4, column=0, columnspan=2, pady=30)
        
        # Resultado
        self.resultado_frame = tk.Frame(main_frame, bg="#f0f0f0")
        self.resultado_frame.grid(row=5, column=0, columnspan=2, pady=10)
        
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
        btn_limpiar.grid(row=6, column=0, columnspan=2, pady=10)
        
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

def main():
    root = tk.Tk()
    app = CalculadoraNotas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
