from docxtpl import DocxTemplate, R, Listing

tpl = DocxTemplate('templates/escape_tpl.docx')

context = {
    'myvar': R(
        '"less than" must be escaped : <, this can be done with RichText() or R()'
    ),
    'myescvar': 'It can be escaped with a "|e" jinja filter in the template too : < ',
    'nlnp': R('Here is a multiple\nlines\nstring\aand some\aother\aparagraphs',
              color='#ff00ff'),
    'mylisting': Listing(
        'the listing\nwith\nsome\nlines\nand special chars : <>& ...'
    ),
    'page_break': R('\f'),
    'new_listing': """
This is a new listing
Now, does not require Listing() Object
Here is a \t tab\a
Here is a new paragraph\a
Here is a page break : \f
That's it
""",
}

tpl.render(context)
tpl.save('output/escape.docx')
