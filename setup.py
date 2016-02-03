"""A setup up script for the APEL-SSM."""
from shutil import copyfile
from os import remove
import sys
from setuptools import setup, find_packages


def main():
    """Called when run as script, i.e. "python setup.py install"."""
    if sys.argv[1] == 'install':
        copyfile('bin/receiver.py', 'bin/ssmreceive')
        copyfile('bin/sender.py', 'bin/ssmsend')

    conf_dir = '/etc/apel/'
    conf_files = ['conf/logging.cfg',
                  'conf/receiver.cfg',
                  'conf/sender.cfg',
                  'conf/dns']

    # For 'python setup.py test' to work (on Linux SL6)
    # 'python-daemon' and 'mock' must be installed
    # or included in 'install_requires'
    setup(name='apel-ssm',
          version='2.1.7-1',
          description=("Secure Stomp Messenger (SSM) is designed to simply "
                       "send messages using the STOMP protocol."),
          author='APEL',
          author_email='apel-admins@stfc.ac.uk',
          url='https://wiki.egi.eu/wiki/APEL/SSM',
          download_url='https://github.com/apel/ssm/archive/2.1.7-1.zip',
          license='Apache License, v2 - http://www.apache.org/licenses/',
          install_requires=['stomp.py<=3.1.6', 'python-ldap', 'dirq'],
          extras_require={
              'python-daemon': ['python-daemon'],
          },
          packages=find_packages(exclude=['bin']),
          scripts=['bin/apel-ssm', 'bin/ssmreceive', 'bin/ssmsend'],
          data_files=[(conf_dir, conf_files),
                      ('/etc/logrotate.d', ['conf/ssm.logrotate'])],
          zip_safe=True,
          test_suite='test',
          tests_require=['unittest2', 'coveralls'])

    if sys.argv[1] == 'install':
        remove('bin/ssmreceive')
        remove('bin/ssmsend')

if __name__ == "__main__":
    main()
