# CRUD of Socies of Humano Mutual
# Dominios

## Descripción del domino de Socies
Tenemos que crear una Graphql API para la Mutual Humano.
- La mutual cuenta con socios productores y socios que compran. Para diferenciar estos tipos se propone usar la
- categoría `Plenos` para los socios productores y `Generales` para los compradores.
- Todos los socios tienen que pagar una cuota mensual, hay que llevar registro de esto pagos.
- Si un socio no pagó la cuota mensual por más de tres meses pasa a estar `inactivo`.
- Esto lo sabemos cuando consultamos el estado de un socio.
- Se activa pagando la cuota del mes en curso.
Existe otro tipo de sujetos, los proveedores, que no son socios de la mutual, a estos se los denomina proveedores
Los socies tienen:

- Nombre(o)<sup><a id="fnr.1" class="footref" href="#fn.1" role="doc-backlink">1</a></sup>
- apellido(o)
- emprendimiento
- dni(o)
- codigo(o)
- domicilio
- codigo postal
- telefono
- email
- Puede estar Activo o No(o) default activo
- Puede ser Pleno o No(o) sin default

Los proveedores tienen

- Nombre(o)<sup><a id="fnr.1.100" class="footref" href="#fn.1" role="doc-backlink">1</a></sup>
- apellido(0)
- emprendimiento
- rubro
- cuil/cuit(o)
- codigo(o)
- domicilio
- codigo postal
- telefono
- email

Nuestra api debe poder:
- crear un socio.
- modificar un socio.
- eliminar un socio.
- listar todos los socios por:
    - activos
    - inactivos
    - plenos
    - generales
- listar un socio por.
    - dni
    - codigo
    - email
- crear un proveedor.
- modificar un proveedor.
- eliminar un proveedor.
- listar todos los proveedores.
  - rubro
- listar un proveedor.
  - nombre
  - apellido
  - emprendimiento
  - cuil/cuit
  - código

- La api debe poder informar automaticamente si un socio esta activo o no.
- La api debe tener contar con un sistema de autenticación y autorización de usarios.
- Los usuarios pueden tener roles de administrador o de usuario.
- Los usuarios administradores pueden crear, modificar, listar y eliminar usuarios.
- Los usuarios administradores pueden crear, modificar, listar y eliminar socios y proveedores.
- Los usuarios no adminstradores solo pueden listar socios y proveedores.
 
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

## Project Deliverables:

1. Install required dependencies like Python, FastAPI, and Strawberry.
2. Write scope of the domanin.
3. Write user stories cards
2. Write the scenarios.
3. Write test cases for the scenarios.
6. Write the implementation code to pass the test cases for the models
5. Define the API schema using GraphQL.
6. Write test cases for the schema.
5. Implement the schema with the appropriate query and mutation functions.
7. Ensure the API is asynchronous by using async/await functions.
8. Add Swagger UI for API documentation.
9. Implement authentication and authorization with JWT.

For the BDD part, we can use the Behave library, which is a popular Python BDD framework. It integrates well with the
FastAPI framework, and we can write Gherkin syntax feature files that describe the behavior of the API.

Let me know if you have any questions or concerns. We can proceed with the above steps and create a great API for your
project.



# Footnotes

<sup><a id="fn.1" href="#fnr.1">1</a></sup> Esto quiere decir Obligatorio
