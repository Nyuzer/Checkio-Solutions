# https://py.checkio.org/en/mission/sort-by-extension/


def sort_by_ext(files):
    res = []
    new_files = []
    files = sorted(files)
    for i in files:
        if not len(i.replace('.', ' ').split()) > 1:
            res.append(i)
        else:
            new_files.append(i)
    new_files = sorted(new_files, key=lambda file: file.split('.')[-1])
    return res + new_files
