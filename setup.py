from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()

# USAGE: to Create the file to distribute: dist/json_df_examples-0.0.1.tar.gz (dist/<ProjectName>-<version>.tar.gz)
#     python setup.py sdist
#
# For More info type:
#     python setup.py --help-commands
setup(name='json_df_examples',
      version='0.0.1',
      description='A repo to demo conversions between json and dataframe representation',
      url='http://tinyurl.com/PythonStarter2',
      author='Ozgur Ozturk',
      author_email='',
      license='MIT',
      packages = find_packages(),
      install_requires=[
          'pandas',
      ],
      zip_safe=True)