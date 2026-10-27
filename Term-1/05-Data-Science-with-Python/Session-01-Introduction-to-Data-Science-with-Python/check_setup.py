# check_setup.py
# Run this first to confirm your computer is ready for the module.
# Command:  python check_setup.py

import sys  # sys tells us about the Python interpreter itself

print("Python version:", sys.version.split()[0])

# The list of libraries we will use in this module
libraries = ["numpy", "pandas", "matplotlib", "seaborn", "sklearn"]

for name in libraries:
    try:
        module = __import__(name)            # try to import the library by its name
        version = getattr(module, "__version__", "unknown")
        print(f"OK      {name:<11} version {version}")
    except ImportError:
        print(f"MISSING {name:<11} -> install with: pip install {name if name != 'sklearn' else 'scikit-learn'}")
