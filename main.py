import config.settingArgs
import config.GetWords
import config.Core
import config.LabelObject
import config.MainWindow

import sys

def main() -> int:

    window = config.MainWindow.MainWindow();
    window.setup();
    window.show();
    #
    # args = config.settingArgs.getparse(sys.argv[1::]);
    #
    # config.GetWords.init(args.path);
    #
    # kernel_tk = config.Core.CoreTkinter(args.mode);
    #
    # kernel_tk.set_style();
    #
    # label_objects = config.LabelObject.LabelObject(
    #     kernel_tk,config.GetWords.LIST_CONTENTS,
    #     config.GetWords.PRONUNCE,
    #     config.GetWords.EXAMPLE,
    #     config.GetWords.TRANSLATE,
    #     args.time
    # );
    #
    # label_objects.create();
    #
    # kernel_tk.root_window.mainloop();
    #
    return 0;



if __name__ == '__main__':
    main()


