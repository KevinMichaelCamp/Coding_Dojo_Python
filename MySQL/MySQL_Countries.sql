# 1
SELECT country.name, countrylanguage.Language, countrylanguage.Percentage
FROM country
JOIN countrylanguage ON country.Code = countrylanguage.CountryCode
WHERE countrylanguage.Language = 'Slovene';

#2
SELECT country.Name, COUNT(city.ID)
FROM country
JOIN city ON country.Code = city.CountryCode
GROUP BY country.Code
ORDER BY COUNT(city.ID) DESC;

#3
SELECT city.Name, country.Name, city.Population
FROM country
JOIN city ON country.Code = city.CountryCode
WHERE city.Population > 500000 AND country.Name = 'Mexico'
ORDER BY city.Population DESC;

#4
SELECT country.Name, countrylanguage.Language, countrylanguage.Percentage
FROM country
JOIN countrylanguage ON country.Code = countrylanguage.CountryCode
WHERE countrylanguage.Percentage > 89
ORDER BY countrylanguage.Percentage DESC;

#5
SELECT country.Name, country.SurfaceArea, country.Population
FROM country
WHERE country.SurfaceArea < 501 AND country.Population > 100000;

#6
SELECT country.Name , country.GovernmentForm, country.Capital, country.LifeExpectancy
FROM country
WHERE country.GovernmentForm = 'Constitutional Monarchy' AND country.Capital > 200 AND country.LifeExpectancy > 75;

#7
SELECT country.Name AS 'country_name', city.Name AS 'city_name', city.District, city.Population
FROM country
JOIN city ON country.Code = city.CountryCode
WHERE country.Name = 'Argentina' AND city.District = 'Buenos Aires' AND city.Population > 500000;

#8
SELECT COUNT(country.Code), country.Region
FROM country
GROUP BY country.Region
ORDER BY COUNT(country.Code) DESC;