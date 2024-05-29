from setuptools import setup, find_packages

setup(
    name="dort_islem",
    version="0.1",
    packages=find_packages(include=['dort_islem', 'dort_islem.*']),
    install_requires=[
        # Bağımlılıklar buraya eklenebilir
    ],
    entry_points={
        'console_scripts': [
            'dort_islem=dort_islem.__main__:main',
        ],
    },
    author="İsminiz",
    author_email="email@ornek.com",
    description="Dört temel matematiksel işlemleri gerçekleştiren bir Python paketi",
    keywords="dort islem matematik",
)
