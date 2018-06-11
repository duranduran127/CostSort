from distutils.core import setup

import py2exe2msi

setup(
    options={
        'py2exe2msi': {'bundle_files': 1, 'compressed': True}
    },
    console=[
        {'script': "Costs.py"}
    ],
    zipfile=None,
)