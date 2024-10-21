
import config.settingArgs
import config.GetWords
import config.Core
import config.LabelObject
import sys

def main() -> int:

    args = config.settingArgs.getparse(sys.argv[1::]);

    config.GetWords.init(args.path);

    kernel_tk = config.Core.CoreTkinter();

    kernel_tk.set_appearence();

    label_objects = config.LabelObject.LabelObject(
        kernel_tk,config.GetWords.LIST_CONTENTS,
        config.GetWords.PRONUNCE,
        config.GetWords.EXAMPLE,
        config.GetWords.TRANSLATE
    );

    label_objects.create();

    kernel_tk.root_window.mainloop();

    return 0;



if __name__ == '__main__':
    main()
