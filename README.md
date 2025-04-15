# PSDLint

a command-line tool for analyzing and fixing issues in PSD files for use in Live2D Cubism.
---

PSDLint is a command-line tool designed to support Live2D artists and riggers by ensuring your PSD files follow the strict naming conventions required by Live2D Cubism. When layer names don't meet these standards, Cubism assigns generic names like ArtMesh1, ArtMesh2, and so on - leading to frustration, confusion, and extra cleanup work during the rigging process.

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

If you haven’t already:

1. Go to https://www.python.org/downloads/
2. Download the latest version of Python (make sure to check "Add Python to PATH" during installation!)

### 2. Get PSDLint
#### Option A - Download Zip
Option A – Download the ZIP (easiest)

1. Go to the GitHub repo: https://github.com/ArctiCerfi/psdlint
2. Click Code → Download ZIP
3. Unzip the folder in a permanent location (e.g. Create a folder C:/Tools)
4. Open a terminal and navigate to the folder, e.g.:
```bash
cd C:\Tools\psdlint
```
5. Then install with
```bash
pip install .
```

#### Option B – Use Git
If you have Git installed, you can just:
```bash
git clone https://github.com/<username>/psdlint.git
cd psdlint
pip install .
```

## Usage

Run psdlint with the desired options:
```bash
psdlint <file.psd> [options]
```

### Examples:
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
