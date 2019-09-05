from setuptools import find_packages, setup

setup(
    name='Check sample submission',
    version='1.0.0',
    entry_points={
        'console_scripts': [
            'check-sample-submission=check_sample_submission.cli:cli_main'
        ]
    },
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'wheel',
        'click',
        'pyperclip',
        'jinja2',
        'openpyxl',
    ]
)