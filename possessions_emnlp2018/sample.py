import argparse
import logging.config

import corpus_reader as reader

def main(annotations_file, max_insts=-1):
    train, dev, test = reader.read_train_dev_test_corpus(annotations_file,
                                                         max_insts=max_insts)

    ## YOUR CODE GOES HERE
    for insts in train:
        for inst in insts:
            print inst
            print
    for insts in dev:
        for inst in insts:
            print inst
            print
    for insts in test:
        for inst in insts:
            print inst
            print


if __name__ == "__main__":
    LOGGING_CONF_FILE = 'logging.conf'

    logging.config.fileConfig(LOGGING_CONF_FILE)
    logging.debug("Loaded configuration file %s" % LOGGING_CONF_FILE)

    parser = argparse.ArgumentParser(description='Read corpus')
    parser.add_argument("ANNOTATIONS_FILE",
                        help="File in csv format with the annotations")
    parser.add_argument("-m", "--max_articles", type=int, default=-1,
                        help="Read this many articles and quit")
    parser.add_argument("-s", "--stats", action='store_true',
                        help="Print stats instead of instances")
    args = parser.parse_args()
    logging.debug(pprint.pformat(args))

    main(args.ANNOTATIONS_FILE, args.max_articles)
