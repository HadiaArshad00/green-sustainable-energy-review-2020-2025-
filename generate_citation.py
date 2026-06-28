#!/usr/bin/env python3
"""
Citation Generator for Green and Sustainable Energy Review
Generates citations in multiple formats (BibTeX, APA, MLA, Chicago)

Usage:
    python generate_citation.py --format bibtex
    python generate_citation.py --format apa
    python generate_citation.py --format mla
    python generate_citation.py --format chicago
    python generate_citation.py --all
"""

import argparse
import sys
from datetime import datetime

# Paper metadata
METADATA = {
    "title": "Green and Sustainable Energy: Emerging Technologies, Global Trends, and Future Directions — A Comprehensive Review (2020–2025)",
    "author": "Hadia Arshad",
    "year": 2026,
    "doi": "10.5281/zenodo.20782240",
    "journal": "Zenodo",
    "url": "https://doi.org/10.5281/zenodo.20782240",
    "publisher": "Zenodo",
}


def generate_bibtex() -> str:
    """Generate BibTeX citation format."""
    return """@article{arshad2026green,
  title     = {Green and Sustainable Energy: Emerging Technologies, Global Trends, and Future Directions — A Comprehensive Review (2020–2025)},
  author    = {Arshad, Hadia},
  journal   = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.20782240},
  url       = {https://doi.org/10.5281/zenodo.20782240},
  publisher = {Zenodo}
}"""


def generate_apa() -> str:
    """Generate APA 7th edition citation format."""
    return "Arshad, H. (2026). Green and Sustainable Energy: Emerging Technologies, Global Trends, and Future Directions — A Comprehensive Review (2020–2025). Zenodo. https://doi.org/10.5281/zenodo.20782240"


def generate_mla() -> str:
    """Generate MLA 9th edition citation format."""
    return 'Arshad, Hadia. "Green and Sustainable Energy: Emerging Technologies, Global Trends, and Future Directions — A Comprehensive Review (2020–2025)." Zenodo, 2026, doi:10.5281/zenodo.20782240.'


def generate_chicago() -> str:
    """Generate Chicago 17th edition citation format."""
    return 'Arshad, Hadia. "Green and Sustainable Energy: Emerging Technologies, Global Trends, and Future Directions — A Comprehensive Review (2020–2025)." Zenodo (2026). https://doi.org/10.5281/zenodo.20782240.'


def generate_all() -> str:
    """Generate all citation formats."""
    separator = "=" * 70
    return f"""{separator}
BIBTEX
{separator}
{generate_bibtex()}

{separator}
APA 7th Edition
{separator}
{generate_apa()}

{separator}
MLA 9th Edition
{separator}
{generate_mla()}

{separator}
Chicago 17th Edition
{separator}
{generate_chicago()}

{separator}
"""


def main():
    parser = argparse.ArgumentParser(
        description="Generate citations for the Green and Sustainable Energy Review"
    )
    parser.add_argument(
        "--format",
        choices=["bibtex", "apa", "mla", "chicago"],
        default="bibtex",
        help="Citation format (default: bibtex)"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Generate all citation formats"
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        help="Output file path (default: print to stdout)"
    )

    args = parser.parse_args()

    if args.all:
        citation = generate_all()
    else:
        formatters = {
            "bibtex": generate_bibtex,
            "apa": generate_apa,
            "mla": generate_mla,
            "chicago": generate_chicago,
        }
        citation = formatters[args.format]()

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(citation)
        print(f"Citation saved to {args.output}")
    else:
        print(citation)


if __name__ == "__main__":
    main()
