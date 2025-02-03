Words = [];
Pronunciation = [];
Examples = [];
Translate = [];

GetArray = [];

lenElements = 0;


def get(path) -> int:
    global GetArray;
    temp = []

    with open(path, "r") as fls:
        if not fls:
            return -1;

        reading = fls.read().strip();
        temp = reading.split(";");

        for i in range(len(temp) - 1):
            GetArray.append(temp[i]);

    return 0;


def spliter() -> int:
    global Words, Pronunciation, Examples, Translate, GetArray;
    global lenElements;

    lenElements = 4;

    for i in range(0, len(GetArray)):
        (Words.append
         (GetArray[i].split(",")[0].strip())
         );

        (Pronunciation.append
         (GetArray[i].split(",")[1].strip())
         );

        (Examples.append
         (GetArray[i].split(",")[2].strip())
         );

        (Translate.append
         (GetArray[i].split(",")[3].strip())
         );

    return 0;


def init(path=None) -> int:

    print("We are going to start getting file words...");

    try:
        if (get(path) != 0):
            print("Check your config file");

        spliter();

    except Exception as ms:
        print(ms);

    return 0;
