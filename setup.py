from setuptools import setup, find_packages

setup(
    name="spambot",
    url="https://github.com/rsouthwi/Spambot",
    description="a bot whose primary function is to spam",
    author="Ron Southwick",
    author_email="github@fool.com",
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    platforms='any',
    install_requires=[
        "slacker"
    ],
    use_scm_version=True,
    skip_upload_docs=True,
    setup_requires=[

    ],
    packages=find_packages(exclude=['tests']),
    test_suite="tests"
)