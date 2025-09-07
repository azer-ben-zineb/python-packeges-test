# Python Package Tester

A comprehensive Python script to test and validate Python packages installed in your NixOS system. This tool helps you quickly verify which packages are available, their versions, and performs basic functionality tests.

## Features

- 🔍 **Package Detection**: Tests imports for common Python packages
- 📊 **Version Information**: Displays version numbers for successfully imported packages
- ✅ **Functionality Testing**: Performs basic operations to verify packages work correctly
- 📈 **Detailed Reporting**: Provides success rates and comprehensive summaries
- 🐍 **System Information**: Shows Python version and configuration details
- 🎯 **NixOS Optimized**: Specifically designed for NixOS environments

## Tested Package Categories

### Data Science & Scientific Computing
- NumPy - Numerical computing
- Matplotlib - Plotting and visualization
- Pandas - Data manipulation and analysis
- SciPy - Scientific computing

### Development Tools
- Requests - HTTP library
- Black - Code formatter
- Flake8 - Code linting
- Pytest - Testing framework
- Sphinx - Documentation generator

### Package Management
- Pip - Package installer
- Setuptools - Package building
- Wheel - Package format
- Virtualenv - Virtual environments

### System & Utilities
- AWS CLI - Amazon Web Services CLI
- YQ - YAML/JSON processor
- HTTPie - HTTP client
- Jupyter - Interactive notebooks
- LLDB - Debugger
- Meson - Build system

### Standard Library
- JSON, OS, Sys, Math, Random - Core Python modules

## Usage

### Basic Usage

```bash
python pythin.py
```



## Code Structure

### Main Functions

#### `test_package(package_name: str, import_name: str = None) -> Tuple[str, bool, str]`
Tests if a package can be imported and retrieves its version information.

**Parameters:**
- `package_name`: Display name of the package
- `import_name`: Name to use for importing (if different from package_name)

**Returns:**
- Tuple containing: (package_name, success_status, version_or_error_message)

#### `main()`
The main function that orchestrates the testing process:
1. Tests all predefined packages
2. Categorizes results into successful and failed imports
3. Displays comprehensive reporting
4. Shows Python system information
5. Performs quick functionality tests

## Customization

### Adding New Packages

To test additional packages, modify the `packages_to_test` list in the `main()` function:

```python
packages_to_test = [
    # Existing packages...
    ("Your Package", "your_package_import_name"),
    ("Another Package", "another_package"),
]
```

### Modifying Functionality Tests

Add custom functionality tests in the "QUICK FUNCTIONALITY TESTS" section:

```python
try:
    import your_package
    # Your test code here
    print(f"  ✅ Your package test passed")
except:
    print(f"  ❌ Your package test failed")
```

## Requirements

- Python 3.6+
- No external dependencies required (uses only standard library)
- Designed for NixOS but works on other systems

## Installation

1. Download the script:
   ```bash
   wget https://your-repo/pythin.py
   ```

2. Make it executable:
   ```bash
   chmod +x pythin.py
   ```

3. Run the script:
   ```bash
   python pythin.py
   ```

## Use Cases

- **Environment Validation**: Verify your Python environment setup
- **Dependency Checking**: Ensure required packages are installed
- **System Diagnostics**: Troubleshoot Python package issues
- **CI/CD Integration**: Include in automated testing pipelines
- **Development Setup**: Validate development environment configuration

## Output Interpretation

### Success Indicators
- ✅ Green checkmarks indicate successful imports
- Version numbers show package availability and version info
- Functionality tests confirm packages work correctly

### Failure Indicators
- ❌ Red X marks show failed imports
- Error messages provide specific failure reasons
- Missing packages are clearly identified

## Troubleshooting

### Common Issues

1. **Import Errors**: Package not installed or not in Python path
2. **Version Detection Failures**: Package lacks standard version attributes
3. **Functionality Test Failures**: Package imported but basic operations fail

### Solutions

- **NixOS**: Use `nix-env -iA` or add packages to your configuration
- **Other Systems**: Use `pip install package-name`
- **Path Issues**: Check `PYTHONPATH` environment variable

## Contributing

Feel free to contribute by:
- Adding more packages to test
- Improving version detection logic
- Adding more comprehensive functionality tests
- Enhancing output formatting

## License

This project is open source. Feel free to use, modify, and distribute as needed.
