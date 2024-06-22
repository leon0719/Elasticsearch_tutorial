import time
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError

# 定義連接參數
es_host = 'http://localhost:9200'
es = Elasticsearch([es_host])

# 重試連接邏輯
for attempt in range(5):
    try:
        # 嘗試獲取 Elasticsearch 狀態
        if es.ping():
            print("Elasticsearch 連接成功")
            break
    except ConnectionError:
        print(f"Elasticsearch 連接失敗，重試 {attempt + 1}/5")
        time.sleep(10)
else:
    print("無法連接到 Elasticsearch，請檢查設置")
    exit(1)

# 索引文檔
doc = {'title': 'Test', 'body': 'Test Document'}
es.index(index='test-index', id=1, document=doc)

# 搜尋文檔
result = es.search(index='test-index', query={'match': {'title': 'Test'}})
print("result", result)
