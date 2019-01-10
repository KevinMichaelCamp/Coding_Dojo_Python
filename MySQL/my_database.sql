
# CREATE
INSERT INTO users ('first_name', 'last_name', 'email', 'password', created_at, updated_at)
VALUES('Kevin', 'Camp', 'kcamp4632@yahoo.com', 'safepass', NOW(), NOW());

# READ
SELECT users.first_name, users.last_name FROM users;

# UPDATE
UPDATE users SET 'password' = 'newpass' WHERE 'id' = '1';

# DELETE
DELETE FROM users WHERE 'id' = '1';
