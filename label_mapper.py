LABEL_NAME_TO_ID = {}


def map_label_to_id(service, label_name):
    if label_name in LABEL_NAME_TO_ID:
        return LABEL_NAME_TO_ID[label_name]
    else:
        label_id = service.users().labels().list(userId='me').execute()
        labels = label_id.get('labels', [])
        for label in labels:
            if label['name'].lower() == label_name.lower():
                LABEL_NAME_TO_ID[label_name] = label['id']
                return label['id']

        # Jeśli etykieta nie istnieje, to ją utwórz
        from gmail_api import create_label
        new_label_id = create_label(service, label_name)
        LABEL_NAME_TO_ID[label_name] = new_label_id
        return new_label_id
