USE company;

-- Create emloyee table
CREATE TABLE employee(
	emp_id INT PRIMARY KEY,
    first_name VARCHAR(40),
    last_name VARCHAR(40),
    birth_date DATE,
    sex VARCHAR(1),
    salary INT,
    super_id INT,
    branch_id INT
);

-- Create branch table
CREATE TABLE branch(
	branch_id INT PRIMARY KEY,
    branch_name VARCHAR(40),
    mgr_id INT,
    mgr_start_date DATE,
    -- Makeing a foreign key
    FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL
);

-- Create foreign keys for the employee table
ALTER TABLE employee ADD FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL;
ALTER TABLE employee ADD FOREIGN KEY(super_id) REFERENCES employee(emp_id) ON DELETE SET NULL;

-- Create clients table
CREATE TABLE clients(
	client_id INT PRIMARY KEY,
	client_name VARCHAR(40),
    branch_id INT,
    FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL
);

-- Create works_with table
CREATE TABLE works_with(
	emp_id INT,
    client_id INT,
    total_sales INT,
    PRIMARY KEY(emp_id, client_id),
    FOREIGN KEY(emp_id) REFERENCES employee(emp_id) ON DELETE CASCADE,
    FOREIGN KEY(client_id) REFERENCES clients(client_id) ON DELETE CASCADE 
);

-- Create branch supplier table
CREATE TABLE branch_supplier(
	branch_id INT,	
    supplier_name VARCHAR(40),
    supply_type VARCHAR(40),
    PRIMARY KEY(branch_id, supplier_name),
    FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE
);

-- 											Insert data to our tables                                          --

-- First I will insert employees by their branch

-- Corporate
-- Employee table insert
INSERT INTO employee VALUES(100, 'David', 'Wallace', '1967-11-17', 'M', 250000, NULL, NULL);
-- Branch table insert
INSERT INTO branch VALUES(1, 'Corporate', 100, '2006-02-09');
-- Continue adding records
INSERT INTO employee VALUES(101, 'Jan', 'Levinson', '1961-05-11', 'F', 110000, 100, NULL);
-- Modifying employee table, beacause we need branch_id as foreign key, but branch_id at the branch table haven't been created
UPDATE employee SET branch_id = 1 WHERE emp_id IN (100, 101);

-- Scranton
-- Employee table insert
INSERT INTO employee VALUES(102, 'Michael', 'Scott', '1964-03-15', 'M', 75000, 100, NULL);
-- Branch table insert
INSERT INTO branch VALUES(2, 'Scranton', 102, '1992-04-06');
-- Continue adding records
INSERT INTO employee VALUES(103, 'Angela', 'Martin', '1971-06-25', 'F', 63000, 102, NULL);
INSERT INTO employee VALUES(104, 'Stanley', 'Hudson', '1958-02-19', 'M', 69000, 102, NULL);
INSERT INTO employee VALUES(105, 'Kelly', 'Kapoor', '1980-02-05', 'F', 55000, 102, NULL);
-- Modifyng employee table
UPDATE employee SET branch_id = 2 WHERE emp_id IN (102, 103, 104, 105); 

-- Stamford
-- Employee table insert
INSERT INTO employee VALUES(106, 'Josh', 'Porter', '1969-09-05', 'M', 78000, 100, NULL);
-- Branch table insert
INSERT INTO branch VALUES(3, 'Stamford', 106, '1998-02-13'); 
-- Continue adding records
INSERT INTO employee VALUES(107, 'Andy', 'Bernard', '1973-07-22', 'M', 65000, 106, NULL);
INSERT INTO employee VALUES(108, 'Jim', 'Halpert', '1978-10-01', 'M', 71000, 106, NULL);
-- Modifying employee table
UPDATE employee SET branch_id = 3 WHERE emp_id IN (106, 107, 108);


-- Then inserting to the brach_supplier table
INSERT INTO branch_supplier VALUES(2, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VALUES(2, 'Uni-ball', 'Writing Utensils');
INSERT INTO branch_supplier VALUES(3, 'Patriots Paper', 'Paper');
INSERT INTO branch_supplier VALUES(2, 'J.T. Forms & Labels', 'Custom Forms');
INSERT INTO branch_supplier VALUES(3, 'Uni-ball', 'Writing Utensils');
INSERT INTO branch_supplier VALUES(3, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VAlUES(3, 'Stamford Labels', 'Custom Forms');


-- Inserting to the clients table
INSERT INTO clients VALUES(400, 'Dunmore Highschool', 2);
INSERT INTO clients VALUES(401, 'Lackawana Country', 2);
INSERT INTO clients VALUES(402, 'FedEx', 3);
INSERT INTO clients VALUES(403, 'John Daly Law, LLC', 3);
INSERT INTO clients VALUES(404, 'Scranton Whitepages', 2);
INSERT INTO clients VALUES(405, 'Times Newspaper', 3);
INSERT INTO clients VALUES(406, 'FedEx', 2);


-- Inserting records to the works_with table
INSERT INTO works_with VALUES(105, 400, 55000);
INSERT INTO works_with VALUES(102, 401, 267000);
INSERT INTO works_with VALUES(108, 402, 22500);
INSERT INTO works_with VALUES(107, 403, 5000);
INSERT INTO works_with VALUES(108, 403, 12000);
INSERT INTO works_with VALUES(105, 404, 33000);
INSERT INTO works_with VALUES(107, 405, 26000);
INSERT INTO works_with VALUES(102, 406, 15000);
INSERT INTO works_with VALUES(105, 406, 130000);






