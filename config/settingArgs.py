
import argparse



def getparse(args=None):

    parser = argparse.ArgumentParser(description='Mnemo: You can learn any language!');

    parser.add_argument('-t',"--time",
                        type=int,
                        default=1,
                        help='(default: 1 minute)'
                        )

    parser.add_argument('-p',"--path",
                        type=str,
                        default="base/words",
                        help='(default: /words)'
                        )

    parser.add_argument('-m',"--mode",
                        type=int,
                        default=1,
                        help='(default: 1)'
                        )


    parsedArguments = parser.parse_args();

    return parsedArguments;
