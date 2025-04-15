# PSDLint

a command-line tool for analyzing and fixing issues in PSD files for use in Live2D Cubism.
---

Live2D Cubism  
PSDLint is a CLI tool meant to relief Live2D artists & riggers in  it helps ensure your PSD files abide by Live2D Cubism ID naming conventions, so that no incoherent ID's are generated when loading in your PSD.

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

## Usage

Run psdlint with the desired options:
```bash
psdlint <file.psd> [options]
```

Examples:
Validate and print the PSD tree:
```
psdlint example.psd
```

Create a backup and fix invalid & duplicate layer names:
```
python cli.py example.psd -b -fi -fd
```

Create a backup and replace a string in all layer names:
```
psdlint example.psd -b -r "OldName" "NewName"
```

Create a backup and add a prefix to all group names:
```
psdlint example.psd -b -pg "GROUP_"
```
