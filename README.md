# CRUD of Socies of Humano Mutual

## Project Description:

This project is a CRUD API for the Humano Mutual. The API will be used to manage the Socies of the Mutual.
The main goal of the project is to follow chapter by chapter the book "Architecture Patterns with Python" by Harry J.W.
Percival and Bob Gregory, using another domanin to the one proposed in the book.
A second goal is to use GitHub projects to manage the task and deliverables of the project.
The first mvp will be a simple CRUD API with to response to the necesite of the management of the Socies of the Mutual.
Humano Mutual is a mutual of producers and buyers, we will use the term socies to refer to the members of the mutual.

## Project Deliverables:

1. A branch for each round of development in base a every chapter of the book "Architecture Patterns with Python".
2. A main branch with the actual state of the project.
3. Iterations documented in the todo file and projects issues.

## Project Requirements:

1. Build a CRUD API using Python and FastAPI framework.
2. Use GraphQL as the query language and Strawberry as the GraphQL library.
3. The API must be asynchronous.
4. Use Behavior Driven Development to develop the API and Strict Test Driven Development with tests written before
   implementation.
5. The API must be well-documented with Swagger UI.
6. The API should support authentication and authorization with JSON Web Tokens (JWT).

## Project Constraints:

1. We'll use Python as the language for the API development.
2. FastAPI will be used as the web framework.
3. GraphQL will be used as the query language and Strawberry as the GraphQL library.
4. The API must be asynchronous.
5. Behavior Driven Development will be used with a library of your choice.
6. Strict Test Driven Development will be used with tests written before implementation.

# Domain Description of Socies

We need to create a GraphQL API for Mutual Humano.

- The mutual has producing members and buying members. To differentiate these types, it is proposed to use the
  category 'adherente' for producing members and 'humane' for buyers.
- All members have to pay a monthly fee, and these payments need to be recorded.
- If a member fails to pay the monthly fee for more than three months, they become 'inactive'.
- We determine this when we check the status of a member.
- The member's status becomes active by paying the current month's fee.
  There is another type of entity, the providers, who are not members of the mutual, and they are referred to as
  providers.

#### Members have:
- Name(s)[^1]
- Last name(s)
- Venture
- ID number(s)
- Code(s)
- Address
- Postal code
- Phone number
- Email
- Can be active or not[^1], default is active
- Can be adherente or humane[^1], default value adherente

Providers have:

- Name(s)[^1]
- Last name(s)
- Venture
- Category
- CUIT number(s)
- Code(s)
- Address
- Postal code
- Phone number
- Email

Our API should be able to:

- Create a member.
- Modify a member.
- Delete a member.
- List all members by:
    - Active status
    - Inactive status
    - Full members
    - General members
- List a member by:
    - ID number
    - Code
    - Email
- Create a provider.
- Modify a provider.
- Delete a provider.
- List all providers by:
    - Category
- List a provider by:
    - Name
    - Last name
    - Venture
    - CUIT number
    - Code

- The API should be able to automatically inform if a member is active or not.
- The API should have an authentication and authorization system for users.
- Users can have administrator or user roles.
- Administrator users can create, modify, list, and delete users.
- Administrator users can create, modify, list, and delete members and providers.
- Non-administrator users can only list members and providers.

# Footnotes

[^1]: (o) denotes optional fields.