from setuptools import setup

setup(
    name='myfirstapp',
    version='1.0',
    long_description=__doc__,
    packages=['myfirstapp'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)

