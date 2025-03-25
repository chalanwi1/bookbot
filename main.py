import sys
from stats import count_words, count_chars, dic_toList


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book_path = sys.argv[1]
    content = get_book_text(book_path)
    words = count_words(content)
    chars = count_chars(content)
    sorted_dic = dic_toList(chars)
    report(book_path, words, sorted_dic)


def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
        return content


def report(book_path, words, sorted_dic):
    print('======== BOOKBOT ========')
    print(f'Analyzing book found at {book_path}')
    print('-------- Word Count --------')
    print(f'Found {words} total words')
    print('-------- Character Count --------')
    for x in sorted_dic:
        if not x['char'].isalpha():
            continue
        print(f'{x['char']}: {x['num']}')
    print('======== End ========')


main()
