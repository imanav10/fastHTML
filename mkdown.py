from fasthtml.common import *

hdrs = (MarkdownJS(), HighlightJS(langs=['python', 'javascript', 'html', 'css']), )

app, rt = fast_app(hdrs=hdrs)

content = """
Here are some _markdown_ elements.

- This is a list item
- This is another list item
- And this is a third list item

```
a code block
```

**Fenced code blocks work here.**
"""

@rt('/')
def get(req):
    return Titled("Markdown rendering example", Div(content,cls="marked"))


def hero(title, statement):
    return Div(H1(title),P(statement), cls="hero")

# usage example
Main(
    hero("Hello World", "This is a hero statement")
)
serve()