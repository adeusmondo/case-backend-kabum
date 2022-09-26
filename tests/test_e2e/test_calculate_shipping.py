import pytest


@pytest.fixture
def shipping_options_response():
    return [
        {
            'nome': 'Entrega Ninja',
            'valor_frete': 12.00,
            'prazo_dias': 6
        },
        {
            'nome': 'Entrega KaBuM',
            'valor_frete': 8.00,
            'prazo_dias': 4
        }
    ]
    

@pytest.mark.asyncio
async def test_post_shipping_options_retrieve_all_shipping_options(client, shipping_options_response):
    # GIVEN
    payload = {'dimensao': {'altura': 102, 'largura': 40}, 'peso': 400}

    # WHEN
    response = await client.post('/v1/calculate-shipping', json=payload)

    # THEN
    assert response.status_code == 200
    assert response.json() == shipping_options_response


@pytest.mark.asyncio
async def test_post_shipping_options_retrieve_one_shipping_option(client, shipping_options_response):
    # GIVEN
    payload = {'dimensao': {'altura': 152, 'largura': 50}, 'peso': 400}

    # WHEN
    response = await client.post('/v1/calculate-shipping', json=payload)

    # THEN
    assert response.status_code == 200
    assert response.json() == [shipping_options_response[0]]


@pytest.mark.asyncio
async def test_post_shipping_options_retrieve_no_shipping_option(client):
    # GIVEN
    payload = {'dimensao': {'altura': 9999, 'largura': 9999}, 'peso': 400}

    # WHEN
    response = await client.post('/v1/calculate-shipping', json=payload)

    # THEN
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.asyncio
async def test_post_shipping_options_retrieve_invalid_payload(client):
    # GIVEN
    payload = {'dimensao': {'altura': 9999, 'largura': 9999}, 'peso': -1}

    # WHEN
    response = await client.post('/v1/calculate-shipping', json=payload)

    # THEN
    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == 'ensure this value is greater than 0'
