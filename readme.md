http://127.0.0.1:8000/admin/ - зайти на страницу админа

 запрос Post http://127.0.0.1:8000/api/register/ - зарегистрировать пользователя.
 данные которые должны быть отправлены:
 {
    "username":"arlen",
    "email": "almamat200@gmail.com",
    "password":"berserk1998",
    "password2":"berserk1998",
    "profile":{
        "first_name":"meerim",
        "last_name":"asdfasf",
        "phone_number":"+996709363345",
        "age":"32"
    }

}

запрос GET http://127.0.0.1:8000/api/email-verify/<str:pk>/ - верификация пользователя

запрос POST http://127.0.0.1:8000/api/signin/ - войти 
 данные которые должны быть отправлены:
 {
    "email": "almamat200@gmail.com",
    "password":"berserk1998",
}

запрос POST http://127.0.0.1:8000/api/forgot-pass/ - смена пароля
{
    "email": "almamat200@gmail.com",
}

запрос POST http://127.0.0.1:8000/api/change-pass/<str:pk>/- новый пароль
{
    "password": "",
    "confirm_password": "",
}

POST http://127.0.0.1:8000/api/token/refresh/- получить новый access token
данные которые должны быть отправлены:
{"access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNTY3LCJqdGkiOiJjNzE4ZTVkNjgzZWQ0NTQyYTU0NWJkM2VmMGI0ZGQ0ZSJ9.ekxRxgb9OKmHkfy-zs1Ro_xs1eMLXiR17dIDBVxeT-w"}



запрос GET http://127.0.0.1:8000/api/v1/latest_products/ - получить меню

запрос GET http://127.0.0.1:8000/api/v1/products/<slug:category_slug>/ - получить меню определенной категории

запрос GET http://127.0.0.1:8000/api/v1/products/<slug:category_slug>/<slug:product_slug>/ - detail page





запрос POST http://127.0.0.1:8000/api/order/checkout/ - сделать заказ  
 данные которые должны быть отправлены:
{
    "address":"dafdaf",
    "place":"fadfafaf",
    "items":[
    {
        "price":250,
        "product":1,
        "quantity":8

    }
    ]
}