SEARCH_RESULTS_PER_PAGE = 20

def define_facets():
    facets = [
        'Brand.raw',
        #'CampaignName.raw',
        'Topic.raw',
        'Subtopic.raw',
        'MediaSpendings.raw',
        'PlacementType.raw',
        # 'PlacementName.raw',
        'TargetGroup.raw',
        'SubTargetGroup.raw',
        #'TargetURL.raw',
        'AdFormat.raw',
        #'AdGroup.raw',
        #'AdSpecification.raw',
        'ContentFormat.raw',
        'ContentSpec.raw',
        'PaymentType.raw',
        #'Description.raw',
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
#    'PlacementType.suggest',
    'PlacementName.suggest',
    'AdFormat.suggest',
#    'AdSpecification.suggest',
    'PaymentType.suggest',
    'Description.suggest'
]
