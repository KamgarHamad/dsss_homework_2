from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1.0',
    packages=find_packages(),
    description='A simple math quiz game',
    author='Kamgar Hamad',
    author_email='K.H.code1996@gmail.com',
    license='Apache License 2.0',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:math_quiz'
        ]
    },
)