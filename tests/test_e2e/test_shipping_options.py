import pytest


@pytest.mark.asyncio
async def test_list_shipping_options(client, shipping_options):
    response = await client.get('/v1/shipping-options')
    assert response.status_code == 200
    assert response.json() == shipping_options
