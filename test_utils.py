# Copyright (c) 2024 Jose Mencia
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

"""
Test suite for the calculadora de notas project.
"""

import unittest
from utils import (
    obtener_letra_calificacion_universal,
    obtener_gpa_unibe_pucmm,
    obtener_gpa_uce,
    validar_nota,
    calcular_nota_unphu,
    calcular_nota_utesa,
    calcular_nota_tradicional,
    calcular_gpa_ponderado,
    formatear_nota,
    es_aprobado,
    predecir_nota_requerida_final,
    generar_escenarios_prediccion
)

class TestUtilsFunctions(unittest.TestCase):
    
    def test_obtener_letra_calificacion_universal(self):
        """Test grade letter assignment"""
        # Test grade A
        letra, desc, color = obtener_letra_calificacion_universal(95.0)
        self.assertEqual(letra, "A")
        self.assertIn("Excelente", desc)
        
        # Test grade B
        letra, desc, color = obtener_letra_calificacion_universal(85.0)
        self.assertEqual(letra, "B")
        self.assertIn("Bueno", desc)
        
        # Test grade C
        letra, desc, color = obtener_letra_calificacion_universal(75.0)
        self.assertEqual(letra, "C")
        self.assertIn("Regular", desc)
        
        # Test grade F
        letra, desc, color = obtener_letra_calificacion_universal(65.0)
        self.assertEqual(letra, "F")
        self.assertIn("Reprobado", desc)
        
        # Test boundary cases
        letra, _, _ = obtener_letra_calificacion_universal(90.0)
        self.assertEqual(letra, "A")
        
        letra, _, _ = obtener_letra_calificacion_universal(89.9)
        self.assertEqual(letra, "B")
    
    def test_obtener_gpa_unibe_pucmm(self):
        """Test GPA conversion for UNIBE and PUCMM"""
        gpa, letra = obtener_gpa_unibe_pucmm(95.0)
        self.assertEqual(gpa, 4.0)
        self.assertEqual(letra, "A")
        
        gpa, letra = obtener_gpa_unibe_pucmm(85.0)
        self.assertEqual(gpa, 3.0)
        self.assertEqual(letra, "B")
        
        gpa, letra = obtener_gpa_unibe_pucmm(75.0)
        self.assertEqual(gpa, 2.0)
        self.assertEqual(letra, "C")
        
        gpa, letra = obtener_gpa_unibe_pucmm(65.0)
        self.assertEqual(gpa, 1.0)
        self.assertEqual(letra, "D")
        
        gpa, letra = obtener_gpa_unibe_pucmm(55.0)
        self.assertEqual(gpa, 0.0)
        self.assertEqual(letra, "F")
    
    def test_obtener_gpa_uce(self):
        """Test GPA conversion for UCE"""
        gpa, letra = obtener_gpa_uce(95.0)
        self.assertEqual(gpa, 4.0)
        self.assertEqual(letra, "A")
        
        gpa, letra = obtener_gpa_uce(87.0)
        self.assertEqual(gpa, 3.5)
        self.assertEqual(letra, "B+")
        
        gpa, letra = obtener_gpa_uce(82.0)
        self.assertEqual(gpa, 3.0)
        self.assertEqual(letra, "B")
        
        gpa, letra = obtener_gpa_uce(77.0)
        self.assertEqual(gpa, 2.5)
        self.assertEqual(letra, "C+")
        
        gpa, letra = obtener_gpa_uce(72.0)
        self.assertEqual(gpa, 2.0)
        self.assertEqual(letra, "C")
    
    def test_validar_nota(self):
        """Test note validation"""
        self.assertTrue(validar_nota(85.0))
        self.assertTrue(validar_nota(0.0))
        self.assertTrue(validar_nota(100.0))
        self.assertFalse(validar_nota(-5.0))
        self.assertFalse(validar_nota(105.0))
        
        # Test custom range
        self.assertTrue(validar_nota(25.0, 0.0, 30.0))
        self.assertFalse(validar_nota(35.0, 0.0, 30.0))
    
    def test_calcular_nota_unphu(self):
        """Test UNPHU grade calculation"""
        nota = calcular_nota_unphu(80.0, 85.0, 90.0, 88.0)
        expected = (80.0 + (85.0 + 90.0) / 2 + 88.0) / 3
        self.assertAlmostEqual(nota, expected, places=2)
        
        # Test with perfect scores
        nota = calcular_nota_unphu(100.0, 100.0, 100.0, 100.0)
        self.assertEqual(nota, 100.0)
    
    def test_calcular_nota_utesa(self):
        """Test UTESA grade calculation"""
        nota = calcular_nota_utesa(25.0, 28.0, 35.0)
        expected = 25.0 + 28.0 + 35.0
        self.assertEqual(nota, expected)
        
        # Test maximum possible score
        nota = calcular_nota_utesa(30.0, 30.0, 40.0)
        self.assertEqual(nota, 100.0)
    
    def test_calcular_nota_tradicional(self):
        """Test traditional grade calculation"""
        nota = calcular_nota_tradicional(80.0, 85.0, 90.0, 88.0)
        promedio_examenes = (80.0 + 85.0) / 2
        expected = (promedio_examenes + 90.0 + 88.0) / 3
        self.assertAlmostEqual(nota, expected, places=2)
        
        # Test with equal scores
        nota = calcular_nota_tradicional(80.0, 80.0, 80.0, 80.0)
        self.assertEqual(nota, 80.0)
    
    def test_calcular_gpa_ponderado(self):
        """Test weighted GPA calculation"""
        materias_data = [
            {"nota": 90.0, "creditos": 3},
            {"nota": 85.0, "creditos": 4},
            {"nota": 95.0, "creditos": 2}
        ]
        
        gpa, total_creditos = calcular_gpa_ponderado(materias_data)
        
        # Manual calculation: ((4.0*3) + (3.0*4) + (4.0*2)) / 9 = 32/9 ≈ 3.56
        expected_gpa = (4.0*3 + 3.0*4 + 4.0*2) / 9
        expected_creditos = 9
        
        self.assertAlmostEqual(gpa, expected_gpa, places=2)
        self.assertEqual(total_creditos, expected_creditos)
        
        # Test with empty data
        gpa, creditos = calcular_gpa_ponderado([])
        self.assertEqual(gpa, 0.0)
        self.assertEqual(creditos, 0)
    
    def test_formatear_nota(self):
        """Test note formatting"""
        self.assertEqual(formatear_nota(85.666), "85.67")
        self.assertEqual(formatear_nota(85.666, 1), "85.7")
        self.assertEqual(formatear_nota(85.0, 0), "85")
        self.assertEqual(formatear_nota(85.123, 3), "85.123")
    
    def test_es_aprobado(self):
        """Test pass/fail determination"""
        self.assertTrue(es_aprobado(75.0, 70.0))
        self.assertTrue(es_aprobado(70.0, 70.0))  # Boundary case
        self.assertFalse(es_aprobado(69.9, 70.0))
        self.assertFalse(es_aprobado(65.0, 70.0))
    
    def test_predecir_nota_requerida_final(self):
        """Test grade prediction for final exam"""
        # Test scenario: need 80 final grade with P1=75, P2=85, Practice=80
        nota_requerida = predecir_nota_requerida_final(75.0, 85.0, 80.0, 80.0)
        # Expected: ((75+85)/2 + 80 + Final)/3 = 80 → Final = 80
        expected = 3 * 80 - ((75 + 85) / 2 + 80)  # 240 - (80 + 80) = 80
        self.assertAlmostEqual(nota_requerida, expected, places=2)
        
        # Test scenario: need 90 with low previous grades
        nota_requerida = predecir_nota_requerida_final(60.0, 70.0, 75.0, 90.0)
        expected = 3 * 90 - ((60 + 70) / 2 + 75)  # 270 - (65 + 75) = 130
        self.assertEqual(nota_requerida, expected)  # Would need impossible 130
    
    def test_generar_escenarios_prediccion(self):
        """Test prediction scenarios generation"""
        escenarios = generar_escenarios_prediccion(80.0, 85.0, 88.0)
        
        # Check that all expected objectives are present
        expected_objectives = ["Para obtener 70", "Para obtener 75", "Para obtener 80", 
                             "Para obtener 85", "Para obtener 90", "Para obtener 95"]
        
        for objective in expected_objectives:
            self.assertIn(objective, escenarios)
        
        # Test a specific calculation
        # For objetivo 80 with P1=80, P2=85, Practice=88
        # ((80+85)/2 + 88 + Final)/3 = 80 → Final = 240 - (82.5 + 88) = 69.5
        expected_final = round(3 * 80 - ((80 + 85) / 2 + 88), 2)
        self.assertEqual(escenarios["Para obtener 80"], expected_final)

class TestEdgeCases(unittest.TestCase):
    
    def test_extreme_values(self):
        """Test with extreme values"""
        # Test with 0 values
        nota = calcular_nota_tradicional(0.0, 0.0, 0.0, 0.0)
        self.assertEqual(nota, 0.0)
        
        # Test with maximum values
        nota = calcular_nota_tradicional(100.0, 100.0, 100.0, 100.0)
        self.assertEqual(nota, 100.0)
        
        # Test GPA with zero credits
        materias_data = [{"nota": 0.0, "creditos": 3}]
        gpa, creditos = calcular_gpa_ponderado(materias_data)
        self.assertEqual(gpa, 0.0)
        self.assertEqual(creditos, 0)

if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)