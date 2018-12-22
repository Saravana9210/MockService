Run api.py
Inovoke the service locally from any REST client like POSTMAN with base url http://localhost:5000

Any endpoint path with GET request will return same response
Response will be changed based on the query param given
Any endpoint path with POST request will return response based on the request json

As of now, the response is served based on "$..GlossDiv..Title"

{
    "glossary": {
        "title": "ABC glossary",
		"GlossDiv": {
			"GlossList": {
                "GlossEntry": {
                    "Title": "xyz",
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
