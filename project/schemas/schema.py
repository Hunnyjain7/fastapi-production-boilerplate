from pydantic import BaseModel


class MstCorporatesSchema(BaseModel):
    corporate_id: str
    corporate_name: str
    display_name: str
    group_term: str
    headquater_address_id: str
    web_url: str
    created_on: str
    created_by: str
    status_term: str
    total_associated_brands: int
    total_competitors: int
    is_active: str
    update_log: str
    updated_on: str
    updated_by: str
    logo_image: str

    class Config:
        orm_mode = True
