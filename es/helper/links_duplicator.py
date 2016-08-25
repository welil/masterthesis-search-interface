import random
import string
import io
import json

json_path_in = 'linksJSON_100000.json'
json_path_out = 'linksJSON-100000000.json'

es_create_instruction = '{"create":{ "_index": "links", "_type": "link"}}'

with io.open(json_path_in, encoding='utf8') as json_fh_in, \
        io.open(json_path_out, encoding='utf8', mode='w') as json_fh_out:
    for line in json_fh_in.readlines():
        line = line.strip()

        # skip empty lines
        if not line:
            continue

        line_json = json.loads(line)

        # skip "create" instructions
        if 'create' in line_json:
            continue

        # use given link and write to out file
        json_fh_out.write('\n'.join([es_create_instruction, line, '']))

        # duplicate link given
        for i in range(0, 99):
            # chg rand link id
            random_link_id = ''.join(random.choice(string.digits + string.ascii_letters) for _ in range(25))
            line_json['UniqueLinkId'] = random_link_id

            # chg short URL
            if 'ShortUrl' in line_json:
                random_url_part = ''.join(random.choice(string.digits + string.ascii_letters) for _ in range(5))
                line_json['ShortUrl'] += '/' + random_url_part

            # chg descript
            if 'Description' in line_json:
                random_word = ''.join(random.choice(string.digits + string.ascii_letters) for _ in
                                      range(random.choice([2, 3, 4, 5, 6, 7, 8])))

                random_word = lambda: ''.join(
                    random.choice(string.digits + string.ascii_letters) for _ in
                    range(random.choice([2, 3, 4, 5, 6, 7, 8])))

                random_description_ext = ' '.join([random_word() for _ in range(0, 3)])
                line_json['Description'] += ' '
                line_json['Description'] += random_description_ext

            line_out = json.dumps(line_json)

            json_fh_out.write('\n'.join([es_create_instruction, line_out, '']))
