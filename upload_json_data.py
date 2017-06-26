


import argparse


def main():
    parser = argparse.ArgumentParser(description='upload json file to mlab database')
    parser.add_argument('jsonFile', type=str,
                    help='the file you want to upload')

    args = parser.parse_args()

    with open(args.jsonFile) as f:
        content = f.readlines()

        print(content)
    

if __name__=="__main__":
    main()
