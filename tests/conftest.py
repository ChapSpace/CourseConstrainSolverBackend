# conftest.py
import sys
import os

# Get the absolute path of the src directory
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Add the src directory to the system path if it's not already there
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Optional: Print sys.path to verify it's been added
print(f"Added to PYTHONPATH: {src_path}")
