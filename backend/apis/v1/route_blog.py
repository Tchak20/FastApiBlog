from typing import List
from fastapi import APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from db.repository.blog import delete_blog
from db.repository.blog import update_blog
from schemas.blog import UpdateBlog
from db.repository.blog import retreive_blog
from db.models.user import User 
from apis.v1.route_login import get_current_user

from db.session import get_db
from schemas.blog import ShowBlog, CreateBlog
from db.repository.blog import create_new_blog, list_blogs

router = APIRouter()

@router.post("/blogs",response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
def create_blog(blog: CreateBlog, db: Session= Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db,author_id=1)
    return blog

@router.get("/blogs/{id}", response_model=ShowBlog)
def get_blog(id: int, db: Session=Depends(get_db)):
    blog = retreive_blog(id=id, db=db)
    if not blog:
        raise HTTPException(detail=f"Blog with ID {id} does not exist.", status_code=status.HTTP_404_NOT_FOUND)
    return blog

@router.get("/blogs", response_model=List[ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return blogs

@router.put("/blog/{id}", response_model=ShowBlog)
def update_a_blog(id:int , blog:UpdateBlog,author_id=1, db:Session = Depends(get_db)):
    blog = update_blog(id=id, blog=blog,author_id=author_id, db=db)
    if not blog:
        raise HTTPException(detail=f"Blog with id {id} doesn't exist")
    return blog
@router.delete("/blogd/{id}")
def delete_a_blog(id: int ,author_id=1,  db: Session = Depends(get_db)):
    blog = delete_blog(id=id,author_id=author_id, db=db)
    if blog.get("error"):
        raise HTTPException(detail=blog.get("error"), status_code=status.HTTP_400_BAD_REQUEST)
    return {"msg":f"Successfully deleted blog with id {id}"}