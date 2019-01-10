#1
SELECT customer.first_name, customer.last_name, customer.email, address.address, address.city_id, city.city
FROM customer
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
WHERE address.city_id = 312;

#2
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS 'category'
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Comedy';

#3
SELECT actor.actor_id, actor.first_name, actor.last_name, film.title, film.description, film.release_year
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
WHERE actor.actor_id = 5;

#4
SELECT customer.first_name, customer.last_name, customer.email, address.address, address.city_id, customer.store_id
FROM customer
JOIN address ON customer.address_id = address.address_id
WHERE customer.store_id = 1 AND address.city_id = 1
OR customer.store_id = 1 AND address.city_id = 42 
OR customer.store_id = 1 AND address.city_id = 312 
OR customer.store_id = 1 AND address.city_id = 459;

#5
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, actor.first_name, actor.last_name
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.rating = 'G' AND film.special_features LIKE '%behind the scenes%' AND film_actor.actor_id = 15;

#6
SELECT film.film_id, film.title, actor.actor_id, actor.first_name, actor.last_name
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;

#7
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE film.rental_rate = 2.99;

#8
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name, actor.first_name AS 'actor_first', actor.last_name AS 'actor_last'
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE category.name = 'Action' AND actor.first_name = 'Sandra' AND actor.last_name = 'Kilmer';