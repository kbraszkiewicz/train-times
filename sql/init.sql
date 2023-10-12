create table trains (
    id int unsigned auto_increment primary key,
    departure_station text(3),
    final_station text(3),
    stops text(4096),
    due datetime,
    status datetime,
    platform int
);

create table users (
    id int unsigned auto_increment primary key,
    email text(4096),
    pass text(4096)
);