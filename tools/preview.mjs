import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const blocked = new Set(["tools", "backup", ".git", ".cursor"]);
const port = Number(process.env.PORT || 4173);
const types = {
  ".html": "text/html; charset=utf-8",
  ".php": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".webp": "image/webp",
};

const server = http.createServer((req, res) => {
  console.log(new Date().toISOString(), req.socket.remoteAddress, req.method, req.url);
  const url = new URL(req.url || "/", "http://127.0.0.1");
  let pathname = decodeURIComponent(url.pathname);
  if (pathname.includes("\0")) {
    res.writeHead(403, { "Content-Type": "text/plain; charset=utf-8" });
    res.end("Forbidden");
    return;
  }
  const bare = pathname.length > 1 && pathname.endsWith("/") ? pathname.slice(0, -1) : pathname;
  let rel = bare.replace(/^\/+/, "");
  if (rel === "" || pathname.endsWith("/")) rel = rel ? rel + "/index.php" : "index.php";
  const file = path.normalize(path.join(root, rel));
  const fromRoot = path.relative(root, file);
  const top = fromRoot.split(path.sep)[0].toLowerCase();
  const rootPrefix = root.endsWith(path.sep) ? root : root + path.sep;
  if ((file !== root && !file.startsWith(rootPrefix)) || fromRoot.startsWith("..") || path.isAbsolute(fromRoot) || blocked.has(top)) {
    res.writeHead(403, { "Content-Type": "text/plain; charset=utf-8" });
    res.end("Forbidden");
    return;
  }
  if (fs.existsSync(file) && fs.statSync(file).isDirectory()) {
    res.writeHead(302, { Location: pathname.endsWith("/") ? pathname : pathname + "/" });
    res.end();
    return;
  }
  fs.readFile(file, (err, data) => {
    if (err) {
      res.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
      res.end("Not found");
      return;
    }
    res.writeHead(200, {
      "Content-Type": types[path.extname(file)] || "application/octet-stream",
      "Cache-Control": "no-cache",
    });
    res.end(data);
  });
});

server.listen({ port, host: "::", ipv6Only: false }, () => {
  console.log("North Desk preview");
  console.log("http://127.0.0.1:" + port + "/");
  console.log("http://[::1]:" + port + "/");
});
