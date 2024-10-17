-- task_4.sql
USE alx_book_store;

SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'books'  -- Ensure lowercase 'books' for Unix systems
AND TABLE_SCHEMA = 'alx_book_store';
