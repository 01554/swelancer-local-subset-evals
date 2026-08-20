// Minimal HTTP forwarder: localhost:9000 -> upstream via HTTP proxy
// (absolute-URI proxying with Proxy-Authorization), so clients with broken
// proxy support can talk plain HTTP to localhost.
const http = require("http");

const TARGET_HOST = process.env.SHIM_TARGET_HOST; // e.g. 172.17.0.1.sslip.io
const TARGET_PORT = process.env.SHIM_TARGET_PORT || "80";
const proxyUrl = new URL(process.env.SHIM_PROXY); // e.g. http://agent:tok@egress-proxy:8080

const auth =
  proxyUrl.username || proxyUrl.password
    ? "Basic " +
      Buffer.from(
        `${decodeURIComponent(proxyUrl.username)}:${decodeURIComponent(proxyUrl.password)}`
      ).toString("base64")
    : null;

const server = http.createServer((req, res) => {
  const headers = { ...req.headers, host: `${TARGET_HOST}:${TARGET_PORT}` };
  if (auth) headers["proxy-authorization"] = auth;
  const upstream = http.request(
    {
      host: proxyUrl.hostname,
      port: proxyUrl.port || 8080,
      method: req.method,
      path: `http://${TARGET_HOST}:${TARGET_PORT}${req.url}`,
      headers,
    },
    (up) => {
      res.writeHead(up.statusCode, up.headers);
      up.pipe(res);
    }
  );
  upstream.on("error", (e) => {
    res.writeHead(502, { "content-type": "text/plain" });
    res.end("shim upstream error: " + e.message);
  });
  req.pipe(upstream);
});

server.listen(9000, "127.0.0.1", () => console.log("shim listening on 9000"));
