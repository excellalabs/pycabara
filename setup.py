from setuptools import setup

# Workaround for http://bugs.python.org/issue15881
try:
    import multiprocessing
except ImportError:
    pass


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pycabara',
      version='0.4',
      description='Python implementation of Capybara, an acceptance test framework for web applications',
      long_description=readme(),
      classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing',
      ],
      keywords='acceptance test Capybara bdd',
      url='http://github.com/ruthlesshelp/pycabara',
      author='Stephen Ritchie',
      author_email='ruthlesshelp@gmail.com',
      license='MIT',
      packages=['pycabara'],
      install_requires=[
          'selenium',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)