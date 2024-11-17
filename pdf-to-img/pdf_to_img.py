import fitz
import os
from glob import glob
import click

@click.command()
@click.argument('folder_name')

def pdf_to_img(folder_name: str):
    """This function is used for conversion pdf to img."""
    file_li = glob(f'./{folder_name}/*.pdf')

    create_date = folder_name.split('_')[1]
    os.makedirs(f'./img_{create_date}', exist_ok=True)

    for file in file_li:
        file_name = file.rsplit('/', maxsplit=1)[-1]
        doc = fitz.open(file)
        for i, page in enumerate(doc):
            img = page.get_pixmap()
            img.save(f"./img_{create_date}/{file_name[:-4]}_{i}.png")
            
            click.echo(f'Pdf to Img ({file_name}): Done!!')

if __name__ == "__main__":
    pdf_to_img()