CREATE TABLE customers(
    id SERIAL PRIMARY KEY,
    first_name varchar(20) NOT NULL,
    last_name varchar(30) NOT NULL,
    email varchar(50) NOT NULL UNIQUE,
    city varchar(30) NOT NULL,
    registration_date DATE NOT NULL
);

CREATE TABLE products(
    id SERIAL PRIMARY KEY,
    product_name varchar(100) NOT NULL,
    product_producer varchar(30) NOT NULL,
    price NUMERIC(10, 2) NOT NULL CHECK (price >= 0)
);

CREATE TABLE employees(
    id SERIAL PRIMARY KEY,
    first_name varchar(20) NOT NULL,
    last_name varchar(30) NOT NULL,
    department varchar(30) NOT NULL CHECK (department in ('IT', 'Sales', 'Marketing', 'Management'))
);

CREATE TABLE orders(
    id SERIAL PRIMARY KEY,
    employee_id INTEGER REFERENCES employees(id),
    customer_id INTEGER REFERENCES customers(id),
    order_date DATE NOT NULL
);

CREATE TABLE order_items(
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER NOT NULL CHECK (quantity > 0)
);
