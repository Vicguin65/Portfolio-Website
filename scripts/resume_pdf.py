"""Render a structured resume to PDF in the same layout as Du_Tyler_Resume.pdf.

Layout measured from the reference PDF: US Letter, 0.5in margins, Times New Roman
throughout, 10pt body on 13.2pt leading, 12pt all-caps section headings, a 16pt
centered name, and Arial bullet glyphs hanging at 18pt with text indented to 36pt.

Real Times New Roman and Arial are used when the system has them; otherwise this
falls back to the base-14 Times and Helvetica, which are metric-compatible.
"""

import re
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib.colors import Color
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

MARGIN = 36
BODY_SIZE = 10
LEADING = 13.2
CONTENT_WIDTH = letter[0] - 2 * MARGIN

FONT_DIR = Path("C:/Windows/Fonts")
_TTF = {
    "TNR": "times.ttf",
    "TNR-Bold": "timesbd.ttf",
    "TNR-Italic": "timesi.ttf",
    "TNR-BoldItalic": "timesbi.ttf",
    "ArialTT": "arial.ttf",
}


def _register_fonts():
    """Return (serif, serif_bold, serif_italic, bullet_font), preferring real system fonts."""
    try:
        for name, filename in _TTF.items():
            path = FONT_DIR / filename
            if not path.exists():
                raise FileNotFoundError(path)
            pdfmetrics.registerFont(TTFont(name, str(path)))
        pdfmetrics.registerFontFamily(
            "TNR", normal="TNR", bold="TNR-Bold", italic="TNR-Italic", boldItalic="TNR-BoldItalic"
        )
        return "TNR", "TNR-Bold", "TNR-Italic", "ArialTT"
    except Exception:
        return "Times-Roman", "Times-Bold", "Times-Italic", "Helvetica"


SERIF, SERIF_BOLD, SERIF_ITALIC, BULLET_FONT = _register_fonts()

NAME = ParagraphStyle(
    "name", fontName=SERIF_BOLD, fontSize=16, leading=18.4, alignment=TA_CENTER, spaceAfter=3.2
)
CONTACT = ParagraphStyle(
    "contact", fontName=SERIF, fontSize=BODY_SIZE, leading=LEADING, alignment=TA_CENTER
)
HEADING = ParagraphStyle(
    "heading", fontName=SERIF_BOLD, fontSize=12, leading=13.8, spaceBefore=13.1, spaceAfter=5.2
)
HEADING_FIRST = ParagraphStyle("headingFirst", parent=HEADING, spaceBefore=7.8)
ENTRY_LEFT = ParagraphStyle("entryLeft", fontName=SERIF_BOLD, fontSize=BODY_SIZE, leading=LEADING)
ENTRY_RIGHT = ParagraphStyle("entryRight", parent=ENTRY_LEFT, alignment=TA_RIGHT)
SUB_LEFT = ParagraphStyle("subLeft", fontName=SERIF_ITALIC, fontSize=BODY_SIZE, leading=LEADING)
SUB_RIGHT = ParagraphStyle("subRight", parent=SUB_LEFT, alignment=TA_RIGHT)
BULLET = ParagraphStyle(
    "bullet",
    fontName=SERIF,
    fontSize=BODY_SIZE,
    leading=LEADING,
    leftIndent=36,
    bulletIndent=18,
    bulletFontName=BULLET_FONT,
    bulletFontSize=BODY_SIZE,
)
PLAIN = ParagraphStyle("plain", fontName=SERIF, fontSize=BODY_SIZE, leading=LEADING)

ROW_STYLE = TableStyle([
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
])


RULE_COLOR = Color(0.5333, 0.5333, 0.5333)
RULE_WIDTH = 0.75
RULE_INSET = 3
RULE_BELOW_BASELINE = 5.4


class SectionHeading(Paragraph):
    """A section heading with the reference resume's grey rule beneath it.

    The rule is drawn below the flowable's own box, inside the trailing space, so it
    adds no height and leaves the measured layout unchanged.
    """

    def draw(self):
        super().draw()
        y = self.height - self.style.fontSize - RULE_BELOW_BASELINE
        self.canv.saveState()
        self.canv.setStrokeColor(RULE_COLOR)
        self.canv.setLineWidth(RULE_WIDTH)
        self.canv.line(RULE_INSET, y, self.width - RULE_INSET, y)
        self.canv.restoreState()


def markup(text: str) -> str:
    """Convert **bold** spans to reportlab <b> tags, escaping everything else."""
    parts = re.split(r"\*\*(.+?)\*\*", text)
    return "".join(
        escape(part) if i % 2 == 0 else f"<b>{escape(part)}</b>"
        for i, part in enumerate(parts)
    )


def split_row(left: str, right: str, left_style, right_style):
    """A line with text on the left and text right-aligned to the margin."""
    if not right:
        return Paragraph(markup(left), left_style)
    right_w = pdfmetrics.stringWidth(right, right_style.fontName, right_style.fontSize) + 4
    table = Table(
        [[Paragraph(markup(left), left_style), Paragraph(markup(right), right_style)]],
        colWidths=[CONTENT_WIDTH - right_w, right_w],
    )
    table.setStyle(ROW_STYLE)
    return table


def build_story(resume) -> list:
    story = [Paragraph(escape(resume.header.name), NAME)]
    story += [Paragraph(markup(line), CONTACT) for line in resume.header.contact_lines]

    for s, section in enumerate(resume.sections):
        story.append(SectionHeading(escape(section.heading.upper()), HEADING_FIRST if s == 0 else HEADING))

        for line in section.lines:
            story.append(Paragraph(markup(line), PLAIN))

        for i, entry in enumerate(section.entries):
            block = []
            if i or section.lines:
                block.append(Spacer(1, LEADING))
            block.append(split_row(entry.title, entry.location, ENTRY_LEFT, ENTRY_RIGHT))
            if entry.subtitle or entry.dates:
                block.append(split_row(entry.subtitle, entry.dates, SUB_LEFT, SUB_RIGHT))
            block += [Paragraph(markup(b), BULLET, bulletText="\u25cf") for b in entry.bullets]
            story.append(KeepTogether(block))

    return story


PAGE_HEIGHT = letter[1] - 2 * MARGIN


def _flatten(story):
    """KeepTogether cannot be measured directly; measure what it holds instead."""
    for flowable in story:
        if isinstance(flowable, KeepTogether):
            yield from _flatten(flowable._content)
        else:
            yield flowable


def overflow_lines(resume) -> int:
    """How many body lines too long the resume is for a single page. 0 means it fits."""
    total = 0
    for i, flowable in enumerate(_flatten(build_story(resume))):
        if i:
            total += max(flowable.getSpaceBefore(), 0)
        total += flowable.wrap(CONTENT_WIDTH, PAGE_HEIGHT)[1]
        total += max(flowable.getSpaceAfter(), 0)

    excess = total - PAGE_HEIGHT
    return -(-int(excess) // int(LEADING)) if excess > 0 else 0


def write_pdf(resume, path, title="Tyler Du Resume") -> None:
    """`path` may be a filesystem path or a writable binary buffer."""
    doc = BaseDocTemplate(
        str(path) if isinstance(path, (str, Path)) else path,
        pagesize=letter,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN,
        title=title,
        author=resume.header.name,
    )
    frame = Frame(
        MARGIN, MARGIN, CONTENT_WIDTH, letter[1] - 2 * MARGIN,
        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
    )
    doc.addPageTemplates([PageTemplate(id="resume", frames=[frame])])
    doc.build(build_story(resume))
