INPUT_SCHEMA = {
    "roles": {
        'datatype': 'STRING',
        'required': True,
        'shape': [-1],
        'example': ["user", "assistant", "user"]
    },
    "chunks": {
        'datatype': 'STRING',
        'required': True,
        'shape': [-1],
        'example': [
            "Inferless is a machine learning model deployment platform.",
            "It simplifies the deployment process for machine learning models.",
            "Users can deploy models without worrying about infrastructure ?"
        ]
    }
}
