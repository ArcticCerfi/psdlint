from utils.layers import traverse_layers
import re

def prepend_group_prefix(psd, prefix="GROUP"):
    if not prefix.endswith("_"):
        prefix += "_"

    def apply_prefix(layer):
        if layer.is_group() and not layer.name.startswith(prefix):
            layer.name = f"{prefix}{layer.name}"

    traverse_layers(psd, apply_prefix)

def replace_spaces(psd):
    def clean_name(layer):
        layer.name = re.sub(r"[^a-zA-Z0-9_]", "_", layer.name.strip().replace(" ", "_"))
        if layer.name and layer.name[0].isdigit():
            layer.name = f"_{layer.name}"

    traverse_layers(psd, clean_name)

def fix_duplicates(psd):
    seen_names = {}

    def rename_duplicates(layer):
        original_name = layer.name
        if original_name in seen_names:
            counter = seen_names[original_name] + 1
            while f"{original_name}_{counter}" in seen_names:
                counter += 1
            layer.name = f"{original_name}_{counter}"
            seen_names[original_name] = counter
        else:
            seen_names[original_name] = 0

    traverse_layers(psd, rename_duplicates)