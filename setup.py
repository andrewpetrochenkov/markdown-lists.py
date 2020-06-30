import setuptools

setuptools.setup(
    name='markdown-lists',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
