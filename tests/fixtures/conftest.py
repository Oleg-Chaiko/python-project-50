import pytest


@pytest.fixture()
def dict_1():
    return {
        "common": {
            "setting1": "Value 1",
            "setting2": 200,
            "setting3": True,
            "setting6": {
                "key": "value",
                "doge": {
                    "wow": ""
                }
            }
        },
        "group1": {
            "baz": "bas",
            "foo": "bar",
            "nest": {
                "key": "value"
            }
        },
        "group2": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    }


@pytest.fixture()
def dict_2():
    return {
        "common": {
            "follow": False,
            "setting1": "Value 1",
            "setting3": None,
            "setting4": "blah blah",
            "setting5": {
                "key5": "value5"
            },
            "setting6": {
                "key": "value",
                "ops": "vops",
                "doge": {
                    "wow": "so much"
                }
            }
        },
        "group1": {
            "foo": "bar",
            "baz": "bars",
            "nest": "str"
        },
        "group3": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }


@pytest.fixture()
def test_diff():
    return {
        'common': {
            'status': 'unchanged',
            'value': {
                'follow': {
                    'status': 'added',
                     'value': False
                }, 
                'setting1': {
                    'status': 'unchanged',
                    'value': 'Value 1'
                },
                'setting2': {
                    'status': 'deleted',
                    'value': 200
                }, 
                'setting3': {
                    'status': 'changed',
                    'initial_value': True,
                    'current_value': None
                }, 
                'setting4': {
                    'status': 'added',
                    'value': 'blah blah'
                },
                'setting5': {
                    'status': 'added',
                    'value': {
                        'key5': {
                            'status': 'unchanged',
                            'value': 'value5'
                        }
                    }
                },
                'setting6': {
                    'status': 'unchanged',
                    'value': {
                        'doge': {
                            'status': 'unchanged',
                            'value': {
                                'wow': {
                                    'status': 'changed',
                                    'initial_value': '',
                                    'current_value': 'so much'
                                }
                            }
                        },
                        'key': {
                            'status': 'unchanged',
                            'value': 'value'
                        },
                        'ops': {
                            'status': 'added',
                            'value': 'vops'
                        }
                    }
                }
            }
        },
        'group1': {
            'status': 'unchanged',
            'value': {
                'baz': {
                    'status': 'changed',
                    'initial_value': 'bas',
                    'current_value': 'bars'
                },
                'foo': {
                    'status': 'unchanged',
                    'value': 'bar'
                },
                'nest': {
                    'status': 'changed',
                    'initial_value': {
                        'key': {
                            'status': 'unchanged',
                            'value': 'value'
                        }
                    },
                    'current_value': 'str'
                }
            }
        },
        'group2': {
            'status': 'deleted',
            'value': {
                'abc': {
                    'status': 'unchanged',
                    'value': 12345
                },
                'deep': {
                    'status': 'unchanged',
                    'value': {
                        'id': {
                            'status': 'unchanged',
                            'value': 45
                        }
                    }
                }
            }
        },
        'group3': {
            'status': 'added',
            'value': {
                'deep': {
                    'status': 'unchanged',
                    'value': {
                        'id': {
                            'status': 'unchanged',
                            'value': {
                                'number': {
                                    'status': 'unchanged',
                                    'value': 45
                                }
                            }
                        }
                    }
                },
                'fee': {
                    'status': 'unchanged',
                    'value': 100500
                }
            }
        }
    }
