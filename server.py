from datetime import date
from dateutil.relativedelta import relativedelta

from flask import render_template, request
from elasticsearch_dsl import Search

from frontend import app
from es import es_instance
from es.definitions import define_facets, define_searched_fields, SEARCH_RESULTS_PER_PAGE, ES_INDEX
from es.utils import get_completions, get_suggestions, get_results, filter_on_date, filter_on_clicked_checkboxes, \
    sort_results


@app.route('/', methods=['GET', 'POST'])
def main():
    suggestions = []
    completions = []
    score_kwargs = {}

    filters = {}
    filters['sort'] = {}
    filters['sort']['sort_type'] = 'Date'
    facets = define_facets()

    created_on_end = date.today().strftime('%d.%m.%Y')
    created_on_start = date.today() - relativedelta(months=+3)
    created_on_start = created_on_start.strftime('%d.%m.%Y')

    search_query = ''
    s = Search(using=es_instance, index=ES_INDEX).sort({"CreatedOn": {"order": "asc"}})[0:SEARCH_RESULTS_PER_PAGE]

    for facet in facets:
        s.aggs.bucket(facet, 'terms', field=facet, size=0)

    s = s.filter('range', CreatedOnDate={'gte': created_on_start})
    s = s.filter('range', CreatedOnDate={'lte': created_on_end})

    results = s.execute()
    hit_count = results.hits.total

    facet_values = []
    for facet in facets:
        list_element = getattr(results.aggregations, facet).buckets
        facet_values.append(list_element)

    return render_template(
        'main.html',
        results=results,
        hit_count=hit_count,
        search_query=search_query,
        filters=filters,
        facets=facets,
        facet_values=facet_values,
        suggestions=suggestions,
        completions=completions,
        score_kwargs=score_kwargs,
        created_on_start=created_on_start,
        created_on_end=created_on_end)


@app.route('/reload', methods=['GET', 'POST'])
def reload_results_filters():
    filters = request.json

    facets = define_facets()
    searched_fields = define_searched_fields()
    suggestions = []
    created_on_start = filters['date']['created_on_start']
    created_on_end = filters['date']['created_on_end']
    sort_type = filters['sort']['sort_type']
    search_query = filters['search_query']

    s = Search(using=es_instance, index=ES_INDEX)

    s = filter_on_date(s, created_on_start, created_on_end)

    for f in filters['checkbox']:
        filter_name = f
        filter_value = filters['checkbox'][f]
        s = filter_on_clicked_checkboxes(s, filter_name, filter_value)

    s = get_results(s, searched_fields, search_query)
    s = sort_results(s, sort_type)

    for facet in facets:
        s.aggs.bucket(facet, 'terms', field=facet, size=0)

    results = s.execute()
    if not results:
        get_suggestions(s, searched_fields, search_query, suggestions)
        get_suggestions(s, facets, search_query, suggestions)

    hit_count = results.hits.total

    facet_values = []
    for facet in facets:
        list_element = getattr(results.aggregations, facet).buckets
        facet_values.append(list_element)

    return render_template(
        'partials/results_facets.html',
        results=results,
        hit_count=hit_count,
        filters=filters,
        search_query=search_query,
        facet_values=facet_values,
        facets=facets,
        suggestions=suggestions,
        created_on_start=created_on_start,
        created_on_end=created_on_end)


@app.route('/autocomplete/', methods=['GET', 'POST'])
@app.route('/autocomplete/<search_query>', methods=['GET', 'POST'])
def autocomplete(search_query=None):
    completions = []
    if search_query is not None:
        completions = get_completions(search_query)
    return render_template('autocomplete.html', completions=completions)


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1')
