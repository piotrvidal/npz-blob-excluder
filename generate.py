#!/usr/bin/env python

def main():
    import argparse
    from modes.generation.charts import Generator 

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help='name of the .csv filename to generate charts from')
    parser.add_argument('-c', help='chart type to be generated. Available so far = trajectory')
    
    csv_file = vars(parser.parse_args())['f']
    chart_type = vars(parser.parse_args())['c']

    if csv_file is None or chart_type is None:
        print('tip: run the script using -f "filename.csv" -c "trajectory" without quotations')
        exit()

    try:
        generator = Generator(csv_file, chart_type)
    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()