import PyInstaller.__main__
import os
import shutil

print("Building Kosaco ScoutMe Executable...")

# Clean previous builds
if os.path.exists('build'):
    shutil.rmtree('build')
if os.path.exists('dist'):
    shutil.rmtree('dist')
if os.path.exists('Release'):
    shutil.rmtree('Release')

# Build the executable
PyInstaller.__main__.run([
    'main.py',
    '--name=KosacoScoutMe',
    '--onefile',
    '--windowed',
    '--icon=Pelota.png',
    '--add-data=ui;ui',
    '--add-data=assets;assets',
    '--add-data=database;database',
    '--add-data=config;config',
    '--add-data=reports;reports',
    '--clean',
    '--noconfirm'
])

print("Build complete.")
print("Creating Release Package...")

# Create Release folder
os.makedirs('Release', exist_ok=True)

# Copy Executable
shutil.copy(os.path.join('dist', 'KosacoScoutMe.exe'), os.path.join('Release', 'KosacoScoutMe.exe'))

# Copy Database (Critical for persistence)
if os.path.exists('kosaco_scoutme.db'):
    shutil.copy('kosaco_scoutme.db', os.path.join('Release', 'kosaco_scoutme.db'))
else:
    print("WARNING: kosaco_scoutme.db not found in source directory. A fresh one will be created on first run.")

# Copy README
if os.path.exists('README.txt'):
    shutil.copy('README.txt', os.path.join('Release', 'README.txt'))

# Copy User Manual
if os.path.exists('Manual_Usuario.pdf'):
    shutil.copy('Manual_Usuario.pdf', os.path.join('Release', 'Manual_Usuario.pdf'))

print("=================================================")
print("  RELEASE READY at: Release/")
print("  Contents:")
print(f"   - {os.path.join('Release', 'KosacoScoutMe.exe')}")
print(f"   - {os.path.join('Release', 'kosaco_scoutme.db')}")
print(f"   - {os.path.join('Release', 'Manual_Usuario.pdf')}")
print(f"   - {os.path.join('Release', 'README.txt')}")
print("=================================================")
