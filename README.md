# 📚 Calculadora de Notas Universitarias

Una aplicación completa con dos interfaces para calcular el promedio de notas universitarias y determinar la calificación final, con soporte especializado para universidades dominicanas.

## 🚀 Nuevas Características v2.0

### 🖥️ Aplicación de Escritorio (tkinter)
- **Interfaz gráfica intuitiva** renovada y moderna
- **🎯 Predictor inteligente** - Calcula qué nota necesitas en el examen final para aprobar
- **💾 Historial de calificaciones** - Guarda y consulta tus notas anteriores
- **📊 Exportación de datos** - Exporta tu historial a CSV
- **🎨 Menú completo** - Herramientas adicionales y opciones
- **✅ Validación mejorada** - Mejor manejo de errores

### 🌐 Aplicación Web (Streamlit)
- **🏛️ 7 Universidades dominicanas** - UNPHU, UNIBE, UTESA, ISFODOSU, UCE, UASD, PUCMM
- **📊 Calculadora de GPA Semestral** - Calcula el GPA de todo tu semestre
- **🎨 Colores institucionales** - Cada universidad con su identidad visual
- **⚖️ Sistemas de calificación específicos** - Adaptado a cada universidad
- **📈 Modo dual** - Individual por materia o GPA completo

## 🎯 Características Originales

- **Cálculo automático** del promedio según la fórmula universitaria
- **Validación de datos** para asegurar notas válidas (0-100)
- **Clasificación por letras** (A, B, C, F)
- **Colores visuales** para identificar rápidamente el resultado

## 📊 Fórmula de Cálculo

1. **Promedio de Exámenes**: `(Primer Examen + Segundo Examen) / 2`
2. **Nota Final**: `(Promedio de Exámenes + Nota Práctica + Examen Final) / 3`

## 🎨 Sistema de Calificaciones

- **A (90-100)**: Excelente 🌟
- **B (80-89)**: Bueno 👍
- **C (70-79)**: Regular ⚠️
- **F (0-69)**: Reprobado ❌

## 🚀 Cómo usar

### Aplicación de Escritorio
1. Ejecuta el programa: `python calculadora_notas.py`
2. Ingresa las 4 notas requeridas (valores entre 0 y 100)
3. Haz clic en "🧮 Calcular Promedio"
4. **NUEVO:** Usa "🎯 ¿Qué necesito para aprobar?" para planificar tu estudio
5. **NUEVO:** Guarda tu resultado en el historial
6. **NUEVO:** Consulta tu historial y exporta a CSV

### Aplicación Web
1. Ejecuta: `streamlit run app.py`
2. Selecciona tu universidad dominicana
3. Elige el modo: Individual o GPA Semestral
4. Ingresa tus notas según el sistema de tu universidad
5. Ve tu resultado con colores institucionales

## 📋 Requisitos

### Desktop
- Python 3.x
- tkinter (incluido por defecto en Python)

### Web
- Python 3.x
- streamlit (ver `requirements.txt`)

## 🏛️ Universidades Soportadas

### 🎓 Con sistemas específicos implementados:
- **UNPHU** - Universidad Nacional Pedro Henríquez Ureña
- **UNIBE** - Universidad Iberoamericana  
- **UTESA** - Universidad Tecnológica de Santiago
- **ISFODOSU** - Instituto Superior de Formación Docente Salomé Ureña
- **UCE** - Universidad Central del Este
- **UASD** - Universidad Autónoma de Santo Domingo
- **PUCMM** - Pontificia Universidad Católica Madre y Maestra

## 💡 Funcionalidades Avanzadas

### Desktop App
- ✅ **Predictor de notas** - Planifica qué necesitas para aprobar
- ✅ **Historial persistente** - Nunca pierdas el registro de tus notas
- ✅ **Exportación CSV** - Lleva tus datos a Excel o Google Sheets
- ✅ **Validación completa** - Mensajes de error informativos
- ✅ **Interfaz moderna** - Diseño actualizado y profesional
- ✅ **Múltiples ventanas** - Herramientas en ventanas separadas

### Web App  
- ✅ **Multi-universidad** - 7 universidades con sus sistemas específicos
- ✅ **GPA Semestral** - Calcula tu índice académico completo
- ✅ **Colores institucionales** - Cada uni con su identidad visual
- ✅ **Responsive** - Funciona en móviles y escritorio
- ✅ **Cálculos específicos** - Adaptado a cada sistema universitario
- ✅ **Desglose detallado** - Ve el rendimiento por materia

## 🛠️ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/Josemcboss/CalculadoraNotas.git

# Instalar dependencias para la app web
pip install -r requirements.txt

# Ejecutar aplicación de escritorio
python calculadora_notas.py

# Ejecutar aplicación web
streamlit run app.py
```

## 👨‍💻 Autor

**Jose Mencia**  
*Estudiante de Ingeniería en Sistemas*  
🇩🇴 República Dominicana

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Josemcboss)

## 📄 Licencia

MIT License - ve el archivo [LICENSE](LICENSE) para más detalles.

---

¡Buena suerte con tus estudios! 🎓🌟
