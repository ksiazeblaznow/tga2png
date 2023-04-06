# tga2png
 Converting TGA files to PNG for multiple files at once.

## How it works?
  Script takes every file in 'tga_files' folder, converts them to .png format and saves them into 'png_files'

## Usage
1. Clone repository
2. Place your .tga files in folder 'tga_files'
3. Run tga2png.bat

Also you can execute command prompt in cmd: python .\tga2png.py <folder_name_with_tga_files> <folder_name_to_save_png_files_to>
> e.g.: python .\tga2png.py tga_files png_files

## Troubleshooting or FAQ
* Q: No module named Pillow

  A: Execute in cmd: pip install Pillow

* Q: How to clone repository?

  A: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
