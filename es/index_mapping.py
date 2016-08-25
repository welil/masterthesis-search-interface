MAPPING = {
    "link": {
        "properties": {
            "CreatedOnDate": {
                "type": "date",
                "format": "dd.MM.yyyy"
            },
            "CreatedOn": {
                "type": "date",
                "format": "dd.MM.yyyy HH:mm:ss"
            },
            "UniqueLinkId": {
                "type": "multi_field",
                "fields": {
                    "UniqueLinkId": {
                        "type": "string",
                        "index": "analyzed"
                    },
                    "raw": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "suggest": {
                        "type": "completion"
                    }
                }
            },
            "TargetGroup": {
                "type": "multi_field",
                "fields": {
                    "TargetGroup": {
                        "type": "string",
                        "index": "analyzed"},
                    "raw": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "suggest": {
                        "type": "completion"
                    }
                }
            },
            "SubTargetGroup": {
                "type": "multi_field",
                "fields": {
                    "SubTargetGroup": {
                        "type": "string",
                        "index": "analyzed"},
                    "raw": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "suggest": {
                        "type": "completion"
                    }
                }
            },
            "TargetURL": {
                "type": "multi_field",
                "fields": {
                    "TargetURL": {
                        "type": "string",
                        "index": "analyzed"},
                    "raw": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "suggest": {
                        "type": "completion"
                    }
                }
            },
            "Brand": {
                "type": "multi_field",
                "fields": {
                    "Brand": {
                        "type": "string",
                        "index": "analyzed"
                    },
                    "raw": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "suggest": {
                        "type": "completion"
                    }
                }
            },
            "CampaignName": {
                "type": "multi_field",
                "fields": {
                    "CampaignName": {
                        "type": "string",
                        "index": "analyzed"
                    },
                    "raw": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "suggest": {
                        "type": "completion"
                    }
                }
            },
            "ContentFormat": {
                "type": "multi_field",
                "fields": {
                    "ContentFormat": {
                        "type": "string",
                        "index": "analyzed"
                    },
                    "raw": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "suggest": {
                        "type": "completion"
                    }
                }
            },
            "ContentSpec": {
                "type": "multi_field",
                "fields": {
                    "ContentSpec": {
                        "type": "string",
                        "index": "analyzed"
                    },
                    "raw": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "suggest": {
                        "type": "completion"
                    }
                }
            },
            "Topic": {
                "type": "multi_field",
                "fields": {
                    "Topic": {
                        "type": "string",
                        "index": "analyzed"
                    },
                    "raw": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "suggest": {
                        "type": "completion"
                    }
                }
            },
            "Subtopic": {
                "type": "multi_field",
                "fields": {
                    "Subtopic": {
                        "type": "string",
                        "index": "analyzed"
                    },
                    "raw": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "suggest": {
                        "type": "completion"
                    }
                }
            },
            "MediaSpendings": {
                "type": "multi_field",
                "fields": {
                    "MediaSpendings": {
                        "type": "string",
                        "index": "analyzed"
                    },
                    "raw": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "suggest": {
                        "type": "completion"
                    }
                }
            },
            "PlacementType": {
                "type": "multi_field",
                "fields": {
                    "PlacementType": {
                        "type": "string",
                        "index": "analyzed"
                    },
                    "raw": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "suggest": {
                        "type": "completion"
                    }
                }
            },
            "PlacementName": {
                "type": "multi_field",
                "fields": {
                    "PlacementName": {
                        "type": "string",
                        "index": "analyzed"
                    },
                    "raw": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "suggest": {
                        "type": "completion"
                    }
                }
            },
            "AdFormat": {
                "type": "multi_field",
                "fields": {
                    "AdFormat": {
                        "type": "string",
                        "index": "analyzed"
                    },
                    "raw": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "suggest": {
                        "type": "completion"
                    }
                }
            },
            "AdSpecification": {
                "type": "string",
                "fields": {
                    "AdSpecification": {
                        "type": "string",
                        "index": "analyzed"
                    },
                    "raw": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "suggest": {
                        "type": "completion"
                    }
                }
            },
            "AdGroup": {
                "type": "string",
                "fields": {
                    "AdGroup": {
                        "type": "string",
                        "index": "analyzed"
                    },
                    "raw": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "suggest": {
                        "type": "completion"
                    }
                }
            },
            "PaymentType": {
                "type": "multi_field",
                "fields": {
                    "PaymentType": {
                        "type": "string",
                        "index": "analyzed"
                    },
                    "raw": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "suggest": {
                        "type": "completion"
                    }
                }
            },
            "Description": {
                "type": "multi_field",
                "fields": {
                    "Description": {
                        "type": "string",
                        "index": "analyzed"
                    },
                    "raw": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "suggest": {
                        "type": "completion"
                    }
                }
            },
            "Market": {
                "type": "multi_field",
                "fields": {
                    "Market": {
                        "type": "string",
                        "index": "analyzed"
                    },
                    "raw": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "suggest": {
                        "type": "completion"
                    }
                }
            }
        }
    }
}
