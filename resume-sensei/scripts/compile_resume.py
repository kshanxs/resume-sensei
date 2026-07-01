#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = []
# ///
import os
import sys
import shutil
import subprocess

def find_typst_compiler():
    """
    Search system paths for the Typst compiler.
    """
    return shutil.which('typst')

def print_fallback_instructions(typ_path):
    """
    Print friendly guidelines for when no local Typst compiler is installed.
    """
    absolute_path = os.path.abspath(typ_path)
    print("\n" + "="*80)
    print(" NO LOCAL TYPST COMPILER DETECTED".center(80))
    print("="*80)
    print(f"We generated your Typst resume source at:\n  {absolute_path}\n")
    print("To compile this code into a professional PDF, choose one of these options:")
    print("\n--- OPTION 1: Compile Online with Typst App (Easiest & Recommended) ---")
    print("1. Open https://typst.app in your web browser.")
    print("2. Log in or create a free account.")
    print("3. Create a new blank project.")
    print("4. Upload the files (e.g. your resume.typ and template.typ).")
    print("5. The PDF will compile instantly in the web editor!")
    print("\n--- OPTION 2: Install Typst Locally ---")
    print("To compile from your terminal, install Typst for your OS:")
    print("  - macOS: Run 'brew install typst'")
    print("  - Windows: Run 'winget install Typst.Typst'")
    print("  - Linux: Install via cargo ('cargo install typst-cli') or your package manager.")
    print("\nOnce installed, compile manually using:")
    print("  typst compile --font-path <path_to_fonts_dir> <input_file.typ> <output_file.pdf>")
    print("="*80 + "\n")

def find_font_directories(typ_path):
    """
    Search for the custom fonts directory in various relative locations.
    """
    font_dirs = []
    input_dir = os.path.dirname(os.path.abspath(typ_path))
    
    # 1. Relative to input file: template fonts folder
    # e.g. Templates/fonts/
    local_fonts = os.path.join(input_dir, "fonts")
    if os.path.isdir(local_fonts):
        font_dirs.append(local_fonts)
        
    # 2. From Tailored/SWE/ -> ../../Templates/fonts
    parent_templates_fonts = os.path.abspath(os.path.join(input_dir, "..", "Templates", "fonts"))
    if os.path.isdir(parent_templates_fonts):
        font_dirs.append(parent_templates_fonts)
        
    parent2_templates_fonts = os.path.abspath(os.path.join(input_dir, "..", "..", "Templates", "fonts"))
    if os.path.isdir(parent2_templates_fonts):
        font_dirs.append(parent2_templates_fonts)
        
    # 3. Relative to CWD: ./Templates/fonts
    cwd_fonts = os.path.abspath(os.path.join(os.getcwd(), "Templates", "fonts"))
    if os.path.isdir(cwd_fonts):
        font_dirs.append(cwd_fonts)
        
    # 4. Relative to the script location (fallback to original template assets)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_assets_fonts = os.path.abspath(os.path.join(script_dir, "..", "assets", "resume-hub", "Templates", "fonts"))
    if os.path.isdir(script_assets_fonts):
        font_dirs.append(script_assets_fonts)
        
    # Deduplicate while preserving order
    seen = set()
    unique_dirs = []
    for d in font_dirs:
        if d not in seen:
            seen.add(d)
            unique_dirs.append(d)
            
    return unique_dirs

def compile_typst(typ_path, output_dir=None):
    """
    Compiles the target Typst file to PDF using the local typst CLI.
    """
    if not os.path.exists(typ_path):
        print(f"Error: Target file not found: {typ_path}", file=sys.stderr)
        return False

    compiler = find_typst_compiler()
    if not compiler:
        print_fallback_instructions(typ_path)
        return False

    if output_dir is None:
        output_dir = os.path.dirname(typ_path) or '.'
    
    os.makedirs(output_dir, exist_ok=True)
    
    base_name = os.path.splitext(os.path.basename(typ_path))[0]
    pdf_path = os.path.join(output_dir, f"{base_name}.pdf")
    
    print(f"Detected Typst compiler: {compiler}")
    print(f"Compiling {typ_path} -> {pdf_path}...")
    
    # Build standard compilation command
    cmd = [compiler, "compile"]
    
    # Add font directories
    font_dirs = find_font_directories(typ_path)
    for d in font_dirs:
        cmd.extend(["--font-path", d])
        
    cmd.extend([typ_path, pdf_path])
    
    try:
        # Run compiler
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0 and os.path.exists(pdf_path):
            print(f"Success! Compiled PDF saved to: {pdf_path}")
            return True
        else:
            print("Typst compilation failed with errors. Compiler output:", file=sys.stderr)
            print(result.stderr, file=sys.stderr)
            return False
            
    except Exception as e:
        print(f"Runtime error occurred while compiling: {str(e)}", file=sys.stderr)
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 compile_resume.py <path_to_typ_file> [output_directory]")
        sys.exit(1)
        
    typ_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    
    success = compile_typst(typ_path, output_dir)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
