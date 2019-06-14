from distutils.core import setup

setup(
    version='0.0.0',
    scripts=['scripts/LedControl.py',
             'scripts/ScreenReader.py'],
    packages=['raspberry_python_ambilight'],
    package_dir={'': 'src'}
)