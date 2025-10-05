"""
Field of Truth Clinical Trials - Core Module

This module contains the core quantum clinical engine and supporting components
for the Field of Truth Clinical Trials system.

NO SIMULATIONS - ALL MAINNET - FIELD OF TRUTH 100%
"""

# Core clinical components
from .clinical.quantum_clinical_engine import (
    QuantumClinicalEngine,
    QuantumClinicalCase,
    vQbitClinicalClaim,
    QuantumClinicalState,
    QuantumVirtueSupervisor
)

from .clinical.data_readiness_checker import (
    ClinicalDataContractValidator,
    ValidationTrack,
    ValidationResult,
    TrackValidationResult,
    DataGap
)

__all__ = [
    'QuantumClinicalEngine',
    'QuantumClinicalCase', 
    'vQbitClinicalClaim',
    'QuantumClinicalState',
    'QuantumVirtueSupervisor',
    'ClinicalDataContractValidator',
    'ValidationTrack',
    'ValidationResult',
    'TrackValidationResult',
    'DataGap'
]

__version__ = "1.0.0"
__author__ = "Field of Truth Foundation"
__email__ = "clinical@fieldoftruth.org"
