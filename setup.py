from setuptools import find_packages, setup

setup(
    name='사진워터마크찌기',
    version='1.2.0',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'Click',
        'Pillow',
        'requests',
        'auto-py-to-exe'
    ],
    entry_points={
        'console_scripts': [
            'lgtm=lgtm.core:cli'
            # 'lgtm=main'
        ]
    }
)