# Sales Analytics System (SAS)

A command-line sales analytics application built with **Python** and **PostgreSQL**.
The system allows users to manage sales data, search records, generate statistics and visualize selected results.

The project was created as a practical exercise in working with relational databases, SQL, Python and data analysis.

## Features

* View data stored in the database
* Add new:

  * customers
  * employees
  * products
  * orders
  * order items
* Remove records from the database
* Search records using multiple optional filters
* Generate sales statistics
* Analyze:

  * customer orders and total spending
  * product sales and earnings
  * employee earnings
  * average earnings by department
* Display statistical results using Pandas
* Generate charts using Matplotlib
* PostgreSQL database running in Docker
* Environment variables managed with `.env`

## Technologies

* **Python**
* **PostgreSQL**
* **SQL**
* **Pandas**
* **Matplotlib**
* **psycopg2**
* **python-dotenv**
* **Docker / Docker Compose**
* **Git / GitHub**


## Database

The application uses PostgreSQL with the following main tables:

```text
customers
products
employees
orders
order_items
```

The database represents a simple sales environment where customers place orders, employees are responsible for orders, and products are included in orders through the `order_items` table.

The relationships between these tables allow the application to perform more advanced SQL queries using:

* `JOIN`
* `GROUP BY`
* aggregate functions such as `SUM()`, `AVG()` and `COUNT()`
* window functions
* filtering with optional parameters

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/makocchigod/Sales-Analytics-System
cd Sales-Analytics-System
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file based on `.env.example`:

```env
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=sales_database
POSTGRES_PORT=5432 (or for example 5433 if you have postgres installed)
```


### 5. Start PostgreSQL with Docker

Make sure Docker is running and execute:

```bash
docker compose up -d
```

Docker Compose will start the PostgreSQL container and initialize the database using the SQL scripts included in the project.

### 6. Run the application

```bash
python main.py
```

## Usage

After starting the application, the main menu is displayed:

```text
=======================================
Welcome to the Sales Analytics System
What do you want to do?

1. See database
2. Add to database
3. Remove from database
4. Find record
5. See statistics
6. Exit
```

The user can select an operation by entering its number.

### Searching records

The search functionality allows users to filter records using different parameters.

For example, customers can be searched using:

* ID
* first name
* last name
* email
* city
* registration date range

Optional filters can be combined to narrow down the results.

### Statistics

The statistics module provides analytical information about the sales database.

Examples include:

* total amount spent by each customer
* number of orders placed by customers
* products sold and their total earnings
* employee earnings
* average earnings within an employee's department

Results are displayed using Pandas DataFrames and can also be visualized with Matplotlib.

## Example SQL Analysis

One of the queries used by the application calculates employee earnings and compares them with the average earnings of their department:

```sql
SELECT
    e.first_name || ' ' || e.last_name AS employee,
    SUM(oi.quantity * products.price) AS earnings,
    e.department,
    ROUND(
        AVG(SUM(oi.quantity * products.price))
        OVER (PARTITION BY e.department),
        2
    ) AS avg_earnings_for_department
FROM employees AS e
JOIN orders AS o
    ON e.id = o.employee_id
JOIN order_items AS oi
    ON o.id = oi.order_id
JOIN products
    ON oi.product_id = products.id
GROUP BY
    e.id,
    e.first_name,
    e.last_name,
    e.department;
```

This query combines multiple tables, aggregation and a window function to produce a more useful business analysis.

## What I Learned

This project was built to practice and improve skills in:

* designing and working with relational databases
* writing SQL queries
* using `JOIN` operations
* aggregation with `SUM()` and `COUNT()`
* SQL window functions
* connecting Python applications to PostgreSQL
* parameterized SQL queries
* handling environment variables
* using Docker for database development
* working with Pandas DataFrames
* creating visualizations with Matplotlib
* organizing a Python project
* using Git and GitHub

## Future Improvements

Possible improvements include:

* adding automated tests with `pytest`
* improving input validation and error handling
* improving the command-line interface
* adding more analytical queries and visualizations
* improving the project architecture by separating database, CRUD, search and analytics logic
* adding more robust reporting functionality

## Author

**Marcin 'makocchi' Korzeniewski**

