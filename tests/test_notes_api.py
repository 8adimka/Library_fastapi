import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_create_and_get_note():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Create note
        response = await ac.post(
            "/notes/", json={"note": "Тестовая заметка", "description": "Описание"}
        )
        assert response.status_code == 201
        note_id = response.json()["id"]

        # Get note
        response = await ac.get(f"/notes/{note_id}/")
        assert response.status_code == 200
        data = response.json()
        assert data["note"] == "Тестовая заметка"
        assert data["description"] == "Описание"


@pytest.mark.asyncio
async def test_delete_note():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/notes/", json={"note": "Удалить", "description": "desc"}
        )
        note_id = response.json()["id"]
        response = await ac.delete(f"/notes/{note_id}/")
        assert response.status_code == 200
        response = await ac.get(f"/notes/{note_id}/")
        assert response.status_code == 404
