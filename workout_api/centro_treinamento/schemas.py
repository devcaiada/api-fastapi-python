from typing import Annotated
from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome da centro de treinamento', example="CT Dakness", max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', example="Rua Osíris, 101", max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do centro de treinamento', example="Caio", max_length=30)]
