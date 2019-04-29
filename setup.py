from setuptools import setup

requirements = [
    "kafka-python==1.4.6"
]

setup(
    name='pygelf',
    version='0.3.8',
    packages=['pygelf'],
    description='Logging handlers with GELF support',
    keywords='logging udp tcp ssl tls graylog2 graylog gelf',
    author='Ivan Mukhin',
    author_email='muhin.ivan@gmail.com',
    install_requirements=requirements,
    url='https://github.com/keeprocking/pygelf',
    long_description=open('README.rst').read(),
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: System :: Logging',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
