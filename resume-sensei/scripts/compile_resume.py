#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess

def find_latex_compiler():
    """
    Search system paths for available LaTeX compilers in order of preference.
    """
    compilers = ['pdflatex', 'xelatex', 'lualatex']
    for compiler in compilers:
        if shutil.which(compiler):
            return compiler
    return None

def print_fallback_instructions(tex_path):
    """
    Print friendly guidelines for when no local LaTeX compiler is installed.
    """
    absolute_path = os.path.abspath(tex_path)
    print("\n" + "="*80)
    print(" NO LOCAL LATEX COMPILER DETECTED".center(80))
    print("="*80)
    print(f"We generated your LaTeX resume source at:\n  {absolute_path}\n")
    print("To compile this code into a professional PDF, choose one of these options:")
    print("\n--- OPTION 1: Compile Online with Overleaf (Easiest & Recommended) ---")
    print("1. Open https://www.overleaf.com in your web browser.")
    print("2. Log in or create a free account.")
    print("3. Click 'New Project' -> 'Blank Project'.")
    print("4. Copy the entire content of your generated .tex file and paste it into the editor.")
    print("5. Click 'Recompile' to render and download your PDF resume.")
    print("\n--- OPTION 2: Install a Local LaTeX Distribution ---")
    print("To compile from your terminal, install one of the following for your OS:")
    print("  - macOS: Run 'brew install --cask mactex-no-gui' (or install full MacTeX)")
    print("  - Windows: Install MiKTeX (https://miktex.org) or TeX Live")
    print("  - Ubuntu/Linux: Run 'sudo apt-get install texlive-latex-extra texlive-fonts-recommended'")
    print("="*80 + "\n")

def compile_latex(tex_path, output_dir=None):
    """
    Compiles the target LaTeX file to PDF using the first available system compiler.
    """
    if not os.path.exists(tex_path):
        print(f"Error: Target file not found: {tex_path}", file=sys.stderr)
        return False

    compiler = find_latex_compiler()
    if not compiler:
        print_fallback_instructions(tex_path)
        return False

    if output_dir is None:
        output_dir = os.path.dirname(tex_path) or '.'
    
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Detected LaTeX compiler: {compiler}")
    print(f"Compiling {tex_path} -> output directory: {output_dir}...")
    
    # Build standard compilation command
    # interaction=nonstopmode prevents hanging on syntax issues
    cmd = [
        compiler,
        "-interaction=nonstopmode",
        f"-output-directory={output_dir}",
        tex_path
    ]
    
    try:
        # Run compiler
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # LaTeX compilers can fail even with exit code 0 if there are critical errors.
        # Let's inspect files generated or stdout for errors.
        base_name = os.path.splitext(os.path.basename(tex_path))[0]
        pdf_path = os.path.join(output_dir, f"{base_name}.pdf")
        
        if result.returncode == 0 and os.path.exists(pdf_path):
            print(f"Success! Compiled PDF saved to: {pdf_path}")
            return True
        else:
            print("LaTeX compilation failed with errors. Compiler output:")
            # Print last 20 lines of compilation stdout to help debug errors
            lines = result.stdout.splitlines()
            for line in lines[-30:]:
                print(f"  {line}")
            return False
            
    except Exception as e:
        print(f"Runtime error occurred while compiling: {str(e)}", file=sys.stderr)
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 compile_resume.py <path_to_tex_file> [output_directory]")
        sys.exit(1)
        
    tex_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    
    success = compile_latex(tex_path, output_dir)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
