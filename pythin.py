import sys
import importlib
from typing import List, Tuple

def test_package(package_name: str, import_name: str = None) -> Tuple[str, bool, str]:
    """
    Test if a package can be imported and get its version
    
    Args:
        package_name: Display name of the package
        import_name: Name to use for importing (if different from package_name)
    
    Returns:
        Tuple of (package_name, success, version_or_error)
    """
    if import_name is None:
        import_name = package_name.lower()
    
    try:
        module = importlib.import_module(import_name)
        
        # Try to get version
        version = "Unknown"
        for attr in ['__version__', 'version', 'VERSION']:
            if hasattr(module, attr):
                version = str(getattr(module, attr))
                break
        
        return (package_name, True, version)
    
    except ImportError as e:
        return (package_name, False, str(e))
    except Exception as e:
        return (package_name, False, f"Error: {str(e)}")

def main():
    """Test all packages found in your NixOS system"""
    
    print("🔍 Testing Python packages in your NixOS system...")
    print("=" * 60)
    
    packages_to_test = [
        ("NumPy", "numpy"),
        ("Matplotlib", "matplotlib"),
        ("Pandas", "pandas"),
        ("SciPy", "scipy"),
        
        ("Requests", "requests"),
        ("Black", "black"),
        ("Flake8", "flake8"),
        ("Pytest", "pytest"),
        ("Sphinx", "sphinx"),
        
        ("Pip", "pip"),
        ("Setuptools", "setuptools"),
        ("Wheel", "wheel"),
        ("Virtualenv", "virtualenv"),
        
        ("AWS CLI", "awscli"),
        
        ("YQ", "yq"),
        
        ("HTTPie", "httpie"),
        
        ("Jupyter", "jupyter"),
        
        ("LLDB", "lldb"),
        
        ("Meson", "mesonbuild"),
        
        ("JSON", "json"),
        ("OS", "os"),
        ("Sys", "sys"),
        ("Math", "math"),
        ("Random", "random"),
    ]
    
    # Test all packages
    results = []
    successful = 0
    failed = 0
    
    for package_name, import_name in packages_to_test:
        result = test_package(package_name, import_name)
        results.append(result)
        
        if result[1]:  
            successful += 1
        else:
            failed += 1
    
    print("\n✅ SUCCESSFUL IMPORTS:")
    print("-" * 40)
    for name, success, version in results:
        if success:
            print(f"  {name:<15} | Version: {version}")
    
    if failed > 0:
        print("\n❌ FAILED IMPORTS:")
        print("-" * 40)
        for name, success, error in results:
            if not success:
                print(f"  {name:<15} | {error}")
    
    print("\n" + "=" * 60)
    print(f"📊 SUMMARY:")
    print(f"  Total packages tested: {len(packages_to_test)}")
    print(f"  ✅ Successful: {successful}")
    print(f"  ❌ Failed: {failed}")
    print(f"  📈 Success rate: {(successful/len(packages_to_test)*100):.1f}%")
    
    print(f"\n🐍 PYTHON INFO:")
    print(f"  Python version: {sys.version}")
    print(f"  Python executable: {sys.executable}")
    print(f"  Python path entries: {len(sys.path)}")
    
    print(f"\n🧪 QUICK FUNCTIONALITY TESTS:")
    try:
        import numpy as np
        arr = np.array([1, 2, 3, 4, 5])
        print(f"  ✅ NumPy array creation: {arr.mean():.1f} (mean of [1,2,3,4,5])")
    except:
        print(f"  ❌ NumPy test failed")
    
    try:
        import requests
        print(f"  ✅ Requests module ready for HTTP calls")
    except:
        print(f"  ❌ Requests test failed")
    
    try:
        import matplotlib
        print(f"  ✅ Matplotlib ready for plotting")
    except:
        print(f"  ❌ Matplotlib test failed")
    
    try:
        import pandas as pd
        df = pd.DataFrame({'test': [1, 2, 3]})
        print(f"  ✅ Pandas DataFrame creation: {len(df)} rows")
    except:
        print(f"  ❌ Pandas test failed")

if __name__ == "__main__":
    main()
