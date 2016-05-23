import urlparse

def app(environ, start_response):
	params = urlparse.parse_qs(environ["QUERY_STRING"])

	start_response("200 OK", [("Content-Type", "text/plain")])
	body = []
	for keys, values in params.iteritems():
		if len(values) > 1:
			for val in values:
				body.append('%s=%s' % (keys, val))
				continue
		else:
			body.append('%s=%s' % (keys, values))
	return body
	
