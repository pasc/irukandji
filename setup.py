from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='irukandji',
      version='0.1',
      description='Mailing list archive creator',
      long_description=readme(),
      url='http://github.com/pasc/irukandji',
      author='Pascal Hakim',
      author_email='pasc@redellipse.net',
      license='GPL',
      packages=['irukandji'],
      include_package_data=True,
      scripts=['bin/irukandji'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)

