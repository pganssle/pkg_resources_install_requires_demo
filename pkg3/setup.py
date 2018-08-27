from setuptools import setup, find_packages

setup(name="pkg3",
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'pkg3script = pkg3.__main__:main'
          ]}
)
