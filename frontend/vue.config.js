module.exports = {
  devServer: {
      disableHostCheck: true,
      proxy: {
        '/api' : {
          target: 'http://192.168.35.120:8000/api',
          changeOrigin: true,
          logLevel: 'debug',
          pathRewrite: {
            '^/api': '',
          }
        }    
      }
    }
  }