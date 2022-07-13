from setuptools import setup, find_packages

VERSION  = '0.0.1'
DESCRIPTION = 'A real-time facial landmarks detector'
LONG_DESCRIPTION = 'A real-time facial landmarks detector which can detect any number of faces by just calling one function'

setup(
    name= "Facial_landmarks",
    version=VERSION,
    author= "Vayansh Garg",
    author_email="<vayanshgarg1@gmail.com>",
    description= DESCRIPTION,
    long_description= LONG_DESCRIPTION,
    long_description_content_type = "text/markdown",
    packages= find_packages(),
    install_requires = [
        'opencv-python>=4.6.0.66',
        'mediapipe>=0.8.10.1',
        'numpy>=1.23.1'],
    keywords= ['face_detection','landmarks','real_time','camera stream','face','facial','live detection','detect landmarks'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10.5",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X"
    ]
    
)