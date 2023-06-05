"""
This program uses a multiline string as a bitmap, a 2D image"""
import os


def create_image(message):
    file = 'bitmapworld.txt'
    with open(file=file, mode='r',  encoding='utf-8') as file_content:
        for line in file_content:
            with open(file='checkmap.txt', mode='a', encoding='utf-8') as w:
                i_ = 0
                for i, e in enumerate(line):
                    s = message[i_]
                    if e != ' ':
                        w.write(s)
                        if i_ < len(message) - 1:
                            i_ += 1
                        else:
                            i_ = 0
                    else:
                        w.write(line[i])
                w.write('\n')


def print_image():
    file = 'checkmap.txt'
    with open(file=file, mode='r', encoding='utf-8') as file_content:
        print(file_content.read())


def main():
    if os.access('checkmap.txt', os.R_OK):
        os.remove('checkmap.txt')
    print('Bitmap Message, by Al Sweigart al@inventwithpython.com')
    print("Enter the message to display with the bitmap.")
    message = input('> ')
    create_image(message)
    print_image()


if __name__ == '__main__':
    main()
