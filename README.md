# PSDLint

a command-line tool for analyzing and fixing issues in PSD files for use in Live2D Cubism.
---

PSDLint is a command-line tool designed to support Live2D artists and riggers by ensuring your PSD files follow the strict naming conventions required by Live2D Cubism. When layer names don't meet these standards, Cubism assigns generic names like ArtMesh1, ArtMesh2, and so on—leading to frustration, confusion, and extra cleanup work during the rigging process.

PSDLint scans your PSD files and flags any layers that don't comply with Cubism's naming rules, helping you catch issues early and maintain clean, coherent layer IDs. Whether you're preparing a PSD for rigging or checking a client's file, this tool helps save time and sanity by enforcing consistent, rig-friendly naming practices.

Stop suffering through chaotic layer names—lint your PSDs before importing!

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

### 1. Install Python
Download and install Python from https://www.python.org/downloads/

### 2. Install PSDLint
```bash
git clone https://github.com/<username>/psdlint.git
cd psdlint
pip install .
```

🔧 Heads up: If you're getting a “command not found” or similar error after installing, you might need to add Python’s Scripts folder to your system’s PATH (Environment Variables).

On Windows, that usually looks like:

```
C:\Users\YourName\AppData\Local\Programs\Python\Python3x\Scripts
```

Make sure you restart your terminal after updating your PATH!

## Usage

Run psdlint with the desired options:
```bash
psdlint <file.psd> [options]
```

Examples:
Validate and print the PSD tree:
```bash
psdlint example.psd
```

Create a backup and fix invalid & duplicate layer names:
```bash
python cli.py example.psd -b -fi -fd
```

Create a backup and replace a string in all layer names:
```bash
psdlint example.psd -b -r "OldName" "NewName"
```

Create a backup and add a prefix to all group names:
```bash
psdlint example.psd -b -pg "GROUP_"
```
