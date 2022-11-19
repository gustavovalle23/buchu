from app.results import Err


# python -m pytest test -s
def test_should_return_a_not_found_err():
    scenarios = [
        {'ret': Err.not_found(payload={'entity': 'user'}, cause={'foo': 'bar'}),
         'expect': {
            'payload': {'entity': 'user'},
            'cause': {'foo': 'bar'},
            'code': 'NOT_FOUND',
            'message': 'Not Found'
        }
        },
        {
            'ret': Err.not_found(message='message', payload={'entity': 'user'}, cause={'foo': 'bar'}),
            'expect': {
                'payload': {'entity': 'user'},
                'cause': {'foo': 'bar'},
                'code': 'NOT_FOUND',
                'message': 'message'
            }
        },
    ]

    for scenario in scenarios:
        assert scenario.get("ret").to_json().get(
            "Error") == scenario.get("expect")
        assert scenario.get("ret").is_not_found_error == True


def test_should_return_a_already_exists_err():
    scenarios = [
        {
            'ret': Err.already_exists(payload={'entity': 'user'}, cause={'foo': 'bar'}),
            'expect': {
                'payload': {'entity': 'user'},
                'cause': {'foo': 'bar'},
                'code': 'ALREADY_EXISTS',
                'message': 'Already exists'
            }
        },
        {
            'ret': Err.already_exists(message='message', payload={'entity': 'user'}, cause={'foo': 'bar'}),
            'expect': {
                'payload': {'entity': 'user'},
                'cause': {'foo': 'bar'},
                'code': 'ALREADY_EXISTS',
                'message': 'message'
            }
        },
        {
            'ret': Err.already_exists(),
            'expect': {
                'payload': None,
                'cause': None,
                'code': 'ALREADY_EXISTS',
                'message': 'Already exists'
            }
        }
    ]

    for scenario in scenarios:
        assert scenario.get("ret").to_json().get(
            "Error") == scenario.get("expect")
        assert scenario.get("ret").is_already_exists_error == True


def test_should_return_a_invalid_entity_Err():
    scenarios = [
        {
            'ret': Err.invalid_entity(payload={'entity': 'user'}, cause={'foo': 'bar'}),
            'expect': {
                'payload': {'entity': 'user'},
                'cause': {'foo': 'bar'},
                'code': 'INVALID_ENTITY',
                'message': 'Invalid entity'
            }
        },
        {
            'ret': Err.invalid_entity(message='message', payload={'entity': 'user'}, cause={'foo': 'bar'}),
            'expect': {
                'payload': {'entity': 'user'},
                'cause': {'foo': 'bar'},
                'code': 'INVALID_ENTITY',
                'message': 'message'
            }
        },
        {
            'ret': Err.invalid_entity(),
            'expect': {
                'payload': None,
                'cause': None,
                'code': 'INVALID_ENTITY',
                'message': 'Invalid entity'
            }
        }
    ]

    for scenario in scenarios:
        assert scenario.get("ret").to_json().get(
            "Error") == scenario.get("expect")
        assert scenario.get("ret").is_invalid_entity_error == True


def test_should_return_a_invalid_arguments_Err():
    scenarios = [
        {
            'ret': Err.invalid_arguments(payload={'entity': 'user'}, args={'foo': 'bar'}, cause={'foo': 'bar'}),
            'expect': {
                'payload': {'entity': 'user', 'invalid_args': {'foo': 'bar'}},
                'cause': {'foo': 'bar'},
                'code': 'INVALID_ARGUMENTS',
                'message': 'Invalid arguments'
            }
        },
        {
            'ret': Err.invalid_arguments(message='message', payload={'entity': 'user'}, cause={'foo': 'bar'}),
            'expect': {
                'payload': {'entity': 'user', 'invalid_args': None},
                'cause': {'foo': 'bar'},
                'code': 'INVALID_ARGUMENTS',
                'message': 'message'
            }
        },
        {
            'ret': Err.invalid_arguments(),
            'expect': {
                'payload': {'invalid_args': None},
                'cause': None,
                'code': 'INVALID_ARGUMENTS',
                'message': 'Invalid arguments'
            }
        }
    ]

    for scenario in scenarios:
        assert scenario.get("ret").to_json().get(
            "Error") == scenario.get("expect")
        assert scenario.get("ret").is_invalid_arguments_error == True


def test_should_return_a_permission_denied_Err():
    scenarios = [
        {
            'ret': Err.permission_denied(payload={'entity': 'user'}, cause={'foo': 'bar'}),
            'expect': {
                'payload': {'entity': 'user'},
                'cause': {'foo': 'bar'},
                'code': 'PERMISSION_DENIED',
                'message': 'Permission denied'
            }
        },
        {
            'ret': Err.permission_denied(message='message', payload={'entity': 'user'}, cause={'foo': 'bar'}),
            'expect': {
                'payload': {'entity': 'user'},
                'cause': {'foo': 'bar'},
                'code': 'PERMISSION_DENIED',
                'message': 'message'
            }
        },
        {
            'ret': Err.permission_denied(),
            'expect': {
                'payload': None,
                'cause': None,
                'code': 'PERMISSION_DENIED',
                'message': 'Permission denied'
            }
        }
    ]

    for scenario in scenarios:
        assert scenario.get("ret").to_json().get(
            "Error") == scenario.get("expect")
        assert scenario.get("ret").is_permission_denied_error == True


def test_should_return_a_unknown_Err():
    scenarios = [
        {
            'ret': Err.unknown(payload={'entity': 'user'}, cause={'foo': 'bar'}),
            'expect': {
                'payload': {'entity': 'user'},
                'cause': {'foo': 'bar'},
                'code': 'UNKNOWN',
                'message': 'Unknown Error'
            }
        },
        {
            'ret': Err.unknown(message='message', payload={'entity': 'user'}, cause={'foo': 'bar'}),
            'expect': {
                'payload': {'entity': 'user'},
                'cause': {'foo': 'bar'},
                'code': 'UNKNOWN',
                'message': 'message'
            }
        },
        {
            'ret': Err.unknown(),
            'expect': {
                'payload': None,
                'cause': None,
                'code': 'UNKNOWN',
                'message': 'Unknown Error'
            }
        }
    ]

    for scenario in scenarios:
        assert scenario.get("ret").to_json().get(
            "Error") == scenario.get("expect")
        assert scenario.get("ret").is_unknown_error == True


def test_should_return_a_custom_Err():
    result = Err.build_custom_err('CUSTOM_ERR', 'message', {
                                  'entity': 'user'}, {'foo': 'bar'}, 'custom')

    assert result.to_json().get("Error") == {
        'payload': {'entity': 'user'},
        'cause': {'foo': 'bar'},
        'code': 'CUSTOM_ERR',
        'message': 'message'
    }

    assert result.is_custom_error == True


def test_should_run_the_same_error_many_time_without_bug():
    scenarios = [
        {
            'ret': Err.already_exists(payload={'entity': 'user'}, cause={'foo': 'bar'}),
            'type': 'is_already_exists_error',
            'expect': {
                'payload': {'entity': 'user'},
                'cause': {'foo': 'bar'},
                'code': 'ALREADY_EXISTS',
                'message': 'Already exists'
            }
        },
        {
            'ret': Err.invalid_entity(payload={'entity': 'user'}, cause={'foo': 'bar'}),
            'type': 'is_invalid_entity_error',
            'expect': {
                'payload': {'entity': 'user'},
                'cause': {'foo': 'bar'},
                'code': 'INVALID_ENTITY',
                'message': 'Invalid entity'
            }
        },
        {
            'ret': Err.invalid_arguments(payload={'entity': 'user'}, args={'foo': 'bar'}, cause={'foo': 'bar'}),
            'type': 'is_invalid_arguments_error',
            'expect': {
                'payload': {'entity': 'user', 'invalid_args': {'foo': 'bar'}},
                'cause': {'foo': 'bar'},
                'code': 'INVALID_ARGUMENTS',
                'message': 'Invalid arguments'
            }
        },
        {
            'ret': Err.permission_denied(payload={'entity': 'user'}, cause={'foo': 'bar'}),
            'type': 'is_permission_denied_error',
            'expect': {
                'payload': {'entity': 'user'},
                'cause': {'foo': 'bar'},
                'code': 'PERMISSION_DENIED',
                'message': 'Permission denied'
            }
        },
        {
            'ret': Err.unknown(),
            'type': 'is_unknown_error',
            'expect': {
                'payload': None,
                'cause': None,
                'code': 'UNKNOWN',
                'message': 'Unknown Error'
            }
        },
        {
            'ret': Err.not_found(),
            'type': 'is_not_found_error',
            'expect': {
                'payload': None,
                'cause': None,
                'code': 'NOT_FOUND',
                'message': 'Not Found'
            }
        }
    ]

    for scenario in scenarios:
        assert scenario.get("ret").to_json().get(
            "Error") == scenario.get('expect')
        assert getattr(scenario.get("ret"), scenario.get('type')) == True
