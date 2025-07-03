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
