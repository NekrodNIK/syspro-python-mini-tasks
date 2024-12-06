from setuptools import Extension, setup

setup(
    name="foreign",
    version="0.0.1",
    ext_modules=[
        Extension(
            name="foreign",
            sources=["foreign.c"],
        ),
    ],
)
