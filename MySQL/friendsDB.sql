SELECT COUNT(users.id), users.first_name, users.last_name, GROUP_CONCAT(' ', friend.first_name) AS 'friend_first', GROUP_CONCAT(' ', friend.last_name) AS 'friend.last'
FROM users
JOIN friendships ON users.id = friendships.friend_1_id
JOIN users AS friend ON friendships.friend_2_id = friend.id
GROUP BY users.id


