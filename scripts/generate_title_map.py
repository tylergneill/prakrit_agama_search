
import json
from pathlib import Path

def clean_name(name):
    """Cleans the filename for display."""
    name = name.replace('_data', '').replace('_', ' ')
    return ' '.join(word.capitalize() for word in name.split())

def main():
    """Main function to generate the title map and write to a JSON file."""
    docs_dir = Path('docs')
    output_file = docs_dir / 'title_map.json'
    
    print(f"Generating title map for files in: {docs_dir}")
    
    title_map = {}
    html_files = [p for p in docs_dir.glob('*.html') if p.name not in ['index.html', 'file_list.html', 'search.html']]
    
    for html_file in html_files:
        filename = html_file.name
        original_title_stem = html_file.stem
        cleaned_title = clean_name(original_title_stem)
        title_map[filename] = cleaned_title
        
    with output_file.open('w', encoding='utf-8') as f:
        json.dump(title_map, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully created title map with {len(title_map)} entries at: {output_file}")

if __name__ == "__main__":
    main()
