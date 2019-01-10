#1
SELECT SUM(amount), charged_datetime
FROM billing
WHERE charged_datetime >= '2012/03/01' AND charged_datetime <= '2012/03/31';

#2
SELECT clients.id, SUM(billing.amount)
FROM clients
JOIN billing ON clients.id = billing.clients_id
WHERE clients.id = 2;

#3
SELECT clients.id, sites.domain_name
FROM clients
JOIN sites ON clients.id = sites.clients_id
WHERE clients.id = 10;

#4
SELECT clients.id, COUNT(sites.id), sites.created_datetime
FROM clients
JOIN sites ON clients.id = sites.clients_id
GROUP BY sites.created_datetime
WHERE clients.id = 1;

SELECT clients.id, COUNT(sites.id), sites.created_datetime
FROM clients
JOIN sites ON clients.id = sites.clients_id
GROUP BY sites.created_datetime
WHERE clients.id = 20;

#5
SELECT sites.domain_name, COUNT(leads.id)
FROM sites
JOIN leads ON sites.id = leads.sites_id
GROUP BY sites.id;

#6
SELECT clients.first_name, clients.last_name, COUNT(leads.id)
FROM clients
JOIN sites ON clients.id = sites.clients_id
JOIN leads ON sites.id = leads.sites_id
WHERE leads.registered_datetime >= '2011/01/01' AND leads.registered_datetime <= '2011/02/15'
GROUP BY clients.id;

#7
SELECT clients.first_name, clients.last_name, COUNT(leads.id)
FROM clients
JOIN sites ON clients.id = sites.clients_id
JOIN leads ON sites.id = leads.sites_id
WHERE leads.registered_datetime >= '2011/01/01' AND leads.registered_datetime <= '2011/12/31'
GROUP BY clients.id;

#8
SELECT clients.first_name, clients.last_name, sites.domain_name, COUNT(leads.id) AS 'num_leads'
FROM clients
JOIN sites ON clients.id = sites.clients_id
JOIN leads ON sites.id = leads.sites_id
WHERE leads.registered_datetime >= '2011/01/01' AND leads.registered_datetime <= '2011/12/31'
GROUP BY clients.id;

#9
SELECT clients.id, billing.amount, billing.charged_datetime
FROM clients
JOIN billing ON clients.id = billing.clients_id
GROUP BY billing.charged_datetime
ORDER BY clients.id

#10
SELECT clients.first_name, clients.last_name, GROUP_CONCAT(' ', sites.domain_name) AS sites
FROM clients
JOIN sites ON clients.id = sites.clients_id
GROUP BY clients.id;