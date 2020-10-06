  
from distutils.core import setup
setup(
  name = 'steamprofile',
  packages = ['steamprofile'],
  version = '0.1',
  license='MIT',
  description = 'Gather Information about Profiles on Steam.',
  author = 'Aaron Levi Can (aaronlyy)',
  author_email = 'aaronlevican@gmail.com',
  url = 'https://github.com/aaronlyy/steamprofile',
  download_url = 'https://github.com/aaronlyy/steamprofile/archive/v_01.tar.gz',
  keywords = ['steam', 'steamcommunity'],
  install_requires=[
        "pyfiglet"
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)