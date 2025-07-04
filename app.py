<<<<<<< HEAD
# Copyright (c) 2024 Jose Mencia
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

import streamlit as st

# Configuración de universidades dominicanas con sus colores representativos
UNIVERSIDADES = {    "UNPHU": {
        "nombre": "Universidad Nacional Pedro Henríquez Ureña",
        "color_primario": "#007A33",  # Verde
        "color_secundario": "#FFFFFF",  # Blanco
        "sistema": "Escala 0-100",
        "minimo_aprobar": 70,
        "descripcion": "Nota final = (Trabajos Prácticos + ((Parcial1 + Parcial2)/2) + Examen Final) / 3"
    },
    "UNIBE": {
        "nombre": "Universidad Iberoamericana",
        "color_primario": "#004A99",  # Azul.
        "color_secundario": "#FFFFFF",  # Blanco. [4]
        "sistema": "Índice Académico (0.00-4.00)",
        "minimo_aprobar": 2.0,
        "descripcion": "Índice = Sumatoria (Créditos x Valor de Calificación) / Total de Créditos"
    },
    "UTESA": {
        "nombre": "Universidad Tecnológica de Santiago",
        "color_primario": "#008A3D",  # Verde. [2]
        "color_secundario": "#FFD700",  # Amarillo. [2]
        "sistema": "Sistema de evaluación por parciales",
        "minimo_aprobar": 70,
        "descripcion": "Tres parciales de 30 puntos cada uno. Nota final: Parcial1 + Parcial2 + Parcial3"
    },
    "ISFODOSU": {
        "nombre": "Instituto Superior de Formación Docente Salomé Ureña",
        "color_primario": "#005EB8",  # Azul institucional. [18]
        "color_secundario": "#FFFFFF",  # Blanco. [21]
        "sistema": "Escala 0-100 convertida a GPA 0-4",
        "minimo_aprobar": 70,
        "descripcion": "A=4 (90-100), B=3 (80-89), C=2 (70-79)"
    },
    "UCE": {
        "nombre": "Universidad Central del Este",
        "color_primario": "#D4002D",  # Rojo Escarlata. [6, 11]
        "color_secundario": "#0047AB",  # Azul Cobalto. [6, 11]
        "sistema": "Escala 0-100 con conversión a GPA 0-4",
        "minimo_aprobar": 70,
        "descripcion": "A=4.0 (90-100), B+=3.5 (85-89), B=3.0 (80-84), C+=2.5 (75-79)"
    },
    "UASD": {
        "nombre": "Universidad Autónoma de Santo Domingo",
        "color_primario": "#002D62",  # Azul Añil. [3, 5]
        "color_secundario": "#FFFFFF",  # Blanco. [1, 3]
        "sistema": "Índice Académico basado en escala 0-100",
        "minimo_aprobar": 70,
        "descripcion": ">=70: condición normal, 60-69: prevención académica, <60: situación crítica"
    },
    "PUCMM": {
        "nombre": "Pontificia Universidad Católica Madre y Maestra",
        "color_primario": "#0038A8",  # Azul Pantone 286 C. [10]
        "color_secundario": "#FFDA00",  # Amarillo Pantone Yellow 012 C. [10]
        "sistema": "Índice Académico Acumulado (escala 0-4)",
        "minimo_aprobar": 2.0,
        "descripcion": "Índice = Sumatoria (Créditos x GPA) / Total de Créditos"
    }
}

def obtener_letra_calificacion_universal(nota):
    """Determina la letra de calificación basada en la nota (sistema universal)"""
    if nota >= 90:
        return "A", "Excelente (90-100)", "#27ae60"  # Verde
    elif nota >= 80:
        return "B", "Bueno (80-89)", "#f39c12"  # Naranja
    elif nota >= 70:
        return "C", "Regular (70-79)", "#e67e22"  # Naranja oscuro
    else:
        return "F", "Reprobado (0-69)", "#e74c3c"  # Rojo

def obtener_gpa_unibe_pucmm(nota):
    """Convierte nota a GPA para UNIBE y PUCMM"""
    if nota >= 90:
        return 4.0, "A"
    elif nota >= 80:
        return 3.0, "B"
    elif nota >= 70:
        return 2.0, "C"
    elif nota >= 60:
        return 1.0, "D"
    else:
        return 0.0, "F"

def obtener_gpa_uce(nota):
    """Convierte nota a GPA para UCE"""
    if nota >= 90:
        return 4.0, "A"
    elif nota >= 85:
        return 3.5, "B+"
    elif nota >= 80:
        return 3.0, "B"
    elif nota >= 75:
        return 2.5, "C+"
    elif nota >= 70:
        return 2.0, "C"
    elif nota >= 60:
        return 1.0, "D"
    else:
        return 0.0, "F"

def calcular_nota_unphu(trabajos, parcial1, parcial2, examen_final):
    """Calcula la nota final para UNPHU"""
    promedio_parciales = (parcial1 + parcial2) / 2
    nota_final = (trabajos + promedio_parciales + examen_final) / 3
    return nota_final

def calcular_nota_utesa(parcial1, parcial2, parcial3):
    """Calcula la nota final para UTESA"""
    return parcial1 + parcial2 + parcial3

# Configuración de la página
st.set_page_config(
    page_title="Calculadora de Notas - Universidades RD",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Selector de universidad en la barra lateral
st.sidebar.title("🏛️ Universidades RD")
universidad_seleccionada = st.sidebar.selectbox(
    "Selecciona tu universidad:",
    options=list(UNIVERSIDADES.keys()),
    format_func=lambda x: f"{x} - {UNIVERSIDADES[x]['nombre'][:20]}..."
)

# Obtener configuración de la universidad seleccionada
config_uni = UNIVERSIDADES[universidad_seleccionada]

# Mostrar información de la universidad en la barra lateral
st.sidebar.markdown("---")
st.sidebar.markdown(f"### 📋 {universidad_seleccionada}")
st.sidebar.markdown(f"**{config_uni['nombre']}**")
st.sidebar.markdown(f"**Sistema:** {config_uni['sistema']}")
st.sidebar.markdown(f"**Mínimo para aprobar:** {config_uni['minimo_aprobar']}")
st.sidebar.markdown(f"**Cálculo:** {config_uni['descripcion']}")

# CSS personalizado con colores de la universidad
st.markdown(f"""
<style>
    .universidad-header {{
        background: linear-gradient(90deg, {config_uni['color_primario']}, {config_uni['color_secundario']});
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
        color: white;
        font-weight: bold;
        font-size: 24px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }}
    .stNumberInput > label {{
        font-weight: bold;
        color: {config_uni['color_primario']};
    }}
    .result-container {{
        background: linear-gradient(135deg, {config_uni['color_primario']}20, {config_uni['color_secundario']}20);
        padding: 20px;
        border-radius: 10px;
        border: 2px solid {config_uni['color_primario']};
        margin-top: 20px;
    }}
    .stButton > button {{
        background-color: {config_uni['color_primario']};
        color: white;
        border: none;
        border-radius: 5px;
        font-weight: bold;
    }}
    .stButton > button:hover {{
        background-color: {config_uni['color_secundario']};
        color: {config_uni['color_primario']};
    }}
</style>
""", unsafe_allow_html=True)

# Título principal con colores de la universidad
st.markdown(f"""
<div class="universidad-header">
    🎓 Calculadora de Notas - {universidad_seleccionada}
</div>
""", unsafe_allow_html=True)

st.markdown(f"### {config_uni['nombre']}")
st.markdown("---")

# Campos de entrada según la universidad seleccionada
if universidad_seleccionada == "UNPHU":
    col1, col2 = st.columns(2)
    
    with col1:
        trabajos_practicos = st.number_input(
            "📝 Trabajos Prácticos (0-100):",
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=0.01,
            format="%.2f",
            help="Nota de trabajos prácticos"
        )
        
        parcial1 = st.number_input(
            "📋 Primer Parcial (0-100):",
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=0.01,
            format="%.2f",
            help="Nota del primer parcial"
        )
    
    with col2:
        parcial2 = st.number_input(
            "📋 Segundo Parcial (0-100):",
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=0.01,
            format="%.2f",
            help="Nota del segundo parcial"
        )
        
        examen_final = st.number_input(
            "🏆 Examen Final (0-100):",
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=0.01,
            format="%.2f",
            help="Nota del examen final"
        )

elif universidad_seleccionada == "UTESA":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        parcial1 = st.number_input(
            "📋 Primer Parcial (0-30):",
            min_value=0.0,
            max_value=30.0,
            value=0.0,
            step=0.01,
            format="%.2f",
            help="Primer parcial (máximo 30 puntos)"
        )
    
    with col2:
        parcial2 = st.number_input(
            "📋 Segundo Parcial (0-30):",
            min_value=0.0,
            max_value=30.0,
            value=0.0,
            step=0.01,
            format="%.2f",
            help="Segundo parcial (máximo 30 puntos)"
        )
    
    with col3:
        parcial3 = st.number_input(
            "📋 Tercer Parcial (0-40):",
            min_value=0.0,
            max_value=40.0,
            value=0.0,
            step=0.01,
            format="%.2f",
            help="Tercer parcial (30 puntos + 10 de participación)"
        )

elif universidad_seleccionada in ["UNIBE", "PUCMM"]:
    st.markdown("### 📚 Ingresa las notas de tus materias")
    
    # Para UNIBE y PUCMM (sistema de créditos)
    num_materias = st.number_input("Número de materias:", min_value=1, max_value=10, value=1)
    
    materias_data = []
    for i in range(num_materias):
        col1, col2 = st.columns(2)
        with col1:
            nota = st.number_input(f"Nota Materia {i+1} (0-100):", min_value=0.0, max_value=100.0, value=0.0, key=f"nota_{i}")
        with col2:
            creditos = st.number_input(f"Créditos Materia {i+1}:", min_value=1, max_value=6, value=3, key=f"creditos_{i}")
        
        materias_data.append({"nota": nota, "creditos": creditos})

else:  # Para las demás universidades (sistema tradicional)
    col1, col2 = st.columns(2)
    
    with col1:
        primer_examen = st.number_input(
            "🎯 Primer Examen (0-100):",
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=0.01,
            format="%.2f",
            help="Ingresa tu nota del primer examen"
        )
        
        nota_practica = st.number_input(
            "📝 Nota Práctica (0-100):",
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=0.01,
            format="%.2f",
            help="Ingresa tu nota de prácticas"
        )
    
    with col2:
        segundo_examen = st.number_input(
            "🎯 Segundo Examen (0-100):",
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=0.01,
            format="%.2f",
            help="Ingresa tu nota del segundo examen"
        )
        
        examen_final = st.number_input(
            "🏆 Examen Final (0-100):",
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=0.01,
            format="%.2f",
            help="Ingresa tu nota del examen final"
        )

# Espaciado
st.markdown("<br>", unsafe_allow_html=True)

# Botón para calcular (centrado)
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    calcular = st.button("🧮 Calcular Resultado", use_container_width=True)

# Lógica de cálculo según la universidad
if calcular:
    resultado_texto = ""
    nota_final = 0
    aprobado = False
    
    if universidad_seleccionada == "UNPHU":
        if all(nota == 0 for nota in [trabajos_practicos, parcial1, parcial2, examen_final]):
            st.warning("⚠️ Por favor, ingresa al menos una nota mayor que 0.")
        else:
            nota_final = calcular_nota_unphu(trabajos_practicos, parcial1, parcial2, examen_final)
            aprobado = nota_final >= config_uni['minimo_aprobar']
            letra, descripcion, color = obtener_letra_calificacion_universal(nota_final)
            
    elif universidad_seleccionada == "UTESA":
        if all(nota == 0 for nota in [parcial1, parcial2, parcial3]):
            st.warning("⚠️ Por favor, ingresa al menos una nota mayor que 0.")
        else:
            nota_final = calcular_nota_utesa(parcial1, parcial2, parcial3)
            aprobado = nota_final >= config_uni['minimo_aprobar']
            letra, descripcion, color = obtener_letra_calificacion_universal(nota_final)
            
    elif universidad_seleccionada in ["UNIBE", "PUCMM"]:
        total_creditos = sum(materia['creditos'] for materia in materias_data if materia['nota'] > 0)
        if total_creditos == 0:
            st.warning("⚠️ Por favor, ingresa al menos una materia con nota mayor que 0.")
        else:
            suma_ponderada = 0
            for materia in materias_data:
                if materia['nota'] > 0:
                    gpa, _ = obtener_gpa_unibe_pucmm(materia['nota'])
                    suma_ponderada += gpa * materia['creditos']
            
            indice_academico = suma_ponderada / total_creditos
            aprobado = indice_academico >= config_uni['minimo_aprobar']
            nota_final = indice_academico
            color = "#27ae60" if aprobado else "#e74c3c"
            
    elif universidad_seleccionada == "UCE":
        if all(nota == 0 for nota in [primer_examen, segundo_examen, nota_practica, examen_final]):
            st.warning("⚠️ Por favor, ingresa al menos una nota mayor que 0.")
        else:
            promedio_examenes = (primer_examen + segundo_examen) / 2
            nota_final = (promedio_examenes + nota_practica + examen_final) / 3
            gpa, letra = obtener_gpa_uce(nota_final)
            aprobado = nota_final >= config_uni['minimo_aprobar']
            color = "#27ae60" if aprobado else "#e74c3c"
            
    else:  # ISFODOSU, UASD
        if all(nota == 0 for nota in [primer_examen, segundo_examen, nota_practica, examen_final]):
            st.warning("⚠️ Por favor, ingresa al menos una nota mayor que 0.")
        else:
            promedio_examenes = (primer_examen + segundo_examen) / 2
            nota_final = (promedio_examenes + nota_practica + examen_final) / 3
            aprobado = nota_final >= config_uni['minimo_aprobar']
            letra, descripcion, color = obtener_letra_calificacion_universal(nota_final)
    
    # Mostrar resultado si hay cálculo válido
    if 'nota_final' in locals() and nota_final > 0:
        st.markdown("---")
        st.subheader(f"📊 Resultado - {universidad_seleccionada}")
        
        # Contenedor del resultado con colores de la universidad
        estado_texto = "🎉 ¡Aprobaste!" if aprobado else "❌ No aprobaste"
        
        if universidad_seleccionada in ["UNIBE", "PUCMM"]:
            valor_mostrar = f"{nota_final:.2f}/4.00"
            metrica_label = "Índice Académico"
        elif universidad_seleccionada == "UCE":
            valor_mostrar = f"{nota_final:.2f} (GPA: {gpa:.2f})"
            metrica_label = "Nota Final"
        else:
            valor_mostrar = f"{nota_final:.2f}/100"
            metrica_label = "Nota Final"
            
        st.markdown(f"""
        <div class="result-container">
            <div style="text-align: center;">
                <p style="font-size: 32px; font-weight: bold; color: {color}; margin: 20px 0;">
                    {estado_texto}
                </p>
                <p style="font-size: 28px; font-weight: bold; color: {config_uni['color_primario']}; margin: 15px 0;">
                    {metrica_label}: {valor_mostrar}
                </p>
                {'<p style="font-size: 18px; color: #7f8c8d; margin-bottom: 20px;">' + letra + ' - ' + descripcion + '</p>' if 'letra' in locals() else ''}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Métricas adicionales específicas por universidad
        st.markdown("<br>", unsafe_allow_html=True)
        
        if universidad_seleccionada == "UNPHU":
            col_m1, col_m2, col_m3 = st.columns(3)
            with col_m1:
                st.metric("📊 Promedio Parciales", f"{(parcial1 + parcial2) / 2:.2f}")
            with col_m2:
                st.metric("📝 Trabajos Prácticos", f"{trabajos_practicos:.2f}")
            with col_m3:
                st.metric("🏆 Examen Final", f"{examen_final:.2f}")
                
        elif universidad_seleccionada == "UTESA":
            col_m1, col_m2, col_m3 = st.columns(3)
            with col_m1:
                st.metric("📋 Parcial 1", f"{parcial1:.0f}/30")
            with col_m2:
                st.metric("📋 Parcial 2", f"{parcial2:.0f}/30")
            with col_m3:
                st.metric("📋 Parcial 3", f"{parcial3:.0f}/40")
                
        elif universidad_seleccionada in ["UNIBE", "PUCMM"]:
            st.metric("📚 Total de Créditos", f"{total_creditos}")
            st.markdown("**Desglose por materia:**")
            for i, materia in enumerate(materias_data):
                if materia['nota'] > 0:
                    gpa_materia, letra_materia = obtener_gpa_unibe_pucmm(materia['nota'])
                    st.write(f"Materia {i+1}: {materia['nota']:.1f} ({letra_materia}) - {materia['creditos']} créditos - GPA: {gpa_materia:.1f}")

# Información adicional específica de la universidad
st.markdown("---")
st.markdown(f"### ℹ️ Sistema de {universidad_seleccionada}")
st.markdown(f"**{config_uni['descripcion']}**")

if universidad_seleccionada == "UNPHU":
    st.markdown("""
    - **A (90-100)**: Excelente 🌟
    - **B (80-89)**: Bueno 👍  
    - **C (70-79)**: Regular ⚠️
    - **F (0-69)**: Reprobado ❌
    - **Mínimo para aprobar**: 70 puntos
    """)
elif universidad_seleccionada == "UTESA":
    st.markdown("""
    - **A (90-100)**: Excelente 🌟
    - **B (80-89)**: Bueno 👍
    - **C (70-79)**: Regular ⚠️  
    - **D/F (<70)**: Reprobado ❌
    - **Sistema**: 3 parciales (30+30+40 puntos)
    """)
elif universidad_seleccionada in ["UNIBE", "PUCMM"]:
    st.markdown("""
    - **A = 4.0** (90-100): Excelente 🌟
    - **B = 3.0** (80-89): Bueno 👍
    - **C = 2.0** (70-79): Regular ⚠️
    - **D = 1.0** (60-69): Deficiente 📉
    - **F = 0.0** (<60): Reprobado ❌
    - **Mínimo para aprobar**: 2.0 GPA
    """)
elif universidad_seleccionada == "UCE":
    st.markdown("""
    - **A = 4.0** (90-100): Excelente 🌟
    - **B+ = 3.5** (85-89): Muy bueno ⭐
    - **B = 3.0** (80-84): Bueno 👍
    - **C+ = 2.5** (75-79): Regular+ 📈
    - **C = 2.0** (70-74): Regular ⚠️
    - **D = 1.0** (60-69): Deficiente 📉
    - **F = 0.0** (<60): Reprobado ❌
    """)
elif universidad_seleccionada == "ISFODOSU":
    st.markdown("""
    - **A = 4** (90-100): Excelente 🌟
    - **B = 3** (80-89): Bueno 👍
    - **C = 2** (70-79): Regular ⚠️
    - **Mínimo para aprobar**: 70 puntos
    """)
elif universidad_seleccionada == "UASD":
    st.markdown("""
    - **≥70**: Condición normal ✅
    - **60-69**: Prevención académica ⚠️
    - **<60**: Situación crítica ❌
    - **Nota**: Promedio ponderado del semestre
    """)

# Footer
st.markdown("---")
st.markdown(
    f"<p style='text-align: center; color: {config_uni['color_primario']}; font-size: 12px;'>🎓 Calculadora de Notas - Universidades de República Dominicana</p>",
    unsafe_allow_html=True
)

# Add author attribution and GitHub link
st.sidebar.markdown("---")
st.sidebar.markdown("### 👨‍💻 Autor")
st.sidebar.markdown("**Jose Mencia**")
st.sidebar.markdown("*Estudiante de Ing En Sistemas*")
st.sidebar.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Josemcboss)")
st.sidebar.markdown("---")
st.sidebar.markdown("### 🇩🇴 Universidades Incluidas")
for uni_key, uni_data in UNIVERSIDADES.items():
    st.sidebar.markdown(f"• **{uni_key}** - {uni_data['nombre'][:25]}...")
=======
import streamlit as st

def obtener_letra_calificacion(nota):
    """Determina la letra de calificación basada en la nota"""
    if nota >= 90:
        return "A", "Excelente (90-100)", "#27ae60"  # Verde
    elif nota >= 80:
        return "B", "Bueno (80-89)", "#f39c12"  # Naranja
    elif nota >= 70:
        return "C", "Regular (70-79)", "#e67e22"  # Naranja oscuro
    else:
        return "F", "Reprobado (0-69)", "#e74c3c"  # Rojo

# Configuración de la página
st.set_page_config(
    page_title="Calculadora de Notas",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Título principal
st.title("📚 Calculadora de Notas Universitarias")
st.markdown("---")
st.write("Ingresa tus notas para calcular tu promedio final y ver si aprobaste.")

# CSS personalizado para mejorar la apariencia
st.markdown("""
<style>
    .stNumberInput > label {
        font-weight: bold;
        color: #34495e;
    }
    .main-header {
        text-align: center;
        color: #2c3e50;
        margin-bottom: 2rem;
    }
    .result-container {
        background-color: #ecf0f1;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #bdc3c7;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Crear columnas para organizar los campos de entrada
col1, col2 = st.columns(2)

with col1:
    primer_examen = st.number_input(
        "🎯 Primer Examen (0-100):",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.01,
        format="%.2f",
        help="Ingresa tu nota del primer examen"
    )
    
    nota_practica = st.number_input(
        "📝 Nota Práctica (0-100):",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.01,
        format="%.2f",
        help="Ingresa tu nota de prácticas"
    )

with col2:
    segundo_examen = st.number_input(
        "🎯 Segundo Examen (0-100):",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.01,
        format="%.2f",
        help="Ingresa tu nota del segundo examen"
    )
    
    examen_final = st.number_input(
        "🏆 Examen Final (0-100):",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.01,
        format="%.2f",
        help="Ingresa tu nota del examen final"
    )

# Espaciado
st.markdown("<br>", unsafe_allow_html=True)

# Botón para calcular (centrado)
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    calcular = st.button("🧮 Calcular Promedio", use_container_width=True)

# Lógica de cálculo
if calcular:
    # Validar que al menos una nota sea mayor que 0
    if all(nota == 0 for nota in [primer_examen, segundo_examen, nota_practica, examen_final]):
        st.warning("⚠️ Por favor, ingresa al menos una nota mayor que 0.")
    else:
        # Cálculo según la fórmula especificada:
        # 1. Promedio de primer y segundo examen
        promedio_examenes = (primer_examen + segundo_examen) / 2
        
        # 2. Promedio final: (promedio_examenes + nota_practica + examen_final) / 3
        nota_final = (promedio_examenes + nota_practica + examen_final) / 3
        
        # Determinar letra de calificación
        letra, descripcion, color = obtener_letra_calificacion(nota_final)

        # Mostrar resultado
        st.markdown("---")
        st.subheader("📊 Resultado Detallado")        # Contenedor del resultado con estilo personalizado
        st.markdown(f"""
        <div class="result-container">
            <div style="text-align: center;">
                <p style="font-size: 32px; font-weight: bold; color: {color}; margin: 20px 0;">
                    {'🎉 ¡Pasaste!' if letra != 'F' else '🔥 ¡Te quemaste!'} 
                </p>
                <p style="font-size: 28px; font-weight: bold; color: {color}; margin: 15px 0;">
                    Calificación: {letra}
                </p>
                <p style="font-size: 18px; color: #7f8c8d; margin-bottom: 20px;">
                    {descripcion}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Mostrar métricas adicionales en columnas
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_m1, col_m2, col_m3 = st.columns(3)
        
        with col_m1:
            st.metric(
                label="📊 Promedio Exámenes",
                value=f"{promedio_examenes:.2f}",
                delta=None
            )
        
        with col_m2:
            st.metric(
                label="🎯 Nota Final",
                value=f"{nota_final:.2f}",
                delta=None
            )
        
        with col_m3:
            st.metric(
                label="📋 Calificación",
                value=letra,
                delta=None
            )

# Información adicional
st.markdown("---")
st.markdown("""
### ℹ️ Información del Sistema de Calificación

- **A (90-100)**: Excelente 🌟
- **B (80-89)**: Bueno 👍
- **C (70-79)**: Regular ⚠️
- **F (0-69)**: Reprobado ❌

### 📐 Fórmula de Cálculo
1. **Promedio de Exámenes**: (Primer Examen + Segundo Examen) / 2
2. **Nota Final**: (Promedio de Exámenes + Nota Práctica + Examen Final) / 3
""")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #7f8c8d; font-size: 12px;'>📚 Calculadora de Notas Universitarias - Desarrollado con Streamlit</p>",
    unsafe_allow_html=True
)

# Add author attribution and GitHub link
st.sidebar.markdown("### Autor")
st.sidebar.markdown("Jose Mencia, Estudiante de Ing En Sistemas")
st.sidebar.markdown("[GitHub](https://github.com/Josemcboss)")
>>>>>>> 3678911547c0ccadb56bab03fdae2a0e02f5d37a
