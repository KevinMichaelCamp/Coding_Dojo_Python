# Join Tables
SELECT users.first_name, users.last_name, friend.first_name AS 'friend_first', friend.last_name AS 'friend.last'
FROM users
JOIN friendships ON users.id = friendships.friend_1_id
JOIN users AS friend ON friendships.friend_2_id = friend.id;

#1
SELECT users.first_name, users.last_name, friend.first_name AS 'friend_first', friend.last_name AS 'friend.last'
FROM users
JOIN friendships ON users.id = friendships.friend_1_id
JOIN users AS friend ON friendships.friend_2_id = friend.id
WHERE users.first_name = 'Kermit' OR friend.first_name = 'Kermit';

#2
SELECT COUNT(users.first_name) AS friendship_count
FROM users
JOIN friendships ON users.id = friendships.friend_1_id
JOIN users AS friend ON friendships.friend_2_id = friend.id;

#3
SELECT COUNT(users.first_name) AS friendship_count
FROM users
JOIN friendships ON users.id = friendships.friend_1_id
JOIN users AS friend ON friendships.friend_2_id = friend.id;

#4
INSERT INTO users (first_name, last_name)
VALUES('Kevin', 'Camp');

INSERT INTO friendships (friend_1_id, friend_2_id)
VALUES('6', '2');

INSERT INTO friendships (friend_1_id, friend_2_id)
VALUES('6', '4');

INSERT INTO friendships (friend_1_id, friend_2_id)
VALUES('6', '5');

#5
SELECT users.first_name, users.last_name, friend.first_name AS 'friend_last', friend.last_name AS 'friend.last'
FROM users
JOIN friendships ON users.id = friendships.friend_1_id
JOIN users AS friend ON friendships.friend_2_id = friend.id
WHERE users.first_name = 'Eli' OR friend.first_name = 'Eli';

#6
DELETE FROM friendships
WHERE friend_1_id = 2 AND friend_2_id = 5;

#7
SELECT users.first_name, users.last_name, friend.first_name AS 'friend_first', friend.last_name AS 'friend.last'
FROM users
JOIN friendships ON users.id = friendships.friend_1_id
JOIN users AS friend ON friendships.friend_2_id = friend.id;