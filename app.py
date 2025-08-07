# Copyright (c) 2024 Jose Mencia
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

import streamlit as st
from typing import Dict, Any, List
from config import UNIVERSIDADES, APP_CONFIG
from utils import (
    obtener_letra_calificacion_universal,
    obtener_gpa_unibe_pucmm,
    obtener_gpa_uce,
    calcular_nota_unphu,
    calcular_nota_utesa,
    calcular_nota_tradicional,
    calcular_gpa_ponderado,
    formatear_nota,
    es_aprobado
)
from export_utils import (
    generar_reporte_json,
    generar_reporte_csv,
    generar_nombre_archivo,
    crear_resumen_resultado
)

# Configuración de la página
st.set_page_config(
    page_title=APP_CONFIG["title"],
    page_icon=APP_CONFIG["icon"],
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
            indice_academico, total_creditos = calcular_gpa_ponderado(materias_data)
            aprobado = es_aprobado(indice_academico, config_uni['minimo_aprobar'])
            nota_final = indice_academico
            color = "#27ae60" if aprobado else "#e74c3c"
            
    elif universidad_seleccionada == "UCE":
        if all(nota == 0 for nota in [primer_examen, segundo_examen, nota_practica, examen_final]):
            st.warning("⚠️ Por favor, ingresa al menos una nota mayor que 0.")
        else:
            nota_final = calcular_nota_tradicional(primer_examen, segundo_examen, nota_practica, examen_final)
            gpa, letra = obtener_gpa_uce(nota_final)
            aprobado = es_aprobado(nota_final, config_uni['minimo_aprobar'])
            color = "#27ae60" if aprobado else "#e74c3c"
            
    else:  # ISFODOSU, UASD
        if all(nota == 0 for nota in [primer_examen, segundo_examen, nota_practica, examen_final]):
            st.warning("⚠️ Por favor, ingresa al menos una nota mayor que 0.")
        else:
            nota_final = calcular_nota_tradicional(primer_examen, segundo_examen, nota_practica, examen_final)
            aprobado = es_aprobado(nota_final, config_uni['minimo_aprobar'])
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
        
        # Botones de exportación
        if 'nota_final' in locals() and nota_final > 0:
            st.markdown("### 📥 Exportar Resultados")
            col_export1, col_export2 = st.columns(2)
            
            # Preparar datos para exportar
            if universidad_seleccionada == "UNPHU":
                datos_entrada = {
                    "trabajos_practicos": trabajos_practicos,
                    "primer_parcial": parcial1, 
                    "segundo_parcial": parcial2,
                    "examen_final": examen_final
                }
            elif universidad_seleccionada == "UTESA":
                datos_entrada = {
                    "primer_parcial": parcial1,
                    "segundo_parcial": parcial2, 
                    "tercer_parcial": parcial3
                }
            elif universidad_seleccionada in ["UNIBE", "PUCMM"]:
                datos_entrada = {"materias": materias_data}
            else:
                datos_entrada = {
                    "primer_examen": primer_examen,
                    "segundo_examen": segundo_examen,
                    "nota_practica": nota_practica,
                    "examen_final": examen_final
                }
            
            resultado = crear_resumen_resultado(
                nota_final, aprobado, universidad_seleccionada, 
                config_uni['sistema']
            )
            
            with col_export1:
                json_data = generar_reporte_json(universidad_seleccionada, datos_entrada, resultado)
                st.download_button(
                    label="📄 Descargar JSON",
                    data=json_data,
                    file_name=generar_nombre_archivo(universidad_seleccionada, "json"),
                    mime="application/json",
                    use_container_width=True
                )
            
            with col_export2:
                csv_data = generar_reporte_csv(universidad_seleccionada, datos_entrada, resultado)
                st.download_button(
                    label="📊 Descargar CSV", 
                    data=csv_data,
                    file_name=generar_nombre_archivo(universidad_seleccionada, "csv"),
                    mime="text/csv",
                    use_container_width=True
                )

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
st.sidebar.markdown(f"**{APP_CONFIG['author']}**")
st.sidebar.markdown("*Estudiante de Ing En Sistemas*")
st.sidebar.markdown(f"[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)]({APP_CONFIG['github_url']})")
st.sidebar.markdown("---")
st.sidebar.markdown("### 🇩🇴 Universidades Incluidas")
for uni_key, uni_data in UNIVERSIDADES.items():
    st.sidebar.markdown(f"• **{uni_key}** - {uni_data['nombre'][:25]}...")