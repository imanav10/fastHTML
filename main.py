from fasthtml.common import *

app,rt = fast_app()

# @rt('/')
# def get(): return Title("test"), Div(P('Hello World!'), hx_get="/change")


# serve()

# @rt('/change')
# def get(): return P('Nice to be here!')

app = FastHTML()
messages = ["This is a message, which will get rendered as a paragraph"]

@app.get("/")
def home():
    return Main(H1('Messages'), 
                *[P(msg) for msg in messages],
                A("Link to Page 2 (to add messages)", href="/page2"))

@app.get("/page2")
def page2():
    return Main(P("Add a message with the form below:"),
                Form(Input(type="text", name="data"),
                     Button("Submit"),
                     action="/", method="post"))

@app.post("/")
def add_message(data:str):
    messages.append(data)
    return home()