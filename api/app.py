import requests
from src.queries.orm import SyncORM
import datetime
syncorm = SyncORM()
url = "http://127.0.0.1:8000/embedding"
data = {"text": "fuck you"}

response = requests.post(url, json=data)

embedding_data = {
    "embedding": "some_embedding_value",
    "hash": 123456,
    "repo": "some_repo",
    "date": datetime.datetime.now()
}

# # if response.status_code == 200:
# #     embedding = response.json()["embedding"]
# #     print("Embedding:", type(embedding))
# #     embedding_data['embedding'] = embedding
# #     syncorm.insert_test_data(embedding_data)
#
# else:
#     print("Error:", response.status_code, response.text)
# #syncorm.insert_test_data(str(embedding))
syncorm.select_all_from_embeddings()