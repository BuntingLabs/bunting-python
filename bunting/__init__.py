import urllib.parse
import urllib.request
import json

OSM_EXTRACT_ENDPOINT = 'http://osm.buntinglabs.com/v1/osm/extract'

class BuntingClient:

    def __init__(self, api_key):
        self.api_key = api_key

    def osm_extract(self, tags, bbox=None):
        # list of tags
        if isinstance(tags, str):
            tags = [tags]
        if not (isinstance(bbox, tuple) and len(bbox) == 4):
            raise TypeError('bbox must be tuple with 4 floats')
        for tag in tags:
            if '=' not in tag:
                raise TypeError('tags argument should be of form "key=value", but got tag "%s" without =' % tag)

        params = {
            'tags': '&'.join(tags),
            'api_key': self.api_key,
            'bbox': '%f,%f,%f,%f' % bbox
        }

        response = urllib.request.urlopen(OSM_EXTRACT_ENDPOINT + "?" + urllib.parse.urlencode(params))

        return json.loads(response.read().decode())

