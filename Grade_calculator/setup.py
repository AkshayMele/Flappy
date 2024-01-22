from setuptools import setup, find_packages

setup(
    name='student_grade_calculator',
    version='1.0.0',
    description='A simple Student Grade Calculator',
    author='Akshay',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'calculate_grades = grade:student_grade_calculator',
        ],
    },
)
