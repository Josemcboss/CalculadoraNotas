# Copyright (c) 2024 Jose Mencia
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

"""
Configuration file for Dominican universities data and settings.
"""

from typing import Dict, Any

# University configuration data
UNIVERSIDADES: Dict[str, Dict[str, Any]] = {
    "UNPHU": {
        "nombre": "Universidad Nacional Pedro Henríquez Ureña",
        "color_primario": "#007A33",  # Verde
        "color_secundario": "#FFFFFF",  # Blanco
        "sistema": "Escala 0-100",
        "minimo_aprobar": 70,
        "descripcion": "Nota final = (Trabajos Prácticos + ((Parcial1 + Parcial2)/2) + Examen Final) / 3"
    },
    "UNIBE": {
        "nombre": "Universidad Iberoamericana",
        "color_primario": "#004A99",  # Azul
        "color_secundario": "#FFFFFF",  # Blanco
        "sistema": "Índice Académico (0.00-4.00)",
        "minimo_aprobar": 2.0,
        "descripcion": "Índice = Sumatoria (Créditos x Valor de Calificación) / Total de Créditos"
    },
    "UTESA": {
        "nombre": "Universidad Tecnológica de Santiago",
        "color_primario": "#008A3D",  # Verde
        "color_secundario": "#FFD700",  # Amarillo
        "sistema": "Sistema de evaluación por parciales",
        "minimo_aprobar": 70,
        "descripcion": "Tres parciales de 30 puntos cada uno. Nota final: Parcial1 + Parcial2 + Parcial3"
    },
    "ISFODOSU": {
        "nombre": "Instituto Superior de Formación Docente Salomé Ureña",
        "color_primario": "#005EB8",  # Azul institucional
        "color_secundario": "#FFFFFF",  # Blanco
        "sistema": "Escala 0-100 convertida a GPA 0-4",
        "minimo_aprobar": 70,
        "descripcion": "A=4 (90-100), B=3 (80-89), C=2 (70-79)"
    },
    "UCE": {
        "nombre": "Universidad Central del Este",
        "color_primario": "#D4002D",  # Rojo Escarlata
        "color_secundario": "#0047AB",  # Azul Cobalto
        "sistema": "Escala 0-100 con conversión a GPA 0-4",
        "minimo_aprobar": 70,
        "descripcion": "A=4.0 (90-100), B+=3.5 (85-89), B=3.0 (80-84), C+=2.5 (75-79)"
    },
    "UASD": {
        "nombre": "Universidad Autónoma de Santo Domingo",
        "color_primario": "#002D62",  # Azul Añil
        "color_secundario": "#FFFFFF",  # Blanco
        "sistema": "Índice Académico basado en escala 0-100",
        "minimo_aprobar": 70,
        "descripcion": ">=70: condición normal, 60-69: prevención académica, <60: situación crítica"
    },
    "PUCMM": {
        "nombre": "Pontificia Universidad Católica Madre y Maestra",
        "color_primario": "#0038A8",  # Azul Pantone 286 C
        "color_secundario": "#FFDA00",  # Amarillo Pantone Yellow 012 C
        "sistema": "Índice Académico Acumulado (escala 0-4)",
        "minimo_aprobar": 2.0,
        "descripcion": "Índice = Sumatoria (Créditos x GPA) / Total de Créditos"
    }
}

# Grade scale configurations
GRADE_SCALES = {
    "universal": {
        "A": {"min": 90, "max": 100, "description": "Excelente", "color": "#27ae60"},
        "B": {"min": 80, "max": 89, "description": "Bueno", "color": "#f39c12"},
        "C": {"min": 70, "max": 79, "description": "Regular", "color": "#e67e22"},
        "F": {"min": 0, "max": 69, "description": "Reprobado", "color": "#e74c3c"}
    }
}

# Application settings
APP_CONFIG = {
    "title": "Calculadora de Notas - Universidades RD",
    "icon": "🎓",
    "version": "1.0.0",
    "author": "Jose Mencia",
    "github_url": "https://github.com/Josemcboss"
}