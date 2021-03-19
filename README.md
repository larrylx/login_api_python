# An Login Api Developed by Python

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
![LICENSE](https://shields.io/badge/license-MIT-green)

This application is a RESTful API for identity authentication. It is developed based on python, MySQL (MariaDB), and Snowflake technologies.

[**Demo**](https://blog.larrylx.com/users/login)

Sign up is coming.

## Approach
- Use bcrypt to hasded password before send to database.
- Validate JWT token in request header in every requet to this application.
- User ID is generate with snowflake.
- Issue two JWT token after login success, token and refresh token.
- JWT carries user id, user name, and expire date.

## Directory

```
├── auth                       //
│   ├── __init__.py            //
│   └── auth.py                //
├── common                     //
│   ├── __init__.py            //
│   ├── db                     //
│   │   ├── __init__.py        //
│   │   ├── user.py            //
│   │   └── init.sql           //
│   ├── settings               //
│   │   ├── __init__.py        //
│   │   └── default.py         //
│   └── utils                  //
│       ├── __init__.py        //
│       ├── decorators.py      //
│       ├── jwt.py             //
│       ├── middlewares.py     //
│       ├── output_json.py     //
│       ├── parser.py          //
│       └── snowflake.py       //
├── __init__.py                //
├── main.py                    //
...
```
