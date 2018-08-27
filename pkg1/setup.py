from setuptools import setup, find_packages

setup(name="pkg1",
      packages=find_packages(),
      install_requires=["pkg2"],
      entry_points={
          'console_scripts': [
              'pkg1script = pkg1.__main__:main'
          ]}
)
