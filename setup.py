from setuptools import setup, find_packages

setup(
    name="pdffilter-cli",
    version="1.0.0",
    description="Extract only the pages containing the keywords from the PDF files in the specified path.",
    packages=["src"],
    author="namacha",
    requires=["fire", "PyPDF2", "pdfminer.six"],
    entry_points={"console_scripts": ["pdffilter=src.main:dummy_main"]},
)
