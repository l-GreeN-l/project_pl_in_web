import re
from cffi.backend_ctypes import long


def delete_trash( stroke: str):
    stroke = stroke.text.replace('\n', '')
    return delete_links(stroke=stroke)

def delete_links( stroke: str):
    stroke = re.split(r'\[\d+\]', stroke)
    return ''.join(stroke)

def transfer_popularity( popularity: str):
    popularity = popularity.text.split('\n')[0]
    popularity = popularity.replace(',', '')
    popularity = popularity.replace('.', '')
    match = re.match(r'^\d+\b', popularity)[0]
    return long(match)

def transfer_websites( website):
    return delete_trash(stroke=website)

def transfer_frontend( frontend):
    return delete_trash(stroke=frontend)

def transfer_backend( backend):
    return delete_trash(stroke=backend)

def transfer_db( database):
    return delete_trash(stroke=database)

def transfer_note( note):
    return delete_trash(stroke=note)