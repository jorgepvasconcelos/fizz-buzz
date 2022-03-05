def validation_fizzbuzz_route(data: dict) -> dict:
    validation = {
        'error': 0,
        'message_response': dict,
        'status_code': int}

    if not data:
        validation['error'] = 1
        validation['message_response'] = {"warning": "you need send a 'value' param"}
        validation['status_code'] = 400
        return validation

    if 'value' not in data:
        validation['error'] = 1
        validation['message_response'] = {"warning": "you need send a 'value' param"}
        validation['status_code'] = 400
        return validation

    if not isinstance(data['value'], int):
        validation['error'] = 1
        validation['message_response'] = {"ValueError": "'value' param must be a integer"}
        validation['status_code'] = 400
        return validation

    return validation
