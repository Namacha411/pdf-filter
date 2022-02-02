from sre_constants import SUCCESS
import os
import glob

import PyPDF2
from pdfminer.high_level import extract_text

import fire


def get_file_name(path: str) -> str:
    return os.path.basename(path).split(".", 1)[0]


def split_pages(src_path: str, dst_path: str) -> None:
    os.makedirs(dst_path)
    src_pdf = PyPDF2.PdfFileReader(src_path)
    for i in range(src_pdf.numPages):
        dst_pdf = PyPDF2.PdfFileWriter()
        dst_pdf.addPage(src_pdf.getPage(i))
        name = f"{get_file_name(src_path)}-{i}.pdf"
        with open(f"{dst_path}{name}", "wb") as f:
            dst_pdf.write(f)


def filter_pages(dst_path: str, x: str) -> None:
    files = glob.glob(f"{dst_path}*.pdf")
    for file in files:
        text = extract_text(file)
        if x in text:
            continue
        os.remove(file)


def merge_pages(dst_path: str, new_pdf_name: str) -> None:
    files = glob.glob(f"{dst_path}*.pdf")
    merger = PyPDF2.PdfFileMerger()
    for file in files:
        merger.append(file)
    merger.write(new_pdf_name)
    merger.close()


def delete_dir(path: str) -> None:
    files = glob.glob(f"{path}*.pdf")
    for file in files:
        os.remove(file)
    os.rmdir(path)


def main(original_pdf: str, filter_word: str, new_pdf: str = "new.pdf") -> None:
    """
    Extract only the pages containing the keywords from the PDF files in the specified path.

    Parameters
    ----------
    original_pdf: str
        original pdf path
    filter_word: str
        extract pages if page contains this word
    new_pdf: str
        new extracted pdf's path or file name
    """
    tmp = "tmp/"

    split_pages(original_pdf, tmp)
    filter_pages(tmp, filter_word)
    merge_pages(tmp, new_pdf)

    delete_dir(tmp)
    exit(SUCCESS)


def dummy_main():
    fire.Fire(main)
