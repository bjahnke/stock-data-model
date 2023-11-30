from setuptools import setup

setup(
    name='stock-data-model',
    version='',
    packages=['stock_model_package', 'stock_model_package.models', 'stock_model_package.repositories'],
    url='',
    license='',
    author='bjahnke',
    author_email='bjahnke71@gmail.com',
    description='',
    install_requires=[
        'SQLAlchemy',
        'pandas',
    ]
)
