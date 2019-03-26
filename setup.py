from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
        name='certificategen',
        version='0.1.1',
        packages=find_packages(),
        license='GPL3',
        url='https://github.com/GDGPetropolis',
        author_email='johnathanfercher22@gmail.com',
        keywords=["GDG", "Event", "Certificate", "Generator"],
        tests_require=["pytest", ], install_requires=['PyPDF2', 'reportlab']
    )
