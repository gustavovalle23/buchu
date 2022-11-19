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
        assert scenario.get("ret").to_json().get("Error") == scenario.get("expect")
        assert scenario.get("ret").isNotFoundError == True
