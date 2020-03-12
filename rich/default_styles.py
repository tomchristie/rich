from typing import Dict

from .style import Style

DEFAULT_STYLES: Dict[str, Style] = {
    "none": Style(),
    "reset": Style(
        color="default",
        bgcolor="default",
        dim=False,
        bold=False,
        italic=False,
        underline=False,
        blink=False,
        blink2=False,
        reverse=False,
        conceal=False,
        strike=False,
    ),
    "dim": Style(dim=True),
    "bright": Style(dim=False),
    "bold": Style(bold=True),
    "strong": Style(bold=True),
    "code": Style(reverse=True, bold=True),
    "b": Style(bold=True),
    "italic": Style(italic=True),
    "emphasize": Style(italic=True),
    "i": Style(italic=True),
    "underline": Style(underline=True),
    "u": Style(underline=True),
    "blink": Style(blink=True),
    "blink2": Style(blink2=True),
    "reverse": Style(reverse=True),
    "strike": Style(strike=True),
    "s": Style(strike=True),
    "black": Style(color="black"),
    "red": Style(color="red"),
    "green": Style(color="green"),
    "yellow": Style(color="yellow"),
    "magenta": Style(color="magenta"),
    "cyan": Style(color="cyan"),
    "white": Style(color="white"),
    "logging.keyword": Style(bold=True, color="yellow"),
    "logging.level.notset": Style(dim=True),
    "logging.level.debug": Style(color="green"),
    "logging.level.info": Style(color="blue"),
    "logging.level.warning": Style(color="red"),
    "logging.level.error": Style(color="red", bold=True),
    "logging.level.critical": Style(color="red", bold=True, reverse=True),
    "log.level": Style(),
    "log.time": Style(color="cyan", dim=True),
    "log.message": Style(),
    "log.path": Style(dim=True),
    "repr.str": Style(color="green", italic=False, bold=False),
    "repr.brace": Style(bold=True),
    "repr.tag_start": Style(bold=True),
    "repr.tag_name": Style(color="bright_magenta", bold=True),
    "repr.tag_contents": Style(color="default"),
    "repr.tag_end": Style(bold=True),
    "repr.attrib_name": Style(color="yellow", italic=True),
    "repr.attrib_equal": Style(bold=True),
    "repr.attrib_value": Style(color="magenta", italic=False),
    "repr.number": Style(color="blue", bold=True, italic=False),
    "repr.bool_true": Style(color="bright_green", italic=True),
    "repr.bool_false": Style(color="bright_red", italic=True),
    "repr.none": Style(color="magenta", italic=True),
    "repr.url": Style(underline=True, color="bright_blue", bold=False),
    "rule.line": Style(color="bright_green"),
    "rule.text": Style(),
    "repr.path": Style(color="magenta"),
    "repr.filename": Style(color="bright_magenta", bold=True),
    "table.header": Style(bold=True),
    "table.footer": Style(bold=True),
    "table.cell": Style(),
    "table.title": Style(italic=True),
    "table.caption": Style(italic=True, dim=True),
    "traceback.text": Style(),
    "traceback.filename": Style(color="green"),
    "traceback.lineno": Style(bold=True, color="cyan"),
    "traceback.name": Style(color="yellow"),
    "traceback.exc_type": Style(color="bright_red", bold=True),
    "traceback.exc_value": Style(),
    "traceback.offset": Style(color="bright_red", bold=True),
    "bar.back": Style(color="grey23"),
    "bar.complete": Style(color="bright_magenta"),
    "bar.finished": Style(color="bright_green"),
    "progress.description": Style(),
    "progress.data": Style(color="green"),
    "progress.percentage": Style(color="magenta"),
    "progress.remaining": Style(color="cyan"),
    "progress.data.speed": Style(color="red"),
}

MARKDOWN_STYLES = {
    "markdown.paragraph": Style(),
    "markdown.text": Style(),
    "markdown.emph": Style(italic=True),
    "markdown.strong": Style(bold=True),
    "markdown.code": Style(bgcolor="black", color="bright_white"),
    "markdown.code_block": Style(dim=True, color="cyan", bgcolor="black"),
    "markdown.block_quote": Style(color="magenta"),
    "markdown.list": Style(color="cyan"),
    "markdown.item": Style(),
    "markdown.item.bullet": Style(color="yellow", bold=True),
    "markdown.item.number": Style(color="yellow", bold=True),
    "markdown.hr": Style(dim=True),
    "markdown.h1.border": Style(),
    "markdown.h1": Style(bold=True),
    "markdown.h2": Style(bold=True, underline=True),
    "markdown.h3": Style(bold=True),
    "markdown.h4": Style(bold=True, dim=True),
    "markdown.h5": Style(underline=True),
    "markdown.h6": Style(italic=True),
    "markdown.h7": Style(italic=True, dim=True),
    "markdown.link": Style(bold=True),
    "markdown.link_url": Style(underline=True),
}


PYTHON_STYLES = {
    "python.background": Style(),
    "python.foreground": Style(),
    "python.keyword": Style(),
    "python.operator": Style(),
    "python.endmarker": Style(),
    "python.name": Style(),
    "python.number": Style(),
    "python.string": Style(),
    "python.newline": Style(),
    "python.indent": Style(),
    "python.dedent": Style(),
    "python.lpar": Style(),
    "python.rpar": Style(),
    "python.lsqb": Style(),
    "python.rsqb": Style(),
    "python.colon": Style(),
    "python.comma": Style(),
    "python.semi": Style(),
    "python.plus": Style(),
    "python.minus": Style(),
    "python.star": Style(),
    "python.slash": Style(),
    "python.vbar": Style(),
    "python.amper": Style(),
    "python.less": Style(),
    "python.greater": Style(),
    "python.equal": Style(),
    "python.dot": Style(),
    "python.percent": Style(),
    "python.lbrace": Style(),
    "python.rbrace": Style(),
    "python.eqequal": Style(),
    "python.notequal": Style(),
    "python.lessequal": Style(),
    "python.greaterequal": Style(),
    "python.tilde": Style(),
    "python.circumflex": Style(),
    "python.leftshift": Style(),
    "python.rightshift": Style(),
    "python.doublestar": Style(),
    "python.plusequal": Style(),
    "python.minequal": Style(),
    "python.starequal": Style(),
    "python.slashequal": Style(),
    "python.percentequal": Style(),
    "python.amperequal": Style(),
    "python.vbarequal": Style(),
    "python.circumflexequal": Style(),
    "python.leftshiftequal": Style(),
    "python.rightshiftequal": Style(),
    "python.doublestarequal": Style(),
    "python.doubleslash": Style(),
    "python.doubleslashequal": Style(),
    "python.at": Style(),
    "python.atequal": Style(),
    "python.rarrow": Style(),
    "python.ellipsis": Style(),
    "python.colonequal": Style(),
    "python.op": Style(),
    "python.await": Style(),
    "python.async": Style(),
    "python.type_ignore": Style(),
    "python.type_comment": Style(),
    "python.errortoken": Style(),
    "python.comment": Style(),
    "python.nl": Style(),
    "python.encoding": Style(),
    "python.n_tokens": Style(),
    "python.nt_offset": Style(),
}

DEFAULT_STYLES.update(MARKDOWN_STYLES)
DEFAULT_STYLES.update(PYTHON_STYLES)


if __name__ == "__main__":
    import token

    for name in token.tok_name.values():
        print(f'"python.{name.lower()}" : Style(),')
