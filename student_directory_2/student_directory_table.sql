CREATE TABLE cohorts (
    id SERIAL PRIMARY KEY,
    cohort_name text,
    start_date date
);

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    student_name text,
    cohort_id int,
    constraint fk_cohort foreign key(cohort_id)
        references cohorts(id)
        on delete cascade
);