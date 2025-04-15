from psd_tools import PSDImage
import argparse
from utils.layers import validate_layer_names, check_duplicate_layers, collect_layer_names
from utils.tree import generate_tree, print_tree
from utils.color import CColor
import utils.fixes as fixes


def parse_arguments():
    parser = argparse.ArgumentParser(description="Check and process PSD files for Live2D.")
    parser.add_argument("file", help="Path to the PSD file")
    parser.add_argument("-t", "--trimmtree", action="store_true", help="Only show relevant layers in the PSD's layer tree.")
    parser.add_argument("-pg", "--prefixgroups", nargs="?", const="GROUP_", help="Prepend a custom prefix to all layer groups. (default: 'GROUP_')")
    parser.add_argument("-b", "--backup", action="store_true", help="Create a backup of the PSD file before processing.")
    parser.add_argument("-r", "--replace", nargs=2, metavar=("TARGET", "REPLACEMENT"), help="Replace a string of characters with another string of characters across all layers.")
    parser.add_argument("-fi", "--fixinvalid", action="store_true", help="Fix invalid layer names by trimming strings & replacing spaces and special characters with underscores.")
    parser.add_argument("-fd", "--fixduplicate", action="store_true", help="Fix duplicate layer names by appending a number. (eg. 'Layer' -> 'Layer_1')")
    
    return parser.parse_args()

def print_psd_stats(psd, path):
    print()
    print(f"PSD Path: \"{CColor.YELLOW}{path}{CColor.RESET}\"")
    print(f"Resolution: {CColor.DIM}{psd.width}x{psd.height}{CColor.RESET}")
    print(f"Layers: {CColor.DIM}{len(collect_layer_names(psd, True))}{CColor.RESET}")

def validate_and_print_tree(psd, args):
    invalid_names = validate_layer_names(psd)
    duplicates = check_duplicate_layers(psd)

    filtered_tree = generate_tree(psd, invalid_names, duplicates, args.trimmtree)
    print_tree(filtered_tree)

    print_psd_stats(psd, args.file)

    if invalid_names or duplicates:
        print()
        print(f"❌ {CColor.RED}Issues found! This PSD will generate incoherent IDs in Live2D.{CColor.RESET}")
    else:
        print()
        print(f"✅ {CColor.GREEN}No issues found! This PSD is Live2D ready!{CColor.RESET}")

def process_psd(psd, args):
    if args.backup:
        backup_file = args.file + ".bak"
        save_psd(psd, backup_file, f"Backup created: {CColor.YELLOW}{backup_file}{CColor.RESET}")

    if args.replace:
        target, replacement = args.replace
        fixes.replace_layer_names(psd, target, replacement)
        save_psd(psd, args.file, f"Layer names replaced successfully!")

    if args.prefixgroups:
        fixes.prepend_group_prefix(psd, args.prefixgroups)
        save_psd(psd, args.file, f"Group layers renamed successfully!")

    if args.fixinvalid:
        fixes.replace_spaces(psd)
        save_psd(psd, args.file, f"Spaces replaced successfully!")

    if args.fixduplicate:
        fixes.fix_duplicates(psd)
        save_psd(psd, args.file, f"Duplicate layers renamed successfully!")

def save_psd(psd, file_path, message):
    psd.save(file_path)
    print(message)


def main():
    args = parse_arguments()

    if not args.file.lower().endswith('.psd'):
        print("Error: This file is not a PSD file.")
        exit(1)

    psd = PSDImage.open(args.file)

    process_psd(psd, args)
    validate_and_print_tree(psd, args)

if __name__ == "__main__":
    main()