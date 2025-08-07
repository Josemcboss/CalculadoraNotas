# Copyright (c) 2024 Jose Mencia
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

"""
Export functionality for saving calculation results.
"""

import json
import csv
from datetime import datetime
from typing import Dict, Any, Optional
from io import StringIO

def generar_reporte_json(universidad: str, datos_entrada: Dict[str, Any], 
                        resultado: Dict[str, Any]) -> str:
    """
    Genera un reporte en formato JSON con los datos del cálculo
    
    Args:
        universidad: Nombre de la universidad
        datos_entrada: Datos ingresados por el usuario
        resultado: Resultados calculados
        
    Returns:
        String en formato JSON
    """
    reporte = {
        "timestamp": datetime.now().isoformat(),
        "universidad": universidad,
        "datos_entrada": datos_entrada,
        "resultado": resultado,
        "version": "1.0.0"
    }
    
    return json.dumps(reporte, indent=2, ensure_ascii=False)

def generar_reporte_csv(universidad: str, datos_entrada: Dict[str, Any], 
                       resultado: Dict[str, Any]) -> str:
    """
    Genera un reporte en formato CSV con los datos del cálculo
    
    Args:
        universidad: Nombre de la universidad
        datos_entrada: Datos ingresados por el usuario  
        resultado: Resultados calculados
        
    Returns:
        String en formato CSV
    """
    output = StringIO()
    writer = csv.writer(output)
    
    # Escribir encabezado
    writer.writerow(["Campo", "Valor"])
    writer.writerow(["Fecha", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
    writer.writerow(["Universidad", universidad])
    
    # Escribir datos de entrada
    writer.writerow([])  # Línea vacía
    writer.writerow(["DATOS DE ENTRADA", ""])
    for key, value in datos_entrada.items():
        writer.writerow([key.title(), value])
    
    # Escribir resultados
    writer.writerow([])  # Línea vacía
    writer.writerow(["RESULTADOS", ""])
    for key, value in resultado.items():
        writer.writerow([key.title(), value])
    
    return output.getvalue()

def generar_nombre_archivo(universidad: str, formato: str = "json") -> str:
    """
    Genera un nombre de archivo único para el reporte
    
    Args:
        universidad: Código de la universidad
        formato: Formato del archivo ('json' o 'csv')
        
    Returns:
        Nombre del archivo
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"reporte_notas_{universidad}_{timestamp}.{formato}"

def crear_resumen_resultado(nota_final: float, aprobado: bool, 
                          universidad: str, sistema: str) -> Dict[str, Any]:
    """
    Crea un diccionario con el resumen del resultado
    
    Args:
        nota_final: La nota final calculada
        aprobado: Si el estudiante aprobó o no
        universidad: Código de la universidad
        sistema: Sistema de calificación usado
        
    Returns:
        Diccionario con el resumen
    """
    return {
        "nota_final": round(nota_final, 2),
        "estado": "APROBADO" if aprobado else "REPROBADO",
        "universidad": universidad,
        "sistema_calificacion": sistema,
        "fecha_calculo": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }