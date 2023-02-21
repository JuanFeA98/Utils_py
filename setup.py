from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
        name='my_package',
        description='Modulo de Utilidades',
        license='MIT',
        url='https://github.com/JuanFeA98/mypacke',
        version='0.0.1',
        author='JuanFe98',
        author_email='jmartinezbernal02@gmail.com',
        long_description=open('README.md').read(),
        packages=find_packages(exclude='test'),
        zip_safe=False,
        install_requires=['pandas', 'cx_Oracle', 'sqlalchemy'],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
        ]
    )