@polizas
Feature: Pólizas

Background:
  * url baseUrl
  * def auth = callonce read('classpath:common/login.feature')
  * header Authorization = 'Bearer ' + auth.token

Scenario: Listar pólizas del cliente
  Given path 'polizas'
  When method get
  Then status 200
  And match response.total == 3

Scenario: Obtener el detalle de una póliza propia
  Given path 'polizas', 'P-1001'
  When method get
  Then status 200
  And match response.tipo == 'AUTO'
