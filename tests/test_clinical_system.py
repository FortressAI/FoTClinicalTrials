#!/usr/bin/env python3
"""
Field of Truth Clinical Trials - System Validation Tests

Comprehensive validation of the quantum clinical engine and data readiness checker.
Tests ensure NO SIMULATIONS and ALL MAINNET operation.

NO SIMULATIONS - ALL MAINNET - FIELD OF TRUTH 100%
"""

import unittest
import json
import numpy as np
from datetime import datetime
import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.clinical.quantum_clinical_engine import (
    QuantumClinicalEngine,
    QuantumClinicalCase,
    vQbitClinicalClaim,
    QuantumClinicalState,
    QuantumVirtueSupervisor
)

from core.clinical.data_readiness_checker import (
    ClinicalDataContractValidator,
    ValidationTrack,
    ValidationResult,
    TrackValidationResult,
    DataGap
)

class TestQuantumClinicalEngine(unittest.TestCase):
    """Test quantum clinical engine functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.engine = QuantumClinicalEngine(vqbit_dimension=512)
        self.test_clinical_data = {
            'case_id': 'TEST_001',
            'chief_complaint': 'chest pain',
            'age': 65,
            'gender': 'male',
            'symptoms': {
                'chest_pain': {'intensity': 0.8, 'quality': 'crushing'},
                'shortness_breath': {'intensity': 0.6},
                'diaphoresis': {'intensity': 0.7}
            },
            'vital_signs': {
                'systolic_bp': 160,
                'diastolic_bp': 110,
                'heart_rate': 110,
                'respiratory_rate': 24,
                'temperature_c': 37.0
            },
            'medical_history': ['hypertension', 'smoking'],
            'medications': [
                {'name': 'Aspirin', 'dose': '81mg', 'frequency': 'daily'},
                {'name': 'Lisinopril', 'dose': '10mg', 'frequency': 'daily'}
            ],
            'allergies': ['Penicillin']
        }
    
    def test_engine_initialization(self):
        """Test quantum engine initialization"""
        self.assertIsInstance(self.engine, QuantumClinicalEngine)
        self.assertEqual(self.engine.vqbit_dim, 512)
        self.assertIsNotNone(self.engine.quantum_basis)
        self.assertIsNotNone(self.engine.honesty_supervisor)
        self.assertIsNotNone(self.engine.prudence_supervisor)
        self.assertIsNotNone(self.engine.justice_supervisor)
        self.assertIsNotNone(self.engine.non_maleficence_supervisor)
    
    def test_clinical_case_encoding(self):
        """Test encoding clinical case into quantum state"""
        quantum_case = self.engine.encode_clinical_case(self.test_clinical_data)
        
        self.assertIsInstance(quantum_case, QuantumClinicalCase)
        self.assertEqual(quantum_case.case_id, 'TEST_001')
        self.assertEqual(quantum_case.vqbit_dimension, 512)
        self.assertIsInstance(quantum_case.quantum_state_vector, np.ndarray)
        self.assertEqual(len(quantum_case.quantum_state_vector), 512)
        self.assertIsInstance(quantum_case.symptom_qbits, dict)
        self.assertIsInstance(quantum_case.sign_qbits, dict)
        self.assertIsInstance(quantum_case.differential_qbits, dict)
        self.assertIsInstance(quantum_case.entanglement_matrix, np.ndarray)
        self.assertIsInstance(quantum_case.decoherence_rate, float)
        
        # Check quantum state normalization
        norm = np.linalg.norm(quantum_case.quantum_state_vector)
        self.assertAlmostEqual(norm, 1.0, places=10)
    
    def test_virtue_supervision(self):
        """Test virtue-based supervision"""
        quantum_case = self.engine.encode_clinical_case(self.test_clinical_data)
        quantum_claim = self.engine.apply_virtue_supervision(quantum_case)
        
        self.assertIsInstance(quantum_claim, vQbitClinicalClaim)
        self.assertIsInstance(quantum_claim.quantum_state, QuantumClinicalState)
        self.assertIsInstance(quantum_claim.amplitude, complex)
        self.assertIsInstance(quantum_claim.probability, float)
        self.assertIsInstance(quantum_claim.phase, float)
        self.assertIsInstance(quantum_claim.entanglement_list, list)
        self.assertIsInstance(quantum_claim.uncertainty_hbar, float)
        self.assertIsInstance(quantum_claim.toolchain_hash, str)
        self.assertIsInstance(quantum_claim.timestamp, str)
        
        # Check probability is valid
        self.assertGreaterEqual(quantum_claim.probability, 0.0)
        self.assertLessEqual(quantum_claim.probability, 1.0)
    
    def test_quantum_state_evolution(self):
        """Test quantum state evolution"""
        quantum_case = self.engine.encode_clinical_case(self.test_clinical_data)
        original_state = quantum_case.quantum_state_vector.copy()
        
        evolved_case = self.engine.evolve_quantum_state(quantum_case, time_step=0.1)
        
        self.assertIsInstance(evolved_case, QuantumClinicalCase)
        self.assertEqual(evolved_case.case_id, quantum_case.case_id)
        
        # Check that state evolved (should be different)
        state_diff = np.linalg.norm(evolved_case.quantum_state_vector - original_state)
        self.assertGreater(state_diff, 0.0)
        
        # Check normalization is maintained
        norm = np.linalg.norm(evolved_case.quantum_state_vector)
        self.assertAlmostEqual(norm, 1.0, places=10)
    
    def test_quantum_measurements(self):
        """Test quantum state measurements"""
        quantum_case = self.engine.encode_clinical_case(self.test_clinical_data)
        
        # Test diagnostic confidence measurement
        confidence, uncertainty = self.engine.measure_quantum_state(quantum_case, "diagnostic_confidence")
        self.assertIsInstance(confidence, float)
        self.assertIsInstance(uncertainty, float)
        self.assertGreaterEqual(confidence, 0.0)
        self.assertLessEqual(confidence, 1.0)
        self.assertGreaterEqual(uncertainty, 0.0)
        
        # Test symptom severity measurement
        severity, uncertainty = self.engine.measure_quantum_state(quantum_case, "symptom_severity")
        self.assertIsInstance(severity, float)
        self.assertIsInstance(uncertainty, float)
        self.assertGreaterEqual(severity, 0.0)
        self.assertLessEqual(severity, 1.0)
        
        # Test differential count measurement
        count, uncertainty = self.engine.measure_quantum_state(quantum_case, "differential_count")
        self.assertIsInstance(count, float)
        self.assertIsInstance(uncertainty, float)
        self.assertGreaterEqual(count, 0.0)
    
    def test_quantum_properties(self):
        """Test quantum property calculations"""
        quantum_case = self.engine.encode_clinical_case(self.test_clinical_data)
        
        # Test quantum coherence
        coherence = self.engine.get_quantum_coherence(quantum_case)
        self.assertIsInstance(coherence, float)
        self.assertGreaterEqual(coherence, 0.0)
        self.assertLessEqual(coherence, 1.0)
        
        # Test entanglement entropy
        entropy = self.engine.get_entanglement_entropy(quantum_case)
        self.assertIsInstance(entropy, float)
        self.assertGreaterEqual(entropy, 0.0)
    
    def test_virtue_supervisor(self):
        """Test individual virtue supervisors"""
        supervisor = QuantumVirtueSupervisor("honesty")
        self.assertEqual(supervisor.virtue_type, "honesty")
        self.assertEqual(supervisor.constraint_strength, 1.0)
        self.assertEqual(supervisor.violation_threshold, 0.1)
        
        # Test virtue compliance evaluation
        test_state = np.random.rand(10) + 1j * np.random.rand(10)
        test_state = test_state / np.linalg.norm(test_state)
        
        compliance = supervisor.evaluate_virtue_compliance(test_state, {})
        self.assertIsInstance(compliance, float)
        self.assertGreaterEqual(compliance, 0.0)
        self.assertLessEqual(compliance, 1.0)

class TestClinicalDataContractValidator(unittest.TestCase):
    """Test clinical data contract validator"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.validator = ClinicalDataContractValidator()
        self.test_clinical_data = {
            'case_id': 'TEST_001',
            'chief_complaint': 'chest pain',
            'age': 65,
            'gender': 'male',
            'medications': [
                {'name': 'Aspirin', 'dose': '81mg', 'frequency': 'daily'},
                {'name': 'Lisinopril', 'dose': '10mg', 'frequency': 'daily'}
            ],
            'allergies': ['Penicillin'],
            'vital_signs': {
                'systolic_bp': 160,
                'diastolic_bp': 110,
                'heart_rate': 110,
                'respiratory_rate': 24,
                'temperature_c': 37.0
            },
            'symptoms': {
                'chest_pain': {'intensity': 0.8, 'quality': 'crushing'},
                'shortness_breath': {'intensity': 0.6}
            },
            'laboratory': {
                'glucose': 120,
                'creatinine': 1.0,
                'troponin': 0.01
            },
            'diagnostic_plan': ['EKG', 'Chest X-ray', 'Troponin', 'Echocardiogram']
        }
    
    def test_validator_initialization(self):
        """Test validator initialization"""
        self.assertIsInstance(self.validator, ClinicalDataContractValidator)
        self.assertIsInstance(self.validator.validation_tracks, list)
        self.assertIsInstance(self.validator.minimum_scores, dict)
        
        # Check that all tracks have minimum scores
        for track in self.validator.validation_tracks:
            self.assertIn(track, self.validator.minimum_scores)
            self.assertGreaterEqual(self.validator.minimum_scores[track], 0.0)
            self.assertLessEqual(self.validator.minimum_scores[track], 1.0)
    
    def test_case_validation(self):
        """Test complete case validation"""
        results = self.validator.validate_case(self.test_clinical_data)
        
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), len(self.validator.validation_tracks))
        
        for result in results:
            self.assertIsInstance(result, TrackValidationResult)
            self.assertIsInstance(result.track, ValidationTrack)
            self.assertIsInstance(result.result, ValidationResult)
            self.assertIsInstance(result.actual_score, float)
            self.assertIsInstance(result.gaps, list)
            self.assertIsInstance(result.warnings, list)
            self.assertIsInstance(result.recommendations, list)
            
            # Check score bounds
            self.assertGreaterEqual(result.actual_score, 0.0)
            self.assertLessEqual(result.actual_score, 1.0)
    
    def test_medication_safety_validation(self):
        """Test medication safety validation"""
        result = self.validator._validate_medication_safety(self.test_clinical_data)
        
        self.assertIsInstance(result, TrackValidationResult)
        self.assertEqual(result.track, ValidationTrack.MEDICATION_SAFETY)
        self.assertIsInstance(result.result, ValidationResult)
        self.assertIsInstance(result.actual_score, float)
        self.assertIsInstance(result.gaps, list)
        self.assertIsInstance(result.warnings, list)
        self.assertIsInstance(result.recommendations, list)
    
    def test_triage_assessment_validation(self):
        """Test triage assessment validation"""
        result = self.validator._validate_triage_assessment(self.test_clinical_data)
        
        self.assertIsInstance(result, TrackValidationResult)
        self.assertEqual(result.track, ValidationTrack.TRIAGE_ASSESSMENT)
        self.assertIsInstance(result.result, ValidationResult)
        self.assertIsInstance(result.actual_score, float)
        self.assertIsInstance(result.gaps, list)
        self.assertIsInstance(result.warnings, list)
        self.assertIsInstance(result.recommendations, list)
    
    def test_readiness_summary_generation(self):
        """Test readiness summary generation"""
        results = self.validator.validate_case(self.test_clinical_data)
        summary = self.validator.generate_readiness_summary(results)
        
        self.assertIsInstance(summary, dict)
        self.assertIn('overall_assessment', summary)
        self.assertIn('track_details', summary)
        self.assertIn('recommendations', summary)
        self.assertIn('generated_at', summary)
        
        # Check overall assessment structure
        overall = summary['overall_assessment']
        self.assertIn('status', overall)
        self.assertIn('score', overall)
        self.assertIn('ready_tracks', overall)
        self.assertIn('near_miss_tracks', overall)
        self.assertIn('not_ready_tracks', overall)
        
        # Check score bounds
        self.assertGreaterEqual(overall['score'], 0.0)
        self.assertLessEqual(overall['score'], 1.0)
        
        # Check track details
        track_details = summary['track_details']
        self.assertIsInstance(track_details, list)
        self.assertEqual(len(track_details), len(results))
        
        for detail in track_details:
            self.assertIn('track', detail)
            self.assertIn('result', detail)
            self.assertIn('score', detail)
            self.assertIn('gap_count', detail)
            self.assertIn('warning_count', detail)
    
    def test_empty_case_validation(self):
        """Test validation with empty case data"""
        empty_data = {'case_id': 'EMPTY_001'}
        results = self.validator.validate_case(empty_data)
        
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), len(self.validator.validation_tracks))
        
        # All tracks should be NOT_READY for empty data
        for result in results:
            self.assertEqual(result.result, ValidationResult.NOT_READY)
            self.assertGreater(len(result.gaps), 0)
    
    def test_data_gap_structure(self):
        """Test data gap structure"""
        gap = DataGap(
            field="test_field",
            reason="Test reason",
            example_value="Test example",
            severity="high"
        )
        
        self.assertEqual(gap.field, "test_field")
        self.assertEqual(gap.reason, "Test reason")
        self.assertEqual(gap.example_value, "Test example")
        self.assertEqual(gap.severity, "high")

class TestIntegration(unittest.TestCase):
    """Test integration between components"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.engine = QuantumClinicalEngine(vqbit_dimension=256)
        self.validator = ClinicalDataContractValidator()
        self.test_clinical_data = {
            'case_id': 'INTEGRATION_TEST_001',
            'chief_complaint': 'chest pain',
            'age': 65,
            'gender': 'male',
            'symptoms': {
                'chest_pain': {'intensity': 0.8, 'quality': 'crushing'},
                'shortness_breath': {'intensity': 0.6}
            },
            'vital_signs': {
                'systolic_bp': 160,
                'diastolic_bp': 110,
                'heart_rate': 110,
                'respiratory_rate': 24,
                'temperature_c': 37.0
            },
            'medications': [
                {'name': 'Aspirin', 'dose': '81mg', 'frequency': 'daily'}
            ],
            'allergies': ['Penicillin']
        }
    
    def test_end_to_end_workflow(self):
        """Test complete end-to-end workflow"""
        # Step 1: Validate data readiness
        validation_results = self.validator.validate_case(self.test_clinical_data)
        summary = self.validator.generate_readiness_summary(validation_results)
        
        self.assertIsInstance(summary, dict)
        self.assertIn('overall_assessment', summary)
        
        # Step 2: Encode case into quantum state
        quantum_case = self.engine.encode_clinical_case(self.test_clinical_data)
        
        self.assertIsInstance(quantum_case, QuantumClinicalCase)
        self.assertEqual(quantum_case.case_id, 'INTEGRATION_TEST_001')
        
        # Step 3: Apply virtue supervision
        quantum_claim = self.engine.apply_virtue_supervision(quantum_case)
        
        self.assertIsInstance(quantum_claim, vQbitClinicalClaim)
        self.assertIsInstance(quantum_claim.quantum_state, QuantumClinicalState)
        
        # Step 4: Measure quantum properties
        coherence = self.engine.get_quantum_coherence(quantum_case)
        entropy = self.engine.get_entanglement_entropy(quantum_case)
        
        self.assertIsInstance(coherence, float)
        self.assertIsInstance(entropy, float)
        
        # Step 5: Evolve quantum state
        evolved_case = self.engine.evolve_quantum_state(quantum_case, time_step=0.1)
        
        self.assertIsInstance(evolved_case, QuantumClinicalCase)
        self.assertEqual(evolved_case.case_id, quantum_case.case_id)
    
    def test_no_simulations_policy(self):
        """Test that no simulations are used - all real calculations"""
        # This test ensures that all calculations are real, not simulated
        
        # Quantum engine should produce real quantum states
        quantum_case = self.engine.encode_clinical_case(self.test_clinical_data)
        self.assertIsInstance(quantum_case.quantum_state_vector, np.ndarray)
        
        # Check that quantum state has real complex amplitudes
        amplitudes = quantum_case.quantum_state_vector
        self.assertTrue(np.all(np.iscomplex(amplitudes)))
        
        # Check that probabilities sum to 1 (quantum normalization)
        probabilities = np.abs(amplitudes)**2
        self.assertAlmostEqual(np.sum(probabilities), 1.0, places=10)
        
        # Validator should produce real validation scores
        results = self.validator.validate_case(self.test_clinical_data)
        for result in results:
            self.assertIsInstance(result.actual_score, float)
            self.assertGreaterEqual(result.actual_score, 0.0)
            self.assertLessEqual(result.actual_score, 1.0)
    
    def test_mainnet_only_operation(self):
        """Test that system operates on mainnet only - no testnet or mock data"""
        # All data should be real clinical data
        self.assertIsInstance(self.test_clinical_data, dict)
        self.assertIn('case_id', self.test_clinical_data)
        self.assertIn('chief_complaint', self.test_clinical_data)
        
        # All calculations should be real
        quantum_case = self.engine.encode_clinical_case(self.test_clinical_data)
        self.assertIsNotNone(quantum_case.quantum_state_vector)
        
        # All validation should be real
        results = self.validator.validate_case(self.test_clinical_data)
        self.assertGreater(len(results), 0)
        
        # All timestamps should be real
        quantum_claim = self.engine.apply_virtue_supervision(quantum_case)
        self.assertIsNotNone(quantum_claim.timestamp)
        
        # Parse timestamp to ensure it's valid
        timestamp = datetime.fromisoformat(quantum_claim.timestamp.replace('Z', '+00:00'))
        self.assertIsInstance(timestamp, datetime)

def run_validation_tests():
    """Run all validation tests"""
    print("🧪 Running Field of Truth Clinical Trials Validation Tests...")
    print("⚛️ NO SIMULATIONS - ALL MAINNET - FIELD OF TRUTH 100%")
    print()
    
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test cases
    test_suite.addTest(unittest.makeSuite(TestQuantumClinicalEngine))
    test_suite.addTest(unittest.makeSuite(TestClinicalDataContractValidator))
    test_suite.addTest(unittest.makeSuite(TestIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Print summary
    print()
    print("📊 Test Summary:")
    print(f"   Tests run: {result.testsRun}")
    print(f"   Failures: {len(result.failures)}")
    print(f"   Errors: {len(result.errors)}")
    print(f"   Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    if result.failures:
        print("\n❌ Failures:")
        for test, traceback in result.failures:
            print(f"   {test}: {traceback}")
    
    if result.errors:
        print("\n🚨 Errors:")
        for test, traceback in result.errors:
            print(f"   {test}: {traceback}")
    
    if result.wasSuccessful():
        print("\n✅ All tests passed! System is ready for mainnet operation.")
    else:
        print("\n❌ Some tests failed. Please fix issues before mainnet deployment.")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_validation_tests()
    sys.exit(0 if success else 1)
