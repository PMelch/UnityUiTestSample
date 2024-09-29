import uitestrunner

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", dest="verbose", action="store_true", default=False, help="Enable verbose")
    parser.add_argument("-r", "--reports", dest="reports", action="store_true", default=False, help="enabled test report")

    args = parser.parse_args()

    uitestrunner.run(args)
