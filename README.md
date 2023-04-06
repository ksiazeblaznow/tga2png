# tga2png
 Converting TGA files to PNG for multiple files at once

## Usage
1. Place your .tga files in folder 'tgaA_files'
2. Run tga2png.bat

Also you can execute command prompt in cmd: python .\tga2png.py <folder_name_with_tga_files> <folder_name_to_save_png_files_to>
> e.g.: python .\tga2png.py tga_files png_files

## Troubleshooting (FAQ but without question marks, I'm not sure if frequent and no one asked yet but it might be useful)
* Q: No module named Pillow

  A: Execute in cmd: pip install Pillow
