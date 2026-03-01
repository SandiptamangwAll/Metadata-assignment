# Network Forensics Image Metadata Tool

**A GUI-based Python application for extracting, analyzing, sanitizing, and reporting EXIF metadata from images in cybersecurity and digital forensics contexts.**

**Module:** ST4017CMD – Introduction to Programming  
**Submitted by:** Sandip  
**Student ID:** [Your Student ID – replace this]  
**Institution:** Softwarica College of IT & E-Commerce / Coventry University  
**Date:** March 2026

## Project Overview

This tool helps ethical hackers, incident responders, and digital forensics analysts quickly inspect and clean sensitive metadata (especially GPS location, device fingerprints, and editing history) from JPEG/TIFF images before sharing or including them in reports.

Key features:
- Load single image or batch folder (demo mode: first 5 images)
- Extract and display all EXIF tags in a sortable table
- Privacy risk scoring (Low / High) with visual feedback
- Sanitize (remove) sensitive tags like GPS coordinates, camera make/model, software
- Export forensic report in JSON format
- Audit logging for traceability

Built with pure Python using only two lightweight dependencies: `exif` and `Pillow`.

## Screenshots

(Add 3–5 screenshots here after running the app – commit them in a folder called `screenshots/`)

Examples:
- Main GUI with metadata table and HIGH risk warning
- Sanitization confirmation dialog
- Exported JSON report

## Features Demonstrated (Coursework Alignment)

- Custom data structure: `MetadataTag` class
- File I/O and binary parsing (EXIF extraction)
- Event-driven GUI programming with Tkinter
- Risk assessment algorithm
- JSON serialization for reporting
- Error handling & user-friendly messages
- Version control (GitHub Classroom commits)

## Requirements

- Python 3.8+
- Operating System: Windows / Linux / macOS

### Dependencies

```text
exif
Pillow

Install with:
Bashpip install -r requirements.txt
Installation & Usage

Clone the repository:Bashgit clone https://github.com/[your-classroom-org]/[your-repo-name].git
cd [your-repo-name]
Install dependencies:Bashpip install exif Pillow
Run the application:Bashpython main.py
Usage steps:
Click Select Single Image or Select Folder (Batch)
View extracted metadata and risk score
Click Sanitize & Save Cleaned Image to remove sensitive tags
Click Export JSON Report to save forensic documentation


Project Structure
textforensics-metadata-tool/
├── main.py                 # Main GUI application
├── requirements.txt        # Dependencies
├── README.md               # This file
├── screenshots/            # (optional) GUI screenshots
└── tests/                  # (future) unit tests
Testing

Unit tests planned for MetadataTag and MetadataExtractor classes
Manual testing performed on:
Images with full EXIF (GPS present)
Images without metadata
Corrupted / invalid files

Achieved stable extraction and sanitization on sample JPEGs

Limitations & Future Improvements

Supports only JPEG/TIFF (EXIF carriers)
Batch processing limited to first 5 files (demo mode)
No support for HEIC, WebP, PNG (XMP/IPTC)
Risk scoring is rule-based (can be enhanced with ML)
Future: recursive folder scan, tampering detection, CLI mode

GitHub Classroom Commit History
All development tracked with meaningful commits.
See the Commits tab for full history (28+ commits during development).
Demonstration Video
A 10-minute video walkthrough is submitted separately, showing:

Repository overview
Running the application
Loading & extracting metadata
Sanitizing an image
Exporting JSON report
