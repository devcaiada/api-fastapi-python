# Desafio Desenvolvendo sua Primeira API com FastAPI, Python e Docker

Desenvolvendo a API WorkoutAPI

## O Desafio

- adicionar query parameters nos endpoints
  - atleta
    - nome
    - cpf
- customizar response de retorno de endpoints
  - get all
    - atleta
      - nome
      - centro_treinamento
      - categoria
- Manipular exceção de integridade dos dados em cada módulo/tabela
  - sqlalchemy.exc.IntegrityError e devolver a seguinte mensagem: “Já existe um atleta cadastrado com o cpf: x”
  - status_code: 303
- Adicionar paginação utilizando a lib: fastapi-pagination
  - limit e offset

Não consegui completar todos os desafios ainda. Mas segue algumas coisas que já fiz.

---

### Adicionando query parameters

```python
try:
    atleta_out = AtletaOut(id=uuid4(), created_at=datetime.utcnow(), **atleta_in.model_dump())
    atleta_model = AtletaModel(**atleta_out.model_dump(exclude={'categoria', 'centro_treinamento'}))

    atleta_model.categoria_id = categoria.pk_id
    atleta_model.centro_treinamento_id = centro_treinamento.pk_id

    db_session.add(atleta_model)
    await db_session.commit()
except IntegrityError:
    raise HTTPException(
        status_code=303,
        detail=f'Já existe um atleta cadastrado com o cpf: {atleta_model.cpf}'
    )
except Exception:
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail='Ocorreu um erro ao inserir os dados no banco'
    )
```

---

### Customizando response de retorno

```python
async def query(db_session: DatabaseDependency, nome: Optional[str] = None, cpf: Optional[str] = None) -> list[
    AtletaOut]:
    query = select(AtletaModel)

    if nome or cpf:
        query = query.where(or_(AtletaModel.nome == nome, AtletaModel.cpf == cpf))

    atletas: list[AtletaOut] = (await db_session.execute(query)).scalars().all()

    return [AtletaOut.model_validate(atleta) for atleta in atletas]
```

---
