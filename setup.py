from setuptools import setup, find_packages

setup(
    name='aventus-backend',
    version='1.0.0',
    author='Praful M',
    author_email='praful.is22@bmsce.ac.in',
    description='Backend Built for the aventus 2.0 hackathon',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)