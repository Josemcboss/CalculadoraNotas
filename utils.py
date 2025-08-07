# Copyright (c) 2024 Jose Mencia
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

"""
Utility functions for grade calculations and validations.
"""

from typing import Tuple, Optional, List, Dict, Any
from config import GRADE_SCALES

def obtener_letra_calificacion_universal(nota: float) -> Tuple[str, str, str]:
    """
    Determina la letra de calificación basada en la nota (sistema universal)
    
    Args:
        nota: Nota numérica (0-100)
        
    Returns:
        Tupla con (letra, descripción, color)
    """
    if nota >= 90:
        return "A", "Excelente (90-100)", "#27ae60"
    elif nota >= 80:
        return "B", "Bueno (80-89)", "#f39c12"
    elif nota >= 70:
        return "C", "Regular (70-79)", "#e67e22"
    else:
        return "F", "Reprobado (0-69)", "#e74c3c"

def obtener_gpa_unibe_pucmm(nota: float) -> Tuple[float, str]:
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

def obtener_gpa_uce(nota: float) -> Tuple[float, str]:
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

def validar_nota(nota: float, min_val: float = 0.0, max_val: float = 100.0) -> bool:
    """
    Valida que una nota esté dentro del rango permitido
    
    Args:
        nota: La nota a validar
        min_val: Valor mínimo permitido
        max_val: Valor máximo permitido
        
    Returns:
        True si la nota es válida, False en caso contrario
    """
    return min_val <= nota <= max_val

def calcular_nota_unphu(trabajos: float, parcial1: float, parcial2: float, examen_final: float) -> float:
    """Calcula la nota final para UNPHU"""
    promedio_parciales = (parcial1 + parcial2) / 2
    return (trabajos + promedio_parciales + examen_final) / 3

def calcular_nota_utesa(parcial1: float, parcial2: float, parcial3: float) -> float:
    """Calcula la nota final para UTESA"""
    return parcial1 + parcial2 + parcial3

def calcular_nota_tradicional(primer_examen: float, segundo_examen: float, 
                            nota_practica: float, examen_final: float) -> float:
    """
    Calcula la nota final usando el sistema tradicional
    Formula: ((Examen1 + Examen2)/2 + Practica + Final)/3
    """
    promedio_examenes = (primer_examen + segundo_examen) / 2
    return (promedio_examenes + nota_practica + examen_final) / 3

def calcular_gpa_ponderado(materias_data: List[Dict[str, Any]]) -> Tuple[float, int]:
    """
    Calcula el GPA ponderado basado en créditos
    
    Args:
        materias_data: Lista de diccionarios con 'nota' y 'creditos'
        
    Returns:
        Tupla con (gpa_ponderado, total_creditos)
    """
    suma_ponderada = 0
    total_creditos = 0
    
    for materia in materias_data:
        if materia['nota'] > 0:
            gpa, _ = obtener_gpa_unibe_pucmm(materia['nota'])
            suma_ponderada += gpa * materia['creditos']
            total_creditos += materia['creditos']
    
    if total_creditos == 0:
        return 0.0, 0
    
    return suma_ponderada / total_creditos, total_creditos

def formatear_nota(nota: float, decimales: int = 2) -> str:
    """Formatea una nota con el número especificado de decimales"""
    return f"{nota:.{decimales}f}"

def es_aprobado(nota: float, minimo: float) -> bool:
    """Determina si una nota es aprobatoria"""
    return nota >= minimo

def predecir_nota_requerida_final(nota_parcial1: float, nota_parcial2: float, 
                                  nota_practica: float, nota_objetivo: float) -> float:
    """
    Calcula la nota requerida en el examen final para alcanzar una nota objetivo
    usando el sistema tradicional: ((P1 + P2)/2 + Practica + Final)/3 = Objetivo
    
    Args:
        nota_parcial1: Nota del primer parcial
        nota_parcial2: Nota del segundo parcial
        nota_practica: Nota de práctica
        nota_objetivo: Nota final objetivo
        
    Returns:
        Nota requerida en el examen final
    """
    promedio_parciales = (nota_parcial1 + nota_parcial2) / 2
    # ((P1 + P2)/2 + Practica + Final)/3 = Objetivo
    # Final = 3 * Objetivo - ((P1 + P2)/2 + Practica)
    nota_final_requerida = 3 * nota_objetivo - (promedio_parciales + nota_practica)
    return nota_final_requerida

def generar_escenarios_prediccion(nota_parcial1: float, nota_parcial2: float, 
                                  nota_practica: float) -> Dict[str, float]:
    """
    Genera escenarios de predicción para diferentes objetivos de nota
    
    Args:
        nota_parcial1: Nota del primer parcial
        nota_parcial2: Nota del segundo parcial  
        nota_practica: Nota de práctica
        
    Returns:
        Diccionario con escenarios {objetivo: nota_requerida_final}
    """
    objetivos = [70, 75, 80, 85, 90, 95]
    escenarios = {}
    
    for objetivo in objetivos:
        nota_requerida = predecir_nota_requerida_final(
            nota_parcial1, nota_parcial2, nota_practica, objetivo
        )
        escenarios[f"Para obtener {objetivo}"] = round(nota_requerida, 2)
    
    return escenarios