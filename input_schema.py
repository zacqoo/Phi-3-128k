INPUT_SCHEMA = {
    "roles": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["user"]
    },
    "chunks": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': [
            "Inferless is a machine learning model deployment platform.",
        ]
    }
}
