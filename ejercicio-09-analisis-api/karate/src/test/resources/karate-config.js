function fn() {
  var env = karate.env || 'local';
  karate.log('Entorno Karate:', env);

  var config = {
    baseUrl: 'http://localhost:3000/api/v1',
    usuario: 'cliente1',
    password: 'Cliente#24'
  };

  if (env === 'test') {
    config.baseUrl = 'https://test.pruebas-seguros.example/api/v1';
  }

  karate.configure('connectTimeout', 5000);
  karate.configure('readTimeout', 10000);
  return config;
}
