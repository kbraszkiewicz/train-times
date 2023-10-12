-- Getting station data
SELECT * FROM trains WHERE station = %s;

-- Getting username
SELECT * FROM users WHERE email = %s AND pass = %s;
