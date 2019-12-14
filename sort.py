from re import match, compile
from datetime import datetime
from argparse import ArgumentParser

REG_COMMENT = '^[;#%|*].*(?:(?:\r\n|\r|\n) *[;#%|*].*)*'
REG_TRANSACTION = '(\d{4,}.+(?:\n[^\S\n\r]{1,}.+)+)'
REG_DATE = '\d{4}/\d{2}/\d{2}'

LEDGER_DATE = '%Y/%m/%d'


def output_sorted(collection):
    for c in sorted(collection, key=lambda t: t['date']):
        if c['comments']:
            for comment in c['comments']:
                print(f'{comment}\n')
        print(f'{c["transaction"]}\n')


def extract_date(trans_str):
    date_match = match(REG_DATE, trans_str)
    if date_match:
        return datetime.strptime(date_match[0], LEDGER_DATE)


def parse_journal(journal):
    comments = []
    collection = []

    for block in [chunk for chunk in filter(None, compile(
            f'(?:{REG_COMMENT}|{REG_TRANSACTION})').split(journal)) if chunk.strip()]:

        if block and block.strip():
            b = block.strip()
            if match(REG_COMMENT, b):
                comments.append(b)
            elif match(REG_TRANSACTION, b):
                collection.append(
                    {
                        'date': extract_date(b),
                        'comments': comments,
                        'transaction': b
                    }
                )
                comments = []

    return collection


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('-f')
    args = parser.parse_args()

    if not args.f:
        exit('Journal file (-f) required')

    filename = args.f

    with open(filename) as f:
        collection = parse_journal(f.read())
        output_sorted(collection)
