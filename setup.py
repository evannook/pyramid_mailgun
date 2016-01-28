try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pyramid_mailgun',
    version='0.0.2',
    packages=['pyramid_mailgun',],
    description='Mailgun integration for Pyramid framework',
    author='Evan Nook',
    author_email='evan@innonook.com',
    url='https://github.com/evannook/pyramid_mailgun',
    license='MIT',
    long_description=open('README.txt').read(),
    install_requires = ['requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
