-- Enable uuid extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS clients (
    id VARCHAR PRIMARY KEY DEFAULT uuid_generate_v4(),
    full_name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(55) UNIQUE NOT NULL,
    email VARCHAR(512) UNIQUE DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS pets (
    id VARCHAR PRIMARY KEY DEFAULT uuid_generate_v4(),
    nickname VARCHAR(125),
    species VARCHAR(125) NOT NULL,
    breed VARCHAR(125),
    owner_id VARCHAR REFERENCES clients(id) DEFAULT NULL ON DELETE SET NULL ON UPDATE SET NULL
);

CREATE TABLE IF NOT EXISTS employees (
    id VARCHAR PRIMARY KEY DEFAULT uuid_generate_v4(),
    full_name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(55) UNIQUE NOT NULL,
    email VARCHAR(512) UNIQUE NOT NULL 
);

CREATE TABLE IF NOT EXISTS appointments (
    id VARCHAR PRIMARY KEY DEFAULT uuid_generate_v4(),
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    cabinet VARCHAR(55) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),

    client_id VARCHAR REFERENCES clients(id) DEFAULT NULL ON DELETE SET NULL ON UPDATE SET NULL,
    employee_id VARCHAR REFERENCES employees(id) ON DELETE SET NULL ON UPDATE SET NULL,
    pet_id VARCHAR REFERENCES pets(id) DEFAULT NULL ON DELETE SET NULL ON UPDATE SET NULL
);

CREATE TABLE IF NOT EXISTS client_payments (
    id VARCHAR PRIMARY KEY DEFAULT uuid_generate_v4(),

    client_id VARCHAR REFERENCES clients(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
    appointment_id VARCHAR REFERENCES appointments(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
    total DECIMAL(7,2) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);