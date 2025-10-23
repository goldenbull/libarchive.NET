import re


def extract_from_txt(txt):
    """
    extract two kinds of code:
        #define MACRO VALUE
        __LA_DECL .... ;

    TODO: find parameter names from .c files
    """

    txt = txt.replace('\t', ' ')

    r1 = re.compile(r'^#define +([A-Z_]+) +(.*)\n', re.MULTILINE)
    macros = []
    for name, val in re.findall(r1, txt):
        # remove comments in val
        pos = val.find("/*")
        if pos != -1:
            val = val[:pos]
        macros.append((name, val.strip()))

    r2 = re.compile(r'^__LA_DECL\s+(.*[ *])([a-z0-9_]+)\s*\((.*)\);', re.MULTILINE)
    functions = []
    for type, name, parameters in re.findall(r2, txt):
        functions.append((type.strip(), name, parameters.strip()))

    return macros, functions


def parse_archive_h():
    txt = open("../libarchive/archive.h", "rt").read()
    macros, functions = extract_from_txt(txt)
    for x in macros + functions:
        print(x)


def parse_archive_entry_h():
    txt = open("../libarchive/archive_entry.h", "rt").read()
    macros, functions = extract_from_txt(txt)
    for x in macros + functions:
        print(x)


if __name__ == '__main__':
    parse_archive_h()
    parse_archive_entry_h()
