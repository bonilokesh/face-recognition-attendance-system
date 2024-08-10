-- CREATE TABLE users (
--     id INT auto_increment,
--     name varchar(100),
--     email varchar(100),
--     password varchar(255),
--     role varchar(10),
--     unique_id varchar(50),
--     primary key(id),
--     unique(email)
-- );

CREATE TABLE attendance (
    id INT auto_increment,
    course_name varchar(100),
    solt varchar(100),
    attended int,
    added_date varchar(30),
    user_email varchar(100),
    primary key(id)
)


