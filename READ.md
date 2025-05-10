# API REST FastAPI – 3DVP

# Description

Ce projet est une API REST développée avec **FastAPI**, permettant de gérer des "items" avec les opérations CRUD.  
Elle est testée avec **pytest**, vérifiée avec **flake8** et automatiquement déployée via **GitHub Actions** sur **Render**.

##  Fonctionnalités

- `GET /items` – Liste tous les items
- `GET /items/{id}` – Récupère un item par ID
- `POST /items` – Crée un nouvel item
- `PUT /items/{id}` – Met à jour un item
- `DELETE /items/{id}` – Supprime un item

# Technologies

- Python 3.10+
- FastAPI
- pytest
- flake8
- GitHub Actions
- Render.com


```bash
pip install -r requirements.txt
uvicorn main:app --reload
