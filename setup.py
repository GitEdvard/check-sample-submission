from distutils.core import setup

setup(
    name='Check sample submission',
    version='1.0.0',
    entry_points={
        'console_scripts': [
            'check-sample-submission=cli:cli_main'
        ]
    }
)