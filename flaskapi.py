from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify
from pymetamap import MetaMap

app = Flask(__name__)
api = Api(app)
mm = MetaMap.get_instance('/Users/subigyanepal/Downloads/public_mm/bin/metamap16')


class MetaMapConcepts(Resource):
    def get(self, text):
        text = [text]
        response = []
        concepts, error = mm.extract_concepts(text)
        print concepts
        for concept in concepts:
            response.append({'score':concept.score, 'preferred_name':concept.preferred_name, 'semtypes':concept.semtypes, 'trigger':concept.trigger, 'pos_info':concept.pos_info})
        return jsonify(concepts = response)
        
        
api.add_resource(MetaMapConcepts, '/text/<string:text>')

if __name__ == '__main__':
    app.run(threaded=True)