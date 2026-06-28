#!/usr/bin/env python3
"""
Repository Validation Script
Checks that all required files are present and properly formatted.

Usage:
    python validate_repo.py
"""

import os
import json
import sys
from pathlib import Path

# Required files and their descriptions
REQUIRED_FILES = {
    "README.md": "Main project documentation",
    "CITATION.cff": "Citation metadata file",
    "LICENSE": "License file (CC-BY-4.0)",
    ".zenodo.json": "Zenodo metadata",
    ".gitignore": "Git ignore rules",
    "requirements.txt": "Python dependencies",
    "setup.py": "Package setup configuration",
    "CONTRIBUTING.md": "Contribution guidelines",
    "generate_citation.py": "Citation generator utility",
    ".github/FUNDING.yml": "Funding configuration",
}

# Optional files
OPTIONAL_FILES = {
    "Green_and_Sustainable_Energy_Review_2020-2025.pdf": "Main review paper",
}


def check_file_exists(filepath: str) -> bool:
    """Check if a file exists."""
    return os.path.isfile(filepath)


def validate_json(filepath: str) -> tuple[bool, str]:
    """Validate JSON file format."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            json.load(f)
        return True, "Valid JSON"
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {e}"
    except Exception as e:
        return False, f"Error reading file: {e}"


def validate_cff(filepath: str) -> tuple[bool, str]:
    """Basic validation of CITATION.cff file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        required_fields = ["cff-version", "title", "authors", "doi"]
        missing = [field for field in required_fields if field not in content]
        if missing:
            return False, f"Missing fields: {', '.join(missing)}"
        return True, "Valid CFF structure"
    except Exception as e:
        return False, f"Error: {e}"


def validate_markdown(filepath: str) -> tuple[bool, str]:
    """Basic validation of Markdown file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        if len(content.strip()) < 50:
            return False, "File appears too short"
        return True, f"Valid Markdown ({len(content)} chars)"
    except Exception as e:
        return False, f"Error: {e}"


def main():
    """Run all validation checks."""
    print("=" * 70)
    print("REPOSITORY VALIDATION REPORT")
    print("=" * 70)
    print()

    all_passed = True
    base_path = Path(".")

    # Check required files
    print("📋 REQUIRED FILES")
    print("-" * 70)
    for filename, description in REQUIRED_FILES.items():
        filepath = base_path / filename
        exists = check_file_exists(filepath)
        status = "✅ PASS" if exists else "❌ FAIL"
        print(f"{status}  {filename:40s} {description}")
        if not exists:
            all_passed = False
    print()

    # Check optional files
    print("📋 OPTIONAL FILES")
    print("-" * 70)
    for filename, description in OPTIONAL_FILES.items():
        filepath = base_path / filename
        exists = check_file_exists(filepath)
        status = "✅ FOUND" if exists else "⚠️  MISSING"
        print(f"{status}  {filename:40s} {description}")
    print()

    # Validate file contents
    print("📋 FILE CONTENT VALIDATION")
    print("-" * 70)

    # Validate .zenodo.json
    zenodo_path = base_path / ".zenodo.json"
    if check_file_exists(zenodo_path):
        valid, msg = validate_json(zenodo_path)
        status = "✅ PASS" if valid else "❌ FAIL"
        print(f"{status}  .zenodo.json: {msg}")
        if not valid:
            all_passed = False

    # Validate CITATION.cff
    cff_path = base_path / "CITATION.cff"
    if check_file_exists(cff_path):
        valid, msg = validate_cff(cff_path)
        status = "✅ PASS" if valid else "❌ FAIL"
        print(f"{status}  CITATION.cff: {msg}")
        if not valid:
            all_passed = False

    # Validate README.md
    readme_path = base_path / "README.md"
    if check_file_exists(readme_path):
        valid, msg = validate_markdown(readme_path)
        status = "✅ PASS" if valid else "❌ FAIL"
        print(f"{status}  README.md: {msg}")
        if not valid:
            all_passed = False

    # Validate CONTRIBUTING.md
    contrib_path = base_path / "CONTRIBUTING.md"
    if check_file_exists(contrib_path):
        valid, msg = validate_markdown(contrib_path)
        status = "✅ PASS" if valid else "❌ FAIL"
        print(f"{status}  CONTRIBUTING.md: {msg}")
        if not valid:
            all_passed = False

    print()
    print("=" * 70)
    if all_passed:
        print("🎉 ALL CHECKS PASSED! Repository is ready for GitHub.")
        return 0
    else:
        print("⚠️  SOME CHECKS FAILED. Please review the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
