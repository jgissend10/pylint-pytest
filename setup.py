from setuptools import setup


setup(
    name='pylint-pytest',
    description='Additional pytest checkers for Pylint',
    long_description=open('README.md').read(),
    author='James Gissendaner',
    author_email='jamestgissendanerjr@gmail.com',
    version='0.20',
    download_url='https://github.com/jgissend10/pylint-pytest.git',
    install_requires=[
        'pylint',
        'pytest',
        'pylint-plugin-utils>=0.2.1'
    ],
    packages=[
        '',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ]
)
