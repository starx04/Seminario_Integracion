from fastapi import APIRouter, HTTPException, Response, status
from pydantic import BaseModel, Field

router = APIRouter(prefix="/equipos", tags=["Equipos móviles"])


class EquipoMovilEntrada(BaseModel):
    marca: str = Field(min_length=1, examples=["Samsung"])
    modelo: str = Field(min_length=1, examples=["Galaxy A55"])
    precio: float = Field(gt=0, examples=[399.99])
    stock: int = Field(ge=0, examples=[8])


class EquipoMovil(EquipoMovilEntrada):
    id: int


catalogo: dict[int, EquipoMovil] = {
    1: EquipoMovil(
        id=1,
        marca="Samsung",
        modelo="Galaxy A55",
        precio=399.99,
        stock=8,
    ),
    2: EquipoMovil(
        id=2,
        marca="Motorola",
        modelo="Moto G84",
        precio=249.99,
        stock=5,
    ),
    3: EquipoMovil(
        id=3,
        marca="Xiaomi",
        modelo="Redmi Note 13",
        precio=199.99,
        stock=10,
    ),
}


def buscar_equipo(equipo_id: int) -> EquipoMovil:
    equipo = catalogo.get(equipo_id)
    if equipo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontró el equipo móvil",
        )
    return equipo


@router.get("", response_model=list[EquipoMovil])
def listar_equipos() -> list[EquipoMovil]:
    return list(catalogo.values())


@router.get("/{equipo_id}", response_model=EquipoMovil)
def obtener_equipo(equipo_id: int) -> EquipoMovil:
    return buscar_equipo(equipo_id)


@router.post("", response_model=EquipoMovil, status_code=status.HTTP_201_CREATED)
def crear_equipo(datos: EquipoMovilEntrada) -> EquipoMovil:
    equipo_id = max(catalogo, default=0) + 1
    equipo = EquipoMovil(id=equipo_id, **datos.model_dump())
    catalogo[equipo_id] = equipo
    return equipo


@router.put("/{equipo_id}", response_model=EquipoMovil)
def actualizar_equipo(equipo_id: int, datos: EquipoMovilEntrada) -> EquipoMovil:
    buscar_equipo(equipo_id)
    equipo = EquipoMovil(id=equipo_id, **datos.model_dump())
    catalogo[equipo_id] = equipo
    return equipo


@router.delete("/{equipo_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_equipo(equipo_id: int) -> Response:
    buscar_equipo(equipo_id)
    del catalogo[equipo_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
