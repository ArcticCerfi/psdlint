# PSDLint

**PSDLint** is a command-line tool for analyzing and fixing issues in PSD files, specifically tailored for Live2D workflows. It helps ensure your PSD files are clean, organized, and ready for use in Live2D.

---

## Features
- **Layer Validation**: Detect invalid layer names and fix them.
- **Duplicate Layer Names**: Automatically rename duplicate layers.
- **String Replacement**: Replace specific strings in layer names.
- **Group Prefixing**: Add custom prefixes to layer groups.
- **Backup Support**: Create backups before making changes.
- **Tree Visualization**: Display a filtered tree of relevant layers.

---

## Installation
Clone the repository and install the required dependencies:
```bash
git clone https://github.com/<username>/psdlint.git
cd psdlint
pip install -r requirements.txt
