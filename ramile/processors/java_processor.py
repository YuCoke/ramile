from ramile.processors import FileProcessorBase
from ramile.processors import BlankLineFilter
from ramile.processors.c_style_comment_block_filter import CStyleCommentBlockFilter
from ramile.processors.double_slash_comment_filter import DoubleSlashCommentFilter
from ramile.processors.import_line_filter import JavaImportLineFilter


class JavaProcessor(FileProcessorBase):
    expected_extensions = ['.java']

    def __init__(self):
        self.filters.append(BlankLineFilter())
        self.filters.append(CStyleCommentBlockFilter())
        self.filters.append(DoubleSlashCommentFilter())
        self.filters.append(JavaImportLineFilter()) # 自己添加的过滤，如不需要可以自行去除
        return
