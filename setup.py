from distutils.core import setup

desc = ""
try: desc=open('README.rst').read()
except: pass
setup(
    name='autolux',
    version='0.0.22',
    author='okay',
    author_email='okay.zed+al@gmail.com',
    packages=['autolux' ],
    scripts=['bin/autolux'],
    url='http://github.com/autolume/autolux',
    license='MIT',
    description='an auto luxer',
    long_description=desc
    )

