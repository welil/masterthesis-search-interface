import requests
import json

from elasticsearch_dsl import Q

from es.definitions import completion_fields, SEARCH_RESULTS_PER_PAGE


def get_results(search_object, searched_fields, value):
    search_query = value

    if not search_query:
        q = Q(query=None)
    else:
        q = Q("multi_match", query=search_query, fields=searched_fields, operator='and')

    search_object = search_object.query(q)[0:SEARCH_RESULTS_PER_PAGE]

    if search_query:
        for searched_field in searched_fields:
            search_object = search_object.highlight(searched_field)

    return search_object


def filter_on_date(search_object, created_on_start, created_on_end):
    search_object = search_object.filter('range', CreatedOnDate={'gte': created_on_start})
    search_object = search_object.filter('range', CreatedOnDate={'lte': created_on_end})

    return search_object


def filter_on_clicked_checkboxes(search_object, filter_name, filter_value):
    search_kwargs = {}
    search_kwargs[filter_name] = []
    search_kwargs[filter_name].append(filter_value)
    search_object = search_object.filter('terms', **search_kwargs)
    return search_object


def sort_results(search_object, sort_type):
    if sort_type == 'Date':
        search_object = search_object.sort({"CreatedOn": {"order": "asc"}})
    elif sort_type == 'Relevance':
        search_object.sort()
    return search_object


def get_suggestions(search_object, fields, query, suggestions):
    for facet in fields:
        search_object = search_object.suggest('my_suggestion', query, term={'field': facet})
        suggestion = search_object.execute_suggest()
        for sug in suggestion.my_suggestion:
            for su in sug.options:
                suggestions.append(su.text)
    return 0


def get_completions(query):
    completions = []

    for completion_field in completion_fields:
        q = json.dumps({
            "comp": {
                "text": query,
                "completion": {
                  "field": completion_field
                }
              }
        })
        response = requests.get('http://localhost:9200/links/_suggest?', data=q)
        query_completions = json.loads(response.text)
        for qcs in query_completions['comp']:
            for qc in qcs['options']:
                completions.append(qc['text'])

    return completions


