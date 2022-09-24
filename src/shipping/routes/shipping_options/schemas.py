from pydantic import BaseModel, Field


class ShippingOptionResponse(BaseModel):
    name: str = Field(
        title='Nome',
        description='Nome do serviço de entrega'
    )
    min_height: int = Field(
        title='Altura Minima',
        description='Altura minima em centimetros necessária para que o pacote possa ser enviado'
    )
    max_height: int = Field(
        title='Altura Máxima',
        description='Altura máxima em centimetros necessária para que o pacote possa ser enviado'
    )
    min_width: int = Field(
        title='Largura Minima',
        description='Largura minima em centimetros necessária para que o pacote possa ser enviado'
    )
    max_width: int = Field(
        title='Largura Máxima',
        description='Largura máxima em centimetros necessária para que o pacote possa ser enviado'
    )
    delivery_deadline: int = Field(
        title='Prazo de entrega',
        description='Quantos dias esta opção de frete leva para entregar o produto'
    )
