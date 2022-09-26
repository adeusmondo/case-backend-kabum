import pytest


@pytest.mark.asyncio
async def test_get_health_api(client):
    response = await client.get('/v1/health')
    assert response.status_code == 200
    assert response.json() == {'api': 'looks like everything is ok'}
