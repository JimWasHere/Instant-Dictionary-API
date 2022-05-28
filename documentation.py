import justpy as jp


class Doc:

    def serve(self):
        wp = jp.WebPage()

        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")

        jp.Div(a=div, text="Dictionary API Documentation", classes="text-4xl")
        jp.Div(a=div, text="Get definitions of words", classes="text-lg")
        jp.Hr(a=div)
        jp.Div(a=div, text="www.website.com/api?w=word")
        jp.Hr(a=div)
        jp.Div(a=div, text="""
        {"word": "word", "definition": 
        ["A distinct unit of language (sounds in speech or written letters) with a 
        particular meaning, composed of one or more morphemes, and also of one or more phonemes that determine its 
        sound pattern."]}
        """)
        return wp




