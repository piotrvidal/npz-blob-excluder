#!/usr/bin/env python

def main():
    import argparse
    from modes.conversion.npz_to_csv import Converter

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help='name of the .npz filename to convert and merge')
    
    filename = vars(parser.parse_args())['f']

    if filename is None:
        print('tip: run the script using -f "filename.npz" without quotations')
        exit()

    try:
        converter = Converter(filename)
        converter.convert_and_merge()
    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()