import re
from collections import Counter

VALID_LAYER_NAME_PATTERN = r'^[a-zA-Z_][a-zA-Z0-9_]{0,62}$'

def traverse_layers(psd, callback):
    stack = list(psd)
    while stack:
        layer = stack.pop()
        callback(layer)
        if layer.is_group():
            stack.extend(layer)

def collect_layer_names(psd, exclude_groups=False):
    layer_names = []

    def add_layer_name(layer):
        if not layer.is_group() or not exclude_groups:
            layer_names.append(layer.name)

    traverse_layers(psd, add_layer_name)
    return layer_names

def check_duplicate_layers(psd):
    layer_names = collect_layer_names(psd)
    return [name for name, count in Counter(layer_names).items() if count > 1]

def validate_layer_names(psd):
    layer_names = collect_layer_names(psd)
    return [name for name in layer_names if not re.match(VALID_LAYER_NAME_PATTERN, name)]