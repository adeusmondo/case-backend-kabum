from pydantic import BaseModel, Field


class Dimension(BaseModel):
    height: int = Field(
        title='Altura',
        description='Altura do produto em centímetros',
        gt=0,
        alias='altura'
    )
    width: int = Field(
        title='Largura',
        description='Largura do produto em centímetros',
        gt=0,
        alias='largura'
    )


class ProductPayload(BaseModel):
    dimension: Dimension = Field(
        title='Dimensão',
        description='Dimensões do produto em centímetros',
        alias='dimensao'
    )
    weight: int = Field(
        title='Peso',
        description='Peso do produto em gramas',
        gt=0,
        alias='peso'
    )


class CalculateShippingResponse(BaseModel):
    nome: str = Field(
        title='Nome',
        description='Nome do serviço de entrega',
        alias='name'
    )
    valor_frete: float = Field(
        title='Valor do frete',
        description='Valor do frete, de acordo com o cálculo da freteadora',
        alias='shipping_cost'
    )
    prazo_dias: int = Field(
        title='Prazo de entrega',
        description='Prazo de entrega em dias úteis',
        alias='delivery_deadline'
    )
