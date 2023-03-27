# truckdriverapi
rest API server to expose a List of Drivers to a client application

## Required Dependencies
- [x]  Python 3.8+ 
- [x]  Pipenv
- [x]  Django rest framework
- [x]  Postgres 13+

## Library
- Django-Filter: Simple library to help ease filtering
- Psycopg2 : PostgreSQL db adapter for Python

## Potential Improvement
- Adding custom front end templates
- Implement authentication
- Pagination: future-proof, if there are a lot objects
- Unit Test: to ensure they API endpoints work as expected
- Caching

## Production Consideration
- Containerization: Docker/Kubernetes to package project into containers

## Assumptions

![Schema Assumption](https://user-images.githubusercontent.com/98715291/227418556-cd588a47-f237-41f5-afe0-11783061b6c9.png)

![Schema Assumption](https://user-images.githubusercontent.com/98715291/227848747-6861bef4-575a-4614-86e3-d7b04c565c9d.png)
