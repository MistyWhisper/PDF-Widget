import sys
from pathlib import Path
from PyInstaller.__main__ import run

if __name__ == '__main__':
    main_file = 'main.py'
    build_dir = Path(__file__).parent / 'dist'
    sys.argv = ['pyinstaller', '--onefile', '--windowed', '--clean', main_file, f'--distpath={build_dir}']
    run()
