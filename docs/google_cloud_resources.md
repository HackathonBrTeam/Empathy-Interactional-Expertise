# Google Cloud Resources

## Project

| Field | Value |
|---|---|
| Project name | EmpathyAI |
| Project ID | empathyai-496601 |
| Project number | 213729457903 |
| Environment | Controlled demo / hackathon |
| Primary region | us-central1 |
| Primary zone | TBD |
| Billing account | TBD |

## Architecture Summary

The controlled demo uses GitHub Pages as the public landing page, a Cloud Run launcher to start the demo on demand, and a Google Compute Engine VM to run Streamlit with Ollama/Gemma local inference.

The infrastructure goals are:

- Start the AI demo only on demand.
- Avoid exposing Ollama directly to the public internet.
- Use short-lived signed demo tokens instead of shared browser credentials.
- Expire inactive browser sessions automatically.
- Allow VM auto-shutdown after no active sessions remain.
- Minimize infrastructure and environmental costs during hackathon testing.

## Public Entry Points

| Resource | URL | Purpose |
|---|---|---|
| GitHub Pages landing | https://hackathonbrteam.github.io/Empathy-Interactional-Expertise/landing/ | Public project landing page and controlled demo launch |
| Session expired page | https://hackathonbrteam.github.io/Empathy-Interactional-Expertise/session-expired.html | Friendly destination after inactivity timeout |
| Cloud Run launcher | https://empathyai-demo-launcher-213729457903.us-central1.run.app/start-demo | Starts/checks the VM and returns a tokenized demo URL |

## Cloud Run

| Field | Value |
|---|---|
| Service name | empathyai-demo-launcher |
| Region | us-central1 |
| Endpoint | https://empathyai-demo-launcher-213729457903.us-central1.run.app/start-demo |
| Purpose | Start the VM on demand and return a signed demo access URL |
| Authentication model | Public launcher endpoint with CORS restricted to GitHub Pages origin |
| Token model | HMAC-signed short-lived demo token |
| Token TTL | 300 seconds |
| Service account | TBD |
| Container image | TBD |
| Secrets used | `DEMO_TOKEN_SECRET` |
| Logs | Cloud Run service logs |

### Required Launcher Response

The launcher must not return usernames, passwords, or Basic Auth URLs.

Expected response:

```json
{
  "url": "https://VM_HOST",
  "auth_url": "https://VM_HOST/?demo_token=SIGNED_TOKEN",
  "expires_in": 300
}
```

### Required CORS Headers

```http
Access-Control-Allow-Origin: https://hackathonbrteam.github.io
Vary: Origin
```

If the launcher handles `OPTIONS`, it should also return the appropriate preflight headers for the GitHub Pages origin.

## Compute Engine VM

| Field | Value |
|---|---|
| VM name | TBD |
| Zone | TBD |
| Machine type | TBD |
| External IP | TBD |
| IP type | TBD: ephemeral or static |
| Operating system | TBD |
| Purpose | Run Nginx, Streamlit, Ollama, and local Gemma inference |
| Startup script | TBD |
| Shutdown script | TBD |
| Open public ports | 80/443 only |
| Private/protected ports | Ollama `11434`, Streamlit internal port |
| Auto-shutdown policy | Stop VM when no active Streamlit sessions remain |

## Runtime Services On VM

| Service | Purpose | Publicly exposed? | Notes |
|---|---|---|---|
| Nginx | Public reverse proxy and optional fallback Basic Auth | Yes, 80/443 | Should not log raw demo tokens where possible |
| Streamlit | Demo UI | Behind Nginx only | Validates `demo_token` when `DEMO_TOKEN_SECRET` is configured |
| Ollama | Local model runtime | No | Must not be accessible from the public internet |
| Gemma | Local inference model | No | Model version TBD |

## Secrets

Do not document actual secret values in this repository.

| Secret | Used by | Purpose |
|---|---|---|
| `DEMO_TOKEN_SECRET` | Cloud Run launcher + Streamlit/VM | Sign and validate short-lived demo tokens |
| Basic Auth fallback credentials | Nginx / operator manual testing only | Manual fallback, not used by GitHub Pages launch flow |

## IAM

| Principal | Role | Scope | Reason |
|---|---|---|---|
| Cloud Run service account | TBD | Demo VM | Start/check VM state |
| Cloud Run service account | Secret Manager Secret Accessor | `DEMO_TOKEN_SECRET` | Sign demo tokens |
| Operator account(s) | TBD | Project or selected resources | Manual demo operations |

## Firewall Rules

| Rule | Source | Target | Ports | Purpose |
|---|---|---|---|---|
| TBD | `0.0.0.0/0` | Demo VM | 80, 443 | Public demo access through Nginx |
| TBD | Internal / localhost only | Demo VM | 11434 | Ollama must remain private |
| TBD | Internal / localhost only | Demo VM | Streamlit port | Streamlit should be proxied by Nginx |

## Runtime Flow

1. User opens the GitHub Pages landing page.
2. User selects **Launch Controlled Demo**.
3. Landing calls the Cloud Run launcher.
4. Cloud Run starts or checks the Compute Engine VM.
5. Cloud Run generates a 5-minute HMAC-signed `demo_token`.
6. Cloud Run returns `auth_url`.
7. Landing redirects the user to `auth_url`.
8. Streamlit validates `demo_token` when `DEMO_TOKEN_SECRET` is configured.
9. Streamlit removes the token from the browser URL after validation.
10. Browser inactivity timeout redirects the user after 3 minutes without human activity.
11. VM shutdown automation stops the VM after zero active sessions remain.

## Security Notes

- Do not return demo usernames or passwords from Cloud Run.
- Do not use URLs in the form `user:password@host`.
- Do not expose the demo password in JSON, JavaScript, browser history, or logs.
- Do not expose the token signing secret to the frontend.
- Keep Basic Auth only as a manual fallback for operators.
- Do not expose Ollama publicly.
- Prefer HTTPS for the VM demo URL before broader testing.
- Avoid logging raw `demo_token` values in Nginx, Streamlit, or Cloud Run logs where possible.

## Cost Controls

- VM starts only on demand.
- Browser inactivity expires sessions after 3 minutes.
- Streamlit health checks are not treated as human activity.
- VM auto-shutdown should detect zero active sessions and stop the instance.
- Public demo diary should remain ephemeral or be cleaned after tests.

## Operational Checklist

### Before Demo

- [ ] Confirm Cloud Run is deployed in `us-central1`.
- [ ] Confirm Cloud Run CORS allows `https://hackathonbrteam.github.io`.
- [ ] Confirm Cloud Run can start/check the VM.
- [ ] Confirm `DEMO_TOKEN_SECRET` is configured consistently in Cloud Run and Streamlit.
- [ ] Confirm launcher returns `auth_url` with `demo_token`.
- [ ] Confirm token expires after 5 minutes.
- [ ] Confirm Streamlit rejects missing, expired, and invalid tokens.
- [ ] Confirm Ollama model is available on the VM.
- [ ] Confirm Ollama port is not public.
- [ ] Confirm the inactivity timeout expires the session after 3 minutes.
- [ ] Confirm the VM shuts down after no active sessions remain.

### After Demo

- [ ] Confirm the VM is stopped.
- [ ] Review Cloud Run logs for launcher errors.
- [ ] Review VM logs for Streamlit/Nginx errors.
- [ ] Remove temporary data if needed.
- [ ] Review billing/cost.

## Discovery Commands

Run these in Google Cloud Shell to fill the `TBD` fields.

```bash
gcloud config set project empathyai-496601

gcloud run services list \
  --platform managed \
  --format='table(metadata.name,metadata.namespace,status.url,spec.template.spec.serviceAccountName)'

gcloud run services describe empathyai-demo-launcher \
  --platform managed \
  --region us-central1 \
  --format='yaml(metadata.name,status.url,spec.template.spec.serviceAccountName,spec.template.spec.containers[].image,spec.template.spec.containers[].env[].name)'

gcloud compute instances list \
  --format='table(name,zone.basename(),machineType.basename(),status,networkInterfaces[0].accessConfigs[0].natIP,networkInterfaces[0].network.basename(),networkInterfaces[0].subnetwork.basename(),tags.items.list())'

gcloud compute firewall-rules list \
  --format='table(name,network.basename(),direction,priority,sourceRanges.list(),targetTags.list(),allowed[].map().firewall_rule().list())'

gcloud secrets list \
  --format='table(name,replication.replication)'

gcloud projects get-iam-policy empathyai-496601 \
  --flatten='bindings[].members' \
  --filter='bindings.members:serviceAccount' \
  --format='table(bindings.members,bindings.role)'
```
