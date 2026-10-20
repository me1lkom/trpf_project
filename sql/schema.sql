CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    inn TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    country TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS offers (
    offer_id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    supplier_id INTEGER NOT NULL,
    price REAL NOT NULL,
    min_lots REAL NOT NULL,
    delivery_time_days INTEGER NOT NULL,

    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

CREATE TABLE IF NOT EXISTS supplier_members (
    user_id INTEGER NOT NULL,
    supplier_id INTEGER NOT NULL,
    
    PRIMARY KEY(user_id, supplier_id),

    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

CREATE TABLE IF NOT EXISTS product_buyers (
    product_id INTEGER PRIMARY KEY,
    user_id INTEGER DEFAULT NULL,
    supplier_id INTEGER DEFAULT NULL,

    CHECK(
        (user_id IS NOT NULL AND supplier_id IS NULL)
        OR
        (user_id IS NULL AND supplier_id IS NOT NULL)
    ),

    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

