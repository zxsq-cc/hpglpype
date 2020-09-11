from setuptools import setup


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="hpglpype",
    version="0.1.1",
    description="",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="zxsq-cc",
    url="",
    license=license,
    packages=["hpglpype"],
    install_requires=[
        'click',
        'vpype @ git+https://github.com/abey79/vpype.git',
    ],
    entry_points='''
            [vpype.plugins]
            hpgl=hpglpype.hpglpype:hpgl
        ''',
)
