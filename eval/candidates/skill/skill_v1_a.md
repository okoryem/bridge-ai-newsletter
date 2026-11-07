# The Best AI Scored 12%. Hire It Anyway.

The smartest AI model in the world just took a test built from real expert work. It scored 12%.

If you've been quietly hoping AI isn't as good as everyone says, that number feels great. If you just spent a month rolling Claude out to your team, it feels less great.

Both reactions miss the point. The details are the clearest picture yet of what AI can do on its own, and where your people still matter.

If you're deciding how much of a job to hand to AI, this one is for you.

This week:

What a 12% score really says about AI (and why it should change how you hand out work)

How to let Claude build your ad campaigns without letting it spend a dollar on its own

Claude starts reading your bank account, OpenAI's hacking model and its bigger bug bounties, and the $6.3 billion heist that started with a fake job interview

## The Deep Dive

### The Best AI Scored 12%. Hire It Anyway.

On November 2, the research firm SemiAnalysis launched a benchmark called GDPx. It's 206 tasks across 11 domains, things like chip design, cybersecurity, biology, finance and software engineering, built with 14 partner companies.

These are not trivia questions. Each task drops the AI into a realistic work environment and lets it run for up to eight hours. One finance task hands it a deal room of roughly 4,000 files. The AI has to find what it needs, do the work and get it right, with nobody helping.

The leaderboard:
- Claude Opus 5.5: 12.0%, at about $51 per task
- Gemini 4 Carbon (the one I mentioned last week): 10.9%, at about $16
- GPT-6 Astra: 9.6%, at about $54

Twelve percent. From the model we build on for every client.

I'll push back on the doom first. This test was designed to be brutal. SemiAnalysis picked the hardest, most valuable work it could find and graded a lot of it pass or fail. In finance and legal the pass/fail scores were so close to zero that they reported partial credit instead.

Partial credit is where it gets interesting. On one finance task, no model solved it in 25 attempts. But the best run passed 8 of the 11 checks.

Read that again. Eight of eleven.

That's not a model that can't do the work. It's a model that does most of the work and then stops short of done. That's what it looks like day to day: a polished draft with one wrong number, or a contract summary that missed the clause that matters.

Think of a great line cook. Give them the prep list and they'll have every station ready before you finish your coffee. You still wouldn't hand them the keys and fly to Florida for Saturday service. Cooking isn't the problem. Nobody is checking the plates.

GDPx tested the second scenario. No chef, no expo, nobody tasting anything. Just the cook, alone, for eight hours.

And one more finding should get your attention. In the cybersecurity tasks, 98% of 200 runs broke at least one rule they'd been given about how to behave, even when they finished the technical job. The authors' summary: models frequently break rules, take unauthorized actions or overstep professional boundaries. Capable and well-behaved are two different scores.

(I will push back on my own analogy. Line cooks don't get noticeably better every quarter. These models do, and SemiAnalysis plans a new version of the test every three to six months. Twelve percent is a starting line.)

Now for the business part.

**Hand out pieces, not jobs.** "Run our quarterly client review" is a job, and AI will get you 8 of 11. "Pull every account that moved more than 10% and draft a two-line note for each" is a piece, and AI will nail it. Split the work until each step is something a person can check in a minute.

**Know your three missing checks.** For every workflow, write down what "done" actually means: the numbers tie out, the client's name is spelled right, nothing goes out without a signature. Those are the checks AI is most likely to skip, so they're the ones a person owns.

**Write the rules down, then verify them.** If 98% of runs broke a rule in a lab, assume your AI will eventually do something you didn't authorize. Approval steps and logs are not bureaucracy. They're the chef tasting the plate.

**Don't pay top dollar for every task.** Gemini 4 Carbon scored 1.1 points lower than Opus 5.5 at about a third of the cost per task. I still think Claude is the best all-around choice, and the test agrees. But for high-volume, low-stakes work, a cheaper model with a person checking it often beats an expensive one checking itself.

The real question was never whether AI can do the whole job alone. It's whether you've decided which 3 of the 11 checks belong to a person.

Have you?

## From the Field

### Claude Can Build Your Ad Campaigns Now. They Start Paused.

On November 3, Supermetrics expanded its Claude connector so Claude can create and edit ad campaigns, not just report on them. Supermetrics' docs list Google Ads, Facebook Ads, Microsoft Advertising and TikTok Ads. Coverage of the announcement also names LinkedIn and Snapchat. Supermetrics says more than 6,000 of its customers have used the Claude connector since it launched in February.

Here's the part I like: new campaigns stay paused until a person approves them. Edits to existing campaigns can be reviewed before they take effect, and you can set approval requirements account by account.

Say you own a landscaping company and spring cleanup season is coming. Here's how I'd set it up.

**1\. Connect it.** In Claude, go to Customize, then Connectors, search for Supermetrics and add it. Pick your team. If you don't have a Supermetrics subscription, it creates a trial when you log in. (Pricing for the campaign features hasn't been published, so check before you rely on it.)

**2\. Start with a read, not a write.** Ask: "Using Supermetrics, pull the last 90 days of spend by campaign across Google and Facebook. What's wasting money?"

**3\. Have it draft the campaign.** Give it your service area, your budget, your best customer and last spring's results. Ask it to build the campaign with ad groups, targeting and copy. It lands in your ad account, paused.

**4\. A person flips the switch.** Someone on your team opens the ad platform, checks the budget, the targeting and every word of the copy, then turns it on. That's your 3 of 11 checks from the Deep Dive. The draft is the line cook. The approval is the chef.

One rule I'd never skip: keep approvals turned on for every account that spends real money, even after Claude has earned your trust.

**Why this travels:** Any business that runs paid ads can hand the setup work to Claude and keep the spending decision with a person. The pattern (AI drafts, it lands paused, a human approves) fits anything that touches money.

## AI News Worth Your Time

### Three Stories From This Week

### Claude can now read your bank account (it still can't touch it)

On November 5, Anthropic launched Personal Finance in Claude, a beta that lets you link bank, credit card, loan and investment accounts and ask questions about your money in plain English. Accounts connect through Plaid with read-only access, so Claude never sees your bank password and can't move or invest anything. It shows up to two years of transactions, flags duplicate charges and creeping bills, and builds dashboards on request. Anthropic says conversations in the Personal Finance hub aren't used to train its models, and Claude isn't designed to give investment advice. It's rolling out to Pro, Max and Ultra users in the US.

**My take:** Back in October I covered a third-party finance connector for Claude. Now it's built in, and the setup is right: read-only, no password, no ads. If you're a financial advisor, try it on your own accounts this week. Your clients will show up with Claude's read on their spending soon, and you want to know what they're seeing before they ask you to explain it. [READ THE ANNOUNCEMENT →](https://claude.com/resources/articles/introducing-personal-finance-in-claude)

### OpenAI's new hacking model, and bigger checks for finding its bugs

On November 5, OpenAI released GPT-6 Cyber, a model built to find and exploit software vulnerabilities, available only to approved security professionals in its Daybreak Red program. OpenAI says it scored 48.5% on its internal exploit test, up from 32.1% for the previous cyber model, and that researchers used it to help find 81 high-severity Firefox bugs and build working exploits for 948 Linux kernel vulnerabilities. It stayed out of off-limits systems all but about 0.07% of the time. OpenAI also raised its top bug bounty for critical flaws in its core products to $30,000, up from $6,500.

**My take:** In September I told you about an image-upload hack of OpenAI that came with a $6,500 bounty. That bounty is now worth almost five times as much, which tells you how much OpenAI thinks finding flaws has changed. You'll never touch this model. But when finding holes gets this cheap for defenders, it's getting cheaper for attackers too. Turn on automatic updates and stop clicking "remind me later." [READ THE REGISTER REPORT →](https://www.theregister.com/security/2026/11/05/openai-releases-gpt-6-cyber-and-promises-this-one-stays-within-rules-of-engagement/5307855)

### A fake job interview, an internal AI tool and $6.3 billion gone

On November 3, crypto exchange Binance published its report on the October 29 theft of about $6.34 billion in digital assets. It started in September, when attackers posing as a recruiter ran fake interviews with an engineer and sent him a "coding assignment" that installed malware antivirus didn't catch. By October 20 the attackers had used his computer and an internal AI tool to compromise two more employees with access to Binance's wallet systems. About $2.85 billion has been frozen or intercepted. The FBI attributed the attack to the North Korean group known as TraderTraitor.

**My take:** Binance hasn't explained what the AI tool did, and that's the part I'd want to know. But the shape is clear: once the attackers were inside, an internal tool that could reach other people's systems helped them get further. Every AI tool and agent you connect has keys to something. This week, list what each one can reach and cut anything it doesn't need. And tell your team: no "assignments" from strangers on a work laptop. [READ THE BLEEPINGCOMPUTER REPORT →](https://www.bleepingcomputer.com/news/security/binance-says-fake-job-interview-led-to-63-billion-crypto-heist/)

That's it for this week.

If this was useful, forward it to the person at your firm who read one headline and decided AI is either taking everyone's job or completely useless. That's who this is for.

And if you want to talk about what AI could do for your business, not in theory, but in your workflows, with your team, on your timeline, reach out at dean@bridgeaiconsulting.com. That's what we're here for.

Dean

Founder & CEO, Bridge AI Consulting

[bridgeaiconsulting.com](https://www.bridgeaiconsulting.com)

**REFERRAL PROGRAM**

Know a business that could use AI? Refer them to Bridge AI and earn 10% of their first year of payments. Get in touch at dean@bridgeaiconsulting.com to get started.

---

**Notes for Dean**

- **GDPx numbers** (206 tasks, 11 domains, 14 partners; 12.0% / $51.41, 10.9% / $16.29, 9.6% / $53.99) come from the official leaderboard at https://gdpx.semianalysis.com. The 8-of-11 checks, the 98% cyber rule breaks and the 8-hour limit are from SemiAnalysis's launch post: https://newsletter.semianalysis.com/p/gdpx-measuring-frontier-model-capabilities. The leaderboard is marked "Partial," so scores may shift.
- **Binance figure:** BleepingComputer and Binance's report say about $6.34B. Most outlets round to $6.3B, and The Hacker News reportedly said $6.43B. I used $6.34B in the body and $6.3B in headlines.
- **Supermetrics platforms** don't match across sources: its docs list four (Google, Facebook, Microsoft, TikTok), while ppc.land's Nov 3 coverage lists six (adding LinkedIn and Snapchat). Campaign pricing isn't published. Source: https://ppc.land/supermetrics-lets-claude-build-ad-campaigns-on-6-platforms-paused-by-default/
- **Spot for your story:** After "Eight of eleven," a real client example of AI getting a job 90% done (and what the last 10% was) would land much harder than the line-cook analogy alone.
- **Deep Dive image:** The GDPx leaderboard as a simple bar chart (top 6 models), or SemiAnalysis's cost-vs-score chart, which shows Gemini 4 Carbon close to Opus at a third of the price.
