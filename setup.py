from setuptools import setup, find_packages

setup(
    name='mcq_generator',
    version='0.0.1',
    author='Utkarsh Agarwal',
    author_email='utkarshagarwal9641@gmail.com',
    install_requires=["groq","langchain","streamlit","python-dotenv",""],
    packages=find_packages()
)