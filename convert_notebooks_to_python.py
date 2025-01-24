import json
import os

def extract_code_cells(notebook_path, output_path=None):
    """
    Extracts code cells from a Jupyter Notebook (.ipynb) file.

    Args:
        notebook_path (str): Path to the input notebook file.
        output_path (str, optional): Path to save the extracted code. If None, saves to 'extracted_code.py'.

    Returns:
        list of str: List of code snippets from the notebook.
    """
    if not os.path.exists(notebook_path):
        raise FileNotFoundError(f"Notebook file not found: {notebook_path}")

    with open(notebook_path, 'r', encoding='utf-8') as file:
        notebook_data = json.load(file)

    # Extract code cells
    code_cells = []
    for cell in notebook_data.get('cells', []):
        if cell.get('cell_type') == 'code':
            code_content = ''.join(cell.get('source', []))
            code_cells.append(code_content)

    # Default output path if none provided
    if output_path is None:
        base_name = os.path.splitext(os.path.basename(notebook_path))[0]
        output_path = f"{base_name}.py"

    # Output the extracted code
    with open(output_path, 'w', encoding='utf-8') as out_file:
        out_file.write('\n\n'.join(code_cells))
    print(f"Code cells extracted and saved to: {output_path}")

    return code_cells

def convert_all_notebooks_to_python():
    """
    Converts all Jupyter Notebook files (.ipynb) in the current directory to Python files (.py)
    with only the source code from code cells.
    """
    for file_name in os.listdir('.'): 
        if file_name.endswith('.ipynb'):
            try:
                extract_code_cells(file_name)
            except Exception as e:
                print(f"Failed to convert {file_name}: {e}")

# Example usage
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Extract code cells from a Jupyter Notebook file.")
    parser.add_argument("notebook_path", nargs="?", help="Path to the Jupyter Notebook file (.ipynb). If not provided, all notebooks in the current directory will be converted.", default=None)
    parser.add_argument("--output", help="Path to save the extracted code (optional).", default=None)

    args = parser.parse_args()
    
    if args.notebook_path:
        try:
            extract_code_cells(args.notebook_path, args.output)
        except Exception as e:
            print(f"Error: {e}")
    else:
        convert_all_notebooks_to_python()
