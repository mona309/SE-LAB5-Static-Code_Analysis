# Lab 5: Static Code Analysis

## Overview
This repository contains the completed static code analysis lab for `inventory_system.py` using Pylint, Bandit, and Flake8.

## Results Summary

| Metric | Before | After |
|--------|--------|-------|
| Pylint Score | 4.80/10 | 10.00/10 |
| Bandit Issues | 2 | 0 |
| Flake8 Issues | 11 | 0 |

## Files Included

- `inventory_system.py` - Fixed Python code
- `reflection.md` - Lab reflection answers
- `pylint_report.txt` - Initial Pylint results
- `bandit_report.txt` - Initial Bandit results
- `flake8_report.txt` - Initial Flake8 results

## Issues Fixed

### Security (2)
- Removed `eval()` usage (B307)
- Fixed bare except clause (B110, W0702, E722)

### Logic Bugs (2)
- Fixed mutable default argument (W0102)
- Implemented context managers for files (R1732)

### Style & Documentation (10)
- Removed unused import (W0611, F401)
- Added blank lines per PEP 8 (E302, E305)
- Converted to f-strings (C0209)
- Renamed functions to snake_case (C0103)
- Added module docstring (C0114)
- Added function docstrings (C0116)
- Added encoding to file operations (W1514)
- Suppressed global statement warning (W0603)

## Running the Code
```bash
# Install tools
pip install pylint bandit flake8

# Run analysis
pylint inventory_system.py
bandit -r inventory_system.py
flake8 inventory_system.py

# Run program
python inventory_system.py
```

## Student Information
- **Lab**: Lab 5 - Static Code Analysis
- **Name**: Monisha Sharma
- **SRN**: PES2UG23CS906
- **Date**: October 27, 2025
- **Status**: Complete - All issues fixed

---

**Final Score: 10.00/10** ✅
