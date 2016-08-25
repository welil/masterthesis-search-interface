import io
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from es import es_instance
from es.definitions import ES_INDEX
from es.index_mapping import MAPPING

from frontend import app


def index(json_path):
    es_instance.indices.delete(index=ES_INDEX, ignore=[400, 404])
    es_instance.indices.create(index=ES_INDEX)
    es_instance.indices.put_mapping(index=ES_INDEX, doc_type="link", body=MAPPING)

    with io.open(json_path, encoding='utf8') as f:
        bulk_data = ''
        i = 0
        for line in f:
            i += 1
            bulk_data += line
            if i % 500 == 0:
                es_instance.bulk(index=ES_INDEX, body=bulk_data, refresh=True)
                bulk_data = ''

    if bulk_data:
        es_instance.bulk(index=ES_INDEX, body=bulk_data, refresh=True)

    return 0

if __name__ == '__main__':
    # dummy context to setup up flask elasticsearch
    context = app.test_request_context('/', method='POST')
    context.push()
    index(sys.argv[1])
