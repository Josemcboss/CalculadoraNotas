# 🚀 Guía de Desarrollo - CalculadoraNotas

## 📁 Estructura del Proyecto

```
CalculadoraNotas/
├── app.py                  # Aplicación web Streamlit
├── calculadora_notas.py    # Aplicación de escritorio tkinter  
├── config.py              # Configuración de universidades
├── utils.py               # Funciones de utilidad
├── export_utils.py        # Funciones de exportación
├── test_utils.py          # Suite de pruebas
├── requirements.txt       # Dependencias principales
├── requirements-dev.txt   # Dependencias de desarrollo
├── setup.cfg             # Configuración de linting
├── Makefile              # Comandos de desarrollo
└── README.md             # Documentación principal
```

## 🛠️ Configuración del Entorno de Desarrollo

### 1. Instalación de Dependencias

```bash
# Instalar dependencias principales
pip install -r requirements.txt

# Instalar dependencias de desarrollo
pip install -r requirements-dev.txt
```

### 2. Usando el Makefile

```bash
# Ver comandos disponibles
make help

# Instalar dependencias
make install

# Ejecutar pruebas
make test

# Formatear código
make format

# Verificar linting
make lint

# Ejecutar aplicación tkinter
make run-tkinter

# Ejecutar aplicación Streamlit
make run-streamlit
```

## 🧪 Ejecutar Pruebas

```bash
# Ejecutar todas las pruebas
python -m unittest test_utils.py -v

# O usando make
make test
```

## 📊 Arquitectura de la Aplicación

### Módulos Principales

1. **config.py**: Configuración centralizada
   - Datos de universidades dominicanas
   - Escalas de calificación
   - Configuración de la aplicación

2. **utils.py**: Funciones de utilidad
   - Cálculos de notas por universidad
   - Conversiones de GPA
   - Validaciones
   - Formateo

3. **export_utils.py**: Funcionalidad de exportación
   - Generación de reportes JSON
   - Generación de reportes CSV
   - Creación de nombres de archivo únicos

4. **app.py**: Aplicación web Streamlit
   - Interfaz web moderna
   - Soporte para 7 universidades
   - Funcionalidad de exportación

5. **calculadora_notas.py**: Aplicación de escritorio
   - Interfaz gráfica tkinter
   - Cálculo de notas tradicional

## 🎯 Agregar Nueva Universidad

Para agregar una nueva universidad:

1. **Actualizar config.py**:
```python
UNIVERSIDADES["NUEVA_UNI"] = {
    "nombre": "Nombre Completo de la Universidad",
    "color_primario": "#HEXCOLOR",
    "color_secundario": "#HEXCOLOR", 
    "sistema": "Descripción del sistema",
    "minimo_aprobar": 70,
    "descripcion": "Fórmula de cálculo"
}
```

2. **Agregar función de cálculo en utils.py** (si necesario):
```python
def calcular_nota_nueva_uni(param1, param2, param3):
    # Lógica de cálculo específica
    return nota_final
```

3. **Actualizar app.py** para incluir la nueva universidad en la lógica de cálculo

4. **Agregar pruebas en test_utils.py**

## 🔧 Estándares de Código

### Linting
- **flake8**: Verificación de estilo PEP8
- **mypy**: Verificación de tipos (opcional)

### Formateo
- **black**: Formateo automático de código

### Estructura de Funciones
```python
def nombre_funcion(param: tipo) -> tipo_retorno:
    """
    Descripción clara de la función
    
    Args:
        param: Descripción del parámetro
        
    Returns:
        Descripción del valor de retorno
    """
    # Implementación
    return resultado
```

## 📈 Mejoras Futuras

### Funcionalidades Pendientes
- [ ] Histórico de cálculos
- [ ] Predicción de notas requeridas
- [ ] Análisis estadístico
- [ ] Modo oscuro
- [ ] Internacionalización
- [ ] API REST
- [ ] Base de datos para persistencia
- [ ] Autenticación de usuarios

### Mejoras Técnicas
- [ ] CI/CD pipeline
- [ ] Docker containerization
- [ ] Monitoring y logging
- [ ] Performance optimization
- [ ] Accessibility improvements
- [ ] Mobile-first responsive design

## 🐛 Reportar Problemas

1. Verificar que el problema no exista ya
2. Incluir pasos para reproducir
3. Incluir información del entorno
4. Proporcionar logs de error si aplica

## 🤝 Contribuir

1. Fork del repositorio
2. Crear rama para la funcionalidad: `git checkout -b feature/nueva-funcionalidad`
3. Agregar pruebas para nueva funcionalidad
4. Ejecutar pruebas: `make test`
5. Formatear código: `make format`
6. Verificar linting: `make lint`
7. Commit y push
8. Crear Pull Request

## 📝 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver archivo LICENSE para más detalles.