// src/setupProxy.js
const { createProxyMiddleware } = require("http-proxy-middleware");

module.exports = function (app) {
  app.use(
    "/api", // Change this to match your API endpoint
    createProxyMiddleware({
      target: "http://localhost:8000", // Your Django backend URL
      changeOrigin: true,
    })
  );
};
