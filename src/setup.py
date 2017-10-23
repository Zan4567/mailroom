from setuptools import setup

setup (
  name ="mailroom",
  description="track donors and create thank-you letters",
  author="Kevin Robinson and Jacob Carstens",
  author_email="",
  package_dir={'': 'src'},
  my_modules=['mailroom'],
  #install_requires=['other_distribution', 'another_one'],
  extras_require={
    'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox'],
    'development': ['ipython']
  }
  # entry_points={
  #   "exec_name = module_path:fn_name"
  # }
)
