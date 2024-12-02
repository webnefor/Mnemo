import argparse



def getparse(args=None):

    parser = argparse.ArgumentParser(description='Mnemo: You can learn any language!');

    parser.add_argument('-t',"--time",
                        type=int,
                        default=3,
                        help='default: 3 minute'
                        )

    parser.add_argument('-p',"--path",
                        type=str,
                        default="base/words",
                        help='default: base/words'
                        )

    parser.add_argument('-m',"--mode",
                        type=bool,
                        default=False,
                        help='default: 1'
                        )


    parsedArguments = parser.parse_args();

    return parsedArguments;
