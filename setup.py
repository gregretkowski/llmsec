from setuptools import setup, find_packages

setup(
    name='llmsec',
    version='0.1.0',
    description='A Python library for LLM security',
    author='Your Name',
    author_email='greg@rage.net',
    url='https://github.com/gregretkowski/llmsec',
    packages=find_packages(include=['llmsec']),
    scripts=['bin/check-prompt'],
    install_requires=['litellm','jinja2'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
