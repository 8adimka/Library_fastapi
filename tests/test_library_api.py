import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_create_and_get_book():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Create book
        response = await ac.post(
            "/api/library/books/",
            json={"title": "Test Book", "author_ids": [], "hall_id": None},
        )
        assert response.status_code == 201
        book_id = response.json()["id"]

        # Get book
        response = await ac.get(f"/api/library/books/{book_id}/")
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Test Book"


@pytest.mark.asyncio
async def test_create_and_get_author():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        import uuid
        unique_name = f"Author Name {uuid.uuid4()}"
        response = await ac.post("/api/library/authors/", json={"name": unique_name})
        assert response.status_code == 201
        author_id = response.json()["id"]
        response = await ac.get(f"/api/library/authors/{author_id}/")
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == unique_name
