@auth
Feature: Autenticación

Background:
  * url baseUrl

Scenario: Login con credenciales válidas
  Given path 'auth', 'login'
  And request { usuario: 'cliente1', password: 'Cliente#24' }
  When method post
  Then status 200
  And match response.token == '#string'
