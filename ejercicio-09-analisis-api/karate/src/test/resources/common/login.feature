@ignore
Feature: Login reutilizable

Scenario: Obtener token
  Given url baseUrl
  And path 'auth', 'login'
  And request { usuario: '#(usuario)', password: '#(password)' }
  When method post
  Then status 200
  * def token = response.token
