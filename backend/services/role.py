from fastapi import HTTPException
from sqlalchemy.orm import Session
import uuid
# model
from models.role import RoleModel
# schema 
from schema import role_schema

class RoleService:
    
    @classmethod
    def get_roles(cls,db:Session):
        """return a list of all roles"""
        return db.query(RoleModel).all()

    @classmethod
    def get_role(cls,roleId:int,db:Session):
        """return a role that matches the roleId provided"""
        # check if role exists and raise an exception if none exists
        role: role_schema.Role = db.query(RoleModel).filter(RoleModel.Id == roleId).first()
        if not role:
            raise HTTPException(detail=f"Could not find role that matches id {roleId}", status_code=404)
        return role

    @classmethod
    def create_new_role(cls,roleData:role_schema.RoleBase, db:Session):
        """create a new role"""
        #check if role exits
        

    @classmethod
    def update_role_details(cls,role_public_id: str, roleData: role_schema.RolePut, db: Session):
        """update role details"""
        role: role_schema.Role = db.query(RoleModel).filter(RoleModel.public_id == role_public_id).first()
        if not role:
            raise HTTPException(detail=f"Could not find role that matches id {role_public_id}", status_code=404)

        role.name = roleData.name
        role.description = roleData.description
        # update the changes
        db.commit()
        db.refresh(role)
        # return the updated role
        return role