# Network Forensics Image Metadata Tool

**A GUI-based Python application for extracting, analyzing, sanitizing, and reporting EXIF metadata from images in cybersecurity and digital forensics contexts.**

**Module:** ST4017CMD – Introduction to Programming  
**Submitted by:** Sandip  
**Student ID:**250589
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

- Python 3.14.0
- Operating System: Windows / Linux / macOS

