#!/usr/bin/env python3
"""
Field of Truth Clinical Trials - Launch Script

Launches the comprehensive clinical trials management system with proper
configuration and validation.

NO SIMULATIONS - ALL MAINNET - FIELD OF TRUTH 100%
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    print("🔍 Checking dependencies...")
    
    required_packages = [
        'streamlit',
        'pandas', 
        'numpy',
        'plotly',
        'scipy'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"   ✅ {package}")
        except ImportError:
            print(f"   ❌ {package} - MISSING")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("Install with: pip install " + " ".join(missing_packages))
        return False
    
    print("✅ All required dependencies are installed")
    return True

def validate_system():
    """Run system validation tests"""
    print("\n🧪 Running system validation...")
    
    try:
        # Run the validation tests
        result = subprocess.run([
            sys.executable, 
            'tests/test_clinical_system.py'
        ], capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print("✅ System validation passed")
            return True
        else:
            print("❌ System validation failed")
            print("Error output:")
            print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print("⏰ System validation timed out")
        return False
    except Exception as e:
        print(f"❌ System validation error: {e}")
        return False

def launch_streamlit_app(port=8501, host="localhost"):
    """Launch the Streamlit application"""
    print(f"\n🚀 Launching Field of Truth Clinical Trials System...")
    print(f"   Port: {port}")
    print(f"   Host: {host}")
    print(f"   URL: http://{host}:{port}")
    print()
    print("⚛️ NO SIMULATIONS - ALL MAINNET - FIELD OF TRUTH 100%")
    print()
    
    try:
        # Launch Streamlit
        cmd = [
            sys.executable, "-m", "streamlit", "run", 
            "clinical_app.py",
            "--server.port", str(port),
            "--server.address", host,
            "--server.headless", "true",
            "--browser.gatherUsageStats", "false"
        ]
        
        subprocess.run(cmd)
        
    except KeyboardInterrupt:
        print("\n👋 Shutting down Field of Truth Clinical Trials System...")
    except Exception as e:
        print(f"❌ Error launching application: {e}")
        sys.exit(1)

def main():
    """Main launch function"""
    parser = argparse.ArgumentParser(
        description="Field of Truth Clinical Trials System Launcher",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python launch_clinical_trials.py                    # Launch with defaults
  python launch_clinical_trials.py --port 8502        # Launch on port 8502
  python launch_clinical_trials.py --skip-validation  # Skip validation tests
  python launch_clinical_trials.py --validate-only    # Only run validation
        """
    )
    
    parser.add_argument(
        "--port", 
        type=int, 
        default=8501,
        help="Port to run the application on (default: 8501)"
    )
    
    parser.add_argument(
        "--host",
        type=str,
        default="localhost", 
        help="Host to bind to (default: localhost)"
    )
    
    parser.add_argument(
        "--skip-validation",
        action="store_true",
        help="Skip system validation tests"
    )
    
    parser.add_argument(
        "--validate-only",
        action="store_true", 
        help="Only run validation tests, don't launch app"
    )
    
    args = parser.parse_args()
    
    # Print header
    print("🏥⚛️ Field of Truth Clinical Trials System")
    print("=" * 50)
    print("Quantum-Enhanced Clinical Trial Management")
    print("Phase-Aware Architecture | vQbit Quantum Substrate")
    print("FoT Claims System | Regulatory Compliance")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("clinical_app.py").exists():
        print("❌ Error: clinical_app.py not found in current directory")
        print("Please run this script from the FoTClinicalTrials directory")
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        print("\n❌ Dependency check failed. Please install missing packages.")
        sys.exit(1)
    
    # Run validation unless skipped
    if not args.skip_validation:
        if not validate_system():
            print("\n❌ System validation failed. Please fix issues before launching.")
            if not args.validate_only:
                sys.exit(1)
        else:
            print("\n✅ System validation passed. Ready for mainnet operation.")
    
    # If validate-only, exit here
    if args.validate_only:
        print("\n✅ Validation complete. System is ready.")
        sys.exit(0)
    
    # Launch the application
    launch_streamlit_app(port=args.port, host=args.host)

if __name__ == "__main__":
    main()
