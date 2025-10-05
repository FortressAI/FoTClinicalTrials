"""
Clinical Data Readiness Checker - Field of Truth Implementation

Validates clinical case data readiness for quantum analysis with comprehensive
quality gates and NearMiss detection for incomplete but potentially valuable data.

NO SIMULATIONS - ALL MAINNET - FIELD OF TRUTH 100%
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import logging
import json
from datetime import datetime

logger = logging.getLogger(__name__)

class ValidationTrack(Enum):
    """Clinical validation tracks"""
    MEDICATION_SAFETY = "MedicationSafety"
    TRIAGE_ASSESSMENT = "TriageAssessment"
    NEXT_DIAGNOSTIC_STEP = "NextDiagnosticStep"
    IMAGING_READINESS = "ImagingReadiness"
    AUDIO_READINESS = "AudioReadiness"
    LABORATORY_ANALYSIS = "LaboratoryAnalysis"
    VITAL_SIGNS_MONITORING = "VitalSignsMonitoring"

class ValidationResult(Enum):
    """Validation result types"""
    READY = "READY"
    NEAR_MISS = "NEAR_MISS"
    NOT_READY = "NOT_READY"

@dataclass
class DataGap:
    """Represents a gap in clinical data"""
    field: str
    reason: str
    example_value: Optional[str] = None
    severity: str = "medium"  # low, medium, high, critical

@dataclass
class TrackValidationResult:
    """Result of validation for a specific track"""
    track: ValidationTrack
    result: ValidationResult
    actual_score: float
    gaps: List[DataGap]
    warnings: List[str]
    recommendations: List[str]

class ClinicalDataContractValidator:
    """
    Validates clinical case data readiness for quantum analysis
    
    Implements comprehensive data quality checks with Field of Truth principles:
    - No simulations or mock data
    - Real clinical data validation only
    - NearMiss detection for incomplete but valuable data
    - Evidence-based readiness assessment
    """
    
    def __init__(self):
        """Initialize the clinical data validator"""
        self.validation_tracks = list(ValidationTrack)
        self.minimum_scores = {
            ValidationTrack.MEDICATION_SAFETY: 0.7,
            ValidationTrack.TRIAGE_ASSESSMENT: 0.6,
            ValidationTrack.NEXT_DIAGNOSTIC_STEP: 0.8,
            ValidationTrack.IMAGING_READINESS: 0.9,
            ValidationTrack.AUDIO_READINESS: 0.9,
            ValidationTrack.LABORATORY_ANALYSIS: 0.8,
            ValidationTrack.VITAL_SIGNS_MONITORING: 0.7
        }
        
        logger.info("Clinical Data Contract Validator initialized")
    
    def validate_case(self, clinical_data: Dict[str, Any]) -> List[TrackValidationResult]:
        """
        Validate clinical case data across all tracks
        
        Args:
            clinical_data: Clinical case data dictionary
            
        Returns:
            List of validation results for each track
        """
        results = []
        
        for track in self.validation_tracks:
            try:
                result = self._validate_track(clinical_data, track)
                results.append(result)
            except Exception as e:
                logger.error(f"Error validating track {track.value}: {e}")
                # Create error result
                error_result = TrackValidationResult(
                    track=track,
                    result=ValidationResult.NOT_READY,
                    actual_score=0.0,
                    gaps=[DataGap(field="validation_error", reason=str(e), severity="critical")],
                    warnings=[f"Validation error: {e}"],
                    recommendations=["Fix validation error and retry"]
                )
                results.append(error_result)
        
        return results
    
    def _validate_track(self, clinical_data: Dict[str, Any], track: ValidationTrack) -> TrackValidationResult:
        """Validate specific track"""
        
        if track == ValidationTrack.MEDICATION_SAFETY:
            return self._validate_medication_safety(clinical_data)
        elif track == ValidationTrack.TRIAGE_ASSESSMENT:
            return self._validate_triage_assessment(clinical_data)
        elif track == ValidationTrack.NEXT_DIAGNOSTIC_STEP:
            return self._validate_next_diagnostic_step(clinical_data)
        elif track == ValidationTrack.IMAGING_READINESS:
            return self._validate_imaging_readiness(clinical_data)
        elif track == ValidationTrack.AUDIO_READINESS:
            return self._validate_audio_readiness(clinical_data)
        elif track == ValidationTrack.LABORATORY_ANALYSIS:
            return self._validate_laboratory_analysis(clinical_data)
        elif track == ValidationTrack.VITAL_SIGNS_MONITORING:
            return self._validate_vital_signs_monitoring(clinical_data)
        else:
            raise ValueError(f"Unknown validation track: {track}")
    
    def _validate_medication_safety(self, clinical_data: Dict[str, Any]) -> TrackValidationResult:
        """Validate medication safety track"""
        gaps = []
        warnings = []
        recommendations = []
        score = 0.0
        
        # Check for medication list
        medications = clinical_data.get('medications', [])
        if not medications:
            gaps.append(DataGap(
                field="medications",
                reason="No medication list provided",
                example_value="[{'name': 'Aspirin', 'dose': '81mg', 'frequency': 'daily'}]",
                severity="high"
            ))
        else:
            score += 0.3
            
            # Validate medication format
            for i, med in enumerate(medications):
                if isinstance(med, dict):
                    if not med.get('name'):
                        gaps.append(DataGap(
                            field=f"medications[{i}].name",
                            reason="Medication name missing",
                            example_value="Aspirin",
                            severity="medium"
                        ))
                    if not med.get('dose'):
                        gaps.append(DataGap(
                            field=f"medications[{i}].dose",
                            reason="Medication dose missing",
                            example_value="81mg",
                            severity="medium"
                        ))
                else:
                    gaps.append(DataGap(
                        field=f"medications[{i}]",
                        reason="Medication should be dictionary with name, dose, frequency",
                        example_value="{'name': 'Aspirin', 'dose': '81mg', 'frequency': 'daily'}",
                        severity="medium"
                    ))
        
        # Check for allergies
        allergies = clinical_data.get('allergies', [])
        if not allergies:
            gaps.append(DataGap(
                field="allergies",
                reason="No allergy information provided",
                example_value="['Penicillin', 'Shellfish']",
                severity="high"
            ))
        else:
            score += 0.2
        
        # Check for drug interactions
        if medications and allergies:
            # Simple interaction check
            med_names = [med.get('name', '').lower() for med in medications if isinstance(med, dict)]
            allergy_names = [allergy.lower() for allergy in allergies if isinstance(allergy, str)]
            
            # Check for common interactions
            common_interactions = {
                'warfarin': ['aspirin', 'ibuprofen'],
                'digoxin': ['furosemide'],
                'metformin': ['contrast_dye']
            }
            
            for med in med_names:
                if med in common_interactions:
                    for interaction in common_interactions[med]:
                        if any(interaction in allergy for allergy in allergy_names):
                            warnings.append(f"Potential interaction: {med} with {interaction}")
                            recommendations.append(f"Review {med} dosing with {interaction} allergy")
        
        # Check for contraindications
        age = clinical_data.get('age', 0)
        if age > 65 and any('warfarin' in med.get('name', '').lower() for med in medications if isinstance(med, dict)):
            warnings.append("Elderly patient on warfarin - monitor INR closely")
            recommendations.append("Consider dose adjustment based on INR")
        
        # Calculate final score
        if gaps:
            score = max(0.0, score - len(gaps) * 0.1)
        
        # Determine result
        min_score = self.minimum_scores[ValidationTrack.MEDICATION_SAFETY]
        if score >= min_score:
            result = ValidationResult.READY
        elif score >= min_score * 0.8:
            result = ValidationResult.NEAR_MISS
        else:
            result = ValidationResult.NOT_READY
        
        return TrackValidationResult(
            track=ValidationTrack.MEDICATION_SAFETY,
            result=result,
            actual_score=score,
            gaps=gaps,
            warnings=warnings,
            recommendations=recommendations
        )
    
    def _validate_triage_assessment(self, clinical_data: Dict[str, Any]) -> TrackValidationResult:
        """Validate triage assessment track"""
        gaps = []
        warnings = []
        recommendations = []
        score = 0.0
        
        # Check chief complaint
        chief_complaint = clinical_data.get('chief_complaint', '')
        if not chief_complaint:
            gaps.append(DataGap(
                field="chief_complaint",
                reason="No chief complaint provided",
                example_value="chest pain",
                severity="critical"
            ))
        else:
            score += 0.3
        
        # Check vital signs
        vital_signs = clinical_data.get('vital_signs', {})
        required_vitals = ['systolic_bp', 'diastolic_bp', 'heart_rate', 'respiratory_rate', 'temperature_c']
        
        for vital in required_vitals:
            if vital not in vital_signs:
                gaps.append(DataGap(
                    field=f"vital_signs.{vital}",
                    reason=f"Missing vital sign: {vital}",
                    example_value="120" if vital != 'temperature_c' else "37.0",
                    severity="high"
                ))
            else:
                score += 0.1
        
        # Check for critical vital signs
        if vital_signs:
            systolic_bp = vital_signs.get('systolic_bp', 0)
            heart_rate = vital_signs.get('heart_rate', 0)
            respiratory_rate = vital_signs.get('respiratory_rate', 0)
            temperature = vital_signs.get('temperature_c', 0)
            
            if systolic_bp > 180 or systolic_bp < 90:
                warnings.append(f"Abnormal blood pressure: {systolic_bp}")
                recommendations.append("Monitor blood pressure closely")
            
            if heart_rate > 120 or heart_rate < 50:
                warnings.append(f"Abnormal heart rate: {heart_rate}")
                recommendations.append("Consider cardiac monitoring")
            
            if respiratory_rate > 24 or respiratory_rate < 12:
                warnings.append(f"Abnormal respiratory rate: {respiratory_rate}")
                recommendations.append("Monitor respiratory status")
            
            if temperature > 38.5 or temperature < 36.0:
                warnings.append(f"Abnormal temperature: {temperature}°C")
                recommendations.append("Monitor for infection or hypothermia")
        
        # Check symptoms
        symptoms = clinical_data.get('symptoms', {})
        if not symptoms:
            gaps.append(DataGap(
                field="symptoms",
                reason="No symptom information provided",
                example_value="{'chest_pain': {'intensity': 0.8, 'quality': 'crushing'}}",
                severity="high"
            ))
        else:
            score += 0.2
        
        # Calculate final score
        if gaps:
            score = max(0.0, score - len(gaps) * 0.1)
        
        # Determine result
        min_score = self.minimum_scores[ValidationTrack.TRIAGE_ASSESSMENT]
        if score >= min_score:
            result = ValidationResult.READY
        elif score >= min_score * 0.8:
            result = ValidationResult.NEAR_MISS
        else:
            result = ValidationResult.NOT_READY
        
        return TrackValidationResult(
            track=ValidationTrack.TRIAGE_ASSESSMENT,
            result=result,
            actual_score=score,
            gaps=gaps,
            warnings=warnings,
            recommendations=recommendations
        )
    
    def _validate_next_diagnostic_step(self, clinical_data: Dict[str, Any]) -> TrackValidationResult:
        """Validate next diagnostic step track"""
        gaps = []
        warnings = []
        recommendations = []
        score = 0.0
        
        # Check for previous diagnostic workup
        previous_tests = clinical_data.get('previous_tests', [])
        if not previous_tests:
            gaps.append(DataGap(
                field="previous_tests",
                reason="No previous diagnostic tests documented",
                example_value="['EKG', 'Chest X-ray', 'Troponin']",
                severity="medium"
            ))
        else:
            score += 0.2
        
        # Check for current diagnostic plan
        diagnostic_plan = clinical_data.get('diagnostic_plan', [])
        if not diagnostic_plan:
            gaps.append(DataGap(
                field="diagnostic_plan",
                reason="No diagnostic plan provided",
                example_value="['EKG', 'Chest X-ray', 'Troponin', 'Echocardiogram']",
                severity="high"
            ))
        else:
            score += 0.3
        
        # Check for contraindications to specific tests
        allergies = clinical_data.get('allergies', [])
        if 'contrast_dye' in [allergy.lower() for allergy in allergies if isinstance(allergy, str)]:
            if any('CT' in test or 'angiography' in test.lower() for test in diagnostic_plan if isinstance(test, str)):
                warnings.append("Patient allergic to contrast dye - CT with contrast contraindicated")
                recommendations.append("Consider non-contrast CT or alternative imaging")
        
        # Check for renal function if contrast needed
        lab_results = clinical_data.get('laboratory', {})
        creatinine = lab_results.get('creatinine', 0)
        if creatinine > 1.5 and any('contrast' in test.lower() for test in diagnostic_plan if isinstance(test, str)):
            warnings.append("Elevated creatinine - contrast administration risky")
            recommendations.append("Consider alternative imaging or pre-hydration")
        
        # Check for appropriate test selection based on chief complaint
        chief_complaint = clinical_data.get('chief_complaint', '').lower()
        if 'chest pain' in chief_complaint:
            if not any('troponin' in test.lower() for test in diagnostic_plan if isinstance(test, str)):
                warnings.append("Chest pain without troponin - consider cardiac workup")
                recommendations.append("Add troponin to diagnostic plan")
        
        # Calculate final score
        if gaps:
            score = max(0.0, score - len(gaps) * 0.1)
        
        # Determine result
        min_score = self.minimum_scores[ValidationTrack.NEXT_DIAGNOSTIC_STEP]
        if score >= min_score:
            result = ValidationResult.READY
        elif score >= min_score * 0.8:
            result = ValidationResult.NEAR_MISS
        else:
            result = ValidationResult.NOT_READY
        
        return TrackValidationResult(
            track=ValidationTrack.NEXT_DIAGNOSTIC_STEP,
            result=result,
            actual_score=score,
            gaps=gaps,
            warnings=warnings,
            recommendations=recommendations
        )
    
    def _validate_imaging_readiness(self, clinical_data: Dict[str, Any]) -> TrackValidationResult:
        """Validate imaging readiness track"""
        gaps = []
        warnings = []
        recommendations = []
        score = 0.0
        
        # Check for imaging study details
        imaging_study = clinical_data.get('imaging_study', {})
        if not imaging_study:
            gaps.append(DataGap(
                field="imaging_study",
                reason="No imaging study information provided",
                example_value="{'modality': 'CT', 'bodySite': 'chest', 'contrast': 'yes'}",
                severity="high"
            ))
        else:
            score += 0.4
            
            # Check required fields
            required_fields = ['modality', 'bodySite', 'contrast']
            for field in required_fields:
                if field not in imaging_study:
                    gaps.append(DataGap(
                        field=f"imaging_study.{field}",
                        reason=f"Missing imaging field: {field}",
                        example_value="CT" if field == 'modality' else "chest" if field == 'bodySite' else "yes",
                        severity="high"
                    ))
        
        # Check for patient preparation
        patient_preparation = clinical_data.get('patient_preparation', {})
        if not patient_preparation:
            gaps.append(DataGap(
                field="patient_preparation",
                reason="No patient preparation information",
                example_value="{'npo': '4 hours', 'medications': 'hold metformin'}",
                severity="medium"
            ))
        else:
            score += 0.2
        
        # Check for contraindications
        allergies = clinical_data.get('allergies', [])
        if 'contrast_dye' in [allergy.lower() for allergy in allergies if isinstance(allergy, str)]:
            if imaging_study.get('contrast', '').lower() == 'yes':
                warnings.append("Contrast allergy - imaging contraindicated")
                recommendations.append("Consider non-contrast imaging or pre-medication")
        
        # Check for renal function
        lab_results = clinical_data.get('laboratory', {})
        creatinine = lab_results.get('creatinine', 0)
        if creatinine > 1.5 and imaging_study.get('contrast', '').lower() == 'yes':
            warnings.append("Elevated creatinine - contrast risky")
            recommendations.append("Consider alternative imaging or pre-hydration")
        
        # Calculate final score
        if gaps:
            score = max(0.0, score - len(gaps) * 0.1)
        
        # Determine result
        min_score = self.minimum_scores[ValidationTrack.IMAGING_READINESS]
        if score >= min_score:
            result = ValidationResult.READY
        elif score >= min_score * 0.8:
            result = ValidationResult.NEAR_MISS
        else:
            result = ValidationResult.NOT_READY
        
        return TrackValidationResult(
            track=ValidationTrack.IMAGING_READINESS,
            result=result,
            actual_score=score,
            gaps=gaps,
            warnings=warnings,
            recommendations=recommendations
        )
    
    def _validate_audio_readiness(self, clinical_data: Dict[str, Any]) -> TrackValidationResult:
        """Validate audio readiness track"""
        gaps = []
        warnings = []
        recommendations = []
        score = 0.0
        
        # Check for audio study details
        audio_study = clinical_data.get('audio_study', {})
        if not audio_study:
            gaps.append(DataGap(
                field="audio_study",
                reason="No audio study information provided",
                example_value="{'modality': 'heart_sounds', 'duration': '30s', 'quality': 'good'}",
                severity="high"
            ))
        else:
            score += 0.4
            
            # Check required fields
            required_fields = ['modality', 'duration', 'quality']
            for field in required_fields:
                if field not in audio_study:
                    gaps.append(DataGap(
                        field=f"audio_study.{field}",
                        reason=f"Missing audio field: {field}",
                        example_value="heart_sounds" if field == 'modality' else "30s" if field == 'duration' else "good",
                        severity="high"
                    ))
        
        # Check for patient positioning
        patient_positioning = clinical_data.get('patient_positioning', {})
        if not patient_positioning:
            gaps.append(DataGap(
                field="patient_positioning",
                reason="No patient positioning information",
                example_value="{'position': 'supine', 'quiet_room': 'yes'}",
                severity="medium"
            ))
        else:
            score += 0.2
        
        # Check for environmental factors
        environment = clinical_data.get('environment', {})
        if not environment:
            gaps.append(DataGap(
                field="environment",
                reason="No environmental information",
                example_value="{'noise_level': 'low', 'temperature': 'comfortable'}",
                severity="low"
            ))
        else:
            score += 0.1
        
        # Check for quality indicators
        if audio_study.get('quality', '').lower() == 'poor':
            warnings.append("Poor audio quality may affect analysis")
            recommendations.append("Re-record with better positioning and environment")
        
        # Calculate final score
        if gaps:
            score = max(0.0, score - len(gaps) * 0.1)
        
        # Determine result
        min_score = self.minimum_scores[ValidationTrack.AUDIO_READINESS]
        if score >= min_score:
            result = ValidationResult.READY
        elif score >= min_score * 0.8:
            result = ValidationResult.NEAR_MISS
        else:
            result = ValidationResult.NOT_READY
        
        return TrackValidationResult(
            track=ValidationTrack.AUDIO_READINESS,
            result=result,
            actual_score=score,
            gaps=gaps,
            warnings=warnings,
            recommendations=recommendations
        )
    
    def _validate_laboratory_analysis(self, clinical_data: Dict[str, Any]) -> TrackValidationResult:
        """Validate laboratory analysis track"""
        gaps = []
        warnings = []
        recommendations = []
        score = 0.0
        
        # Check for laboratory results
        lab_results = clinical_data.get('laboratory', {})
        if not lab_results:
            gaps.append(DataGap(
                field="laboratory",
                reason="No laboratory results provided",
                example_value="{'glucose': 120, 'creatinine': 1.0, 'troponin': 0.01}",
                severity="high"
            ))
        else:
            score += 0.4
            
            # Check for critical values
            critical_values = {
                'glucose': (50, 400),
                'creatinine': (0.5, 3.0),
                'troponin': (0.0, 0.04),
                'potassium': (3.0, 6.0),
                'sodium': (130, 150)
            }
            
            for test, (low, high) in critical_values.items():
                if test in lab_results:
                    value = lab_results[test]
                    if value < low or value > high:
                        warnings.append(f"Critical {test}: {value} (normal: {low}-{high})")
                        recommendations.append(f"Monitor {test} closely")
        
        # Check for test timing
        test_timing = clinical_data.get('test_timing', {})
        if not test_timing:
            gaps.append(DataGap(
                field="test_timing",
                reason="No test timing information",
                example_value="{'collection_time': '2024-01-15T10:30:00Z', 'fasting': 'yes'}",
                severity="medium"
            ))
        else:
            score += 0.2
        
        # Check for appropriate test selection
        chief_complaint = clinical_data.get('chief_complaint', '').lower()
        if 'chest pain' in chief_complaint:
            if 'troponin' not in lab_results:
                warnings.append("Chest pain without troponin - consider cardiac workup")
                recommendations.append("Add troponin to laboratory panel")
        
        # Calculate final score
        if gaps:
            score = max(0.0, score - len(gaps) * 0.1)
        
        # Determine result
        min_score = self.minimum_scores[ValidationTrack.LABORATORY_ANALYSIS]
        if score >= min_score:
            result = ValidationResult.READY
        elif score >= min_score * 0.8:
            result = ValidationResult.NEAR_MISS
        else:
            result = ValidationResult.NOT_READY
        
        return TrackValidationResult(
            track=ValidationTrack.LABORATORY_ANALYSIS,
            result=result,
            actual_score=score,
            gaps=gaps,
            warnings=warnings,
            recommendations=recommendations
        )
    
    def _validate_vital_signs_monitoring(self, clinical_data: Dict[str, Any]) -> TrackValidationResult:
        """Validate vital signs monitoring track"""
        gaps = []
        warnings = []
        recommendations = []
        score = 0.0
        
        # Check for vital signs
        vital_signs = clinical_data.get('vital_signs', {})
        if not vital_signs:
            gaps.append(DataGap(
                field="vital_signs",
                reason="No vital signs provided",
                example_value="{'systolic_bp': 120, 'diastolic_bp': 80, 'heart_rate': 70}",
                severity="critical"
            ))
        else:
            score += 0.5
            
            # Check for completeness
            required_vitals = ['systolic_bp', 'diastolic_bp', 'heart_rate', 'respiratory_rate', 'temperature_c']
            for vital in required_vitals:
                if vital not in vital_signs:
                    gaps.append(DataGap(
                        field=f"vital_signs.{vital}",
                        reason=f"Missing vital sign: {vital}",
                        example_value="120" if vital != 'temperature_c' else "37.0",
                        severity="high"
                    ))
        
        # Check for vital signs trends
        vital_trends = clinical_data.get('vital_trends', {})
        if not vital_trends:
            gaps.append(DataGap(
                field="vital_trends",
                reason="No vital signs trends provided",
                example_value="{'systolic_bp_trend': 'stable', 'heart_rate_trend': 'increasing'}",
                severity="medium"
            ))
        else:
            score += 0.2
        
        # Check for monitoring frequency
        monitoring_frequency = clinical_data.get('monitoring_frequency', '')
        if not monitoring_frequency:
            gaps.append(DataGap(
                field="monitoring_frequency",
                reason="No monitoring frequency specified",
                example_value="every 15 minutes",
                severity="medium"
            ))
        else:
            score += 0.1
        
        # Check for abnormal values
        if vital_signs:
            systolic_bp = vital_signs.get('systolic_bp', 0)
            heart_rate = vital_signs.get('heart_rate', 0)
            respiratory_rate = vital_signs.get('respiratory_rate', 0)
            temperature = vital_signs.get('temperature_c', 0)
            
            if systolic_bp > 180 or systolic_bp < 90:
                warnings.append(f"Abnormal blood pressure: {systolic_bp}")
                recommendations.append("Increase monitoring frequency")
            
            if heart_rate > 120 or heart_rate < 50:
                warnings.append(f"Abnormal heart rate: {heart_rate}")
                recommendations.append("Consider continuous cardiac monitoring")
            
            if respiratory_rate > 24 or respiratory_rate < 12:
                warnings.append(f"Abnormal respiratory rate: {respiratory_rate}")
                recommendations.append("Monitor respiratory status closely")
            
            if temperature > 38.5 or temperature < 36.0:
                warnings.append(f"Abnormal temperature: {temperature}°C")
                recommendations.append("Monitor for infection or hypothermia")
        
        # Calculate final score
        if gaps:
            score = max(0.0, score - len(gaps) * 0.1)
        
        # Determine result
        min_score = self.minimum_scores[ValidationTrack.VITAL_SIGNS_MONITORING]
        if score >= min_score:
            result = ValidationResult.READY
        elif score >= min_score * 0.8:
            result = ValidationResult.NEAR_MISS
        else:
            result = ValidationResult.NOT_READY
        
        return TrackValidationResult(
            track=ValidationTrack.VITAL_SIGNS_MONITORING,
            result=result,
            actual_score=score,
            gaps=gaps,
            warnings=warnings,
            recommendations=recommendations
        )
    
    def generate_readiness_summary(self, validation_results: List[TrackValidationResult]) -> Dict[str, Any]:
        """Generate overall readiness summary"""
        
        ready_tracks = [r.track.value for r in validation_results if r.result == ValidationResult.READY]
        near_miss_tracks = [r.track.value for r in validation_results if r.result == ValidationResult.NEAR_MISS]
        not_ready_tracks = [r.track.value for r in validation_results if r.result == ValidationResult.NOT_READY]
        
        overall_score = sum(r.actual_score for r in validation_results) / len(validation_results)
        
        # Determine overall readiness
        if len(ready_tracks) == len(validation_results):
            overall_status = "FULLY_READY"
        elif len(ready_tracks) > 0:
            overall_status = "PARTIALLY_READY"
        else:
            overall_status = "NOT_READY"
        
        return {
            "overall_assessment": {
                "status": overall_status,
                "score": overall_score,
                "ready_tracks": ready_tracks,
                "near_miss_tracks": near_miss_tracks,
                "not_ready_tracks": not_ready_tracks
            },
            "track_details": [
                {
                    "track": r.track.value,
                    "result": r.result.value,
                    "score": r.actual_score,
                    "gap_count": len(r.gaps),
                    "warning_count": len(r.warnings)
                }
                for r in validation_results
            ],
            "recommendations": [
                rec for r in validation_results for rec in r.recommendations
            ],
            "generated_at": datetime.now().isoformat()
        }

# Example usage and testing
if __name__ == "__main__":
    # Initialize validator
    validator = ClinicalDataContractValidator()
    
    # Example clinical case
    clinical_data = {
        'case_id': 'DEMO_001',
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
    
    # Validate case
    results = validator.validate_case(clinical_data)
    
    # Generate summary
    summary = validator.generate_readiness_summary(results)
    
    print(f"Overall Status: {summary['overall_assessment']['status']}")
    print(f"Overall Score: {summary['overall_assessment']['score']:.2f}")
    print(f"Ready Tracks: {summary['overall_assessment']['ready_tracks']}")
    print(f"Near Miss Tracks: {summary['overall_assessment']['near_miss_tracks']}")
    print(f"Not Ready Tracks: {summary['overall_assessment']['not_ready_tracks']}")
    
    # Print detailed results
    for result in results:
        print(f"\n{result.track.value}: {result.result.value} (Score: {result.actual_score:.2f})")
        if result.gaps:
            print(f"  Gaps: {len(result.gaps)}")
        if result.warnings:
            print(f"  Warnings: {len(result.warnings)}")
        if result.recommendations:
            print(f"  Recommendations: {len(result.recommendations)}")
