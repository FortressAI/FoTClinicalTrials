# 🧪 Field of Truth Clinical Trials - Streamlit UI Testing Guide

## 🚀 **App Access**
**URL:** http://localhost:8502  
**Status:** ✅ Running and Ready for Testing

---

## 🎯 **Complete UI Testing Checklist**

### **1. 🏥 Main Interface Testing**

#### **Header & Branding**
- [ ] **Quantum Branding** - Check the gradient header with "🏥⚛️ Field of Truth Clinical Trials"
- [ ] **Subtitle** - Verify "Quantum-Enhanced Clinical Trial Management" 
- [ ] **Feature Tags** - Confirm "Phase-Aware Architecture | vQbit Quantum Substrate | FoT Claims System"

#### **Field of Truth Compliance Banner**
- [ ] **Red Banner** - Verify the prominent red compliance banner
- [ ] **"FIELD OF TRUTH 100% - NO SIMULATIONS"** - Check main message
- [ ] **"LIVE MAINNET ONLY"** - Confirm live system messaging
- [ ] **Compliance Tags** - Verify "🚫 ZERO MOCKS", "⚛️ QUANTUM SUBSTRATE", "🛡️ VIRTUE SUPERVISION", "📊 REAL EVIDENCE"

### **2. 🎛️ Sidebar Trial Wizard Testing**

#### **Trial Initialization**
- [ ] **Candidate ID Input** - Test with "Protein-X17" (default)
- [ ] **Indication Input** - Test with "Type 2 Diabetes" (default)
- [ ] **Phase Selection** - Test all phases:
  - [ ] Phase 0 (In-Silico)
  - [ ] Phase I
  - [ ] Phase II
  - [ ] Phase III
- [ ] **Initialize/Update Trial Button** - Click and verify success message

#### **Default Endpoints Creation**
- [ ] **HbA1c Change Endpoint** - Verify efficacy endpoint creation
- [ ] **TEAE Endpoint** - Verify safety endpoint creation
- [ ] **Collapse Policies** - Check replications, completeness, agreement settings

### **3. 📋 Tab-by-Tab Testing**

#### **Tab 1: Design & Protocol**
- [ ] **Trial Info Display** - Verify candidate, indication, phase display
- [ ] **Endpoint Editor** - Test editing endpoint names, types, metrics
- [ ] **Success Rules** - Test editing human-readable success rules
- [ ] **Collapse Policy Settings**:
  - [ ] Replications slider (1-5)
  - [ ] Min completeness slider (0.5-1.0)
  - [ ] Max agreement delta slider (0.0-0.2)
- [ ] **Save Functionality** - Verify "Design saved" message

#### **Tab 2: Phase 0 (In-Silico)**
- [ ] **Hypothesis Registration**:
  - [ ] Enter hypothesis text
  - [ ] Click "Pre-register Hypothesis"
  - [ ] Verify success message
- [ ] **Quantum Screen Execution**:
  - [ ] Click "Execute In-Silico Screen (LIVE)"
  - [ ] Verify FoT claim creation
  - [ ] Check measurements: MeanDelta, PValue, ToolchainAgreementDelta
  - [ ] Verify evidence tracking
  - [ ] Check collapse status

#### **Tab 3: Phase I (Safety)**
- [ ] **AE Intake Form**:
  - [ ] Enter AE description (e.g., "Headache, mild")
  - [ ] Select seriousness (No/Yes)
  - [ ] Enter concomitant medication
  - [ ] Submit form
  - [ ] Verify AE recorded with coding advice
  - [ ] Check FoT claim creation

#### **Tab 4: Phase II (Efficacy/Dose)**
- [ ] **Endpoint Modality Selection**:
  - [ ] Test "imaging" radio button
  - [ ] Test "audio" radio button
- [ ] **Readiness Gate Testing**:

##### **Image Readiness Test**
```json
{
  "modality": "CT",
  "bodySite": "chest",
  "acquiredAt": "2025-01-05T12:00:00Z",
  "deviceModel": "Test Scanner",
  "widthPx": 512,
  "heightPx": 512,
  "pixelSpacingMm": 0.5,
  "phiBurninFlag": 0,
  "qualityMeasurements": [
    {"hasMetric": "fimg:Quality_FocusScore", "value": 0.8},
    {"hasMetric": "fimg:Quality_ExposureScore", "value": 0.7},
    {"hasMetric": "fimg:Quality_SNR_dB", "value": 25.0}
  ]
}
```

##### **Audio Readiness Test**
```json
{
  "bodySite": "heart",
  "sampleRateHz": 8000,
  "bitDepth": 16,
  "channels": 1,
  "durationSec": 30.0,
  "deviceModel": "Test Microphone",
  "acquiredAt": "2025-01-05T12:00:00Z",
  "calibrationPassed": true,
  "qualityMeasurements": [
    {"hasMetric": "faud:Quality_SNR_dB", "value": 30.0},
    {"hasMetric": "faud:Quality_NoiseFloor_dBFS", "value": -40.0},
    {"hasMetric": "faud:Quality_ArtifactScore", "value": 0.2}
  ]
}
```

- [ ] **Readiness Results**:
  - [ ] Test with valid data → Should show "Ready ✅"
  - [ ] Test with invalid data → Should show warnings and missing fields
  - [ ] Verify FoT claim creation regardless of readiness

#### **Tab 5: Phase III (Confirmatory)**
- [ ] **Twin Toolchain Input**:
  - [ ] Set Toolchain A estimate (e.g., -0.72)
  - [ ] Set Toolchain B estimate (e.g., -0.74)
  - [ ] Verify agreement delta calculation
- [ ] **Confirmatory Claim**:
  - [ ] Click "Emit Confirmatory Claim"
  - [ ] Verify claim creation with both estimates
  - [ ] Check collapse status based on agreement

#### **Tab 6: Safety & PV**
- [ ] **Safety Claims Review**:
  - [ ] Verify safety claims display
  - [ ] Check JSON structure of claims
  - [ ] Verify MedDRA coding advice

#### **Tab 7: Billing & Coding**
- [ ] **Diagnosis Input**:
  - [ ] Enter primary diagnosis
  - [ ] Click "Suggest Codes"
  - [ ] Verify ICD-10-CM suggestions
  - [ ] Verify CPT/HCPCS suggestions
  - [ ] Check coverage analysis note

#### **Tab 8: Evidence Graph**
- [ ] **Claims Display**:
  - [ ] Verify all FoT claims shown
  - [ ] Check claim IDs and problem addresses
  - [ ] Verify collapse status display
  - [ ] Check JSON structure of claims
  - [ ] Test scrolling through claims (last 25)

#### **Tab 9: Exports**
- [ ] **Protocol Export**:
  - [ ] Click "Download Protocol (JSON)"
  - [ ] Verify file download
  - [ ] Check JSON structure
- [ ] **SAP Export**:
  - [ ] Click "Download SAP (JSON)"
  - [ ] Verify file download
  - [ ] Check statistical analysis plan structure
- [ ] **Claims Export**:
  - [ ] Click "Download Claims (JSON)"
  - [ ] Verify file download
  - [ ] Check all claims included

### **4. ⚛️ Quantum Engine Testing**

#### **Real Quantum Calculations**
- [ ] **No Simulations** - Verify all calculations are real
- [ ] **Complex Amplitudes** - Check quantum states have complex values
- [ ] **Normalization** - Verify quantum state normalization
- [ ] **Virtue Supervision** - Check ethical constraints applied

#### **FoT Claims System**
- [ ] **Complete Provenance** - Verify all claims have full audit trails
- [ ] **Evidence Tracking** - Check evidence sources and timestamps
- [ ] **Collapse Policies** - Verify collapse criteria enforcement
- [ ] **Uncertainty Quantification** - Check quantum uncertainty measurements

### **5. 🔒 Security & Compliance Testing**

#### **Data Integrity**
- [ ] **ALCOA+ Compliance** - Verify all data meets ALCOA+ principles
- [ ] **Audit Trails** - Check complete audit trail for all operations
- [ ] **Data Validation** - Verify all data passes validation checks

#### **Regulatory Compliance**
- [ ] **FDA 21 CFR Part 11** - Check electronic records compliance
- [ ] **ICH E6 (R2)** - Verify Good Clinical Practice implementation
- [ ] **EMA GCP** - Check European compliance
- [ ] **ISO 14155** - Verify medical device standards

### **6. 🎨 UI/UX Testing**

#### **Responsive Design**
- [ ] **Wide Layout** - Test with wide screen
- [ ] **Sidebar Functionality** - Verify sidebar interactions
- [ ] **Tab Navigation** - Test all tab switches
- [ ] **Form Interactions** - Test all input fields and buttons

#### **Error Handling**
- [ ] **Invalid JSON** - Test with malformed JSON in readiness gates
- [ ] **Missing Data** - Test with incomplete trial data
- [ ] **Edge Cases** - Test with extreme values

### **7. 🚀 Performance Testing**

#### **Response Times**
- [ ] **Quantum Calculations** - Should complete in < 1 second
- [ ] **Data Validation** - Should be near-instantaneous
- [ ] **UI Updates** - Should be responsive
- [ ] **File Downloads** - Should be fast

#### **Concurrent Operations**
- [ ] **Multiple Claims** - Create multiple claims and verify system stability
- [ ] **Tab Switching** - Rapid tab switching should work smoothly
- [ ] **Form Submissions** - Multiple rapid form submissions

---

## 🎯 **Expected Results**

### **✅ Successful Operations**
- All forms should submit successfully
- All buttons should respond immediately
- All data should be validated and stored
- All FoT claims should be created with complete provenance
- All exports should download valid JSON files

### **⚠️ Warning Cases**
- Invalid data should show appropriate warnings
- Missing fields should be clearly indicated
- Quality issues should be flagged with specific recommendations

### **❌ Error Cases**
- Malformed JSON should show parse errors
- System should gracefully handle edge cases
- All errors should be logged and recoverable

---

## 📊 **Testing Summary**

After completing all tests, you should have:
- [ ] **Complete Trial Workflow** - From Phase 0 through Phase III
- [ ] **Multiple FoT Claims** - Various types of claims created
- [ ] **Data Validation** - All readiness gates tested
- [ ] **Export Files** - Protocol, SAP, and claims JSON files
- [ ] **Quantum Calculations** - Real quantum mechanics verified
- [ ] **Regulatory Compliance** - All standards met

---

## 🏆 **Success Criteria**

The UI testing is successful when:
1. **All tabs function correctly** with proper data flow
2. **All forms submit successfully** with appropriate feedback
3. **All quantum calculations complete** without errors
4. **All FoT claims are created** with complete provenance
5. **All exports work** and produce valid files
6. **No simulations detected** - all calculations are real
7. **Complete audit trails** maintained throughout

**🚀 Ready for Production Use!**
