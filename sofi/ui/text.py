import html

from .element import Element


class Underlined(Element):
    """Implements <u> tag"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<Underlined>"

    def __str__(self):
        output = ["<u"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</u>")

        return "".join(output)


class UserInput(Element):
    """Implements <kbd> tag"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<UserInput>"

    def __str__(self):
        output = ["<kbd"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</kbd>")

        return "".join(output)


class Variable(Element):
    """Implements <var> tag"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<Variable>"

    def __str__(self):
        output = ["<var"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</var>")

        return "".join(output)


class Strikethrough(Element):
    """Implements <s> tag"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<Strikethrough>"

    def __str__(self):
        output = ["<s"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</s>")

        return "".join(output)


class Small(Element):
    """Implements <small> tag"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<Small>"

    def __str__(self):
        output = ["<small"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</small>")

        return "".join(output)


class Sample(Element):
    """Implements <samp> tag"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<Sample>"

    def __str__(self):
        output = ["<samp"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</samp>")

        return "".join(output)


class Mark(Element):
    """Implements <mark> tag"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<Mark>"

    def __str__(self):
        output = ["<mark"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</mark>")

        return "".join(output)


class Italics(Element):
    """Implements <em> tag"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<Italics>"

    def __str__(self):
        output = ["<em"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</em>")

        return "".join(output)


class Inserted(Element):
    """Implements <ins> tag"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<Inserted>"

    def __str__(self):
        output = ["<ins"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</ins>")

        return "".join(output)


class Deleted(Element):
    """Implements <del> tag"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<Deleted>"

    def __str__(self):
        output = ["<del"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</del>")

        return "".join(output)


class Code(Element):
    """Implements <code> tag"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<Code>"

    def __str__(self):
        output = ["<code"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</code>")

        return "".join(output)


class Bold(Element):
    """Implements the <strong> tag"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<Bold>"

    def __str__(self):
        output = ["<strong"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</strong>")

        return "".join(output)


class Address(Element):
    """Implements the <address> tag"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<Address()>"

    def __str__(self):
        output = ["<address"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</address>")

        return "".join(output)


class Abbreviation(Element):
    """Implementation of the <abbr> tag"""

    def __init__(self, title="", text=None, initialism=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.title = title
        self.initialism = initialism

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<Abbreviation(title='" + self.title + "',initialism=" + str(self.initialism) + ")>"

    def __str__(self):
        output = ["<abbr title=\"", self.title, "\""]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.initialism:
            if self.cl is None:
                self.cl = "initialism"
            else:
                self.cl = f"{self.cl} initialism"

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</abbr>")

        return "".join(output)


class Cite(Element):
    """Implementation of the <cite> tag"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<Cite>"

    def __str__(self):
        output = ["<cite"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        return "".join(output)


class CodeBlock(Element):
    """Implements <pre> tag"""

    def __init__(self, text=None, scrollable=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.scrollable = scrollable

        if text is not None:
            self.addelement(html.escape(text))

    def __repr__(self):
        return "<CodeBlock>"

    def __str__(self):
        output = ["<pre"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.scrollable:
            if self.cl is None:
                self.cl = "pre-scrollable"
            else:
                self.cl = f"{self.cl} pre-scrollable"

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append("><code>")

        output.extend([str(child) for child in self._children])

        output.append("</code></pre>")

        return "".join(output)


class Blockquote(Element):
    """Implements the <blockquote> tag"""

    ALIGNMENT = {
        'center': 'text-center',
        'right': 'text-right',
    }

    def __init__(self, text=None, footer=None, cite=None, alignment=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)
        
        if alignment is not None and alignment not in ALIGNMENT:
            raise ValueError("Unknown blockquote alignment")
        
        self.alignment = alignment
        self.reverse = reverse

        if text is not None:
            self.addelement(text)
        
        if footer is not None or cite is not None:
            f = Footer(footer, cl='blockquote-footer')

            if cite is not None:
                f.addelement(Cite(cite))

            self.addelement(Footer(footer, cl='blockquote-footer'))

    def settext(self, text):
        """Update blockquote text"""

        for i, child in enumerate(self._children):
            if isinstance(child, str):
                if text is None:
                    self._children.pop(i)
                else:
                    child = text
                return
    
    def setfooter(self, text):
        """Update the footer text"""

        for i, child in enumerate(self._children):
            if isinstance(child, Footer) and 'blockquote-footer' in child.cl:
                for c in child._children:
                    if isinstance(c, str):
                        if text is None:
                            self._children.pop(i)
                        else:
                            c = text
                        return
    def __repr__(self):
        return "<Blockquote(reverse=" + str(self.reverse) + ")>"

    def __str__(self):
        output = ["<blockquote"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.alignment:
            if self.cl:
                self.cl = f'{self.cl} {Blockquote.ALIGNMENT[self.alignment]}'
            else:
                self.cl = Blockquote.ALIGNMENT

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</blockquote>")

        return "".join(output)


class Footer(Element):
    """Implements <footer> tag"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<Footer>"

    def __str__(self):
        output = ["<footer"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</footer>")

        return "".join(output)


class Heading(Element):
    """Implements heading tags using size attribute: <h1>, <h2>, etc."""

    def __init__(self, size=1, text=None, secondary_text=None, display=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.size = size
        self.display = display

        if text is not None:
            self.addelement(text)
        
        if secondary_text:
            self.addelement(Small(secondary_text, cl='text-muted'))
    
    def settext(self, text):
        """Update heading text"""

        for i, child in enumerate(self._children):
            if isinstance(child, str):
                if text is None:
                    self._children.pop(i)
                else:
                    child = text
                return
    
    def setsecondarytext(self, text):
        """Update the secondary text"""

        for i, child in enumerate(self._children):
            if isinstance(child, Small) and 'text-muted' in child.cl:
                for c in child._children:
                    if isinstance(c, str):
                        if text is None:
                            self._children.pop(i)
                        else:
                            c = text
                        return

    def __repr__(self):
        return f"<Heading(size={self.size})>"

    def __str__(self):
        output = ["<h", str(self.size)]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.display is not None:
            if self.cl is None:
                self.cl = "display-{self.display}"
            else:
                self.cl = f"{self.cl} display-{self.display}"

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append(f"</h{self.size}>")

        return "".join(output)


class Paragraph(Element):
    """Implements <p> tag"""

    def __init__(self, text=None, lead=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.lead = lead

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<Paragraph>"

    def __str__(self):
        output = ["<p"]

        if self.ident:
            output.append(f' id="{self.ident}" ')

        if self.lead:
            if self.cl is None:
                self.cl = "lead"
            else:
                self.cl = f"{self.cl} lead"

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</p>")

        return "".join(output)
