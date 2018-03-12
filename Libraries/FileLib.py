# Simplest ever library for Robot Framework.
# For an education purposes only.


from os.path import exists, isdir


class FileLib:
    def __init__(self):
        pass

    @staticmethod
    def files_exist(*files):
        for file in files:
            if not exists(file) or isdir(file):
                raise OSError("%s missing" % file)
        return True
