# Django-Ninja 开发示例

这是一个使用 Django-Ninja 框架开发的 RESTful API 示例项目，展示了如何构建一个完整的 CRUD 应用。

## 项目简介

本项目实现了人员和博客管理的 RESTful API，包含以下功能：
- 人员（Person）的增删改查
- 博客（Blog）的增删改查
- 人员与博客的关联查询
- 分页支持

## 技术栈

- Django 6.0
- Django-Ninja
- SQLite
- Pydantic

## 项目结构

```
djangoweb/
├── crud/                    # CRUD 应用
│   ├── models.py           # 数据模型
│   ├── schemas.py          # Pydantic schemas
│   ├── views.py            # API 视图
│   ├── urls.py             # URL 配置
│   └── migrations/         # 数据库迁移
├── djangoweb/              # 项目配置
│   ├── settings.py         # Django 设置
│   └── urls.py             # 主 URL 配置
└── manage.py               # Django 管理脚本
```

## 数据模型

### Person（人员）
- id: UUID (主键)
- name: 姓名 (唯一)
- email: 邮箱
- phone: 电话
- created_at: 创建时间

### Blog（博客）
- id: UUID (主键)
- title: 标题
- description: 描述
- completed: 是否完成
- person_name: 关联的人员姓名
- created_at: 创建时间

## API 端点

### 人员相关
- `GET /api/crud/persons` - 获取所有人员
- `GET /api/crud/persons/{person_name}` - 获取指定人员
- `POST /api/crud/persons` - 创建新人员
- `PUT /api/crud/persons/{person_name}` - 更新人员信息
- `DELETE /api/crud/persons/{person_name}` - 删除人员
- `GET /api/crud/persons/{person_name}/blogs` - 获取人员的博客列表

### 博客相关
- `GET /api/crud/blogs` - 获取所有博客（支持分页）
- `GET /api/crud/blogs/{blog_id}` - 获取指定博客
- `POST /api/crud/blogs` - 创建新博客
- `PUT /api/crud/blogs/{blog_id}` - 更新博客
- `DELETE /api/crud/blogs/{blog_id}` - 删除博客

## 安装和运行

1. 安装依赖：
```bash
pip install django django-ninja
```

2. 运行数据库迁移：
```bash
python manage.py migrate
```

3. 启动开发服务器：
```bash
python manage.py runserver
```

4. 访问 API 文档：
打开浏览器访问 `http://localhost:8000/api/docs`

## 使用示例

### 创建人员
```bash
curl -X POST http://localhost:8000/api/crud/persons \
  -H "Content-Type: application/json" \
  -d '{"name": "张三", "email": "zhangsan@example.com", "phone": "13800138000"}'
```

### 创建博客
```bash
curl -X POST http://localhost:8000/api/crud/blogs \
  -H "Content-Type: application/json" \
  -d '{"title": "我的第一篇博客", "description": "这是博客内容", "person_name": "张三"}'
```

### 获取所有博客（带分页）
```bash
curl "http://localhost:8000/api/crud/blogs?limit=10&offset=0"
```

## 特性说明

1. **Schema 分离**：创建了单独的 Create、Update 和 Output schemas，遵循最佳实践
2. **部分更新**：支持只更新提供的字段
3. **数据验证**：使用 Pydantic 进行数据验证
4. **UUID 主键**：使用 UUID 作为主键，提高安全性
5. **自动文档**：Django-Ninja 自动生成交互式 API 文档
6. **分页支持**：博客列表支持分页查询

## 作者

Liu MingXuan

## 许可证

MIT
