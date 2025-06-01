# build & run
'''
docker compose up
'''

# confirm api-server is up
Execute the REST API
'''
curl http://0.0.0.0:8000/version
'''

# enter data into db by phpmyadmin
Access the following URL in the browser
'''
http://localhost:8081
'''

Language : Japanese
Username : root
Password : example

1. Select the database testdb
2. Create the table prefectures
In the console at the bottom of the screen, enter the following
'''
CREATE TABLE prefectures (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);
'''

3. insert values into the table
In the console at the bottom of the screen, enter the following
'''
INSERT INTO prefectures (name) VALUES
('Hokkaido'), ('Aomori'), ('Iwate'), ('Miyagi'), ('Akita'), ('Yamagata'), ('Fukushima'),
('Ibaraki'), ('Tochigi'), ('Gunma'), ('Saitama'), ('Chiba'), ('Tokyo'), ('Kanagawa'),
('Niigata'), ('Toyama'), ('Ishikawa'), ('Fukui'), ('Yamanashi'), ('Nagano'), ('Gifu'),
('Shizuoka'), ('Aichi'), ('Mie'), ('Shiga'), ('Kyoto'), ('Osaka'), ('Hyogo'),
('Nara'), ('Wakayama'), ('Tottori'), ('Shimane'), ('Okayama'), ('Hiroshima'), ('Yamaguchi'),
('Tokushima'), ('Kagawa'), ('Ehime'), ('Kochi'), ('Fukuoka'), ('Saga'), ('Nagasaki'),
('Kumamoto'), ('Oita'), ('Miyazaki'), ('Kagoshima'), ('Okinawa');
'''

# Execute the REST API
'''
curl http://localhost:8000/api/prefectures
'''

# Execute the Web GUI
ブラウザで以下にアクセスする
'''
http://localhost:8080
'''