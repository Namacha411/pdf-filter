# pdf-filter

## How to use

指定されたパスにあるPDFファイルから、キーワードを含んだページのみを抽出します。
結果は`new.pdf`で出力されます。

```sh
INFO: Showing help with the command 'pdffilter -- --help'.

NAME
    pdffilter - Extract only the pages containing the keywords from the PDF files in the specified path.

SYNOPSIS
    pdffilter ORIGINAL_PDF FILTER_WORD <flags>

DESCRIPTION
    Extract only the pages containing the keywords from the PDF files in the specified path.

POSITIONAL ARGUMENTS
    ORIGINAL_PDF
        Type: str
        original pdf path
    FILTER_WORD
        Type: str
        extract pages if page contains this word

FLAGS
    --new_pdf=NEW_PDF
        Type: str
        Default: 'new.pdf'
        new extracted pdf's path or file name

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS
```

## How to install

```sh
pip install git+https://github.com/Namacha411/pdf-filter
```
