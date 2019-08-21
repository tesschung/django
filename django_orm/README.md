[TOC]

### 데이터베이스(DB: Database)

- 체계화된 데이터의 모임

- 여러 사람이 **공유**하고 **사용**할 목적으로 통합 관리되는 정보의 집합

- 몇 개의 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜 놓은 자료의 집합체



### RDBMS(관계형데이터베이스 관리 시스템)







### 기본용어

**스키마(scheme)**

| column | datatype |
| ------ | -------- |
| id     | INT      |
| age    | INT      |
| phone  | TEXT     |
| email  | TEXT     |

**테이블(table)**

열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합. SQL 데이터베이스에서는 테이블을 관계 라고도 한다.



**행(row),레코드**

테이블의 데이터는 행에 저장된다.
즉, user 테이블에 4명의 고객정보가 저장되어 있으며, 행은 4개가 존재한다.



**PK(기본키)** 

각 행(레코드)의 고유값으로 Primary Key로 불린다.
반드시 설정하여야하며, 데이터베이스 관리 및 관계 설정시 주요하게 활용된다.



### ORM(Object-Relational Mapping)으로 구현하는 CRUD





models.py



models.py 작성후 선언

```bash
$ python manage.py makemigrations
Migrations for 'articles':
  articles\migrations\0001_initial.py
    - Create model Article
(venv)


# 데이터베이스에 반영 시작
student@M702 MINGW64 ~/development/django/django/django_orm (master)
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, articles, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying articles.0001_initial... OK # 우리가 만든 것
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
(venv)
```



데이터 베이스 확인 extension 설치 

