
LIST_CONTENTS               = [];
PRONUNCE                    = [];
EXAMPLE                     = [];
TRANSLATE                   = [];

GetArray                    = [];

len_elemnt                  = 0;

def get(path) -> int:
    global GetArray;
    temp = []

    with open(path, "r") as fls:
        if not fls:
            return -1;

        reading = fls.read().strip();
        temp = reading.split(";");

        for i in range(len(temp)-1):
            GetArray.append(temp[i]);

    return 0;

def spliter() -> int:

    global LIST_CONTENTS, PRONUNCE, EXAMPLE, TRANSLATE, GetArray;
    global len_elemnt;
    len_elemnt = 4;
    for i in range(0, len(GetArray)):
        (LIST_CONTENTS.append
            (GetArray[i].split(",")[0].strip())
         );

        (PRONUNCE.append
         (GetArray[i].split(",")[1].strip())
         );

        (EXAMPLE.append
         (GetArray[i].split(",")[2].strip())
         );

        (TRANSLATE.append
         (GetArray[i].split(",")[3].strip())
         );

    return 0;


def init(path=None) -> int:

    try:
        if (get(path) != 0):
            print("Check your config file");

        spliter();

    except Exception as ms:
        print(ms);

    return 0;
