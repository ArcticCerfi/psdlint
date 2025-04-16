# PSDLint

a command-line tool for analyzing and fixing issues in PSD files for use in Live2D Cubism.
---

PSDLint is a command-line tool designed to support Live2D artists and riggers by ensuring your PSD files follow the strict naming conventions required by Live2D Cubism. When layer names don't meet these standards, Cubism assigns generic names like ArtMesh1, ArtMesh2, and so on - leading to frustration, confusion, and extra cleanup work during the rigging process.

PSDLint scans your PSD files and flags any layers that don't comply with Cubism's naming rules, helping you catch issues early and maintain clean, coherent layer IDs. Whether you're preparing a PSD for rigging or checking a client's file, this tool helps save time and sanity by enforcing consistent, rig-friendly naming practices.

Stop suffering through chaotic layer names - lint your PSDs before importing!

## Features
- **Layer Validation**: Detect invalid layer names and fix them.
- **Duplicate Layer Names**: Automatically rename duplicate layers.
- **String Replacement**: Replace specific strings in layer names.
- **Group Prefixing**: Add custom prefixes to layer groups.
- **Backup Support**: Create backups before making changes.
- **Tree Visualization**: Display a filtered tree of relevant layers.

---

![Unbenannt](https://github.com/user-attachments/assets/2623cff1-4ec3-48f1-9ce9-cc86b72f6ec2)
![Unbenannt](https://github.com/user-attachments/assets/21da00c3-3083-4368-bd16-8e627471a9ad)

## Installation

### 1. Install Python

If you haven’t already:

1. Go to https://www.python.org/downloads/
2. Download the latest version of Python (make sure to check "Add Python to PATH" during installation!)

### 2. Get PSDLint
#### Option A - Download the Zip

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
git clone https://github.com/ArcticCerfi/psdlint.git
cd psdlint
pip install .
```

## Usage

```
usage: psdlint [-h] [-t] [-pg [PREFIXGROUPS]] [-b] [-r TARGET REPLACEMENT] [-fi] [-fd] file

Check and process PSD files for Live2D.

positional arguments:
  file                                  Path to the PSD file

options:
  -h, --help                            show this help message and exit
  -t, --trimmtree                       Only show relevant layers in the PSD's layer tree.
  -pg, --prefixgroups [PREFIXGROUPS]    Prepend a custom prefix to all layer groups. (default: 'GROUP_')
  -b, --backup                          Create a backup of the PSD file before processing.
  -r, --replace TARGET REPLACEMENT      Replace a string of characters with another string of characters across all layers.
  -fi, --fixinvalid                     Fix invalid layer names by trimming strings & replacing spaces and special characters with underscores.
  -fd, --fixduplicate                   Fix duplicate layer names by appending a number. (eg. 'Layer' -> 'Layer_1')
```


### Examples:
Validate and print the PSD tree:
```bash
psdlint example.psd
```

Create a backup and fix invalid & duplicate layer names:
```bash
psdlint example.psd -b -fi -fd
```

Create a backup and replace a string in all layer names:
```bash
psdlint example.psd -b -r "OldName" "NewName"
```

Create a backup and add a prefix to all group names:
```bash
psdlint example.psd -b -pg "GROUP_"
```
