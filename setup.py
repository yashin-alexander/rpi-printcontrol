from setuptools import setup

setup(
    name='printcontrol',
    version='1.0.0',
    author='Alexander Yashin',
    author_email='yashin.alexander.42@gmail.com',
    packages=['printcontrol'],
    install_requires=[],
    license='WTFPL',
    url='https://github.com/yashin-alexander/rpi-printcontrol',
    description='rpi printer control application',
    entry_points={
        'console_scripts': [
            'printcontrol-server = printcontrol.printcontrol_server:main',
            'printcontrol-test-client = printcontrol.printcontrol_client:main',
        ],
    },
)