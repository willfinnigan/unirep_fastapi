import requests
import json

url = 'http://0.0.0.0:80/unirep'

def get_embedding(sequence):
    r = requests.post(url, json={'protein': sequence})
    return json.loads(r.text)['unirep']

if __name__ == '__main__':
    sequence = 'MAVDSPDERLQRRIAQL'
    embedding = get_embedding(sequence)

    print(embedding)
