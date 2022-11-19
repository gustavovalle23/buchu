# -*- coding: utf-8 -*-
import json


class _Ok:
    value: any = None

    def __init__(self, value) -> None:
        self.value = value

        if isinstance(value, _Ok):
            self.value = value.value

    @property
    def is_ok(self) -> bool:
        return True

    @property
    def is_err(self) -> bool:
        return False

    @property
    def ok(self):
        return self.value

    @property
    def err(self):
        return None

    def to_string(self):
        if self.value:
            return f'Ok: {json.dumps(self.value)}'
        return 'Ok'

    def to_json(self):
        return {
            'Ok': '' if self.value == None else self.value
        }


class _Err:
    def __init__(self, error) -> None:
        self._error = error

        if isinstance(error, _Err):
            self._error = error._error

    @property
    def is_ok(self) -> bool:
        return False

    @property
    def is_err(self) -> bool:
        return True

    @property
    def ok(self):
        return None

    @property
    def err(self):
        return self._error

    def to_string(self):
        if self._error:
            return f'Error: {json.dumps(self._error)}'
        return 'Error'

    def to_json(self):
        error = '' if self._error == None else self._error
        error = str(error) if isinstance(error, Exception) else error
        return {'Error': error}

    def __str__(self) -> str:
        return json.dumps(self.to_json().get('Error'))


class _ErrBuilder:
    @staticmethod
    def build_custom_err(code, message, payload, cause, caller):
        err = _Err({'payload': payload, 'cause': cause,
                   'code': code, 'message': message})
        setattr(err, f'is_{caller}_error', True)
        return err

    @staticmethod
    def not_found(payload=None, cause=None, message='Not Found'):
        return _ErrBuilder.build_custom_err('NOT_FOUND', message, payload, cause, 'not_found')

    @staticmethod
    def already_exists(payload=None, cause=None, message='Already exists'):
        return _ErrBuilder.build_custom_err('ALREADY_EXISTS', message, payload, cause, 'already_exists')

    @staticmethod
    def invalid_entity(payload=None, cause=None, message='Invalid entity'):
        return _ErrBuilder.build_custom_err('INVALID_ENTITY', message, payload, cause, 'invalid_entity')

    @staticmethod
    def invalid_arguments(args=None,  cause=None, payload={}, message='Invalid arguments'):
        payload['invalid_args'] = args
        return _ErrBuilder.build_custom_err('INVALID_ARGUMENTS', message, payload, cause, 'invalid_arguments')

    @staticmethod
    def permission_denied(payload=None, cause=None, message='Permission denied'):
        return _ErrBuilder.build_custom_err('PERMISSION_DENIED', message, payload, cause, 'permission_denied')

    @staticmethod
    def unknown(payload=None, cause=None, message='Unknown Error'):
        return _ErrBuilder.build_custom_err('UNKNOWN', message, payload, cause, 'unknown')


def Ok(value): return _Ok(value)


Err = _ErrBuilder
