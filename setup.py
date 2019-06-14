from distutils.core import setup

setup(
    version='0.0.0',
    scripts=['scripts/led_control.py',
             'scripts/screen_reader.py'],
    packages=['raspberry_python_ambilight'],
    package_dir={'': 'src'}
)