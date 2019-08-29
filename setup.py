from setuptools import setup, find_packages

setup(
    name='ledgerctl',
    python_requires='>=3.5',
    version='0.1',
    py_modules=['ledgerctl'],
    description="Ledger Donjon Python3 client for communicating with Ledger devices",
    install_requires=['click>=7.0', 'construct>=2.9', 'cryptography>=2.5', 'ecdsa', 'hidapi', 'intelhex',
                      'protobuf>=3.6', 'requests', 'tabulate'],
    packages=find_packages(),
    include_package_data=True,
    entry_points='''
        [console_scripts]
        ledgerctl=ledgerctl:cli
    ''',
)