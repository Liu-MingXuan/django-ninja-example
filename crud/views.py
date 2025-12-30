from ninja import Router
from ninja.pagination import paginate
from django.shortcuts import get_object_or_404
from .models import Blog, Person
from django.http import Http404
from .schemas import (
    PersonCreate,
    PersonUpdate,
    Person as PersonSchema,
    BlogCreate,
    BlogUpdate,
    Blog as BlogSchema,
)
import uuid

router = Router()


@router.get("/blogs", response=list[BlogSchema])
@paginate
def list_blogs(request):
    blogs = Blog.objects.all()
    return blogs


@router.get("/blogs/{blog_id}", response=BlogSchema)
def get_blog(request, blog_id: str):
    try:
        uuid_obj = uuid.UUID(blog_id)
        blog = get_object_or_404(Blog, id=uuid_obj)
        return blog
    except ValueError:
        raise Http404("Invalid UUID format")


@router.post("/blogs", response=BlogSchema)
def create_blog(request, payload: BlogCreate):
    # 验证person_name是否存在于Person表中
    try:
        person = Person.objects.get(name=payload.person_name)
    except Person.DoesNotExist:
        raise Http404(f"Person with name '{payload.person_name}' does not exist")

    blog = Blog.objects.create(
        title=payload.title,
        description=payload.description,
        completed=payload.completed,
        person_name=payload.person_name
    )
    return blog


@router.put("/blogs/{blog_id}", response=BlogSchema)
def update_blog(request, blog_id: str, payload: BlogUpdate):
    try:
        uuid_obj = uuid.UUID(blog_id)
        blog = get_object_or_404(Blog, id=uuid_obj)
    except ValueError:
        raise Http404("Invalid UUID format")

    if payload.title is not None:
        blog.title = payload.title
    if payload.description is not None:
        blog.description = payload.description
    if payload.completed is not None:
        blog.completed = payload.completed
    if payload.person_name is not None:
        try:
            person = Person.objects.get(name=payload.person_name)
        except Person.DoesNotExist:
            raise Http404(f"Person with name '{payload.person_name}' does not exist")

        blog.person_name = payload.person_name

    blog.save()
    return blog


@router.delete("/blogs/{blog_id}")
def delete_blog(request, blog_id: str):
    try:
        uuid_obj = uuid.UUID(blog_id)
        blog = get_object_or_404(Blog, id=uuid_obj)
        blog.delete()
        return {"success": True}
    except ValueError:
        raise Http404("Invalid UUID format")


# Person相关的API端点
@router.get("/persons", response=list[PersonSchema])
def list_persons(request):
    persons = Person.objects.all()
    return persons


@router.get("/persons/{person_name}", response=PersonSchema)
def get_person_by_name(request, person_name: str):
    person = get_object_or_404(Person, name=person_name)
    return person


@router.get("/persons/{person_name}/blogs", response=list[BlogSchema])
def get_person_blogs(request, person_name: str):
    blogs = Blog.objects.filter(person_name=person_name)
    return blogs


@router.post("/persons", response=PersonSchema)
def create_person(request, payload: PersonCreate):
    if Person.objects.filter(name=payload.name).exists():
        raise Http404(f"Person with name '{payload.name}' already exists")
    person = Person.objects.create(
        name=payload.name,
        email=payload.email,
        phone=payload.phone
    )
    return person


@router.put("/persons/{person_name}", response=PersonSchema)
def update_person(request, person_name: str, payload: PersonUpdate):
    person = get_object_or_404(Person, name=person_name)

    # 只更新提供的字段
    if payload.name is not None:
        # 检查新名称是否与其他现有人员冲突
        if payload.name != person_name and Person.objects.filter(name=payload.name).exclude(id=person.id).exists():
            raise Http404(f"Person with name '{payload.name}' already exists")
        person.name = payload.name
    
    if payload.email is not None:
        person.email = payload.email
    
    if payload.phone is not None:
        person.phone = payload.phone
    
    person.save()
    return person


@router.delete("/persons/{person_name}")
def delete_person(request, person_name: str):
    person = get_object_or_404(Person, name=person_name)

    # 检查是否有博客关联到此人员
    blogs = Blog.objects.filter(person_name=person_name)
    if blogs.exists():
        # 删除与该人员关联的所有博客
        blogs.delete()

    person.delete()
    return {"success": True}
