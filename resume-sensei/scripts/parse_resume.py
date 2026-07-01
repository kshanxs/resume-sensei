#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = []
# ///
import os
import sys
import zipfile
import xml.etree.ElementTree as ET

def extract_text_from_docx(docx_path):
    """
    Extracts text from a .docx file cleanly without external dependencies.
    """
    if not os.path.exists(docx_path):
        raise FileNotFoundError(f"File not found: {docx_path}")
        
    try:
        with zipfile.ZipFile(docx_path) as docx:
            # Open and parse the main document XML
            xml_content = docx.read('word/document.xml')
            root = ET.fromstring(xml_content)
            
            # XML Namespaces used in docx files
            namespaces = {
                'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
            }
            
            body = root.find('.//w:body', namespaces)
            if body is None:
                return ""
                
            text_lines = []
            
            # Helper to extract text from a paragraph or run
            def get_text_from_node(node):
                parts = []
                for child in node.iter():
                    if child.tag.endswith('}t'):  # w:t element (text)
                        parts.append(child.text or '')
                    elif child.tag.endswith('}tab'):  # w:tab element (tab)
                        parts.append('\t')
                    elif child.tag.endswith('}br'):  # w:br element (break)
                        parts.append('\n')
                return ''.join(parts)
            
            # Iterate through direct children of body to maintain correct order
            for child in body:
                tag = child.tag
                
                # Check for paragraph (w:p)
                if tag.endswith('}p'):
                    p_text = get_text_from_node(child)
                    text_lines.append(p_text)
                    
                # Check for table (w:tbl)
                elif tag.endswith('}tbl'):
                    # Find all table rows
                    rows = child.findall('.//w:tr', namespaces)
                    for row in rows:
                        row_cells = []
                        cells = row.findall('.//w:tc', namespaces)
                        for cell in cells:
                            cell_text = get_text_from_node(cell).strip()
                            # Replace internal newlines inside table cells with spaces for flat layout
                            cell_text = cell_text.replace('\n', ' ')
                            row_cells.append(cell_text)
                        if any(row_cells):
                            # Format table row with pipes
                            text_lines.append(" | ".join(row_cells))
                            
            return '\n'.join(text_lines)
            
    except zipfile.BadZipFile:
        raise ValueError(f"File is not a valid DOCX file: {docx_path}")
    except Exception as e:
        raise RuntimeError(f"Error parsing DOCX file: {str(e)}")

def extract_text_from_file(file_path):
    """
    Detects file type and extracts clean text.
    """
    _, ext = os.path.splitext(file_path.lower())
    
    if ext == '.docx':
        return extract_text_from_docx(file_path)
    elif ext in ['.txt', '.md', '.markdown', '.tex']:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    else:
        raise ValueError(f"Unsupported file format: {ext}. Supported formats are: .docx, .txt, .md, .tex")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 parse_resume.py <input_file_path> [output_file_path]")
        sys.exit(1)
        
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        extracted_text = extract_text_from_file(input_path)
        
        if output_path:
            # Create directory if it doesn't exist
            out_dir = os.path.dirname(output_path)
            if out_dir and not os.path.exists(out_dir):
                os.makedirs(out_dir, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(extracted_text)
            print(f"Success: Extracted text saved to {output_path}")
        else:
            print(extracted_text)
            
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
