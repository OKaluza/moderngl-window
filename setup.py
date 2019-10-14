from setuptools import setup, find_namespace_packages

setup(
    name="moderngl_window",
    version="1.5.1",
    description="A cross platform helper library for ModernGL making window creation and resource loading simple",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/moderngl/moderngl_window",
    author="Einar Forselv",
    author_email="eforselv@gmail.com",
    packages=find_namespace_packages(include=['moderngl_window', 'moderngl_window.*']),
    include_package_data=True,
    keywords=['moderngl', 'window', 'context'],
    license='MIT',
    platforms=['any'],
    python_requires='>=3.5',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Games/Entertainment',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: 3D Rendering',
        'Topic :: Scientific/Engineering :: Visualization',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'moderngl<6',
        'pyglet>=1.4.2<2',
        'numpy>=1.16<2',
        'pyrr>=0.10.3<1',
        'Pillow>=5,<7',
    ],
    extras_require={
        "PySide2": ['PySide2<6'],
        "pyqt5": ['PyQt5<6'],
        "glfw": ['glfw<2'],
        "PySDL2": ['PySDL2<1'],
        "pywavefront": ["pywavefront>=1.2.0<2"],
        "trimesh": ["trimesh==3.2.6", "scipy>=1.3"],
        "tk": ["pyopengl==3.1.0", "pyopengltk==0.0.3"],
    },
    project_urls={
        'Documentation': 'https://moderngl-window.readthedocs.io',
        'ModernGL': 'https://github.com/moderngl/moderngl',
    },
)
