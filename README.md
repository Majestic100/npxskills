# Hero Media skills

Our shared library of Claude skills. Everything lives in this repo, both the skills we write ourselves and the ones we find elsewhere, so anyone can install them in **Claude Code** and in the **Claude app**.

Skills are grouped into *plugins* by category, so you install a whole topic at once, for example all SEO skills.

## Install

### Colleagues in the Hero Media Claude organization (Claude app and Claude Code)

The plugins are published to our Claude organization. Find them in the organization's plugin library on claude.ai and install the ones you want. They then work in both the Claude app and Claude Code, and you get updates when a new version is published.

If you only install some of the marketing plugins, start with **marketing-strategy**: its `product-marketing` skill creates the product context file the other marketing skills read.

### Friends and others outside the organization

**Claude Code:** add this repo as a marketplace and install the plugins you want:

```
/plugin marketplace add majestic100/npxskills
/plugin install marketing-strategy@heromedia-skills
/plugin install marketing-seo@heromedia-skills
```

The repo is private, so you need to be invited on GitHub and signed in with git on your machine.

**Claude app:** download the zip for the skill you want from [`dist/`](dist/) and upload it under *Settings → Skills* in the Claude app. One zip per skill.

## Add a skill

The easiest way is to ask Claude in a session in this repo, for example *"add the skill X from github.com/owner/repo"* or *"write a new skill that does Y"*. The procedure is in [CLAUDE.md](CLAUDE.md).

By hand:

1. Put the skill folder in `plugins/<plugin>/skills/<skill-name>/` with its `SKILL.md` and any `references/` and scripts. If someone else made it, include their `LICENSE`.
2. Add the skill to [`sources.json`](sources.json) (source and license, or `"source": "own"` for our own).
3. Bump `version` in the plugin's `.claude-plugin/plugin.json`.
4. Run `python3 scripts/build.py`. It checks the skill and regenerates the overview below, the zip files and the marketplace file.
5. Commit, push, and publish the plugin to the organization again.

## Skills

<!-- CATALOG:BEGIN -->

51 skills in 9 plugins. Click a skill name to read the full skill.

### design (2 skills)

Frontend and web design: avoid generic AI-looking interfaces and build pages with a clear visual direction.

| Skill | What it does | Source |
|---|---|---|
| [design-taste-frontend](plugins/design/skills/design-taste-frontend/SKILL.md) | Anti-slop frontend skill for landing pages, portfolios, and redesigns. | [leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill) (MIT) |
| [frontend-design](plugins/design/skills/frontend-design/SKILL.md) | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. | [anthropics/skills](https://github.com/anthropics/skills) (Apache-2.0) |

### find-skills (1 skill)

Find and install new skills from the open skills ecosystem (via npx skills). Claude Code only.

| Skill | What it does | Source |
|---|---|---|
| [find-skills](plugins/find-skills/skills/find-skills/SKILL.md) | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending capabilities. | [vercel-labs/skills](https://github.com/vercel-labs/skills) (MIT) |

### marketing-ads (4 skills)

Paid acquisition and measurement: ad campaigns, ad creative, analytics tracking and A/B testing.

| Skill | What it does | Source |
|---|---|---|
| [ab-testing](plugins/marketing-ads/skills/ab-testing/SKILL.md) | When the user wants to plan, design, or implement an A/B test or experiment, or build a growth experimentation program. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [ad-creative](plugins/marketing-ads/skills/ad-creative/SKILL.md) | When the user wants to generate, iterate, or scale ad creative — headlines, descriptions, primary text, or full ad variations — for any paid advertising platform. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [ads](plugins/marketing-ads/skills/ads/SKILL.md) | When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X, or other ad platforms. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [analytics](plugins/marketing-ads/skills/analytics/SKILL.md) | When the user wants to set up, improve, or audit analytics tracking and measurement. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |

### marketing-content (11 skills)

Content and copy: copywriting, copy editing, content strategy, social, video, images, lead magnets, free tools, community, PR and co-marketing.

| Skill | What it does | Source |
|---|---|---|
| [co-marketing](plugins/marketing-content/skills/co-marketing/SKILL.md) | When the user wants to find co-marketing partners, plan joint campaigns, or brainstorm partnership opportunities. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [community-marketing](plugins/marketing-content/skills/community-marketing/SKILL.md) | Build and leverage online communities to drive product growth and brand loyalty. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [content-strategy](plugins/marketing-content/skills/content-strategy/SKILL.md) | When the user wants to plan a content strategy, decide what content to create, or figure out what topics to cover. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [copy-editing](plugins/marketing-content/skills/copy-editing/SKILL.md) | When the user wants to edit, review, or improve existing marketing copy, or refresh outdated content. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [copywriting](plugins/marketing-content/skills/copywriting/SKILL.md) | When the user wants to write, rewrite, or improve marketing copy for any page — including homepage, landing pages, pricing pages, feature pages, about pages, or product pages. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [free-tools](plugins/marketing-content/skills/free-tools/SKILL.md) | When the user wants to plan, evaluate, or build a free tool for marketing purposes — lead generation, SEO value, or brand awareness. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [image](plugins/marketing-content/skills/image/SKILL.md) | When the user wants to create, generate, edit, or optimize images for marketing — blog heroes, social graphics, product mockups, profile banners, listing visuals, or brand assets. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [lead-magnets](plugins/marketing-content/skills/lead-magnets/SKILL.md) | When the user wants to create, plan, or optimize a lead magnet for email capture or lead generation. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [public-relations](plugins/marketing-content/skills/public-relations/SKILL.md) | When the user wants help with public relations, earned media, press coverage, journalist outreach, or media strategy (not pull requests). | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [social](plugins/marketing-content/skills/social/SKILL.md) | When the user wants help creating, scheduling, or optimizing social media content for LinkedIn, Twitter/X, Instagram, TikTok, Facebook, or other platforms, or wants to do social listening and engagement triage. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [video](plugins/marketing-content/skills/video/SKILL.md) | When the user wants to create, generate, or produce video content using AI tools or programmatic frameworks. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |

### marketing-conversion (9 skills)

Conversion and retention: CRO, signup and onboarding flows, paywalls, popups, lifecycle email and SMS, referrals and churn prevention.

| Skill | What it does | Source |
|---|---|---|
| [churn-prevention](plugins/marketing-conversion/skills/churn-prevention/SKILL.md) | When the user wants to reduce churn, build cancellation flows, set up save offers, recover failed payments, or implement retention strategies. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [cro](plugins/marketing-conversion/skills/cro/SKILL.md) | When the user wants to optimize, improve, or increase conversions on any marketing page or form — including homepage, landing pages, pricing pages, feature pages, lead capture forms, or contact forms. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [emails](plugins/marketing-conversion/skills/emails/SKILL.md) | When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email program. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [onboarding](plugins/marketing-conversion/skills/onboarding/SKILL.md) | When the user wants to optimize post-signup onboarding, user activation, first-run experience, or time-to-value. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [paywalls](plugins/marketing-conversion/skills/paywalls/SKILL.md) | When the user wants to create or optimize in-app paywalls, upgrade screens, upsell modals, or feature gates. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [popups](plugins/marketing-conversion/skills/popups/SKILL.md) | When the user wants to create or optimize popups, modals, overlays, slide-ins, or banners for conversion purposes. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [referrals](plugins/marketing-conversion/skills/referrals/SKILL.md) | When the user wants to create, optimize, or analyze a referral program, affiliate program, or word-of-mouth strategy. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [signup](plugins/marketing-conversion/skills/signup/SKILL.md) | When the user wants to optimize signup, registration, account creation, or trial activation flows. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [sms](plugins/marketing-conversion/skills/sms/SKILL.md) | When the user wants to plan, build, or optimize SMS or MMS marketing — including welcome flows, abandoned cart texts, post-purchase, win-back, promotional sends, or transactional/auth SMS. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |

### marketing-sales (4 skills)

Sales and outbound: prospecting, cold email, sales enablement and RevOps.

| Skill | What it does | Source |
|---|---|---|
| [cold-email](plugins/marketing-sales/skills/cold-email/SKILL.md) | Write B2B cold emails and follow-up sequences that get replies. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [prospecting](plugins/marketing-sales/skills/prospecting/SKILL.md) | When the user wants to find, qualify, and build a list of prospects to reach out to — across B2B SaaS, general B2B, or local small businesses. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [revops](plugins/marketing-sales/skills/revops/SKILL.md) | When the user wants help with revenue operations, lead lifecycle management, or marketing-to-sales handoff processes. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [sales-enablement](plugins/marketing-sales/skills/sales-enablement/SKILL.md) | When the user wants to create sales collateral, pitch decks, one-pagers, objection handling docs, or demo scripts. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |

### marketing-seo (8 skills)

Search visibility: SEO audits, AI search (AEO/GEO), programmatic SEO, schema markup, site architecture, comparison pages, directory submissions and app store optimization.

| Skill | What it does | Source |
|---|---|---|
| [ai-seo](plugins/marketing-seo/skills/ai-seo/SKILL.md) | When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [aso](plugins/marketing-seo/skills/aso/SKILL.md) | When the user wants to audit or optimize an App Store or Google Play listing. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [competitors](plugins/marketing-seo/skills/competitors/SKILL.md) | When the user wants to create competitor comparison or alternative pages for SEO and sales enablement. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [directory-submissions](plugins/marketing-seo/skills/directory-submissions/SKILL.md) | When the user wants to submit their product to startup, SaaS, AI, agent, MCP, no-code, or review directories for backlinks, domain rating, and discovery. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [programmatic-seo](plugins/marketing-seo/skills/programmatic-seo/SKILL.md) | When the user wants to create SEO-driven pages at scale using templates and data. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [schema](plugins/marketing-seo/skills/schema/SKILL.md) | When the user wants to add, fix, or optimize schema markup and structured data on their site. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [seo-audit](plugins/marketing-seo/skills/seo-audit/SKILL.md) | When the user wants to audit, review, or diagnose SEO issues on their site. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [site-architecture](plugins/marketing-seo/skills/site-architecture/SKILL.md) | When the user wants to plan, map, or restructure their website's page hierarchy, navigation, URL structure, or internal linking. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |

### marketing-strategy (11 skills)

Marketing strategy and positioning: product-marketing context, marketing plans, ideas, customer research, competitor profiles, pricing, offers and launches. Install this first; the other marketing plugins read the product-marketing context it creates.

| Skill | What it does | Source |
|---|---|---|
| [competitor-profiling](plugins/marketing-strategy/skills/competitor-profiling/SKILL.md) | When the user wants to research, profile, or analyze competitors from their URLs. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [customer-research](plugins/marketing-strategy/skills/customer-research/SKILL.md) | When the user wants to conduct, analyze, or synthesize customer research. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [launch](plugins/marketing-strategy/skills/launch/SKILL.md) | When the user wants to plan a product launch, feature announcement, or release strategy. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [marketing-council](plugins/marketing-strategy/skills/marketing-council/SKILL.md) | When the user wants multiple expert perspectives on a marketing question — a simulated board of advisors staffed by legendary marketers (Seth Godin, David Ogilvy, Eugene Schwartz, April Dunford, Rory Sutherland, Alex Hormozi, Byron Sharp, and more). | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [marketing-ideas](plugins/marketing-strategy/skills/marketing-ideas/SKILL.md) | When the user needs marketing ideas, inspiration, or strategies for their SaaS or software product. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [marketing-loops](plugins/marketing-strategy/skills/marketing-loops/SKILL.md) | When the user wants to set up a recurring, self-running marketing workflow — a repeatable loop an AI agent runs on a cadence (weekly, daily, on a trigger) rather than a one-off task. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [marketing-plan](plugins/marketing-strategy/skills/marketing-plan/SKILL.md) | When the user needs a comprehensive marketing plan for a client, a company they advise, or their own product. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [marketing-psychology](plugins/marketing-strategy/skills/marketing-psychology/SKILL.md) | When the user wants to apply psychological principles, mental models, or behavioral science to marketing. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [offers](plugins/marketing-strategy/skills/offers/SKILL.md) | When the user wants to design, construct, or improve an offer — the thing they actually sell — including value framing, bonus stacking, guarantee design, scarcity/urgency, naming, and payment structure. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [pricing](plugins/marketing-strategy/skills/pricing/SKILL.md) | When the user wants help with pricing decisions, packaging, or monetization strategy. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |
| [product-marketing](plugins/marketing-strategy/skills/product-marketing/SKILL.md) | When the user wants to create or update their product marketing context document. | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) |

### security-audit (1 skill)

Security audit of a codebase using isolated agents, from reconnaissance to verified findings and a report. From Cloudflare.

| Skill | What it does | Source |
|---|---|---|
| [security-audit](plugins/security-audit/skills/security-audit/SKILL.md) | Security guidance and vulnerability review for codebases, APIs, services, CLI tools, libraries, and daemons. | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) (MIT) |

<!-- CATALOG:END -->
