#!/bin/bash
# This script sets the PYTHONPATH to include the src directory

# Get the absolute path to the current directory (repository root)
REPO_ROOT="$(pwd)"

# Append the src/ directory to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:${REPO_ROOT}/src"

# Print the new PYTHONPATH to confirm
echo "PYTHONPATH has been set to include ${REPO_ROOT}/src"
