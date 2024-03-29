from distutils.core import setup
setup(
  name = 'binbymean',         # How you named your package folder (MyLib)
  packages = ['binbymean'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Calculate Bin by mean values for each records in your dataset.',   # Give a short description about your library
  author = 'KOUSTABH KRISHNA',                   # Type in your name
  author_email = 'koustabh.krishna@mca.christuniversity.in',      # Type in your E-Mail
  url = 'https://github.com/koustabh69/binbymean.git',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/koustabh69/binbymean/archive/v0.1.tar.gz',    # I explain this later on
  keywords = ['bin', 'mean', 'python'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which python versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
