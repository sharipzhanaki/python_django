SELECT "shopapp_product"."id",
        "shopapp_product"."name",
        "shopapp_product"."description",
        "shopapp_product"."price",
        "shopapp_product"."discount",
        "shopapp_product"."created_at",
        "shopapp_product"."archived",
        "shopapp_product"."created_by_id",
        "shopapp_product"."preview"
FROM "shopapp_product"
WHERE NOT "shopapp_product"."archived"
ORDER BY "shopapp_product"."price" ASC;



SELECT "shopapp_product"."id",
        "shopapp_product"."name",
        "shopapp_product"."description",
        "shopapp_product"."price",
        "shopapp_product"."discount",
        "shopapp_product"."created_at",
        "shopapp_product"."archived",
        "shopapp_product"."created_by_id",
        "shopapp_product"."preview"
FROM "shopapp_product"
WHERE "shopapp_product"."id" = 2
LIMIT 21;


SELECT "shopapp_productimage"."id",
        "shopapp_productimage"."product_id",
        "shopapp_productimage"."image",
        "shopapp_productimage"."description"
FROM "shopapp_productimage"
WHERE "shopapp_productimage"."product_id" IN (2);


-----
SELECT "django_session"."session_key",
        "django_session"."session_data",
        "django_session"."expire_date"
FROM "django_session"
WHERE ("django_session"."expire_date" > '2025-09-02 17:03:18.141936' AND
       "django_session"."session_key" = 'bhjw2bnhxfl9nxnyh97e19kzvmj4b40z')
LIMIT 21;

SELECT "auth_user"."id",
        "auth_user"."password",
        "auth_user"."last_login",
        "auth_user"."is_superuser",
        "auth_user"."username",
        "auth_user"."first_name",
        "auth_user"."last_name",
        "auth_user"."email",
        "auth_user"."is_staff",
        "auth_user"."is_active",
        "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21;

SELECT "shopapp_order"."id",
        "shopapp_order"."delivery_address",
        "shopapp_order"."promocode",
        "shopapp_order"."created_at",
        "shopapp_order"."user_id",
        "shopapp_order"."receipt",
        "auth_user"."id",
        "auth_user"."password",
        "auth_user"."last_login",
        "auth_user"."is_superuser",
        "auth_user"."username",
        "auth_user"."first_name",
        "auth_user"."last_name",
        "auth_user"."email",
        "auth_user"."is_staff",
        "auth_user"."is_active",
        "auth_user"."date_joined"
FROM "shopapp_order"
INNER JOIN "auth_user" ON ("shopapp_order"."user_id" = "auth_user"."id");

SELECT ("shopapp_order_products"."order_id") AS "_prefetch_related_val_order_id",
        "shopapp_product"."id",
        "shopapp_product"."name",
        "shopapp_product"."description",
        "shopapp_product"."price",
        "shopapp_product"."discount",
        "shopapp_product"."created_at",
        "shopapp_product"."archived",
        "shopapp_product"."created_by_id",
        "shopapp_product"."preview"
FROM "shopapp_product"
        INNER JOIN "shopapp_order_products" ON ("shopapp_product"."id" = "shopapp_order_products"."product_id")
WHERE "shopapp_order_products"."order_id" IN (2, 3)
ORDER BY "shopapp_product"."price" ASC;



----
SELECT "django_session"."session_key",
        "django_session"."session_data",
        "django_session"."expire_date"
FROM "django_session"
WHERE ("django_session"."expire_date" > '2025-09-02 17:16:11.667705' AND
        "django_session"."session_key" = 'bhjw2bnhxfl9nxnyh97e19kzvmj4b40z')
LIMIT 21;

SELECT "auth_user"."id",
        "auth_user"."password",
        "auth_user"."last_login",
        "auth_user"."is_superuser",
        "auth_user"."username",
        "auth_user"."first_name",
        "auth_user"."last_name",
        "auth_user"."email",
        "auth_user"."is_staff",
        "auth_user"."is_active",
        "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21;

SELECT "shopapp_order"."id",
        "shopapp_order"."delivery_address",
        "shopapp_order"."promocode",
        "shopapp_order"."created_at",
        "shopapp_order"."user_id",
        "shopapp_order"."receipt"
FROM "shopapp_order";

SELECT ("shopapp_order_products"."order_id") AS "_prefetch_related_val_order_id",
        "shopapp_product"."id",
        "shopapp_product"."name",
        "shopapp_product"."description",
        "shopapp_product"."price",
        "shopapp_product"."discount",
        "shopapp_product"."created_at",
        "shopapp_product"."archived",
        "shopapp_product"."created_by_id",
        "shopapp_product"."preview"
FROM "shopapp_product"
INNER JOIN "shopapp_order_products" ON ("shopapp_product"."id" = "shopapp_order_products"."product_id")
WHERE "shopapp_order_products"."order_id" IN (2, 3)
ORDER BY "shopapp_product"."price" ASC;

SELECT "auth_user"."id",
        "auth_user"."password",
        "auth_user"."last_login",
        "auth_user"."is_superuser",
        "auth_user"."username",
        "auth_user"."first_name",
        "auth_user"."last_name",
        "auth_user"."email",
        "auth_user"."is_staff",
        "auth_user"."is_active",
        "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21;

SELECT "auth_user"."id",
        "auth_user"."password",
        "auth_user"."last_login",
        "auth_user"."is_superuser",
        "auth_user"."username",
        "auth_user"."first_name",
        "auth_user"."last_name",
        "auth_user"."email",
        "auth_user"."is_staff",
        "auth_user"."is_active",
        "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21;



---
SELECT "django_session"."session_key",
        "django_session"."session_data",
        "django_session"."expire_date"
FROM "django_session"
WHERE ("django_session"."expire_date" > '2025-09-02 19:08:19.391578' AND
        "django_session"."session_key" = 'bhjw2bnhxfl9nxnyh97e19kzvmj4b40z')
LIMIT 21;

SELECT "auth_user"."id",
        "auth_user"."password",
        "auth_user"."last_login",
        "auth_user"."is_superuser",
        "auth_user"."username",
        "auth_user"."first_name",
        "auth_user"."last_name",
        "auth_user"."email",
        "auth_user"."is_staff",
        "auth_user"."is_active",
        "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21;

SELECT "shopapp_order"."id",
        "shopapp_order"."delivery_address",
        "shopapp_order"."promocode",
        "shopapp_order"."created_at",
        "shopapp_order"."user_id",
        "shopapp_order"."receipt"
FROM "shopapp_order";

SELECT "auth_user"."id",
        "auth_user"."password",
        "auth_user"."last_login",
        "auth_user"."is_superuser",
        "auth_user"."username",
        "auth_user"."first_name",
        "auth_user"."last_name",
        "auth_user"."email",
        "auth_user"."is_staff",
        "auth_user"."is_active",
        "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21; args=(1,);

SELECT "shopapp_product"."id",
        "shopapp_product"."name",
        "shopapp_product"."description",
        "shopapp_product"."price",
        "shopapp_product"."discount",
        "shopapp_product"."created_at",
        "shopapp_product"."archived",
        "shopapp_product"."created_by_id",
        "shopapp_product"."preview"
FROM "shopapp_product"
    INNER JOIN "shopapp_order_products" ON ("shopapp_product"."id" = "shopapp_order_products"."product_id")
WHERE "shopapp_order_products"."order_id" = 2
ORDER BY "shopapp_product"."price" ASC;

SELECT "auth_user"."id",
        "auth_user"."password",
        "auth_user"."last_login",
        "auth_user"."is_superuser",
        "auth_user"."username",
        "auth_user"."first_name",
        "auth_user"."last_name",
        "auth_user"."email",
        "auth_user"."is_staff",
        "auth_user"."is_active",
        "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21;

SELECT "shopapp_product"."id",
        "shopapp_product"."name",
        "shopapp_product"."description",
        "shopapp_product"."price",
        "shopapp_product"."discount",
        "shopapp_product"."created_at",
        "shopapp_product"."archived",
        "shopapp_product"."created_by_id",
        "shopapp_product"."preview"
FROM "shopapp_product"
    INNER JOIN "shopapp_order_products" ON ("shopapp_product"."id" = "shopapp_order_products"."product_id")
WHERE "shopapp_order_products"."order_id" = 3
ORDER BY "shopapp_product"."price" ASC;



--
--SELECT "django_session"."session_key", "django_session"."session_data", "django_session"."expire_date" FROM "django_session" WHERE ("django_session"."expire_date" > '2025-09-02 19:21:58.932096' AND "django_session"."session_key" = 'bhjw2bnhxfl9nxnyh97e19kzvmj4b40z') LIMIT 21; args=('2025-09-02 19:21:58.932096', 'bhjw2bnhxfl9nxnyh97e19kzvmj4b40z'); alias=default
--SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" = 1 LIMIT 21; args=(1,); alias=default
SELECT "shopapp_order"."id", "shopapp_order"."delivery_address", "shopapp_order"."promocode", "shopapp_order"."created_at", "shopapp_order"."user_id", "shopapp_order"."receipt" FROM "shopapp_order"; args=(); alias=default
SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" = 1 LIMIT 21; args=(1,); alias=default
SELECT "shopapp_product"."id", "shopapp_product"."name", "shopapp_product"."description", "shopapp_product"."price", "shopapp_product"."discount", "shopapp_product"."created_at", "shopapp_product"."archived", "shopapp_product"."created_by_id", "shopapp_product"."preview" FROM "shopapp_product" INNER JOIN "shopapp_order_products" ON ("shopapp_product"."id" = "shopapp_order_products"."product_id") WHERE "shopapp_order_products"."order_id" = 2 ORDER BY "shopapp_product"."price" ASC; args=(2,); alias=default
SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" = 1 LIMIT 21; args=(1,); alias=default
SELECT "shopapp_product"."id", "shopapp_product"."name", "shopapp_product"."description", "shopapp_product"."price", "shopapp_product"."discount", "shopapp_product"."created_at", "shopapp_product"."archived", "shopapp_product"."created_by_id", "shopapp_product"."preview" FROM "shopapp_product" INNER JOIN "shopapp_order_products" ON ("shopapp_product"."id" = "shopapp_order_products"."product_id") WHERE "shopapp_order_products"."order_id" = 3 ORDER BY "shopapp_product"."price" ASC; args=(3,); alias=default
SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" = 2 LIMIT 21; args=(2,); alias=default
SELECT "shopapp_product"."id", "shopapp_product"."name", "shopapp_product"."description", "shopapp_product"."price", "shopapp_product"."discount", "shopapp_product"."created_at", "shopapp_product"."archived", "shopapp_product"."created_by_id", "shopapp_product"."preview" FROM "shopapp_product" INNER JOIN "shopapp_order_products" ON ("shopapp_product"."id" = "shopapp_order_products"."product_id") WHERE "shopapp_order_products"."order_id" = 5 ORDER BY "shopapp_product"."price" ASC;



--
SELECT "django_session"."session_key",
        "django_session"."session_data",
        "django_session"."expire_date"
FROM "django_session"
WHERE ("django_session"."expire_date" > '2025-09-02 19:23:46.258592' AND
        "django_session"."session_key" = 'bhjw2bnhxfl9nxnyh97e19kzvmj4b40z')
LIMIT 21;

SELECT "auth_user"."id",
        "auth_user"."password",
        "auth_user"."last_login",
        "auth_user"."is_superuser",
        "auth_user"."username",
        "auth_user"."first_name",
        "auth_user"."last_name",
        "auth_user"."email",
        "auth_user"."is_staff",
        "auth_user"."is_active",
        "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21; args=(1,);

SELECT "shopapp_order"."id",
        "shopapp_order"."delivery_address",
        "shopapp_order"."promocode",
        "shopapp_order"."created_at",
        "shopapp_order"."user_id",
        "shopapp_order"."receipt",
        "auth_user"."id",
        "auth_user"."password",
        "auth_user"."last_login",
        "auth_user"."is_superuser",
        "auth_user"."username",
        "auth_user"."first_name",
        "auth_user"."last_name",
        "auth_user"."email",
        "auth_user"."is_staff",
        "auth_user"."is_active",
        "auth_user"."date_joined"
FROM "shopapp_order"
    INNER JOIN "auth_user" ON ("shopapp_order"."user_id" = "auth_user"."id");

SELECT ("shopapp_order_products"."order_id") AS "_prefetch_related_val_order_id",
        "shopapp_product"."id",
        "shopapp_product"."name",
        "shopapp_product"."description",
        "shopapp_product"."price",
        "shopapp_product"."discount",
        "shopapp_product"."created_at",
        "shopapp_product"."archived",
        "shopapp_product"."created_by_id",
        "shopapp_product"."preview"
FROM "shopapp_product"
    INNER JOIN "shopapp_order_products" ON ("shopapp_product"."id" = "shopapp_order_products"."product_id")
WHERE "shopapp_order_products"."order_id" IN (2, 3, 5)
ORDER BY "shopapp_product"."price" ASC;


--
SELECT "shopapp_order"."id",
        "shopapp_order"."delivery_address",
        "shopapp_order"."promocode",
        "shopapp_order"."created_at",
        "shopapp_order"."user_id",
        "shopapp_order"."receipt",
        CAST(SUM("shopapp_product"."price") AS NUMERIC) AS "total",
        COUNT("shopapp_order_products"."product_id") AS "products_count"
FROM "shopapp_order"
    LEFT OUTER JOIN "shopapp_order_products" ON ("shopapp_order"."id" = "shopapp_order_products"."order_id")
    LEFT OUTER JOIN "shopapp_product" ON ("shopapp_order_products"."product_id" = "shopapp_product"."id")
GROUP BY "shopapp_order"."id", "shopapp_order"."delivery_address", "shopapp_order"."promocode",
         "shopapp_order"."created_at", "shopapp_order"."user_id", "shopapp_order"."receipt";


SELECT "shopapp_order"."id",
        "shopapp_order"."delivery_address",
        "shopapp_order"."promocode",
        "shopapp_order"."created_at",
        "shopapp_order"."user_id",
        "shopapp_order"."receipt",
        CAST(COALESCE(CAST(SUM("shopapp_product"."price") AS NUMERIC),
        CAST('0' AS NUMERIC)) AS NUMERIC) AS "total",
        COUNT("shopapp_order_products"."product_id") AS "products_count"
FROM "shopapp_order"
    LEFT OUTER JOIN "shopapp_order_products" ON ("shopapp_order"."id" = "shopapp_order_products"."order_id")
    LEFT OUTER JOIN "shopapp_product" ON ("shopapp_order_products"."product_id" = "shopapp_product"."id")
GROUP BY "shopapp_order"."id", "shopapp_order"."delivery_address", "shopapp_order"."promocode",
         "shopapp_order"."created_at", "shopapp_order"."user_id", "shopapp_order"."receipt";