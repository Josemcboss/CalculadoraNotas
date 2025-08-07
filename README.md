# 📚 Calculadora de Notas Universitarias

Una aplicación completa para calcular promedios de notas universitarias con soporte para múltiples universidades dominicanas.

## 🎯 Características

- **Dos Interfaces Disponibles**:
  - 🖥️ **Aplicación de Escritorio** (tkinter) - Interfaz clásica para cálculo básico
  - 🌐 **Aplicación Web** (Streamlit) - Interfaz moderna con soporte para 7 universidades

- **Soporte Universitario Completo**:
  - UNPHU, UNIBE, UTESA, ISFODOSU, UCE, UASD, PUCMM
  - Sistemas de calificación específicos por universidad
  - Colores y branding institucional

- **Funcionalidades Avanzadas**:
  - ✅ Validación completa de datos de entrada
  - 📊 Cálculos precisos según fórmulas universitarias
  - 📥 Exportación de resultados (JSON/CSV)
  - 🎨 Interfaz visual con identificación por colores
  - 🧪 Suite completa de pruebas

## 🚀 Instalación y Uso

### Opción 1: Aplicación Web (Recomendado)

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación web
streamlit run app.py
```

### Opción 2: Aplicación de Escritorio

```bash
# Ejecutar aplicación tkinter (requiere GUI)
python calculadora_notas.py
```

### Opción 3: Usando Makefile

```bash
make install     # Instalar dependencias
make run-streamlit  # Ejecutar app web
make run-tkinter    # Ejecutar app escritorio
make test           # Ejecutar pruebas
```

## 📊 Sistemas de Calificación Soportados

### UNPHU - Universidad Nacional Pedro Henríquez Ureña
- **Fórmula**: `(Trabajos Prácticos + ((Parcial1 + Parcial2)/2) + Examen Final) / 3`
- **Escala**: 0-100 puntos
- **Mínimo**: 70 puntos para aprobar

### UNIBE & PUCMM - Sistemas de GPA
- **Índice Académico**: 0.00-4.00
- **Ponderación**: Por créditos de materia
- **Mínimo**: 2.0 GPA para aprobar

### UTESA - Sistema de Parciales
- **Estructura**: 3 parciales (30+30+40 puntos)
- **Total**: 100 puntos máximo
- **Mínimo**: 70 puntos para aprobar

### UCE - Sistema GPA Extendido
- **Conversión**: Escala 0-100 a GPA 0-4.0
- **Graduaciones**: A, B+, B, C+, C, D, F
- **Mínimo**: 70 puntos (2.0 GPA) para aprobar

### ISFODOSU & UASD - Sistema Tradicional
- **Fórmula**: `((Examen1 + Examen2)/2 + Práctica + Final) / 3`
- **Clasificación**: A (90-100), B (80-89), C (70-79), F (0-69)
- **Mínimo**: 70 puntos para aprobar

## 🔧 Para Desarrolladores

Ver [DEVELOPER.md](DEVELOPER.md) para:
- Configuración del entorno de desarrollo
- Arquitectura del proyecto
- Estándares de código
- Guías de contribución
- Agregar nuevas universidades

### Estructura del Proyecto

```
├── app.py                 # Aplicación web Streamlit
├── calculadora_notas.py   # Aplicación de escritorio tkinter
├── config.py             # Configuración de universidades  
├── utils.py              # Funciones de utilidad
├── export_utils.py       # Funciones de exportación
├── test_utils.py         # Suite de pruebas
├── requirements.txt      # Dependencias principales
├── requirements-dev.txt  # Dependencias de desarrollo
└── DEVELOPER.md          # Guía de desarrollo
```

### Ejecutar Pruebas

```bash
# Ejecutar suite de pruebas
python -m unittest test_utils.py -v

# O usando make
make test
```

## 📥 Funcionalidades de Exportación

La aplicación web permite exportar los resultados de cálculo en dos formatos:

- **📄 JSON**: Formato estructurado con metadatos completos
- **📊 CSV**: Formato tabular para análisis en Excel/Google Sheets

Los archivos incluyen:
- Timestamp del cálculo
- Datos de entrada
- Resultados calculados
- Información de la universidad

## 🎓 Ejemplos de Uso

### Ejemplo UNPHU
- Trabajos Prácticos: 85
- Primer Parcial: 80
- Segundo Parcial: 90
- Examen Final: 88
- **Resultado**: 85.83 (B - Bueno)

### Ejemplo UNIBE (Múltiples Materias)
- Materia 1: 90 puntos, 3 créditos → GPA 4.0
- Materia 2: 85 puntos, 4 créditos → GPA 3.0  
- Materia 3: 95 puntos, 2 créditos → GPA 4.0
- **Resultado**: 3.56 GPA (Aprobado)

## 📋 Requisitos Técnicos

- **Python**: 3.8 o superior
- **Aplicación Web**: Streamlit 1.28.0+
- **Aplicación Escritorio**: tkinter (incluido en Python)

### Dependencias Principales
- streamlit>=1.28.0

### Dependencias de Desarrollo  
- pytest>=7.0.0
- black>=22.0.0
- flake8>=5.0.0
- mypy>=1.0.0
- reportlab>=4.0.0

## 🤝 Contribuir

1. Fork este repositorio
2. Crea una rama para tu funcionalidad: `git checkout -b feature/nueva-funcionalidad`
3. Agrega pruebas para nueva funcionalidad
4. Ejecuta las pruebas: `make test`
5. Formatea el código: `make format`  
6. Haz commit de tus cambios
7. Crea un Pull Request

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Jose Mencia** - Estudiante de Ingeniería en Sistemas

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Josemcboss)

---

¡Buena suerte con tus estudios! 🎓 ¡Espero que esta calculadora te sea útil!
