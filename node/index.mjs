import { readFile } from "node:fs/promises";

const apiKey = process.env.SOCQ_API_KEY;
const baseUrl = (process.env.SOCQ_BASE_URL || "https://api.socq.ai").replace(/\/+$/, "");
const endpointPath = process.env.SOCQ_ENDPOINT_PATH || "/v1/platform/resource";

if (!apiKey || apiKey === "your-api-key") {
  throw new Error("Set SOCQ_API_KEY before running this example.");
}

const payload = JSON.parse(
  await readFile(new URL("../payload.example.json", import.meta.url), "utf8"),
);
const response = await fetch(`${baseUrl}${endpointPath}`, {
  method: "POST",
  headers: {
    Authorization: `Bearer ${apiKey}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify(payload),
});
const body = await response.json();

if (!response.ok) {
  throw new Error(body?.error?.message || `SocQ request failed with HTTP ${response.status}.`);
}

console.log(JSON.stringify(body, null, 2));
