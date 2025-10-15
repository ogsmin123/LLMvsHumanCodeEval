import difflib

def diff_ratio(file1, file2):
    with open(file1, encoding="utf-8", errors="ignore") as f1, open(file2, encoding="utf-8", errors="ignore") as f2:
        t1, t2 = f1.readlines(), f2.readlines()
    sm = difflib.SequenceMatcher(None, t1, t2)
    return 1 - sm.ratio()
