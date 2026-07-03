# InventoryProg

A **Django e-commerce inventory system** — products, brands, categories, stores, and a custom user model for multi-store stock management.

![Django](https://img.shields.io/badge/Django-4.0-092E20?style=flat-square&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)

## Features

- Rich **Product** model (pricing, stock, media, brand, category, store)
- Custom **`AbstractBaseUser`** authentication (`users` app)
- **CKEditor** for rich product descriptions
- **Phone number** field validation
- SQLite + media uploads for local dev
- `InventoryV2.0/` iteration folder for evolved schema experiments

## Tech stack

| Layer | Choice |
|-------|--------|
| Framework | Django 4.0 |
| Editor | django-ckeditor |
| Auth | Custom user model |
| DB | SQLite |

## Quick start

```bash
cd Inventory
pip install django django-ckeditor phonenumber-field pillow
python manage.py migrate
python manage.py runserver
```

Admin: **http://127.0.0.1:8000/admin** (create a superuser first).

## Project layout

```
Inventory/
  manage.py
  mainsite/       # Product, Brand, Category, Store models
  users/          # Custom user model
  db.sqlite3
InventoryV2.0/    # Alternate / evolved version
```

---

[malimba](https://github.com/malimba)
