from setuptools import setup, find_packages


setup(
    name='t_pop',
    version='0.1.0',
    author='maxwell flitton',
    author_email='maxwellflitton@gmail.com',
    packages=find_packages(exclude=("tests",)),
    scripts=[],
    url="https://github.com/maxwellflitton/tpop",
    description='T pop algorithm',
    long_description="T pop algorithm",
    package_data={'': ['script.sh']},
    include_package_data=True,
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            # "cml=camel.interface.entry_points.main_interface:main",
        ]
    },
)
