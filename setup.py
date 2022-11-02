from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0',
    entry_points = {
        'console_scripts': ['clean-folder=clean_folder.clean:start']
    },
    zip_safe=False,
    packages=find_namespace_packages(),
    include_package_data=True,
    description='Clean folder',
)