import responder
import json
import jsonpath_rw_ext as jp
# from jsonpath_rw import jsonpath, parse

api = responder.API()


@api.route("/{anything}")
class AnyApi:

    def on_get(self, req, res, *, anything):
        print("Inside GET method")
        if len(req.params) == 0:
            res.media = outputJson("abc123.json")
        elif len(req.params) == 1 and 'param' in req.params:
            if req.params['param'] == "abc":
                res.media = outputJson("abc.json")
            elif req.params['param'] == "xyz":
                res.media = outputJson("xyz.json")
            else:
                res.text = "Invalid query param given, 'param' can be either abc or xyz"
        elif len(req.params) == 2 and 'param1' in req.params:
            if req.params['param'] == "abc" and req.params['param1'] == "abcxyz":
                res.media = outputJson("abcxyz.json")
            elif req.params['param'] == "xyz" and req.params['param1'] == "xyzabc":
                res.media = outputJson("xyzabc.json")
            else:
                res.text = "Invalid query param given, 'param1' can be either abcxyz or xyzabc "
        else:
            res.text = "Invalid query param given, 'param' and 'param1' are the accepted query parameters"


    async def on_post(self, req, res, *, anything):
        print("Inside POST method")
        postedJson = await req.media()
        actualJson = json.dumps(postedJson, indent=4)
        matches = jp.match('$..GlossDiv..Title', postedJson)
        if len(matches) <= 0:
            res.text = "No match found for the query"
        elif len(matches) == 1:
            if matches[0] == 'abc':
                res.media = outputJson("abc.json")
            elif matches[0] == 'xyz':
                res.media = outputJson("xyz.json")
            else:
                res.media = outputJson("abcxyz.json")
        elif len(matches) > 1:
            res.text = "More than one value matched for the query"


def outputJson(fileName):
    filePath = 'resources/' + fileName
    resJson = json.loads(open(filePath).read())
    return resJson


if __name__ == "__main__":
    api.run(port=5000)

