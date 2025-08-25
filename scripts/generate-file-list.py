from pathlib import Path

def generate_tree_string(startpath):
    """Generates a string representation of a directory tree and counts files."""
    tree_lines = []
    startpath = Path(startpath)

    all_paths = [p for p in startpath.rglob('*') if p.name != '.DS_Store']
    paths = sorted(all_paths, key=lambda p: str(p).lower())

    file_count = sum(1 for p in paths if p.is_file())

    dir_structure = {str(p): [] for p in paths if p.is_dir()}
    dir_structure[str(startpath)] = []

    for path in paths:
        parent = str(path.parent)
        if parent in dir_structure:
            dir_structure[parent].append(path)

    def clean_name(name):
        """Cleans the filename for display."""
        # Remove suffix and underscores, then title case
        name = name.removesuffix('.docx').replace('_data', '').replace('_', ' ')
        return ' '.join(word.capitalize() for word in name.split())

    def get_file_size(path):
        """Returns the file size in MB."""
        if path.is_file():
            size_mb = path.stat().st_size / (1024 * 1024)
            return f" ({size_mb:.1f} MB)"
        return ""

    def build_tree(dir_path, prefix=""):
        """Recursively builds the tree string."""
        contents = sorted(dir_structure.get(str(dir_path), []), key=lambda p: str(p).lower())
        for i, path in enumerate(contents):
            is_last = i == (len(contents) - 1)
            connector = "└── " if is_last else "├── "
            
            display_name = clean_name(path.name)
            size_str = get_file_size(path)
            
            tree_lines.append(f"{prefix}{connector}{display_name}{size_str}")
            if path.is_dir():
                new_prefix = prefix + ("    " if is_last else "│   ")
                build_tree(path, new_prefix)

    tree_lines.append(f"{startpath.name}/")
    build_tree(startpath)
    return "\n".join(tree_lines), file_count


def main():
    """Main function to generate the tree and write to an HTML file."""
    docx_dir = Path('docx_source')
    output_file = Path('docs/file_list.html')
    
    print(f"Generating directory tree for: {docx_dir}")
    tree_diagram_str, file_count = generate_tree_string(docx_dir)
    
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Structure of {docx_dir.name}</title>
    <style>
        body {{ font-family: monospace; background-color: #f4f4f4; color: #333; padding: 2em; }}
        pre {{ background-color: #fff; padding: 1.5em; border-radius: 5px; border: 1px solid #ddd; }}
    </style>
</head>
<body>
    <h1>Directory Structure of <code>{docx_dir.name}/</code></h1>
    <p>Total files: {file_count}</p>
    <pre>{tree_diagram_str}</pre>
</body>
</html>
"""
    
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(html_content, encoding='utf-8')
    print(f"Successfully created HTML diagram at: {output_file}")

if __name__ == "__main__":
    main()