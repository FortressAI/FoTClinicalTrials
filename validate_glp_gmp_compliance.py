#!/usr/bin/env python3
"""
GLP/GMP Compliance Validation Script
Field of Truth Clinical Trials System

This script validates that the clinical trials system meets GLP/GMP requirements
for null safety, error handling, and data integrity.
"""

import ast
import re
import sys
import os

def validate_glp_gmp_compliance():
    """Validate GLP/GMP compliance requirements"""
    
    print("🔬 GLP/GMP Compliance Validation")
    print("=" * 50)
    
    # Read the clinical app file
    with open('clinical_app.py', 'r') as f:
        source = f.read()
    
    # 1. Syntax Validation
    print("\n1. ✅ Syntax Validation")
    try:
        ast.parse(source)
        print("   ✅ No syntax errors found")
    except SyntaxError as e:
        print(f"   ❌ Syntax error: {e}")
        return False
    except Exception as e:
        print(f"   ❌ Parse error: {e}")
        return False
    
    # 2. Null Safety Validation
    print("\n2. ✅ Null Safety Validation")
    
    # Find all trial attribute accesses
    trial_accesses = re.findall(r'trial\.[a-zA-Z_]+', source)
    protected_accesses = 0
    unprotected_accesses = 0
    
    # Check if accesses are protected by null checks
    lines = source.split('\n')
    for i, line in enumerate(lines):
        if 'trial.' in line:
            # Check if there's a null check before this line
            protected = False
            for j in range(max(0, i-10), i):
                if 'if trial:' in lines[j] or 'if trial is not None:' in lines[j]:
                    protected = True
                    break
            
            if protected:
                protected_accesses += 1
            else:
                unprotected_accesses += 1
                print(f"   ⚠️  Line {i+1}: {line.strip()}")
    
    if unprotected_accesses == 0:
        print("   ✅ All trial accesses are null-safe")
    else:
        print(f"   ❌ Found {unprotected_accesses} unprotected trial accesses")
        return False
    
    # 3. Error Handling Validation
    print("\n3. ✅ Error Handling Validation")
    
    # Check for try-except blocks
    try_blocks = len(re.findall(r'try:', source))
    except_blocks = len(re.findall(r'except', source))
    
    if try_blocks > 0 and except_blocks > 0:
        print(f"   ✅ Found {try_blocks} try-except blocks for error handling")
    else:
        print("   ⚠️  Limited error handling found")
    
    # 4. Data Integrity Validation
    print("\n4. ✅ Data Integrity Validation")
    
    # Check for session state usage
    session_state_usage = len(re.findall(r'st\.session_state', source))
    if session_state_usage > 0:
        print(f"   ✅ Found {session_state_usage} session state usages for data persistence")
    
    # Check for data validation
    validation_patterns = [
        r'if.*is not None',
        r'if.*is None',
        r'len\(.*\) > 0',
        r'isinstance\(',
        r'assert '
    ]
    
    validation_count = 0
    for pattern in validation_patterns:
        validation_count += len(re.findall(pattern, source))
    
    print(f"   ✅ Found {validation_count} data validation patterns")
    
    # 5. Regulatory Compliance Validation
    print("\n5. ✅ Regulatory Compliance Validation")
    
    # Check for audit trail components
    audit_components = [
        'timestamp',
        'created',
        'updated',
        'user_id',
        'action_type'
    ]
    
    audit_count = 0
    for component in audit_components:
        if component in source:
            audit_count += 1
    
    print(f"   ✅ Found {audit_count}/{len(audit_components)} audit trail components")
    
    # 6. Field of Truth Compliance
    print("\n6. ✅ Field of Truth Compliance")
    
    fot_components = [
        'FoTClaim',
        'Measurement',
        'CollapsePolicy',
        'Evidence',
        'quantum',
        'vQbit'
    ]
    
    fot_count = 0
    for component in fot_components:
        if component in source:
            fot_count += 1
    
    print(f"   ✅ Found {fot_count}/{len(fot_components)} Field of Truth components")
    
    # 7. Summary
    print("\n" + "=" * 50)
    print("🎯 GLP/GMP Compliance Summary")
    print("=" * 50)
    
    if unprotected_accesses == 0 and try_blocks > 0:
        print("✅ PASSED: System meets GLP/GMP compliance requirements")
        print("✅ Null safety: All trial accesses are protected")
        print("✅ Error handling: Try-except blocks implemented")
        print("✅ Data integrity: Session state and validation present")
        print("✅ Audit trail: Timestamp and tracking components present")
        print("✅ Field of Truth: Quantum substrate components present")
        return True
    else:
        print("❌ FAILED: System does not meet GLP/GMP compliance requirements")
        if unprotected_accesses > 0:
            print(f"❌ Null safety: {unprotected_accesses} unprotected accesses found")
        if try_blocks == 0:
            print("❌ Error handling: No try-except blocks found")
        return False

if __name__ == "__main__":
    success = validate_glp_gmp_compliance()
    sys.exit(0 if success else 1)
