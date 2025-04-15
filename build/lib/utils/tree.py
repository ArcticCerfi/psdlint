from utils.color import CColor
from utils.layers import collect_layer_names

class TreeNode:
    def __init__(self, name, node_type="group", status=None):
        self.name = name
        self.node_type = node_type  # "group" or "layer"
        self.status = status  # "invalid", "duplicate", or None
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def to_dict(self):
        return {
            "name": self.name,
            "type": self.node_type,
            "status": self.status,
            "children": [child.to_dict() for child in self.children],
        }

    def __repr__(self):
        return f"TreeNode(name={self.name}, type={self.node_type}, status={self.status})"
    
def generate_tree(psd, invalid_names, duplicates, filter_important=False):
    node = TreeNode("Root", "group")

    for layer in psd:
        layer_name = layer.name

        is_invalid = layer_name in invalid_names
        is_duplicate = layer_name in duplicates

        status = ", ".join(filter(None, [
            "invalid" if is_invalid else None,
            "duplicate" if is_duplicate else None
        ])) or None

        if layer.is_group():
            child_tree = generate_tree(layer, invalid_names, duplicates, filter_important)
            if child_tree.children or not filter_important or is_invalid or is_duplicate:
                group_node = TreeNode(layer_name, "group", status)
                group_node.children = child_tree.children
                node.add_child(group_node)
        else:
            if not filter_important or is_invalid or is_duplicate:
                node.add_child(TreeNode(layer_name, "layer", status))

    return node

def print_tree(node, indent="", is_last=True):
    group_icon = "📂"
    layer_icon = "📄"
    icon = group_icon if node.node_type == "group" else layer_icon
    status_label = ""

    if node.status:
        if node.status and "invalid" in node.status:
            status_label += f"{CColor.RED}{CColor.BOLD}[Invalid]{CColor.RESET} "
        if node.status and "duplicate" in node.status:
            status_label += f"{CColor.MAGENTA}{CColor.BOLD}[Duplicate]{CColor.RESET} "

    connector = "└── " if is_last else "├── "
    print(f"{indent}{connector}{icon} {node.name} {status_label}")

    child_indent = indent + ("   " if is_last else "│  ")
    for i, child in enumerate(node.children):
        print_tree(child, child_indent, (i == len(node.children) - 1))
