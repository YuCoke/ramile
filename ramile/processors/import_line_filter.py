from ramile.processors import LineFilterBase


class JavaImportLineFilter(LineFilterBase):
    """
    Filters out Java import statements like 'import xxx.yyy;' or 'import static xxx.yyy;'.
    """

    def filter(self, file, line):
        # stripped_line = line.strip()
        if line.startswith("import ") or line.startswith("package "):
            file.found_comment_line()  # 可选：记录过滤
            return line, True
        return line, False
