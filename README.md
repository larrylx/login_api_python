# An Login Api Developed by Python

![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)

This application is a RESTful API for identity authentication. It is developed based on python, MySQL (MariaDB), and Snowflake technologies.

## Directory

```shell
├── auth                				  // 
│   ├── __init__.py               // 
│   └── auth.py  				          // 
├── common                				// 
│   ├── db                				// 
│   │   ├── __init__.py   				// 
│   │   ├── user.py       				// 
│   │   └── init.sql      				// 
│   ├── settings          				// 
│   │   ├── __init__.py   				// 
│   │   └── default.py    				// 
│   └── utils             				// 
│       ├── __init__.py   				// 
│       ├── decorators.py 				// 
│       ├── jwt.py        				// 
│       ├── middlewares.py				// 
│       ├── output_json.py				// 
│       ├── parser.py     				// 
│       └── snowflake.py  				// 
├── __init__.py                   // 
├── main.py                   		// 
...
```

