## Project File Structure 

```
contextify-ai/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── routes.py
│   ├── services/
│   │   ├── rag_service.py
│   │   ├── minio_service.py
│   │   ├── embedding_service.py
│   │   ├── loader_service.py
│   ├── utils/
│
├── data/
├── faiss_index/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env
```