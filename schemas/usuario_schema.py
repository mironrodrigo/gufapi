from typing import Optional, List

from pydantic import BaseModel as SCBaseModel, EmailStr

from schemas.artigo_schema import ArtigoSchema


class UsuarioSchemaBase(SCBaseModel):
    id: Optional[int] = None
    nome: Optional[str]
    sobrenome: Optional[str]
    email: EmailStr
    eh_admin: bool = False

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str


class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: Optional[List[ArtigoSchema]]


class UsuarioSchemaUp(UsuarioSchemaBase):
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    eh_admin = bool
