# FreeDomain — Free Domain Registration Skill

Register free subdomains for projects using DigitalPlat FreeDomain service.

## Available Extensions
- `.dpdns.org`, `.us.kg`, `.qzz.io`, `.xx.kg`, `.qd.je`

## Process
1. **Create account**: `https://dash.domain.digitalplat.org/auth/register` (username, password, email, WHOIS info)
2. **Choose DNS provider**: Cloudflare recommended (free plan)
3. **Add domain to Cloudflare**: `https://dash.cloudflare.com` → Add a site → Free plan
4. **Update nameservers**: Copy Cloudflare's NS → paste in DigitalPlat dashboard domain settings
5. **Add DNS records** in Cloudflare: A/AAAA/CNAME/TXT as needed
6. **Domain active** when Cloudflare shows status Active

## Limits
- **1 domain per account** (subdomains unlimited via DNS provider)
- Works with Cloudflare, FreeDNS, Hostry, or custom NS

## Links
- Dashboard: `https://dash.domain.digitalplat.org/`
- Discord: `https://discord.gg/ma4RZzMmVW`
- Abuse: `abusereport@digitalplat.org`
