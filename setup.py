from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["PyQt6"],
    "includes": ["src"],
    "include_files": [
        "assets/",  # Make sure your .ico file is in this folder
    ]
}

setup(
    name="Sparcle",
    version="0.1",
    description="Spine Particle VFX Tool",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "src/main.py",
            base="Win32GUI",
            icon="assets/sparcle_icon.ico",
            target_name="Sparcle.exe"  # This sets the executable name
        )
    ]
) 