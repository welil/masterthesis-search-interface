ES_INDEX = 'links'

SEARCH_RESULTS_PER_PAGE = 20


def define_facets():
    facets = [
        'Brand.raw',
        'Topic.raw',
        'Subtopic.raw',
        'MediaSpendings.raw',
        'PlacementType.raw',
        'TargetGroup.raw',
        'SubTargetGroup.raw',
        'AdFormat.raw',
        'ContentFormat.raw',
        'ContentSpec.raw',
        'PaymentType.raw',
        'Market.raw'
    ]
    return facets


def define_searched_fields():
    searched_fields = [
        'Brand',
        'CampaignName',
        'Topic',
        'Subtopic',
        'MediaSpendings',
        'TargetGroup',
        'TargetURL.raw',
        'PlacementType',
        'PlacementName',
        'AdFormat',
        'AdSpecification',
        'PaymentType',
        'Description',
        'Market',
        'UniqueLinkId',
        'ShortUrl'
    ]
    return searched_fields


completion_fields = [
    'UniqueLinkId.suggest',
    'Brand.suggest',
    'CampaignName.suggest',
    'Topic.suggest',
    'Subtopic.suggest',
    'MediaSpendings.suggest',
    'TargetURL.suggest',
    'PlacementName.suggest',
    'AdFormat.suggest',
    'PaymentType.suggest',
    'Description.suggest'
]
