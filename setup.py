from setuptools import setup
from setuptools import find_packages


setup(
    # Project
    name='AstroKundli',
    version='1.0.0',
    
    # Sources
    packages=find_packages(),
    package_data={
        'FlatlibAstroSidereal': [
            'resources/README.md',
            'resources/swefiles/*'
        ],
    },
    
    # Dependencies
    install_requires=['pyswisseph==2.08.00-1'],
    
    # Metadata
    description='Python library for Astrology',
    url='https://github.com/EH30/AstroKundli',
    keywords=['Astrology', 'Sidereal Astrology'],
    license='MIT',
    
    # Authoring
    author='EH',
    author_email=None,
    
    # Classifiers
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ], 
)
