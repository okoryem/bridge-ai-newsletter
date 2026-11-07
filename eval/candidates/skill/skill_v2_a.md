# Apple Is Rationing AI. You Should Be Ordering More.

Somewhere in Cupertino, an engineer just found out their daily AI allowance is dropping from $300 to $200. That's still roughly $4,000 a month. Per person.

Meanwhile, the median company in Ramp's spending data puts $12 to $15 per employee per month into AI. Not per day. Per month.

So when this week's headlines say companies are cutting back on AI, ask who "companies" means. It almost certainly doesn't mean you. If you've been waiting for a sign that you can skip AI for another year, this isn't it.

This week:

Why the AI spending slowdown is great news for small businesses (and what to do about it)

How to let Claude read your bank accounts safely, and why you should try it on your own money first

Claude Enterprise gets a security report card, Meta's Muse starts building mini apps, and researchers find 800 AI hacking tools sitting open on the internet

## The Deep Dive

### Apple Is Rationing AI. You Should Be Ordering More.

Two stories landed this week that, read together, sound like the AI party is winding down.

First, Bloomberg reported on November 4 that Apple cut the daily AI spending cap for its engineering teams from $300 to $200 in October. Some allowances are expected to fall to $100, and Apple is reportedly considering a limit as low as $25 a day for people outside engineering. (The sources are anonymous, and Apple didn't comment.)

Second, Ramp, the corporate card and spend company, says its data shows AI token spend barely grew in August and September: 1.5% across both months, after jumping 42% in July alone. It picked back up 8.9% between late September and late October, but Ramp's lead economist, Ara Kharazian, still calls the slowdown "unusually stubborn."

Earlier this year the trend had a name: tokenmaxxing. Use as much AI as possible, figure out the payoff later. Now the bills have arrived and the big spenders are rationing. Notion's co-founder Akshay Kothari summed it up in a post on October 22: "tokens go brrr. costs go ahhh."

Here's what's actually going on, because it isn't what the headline suggests.

**People are using more AI, not less.** Ramp is clear that token volume kept rising. What stalled was the bill. In September, OpenAI cut API prices in half for GPT-6 Sol and GPT-6 Luna, and Anthropic made big cuts on Fable 5.1 and Opus 5.5 (it said in a recent filing that this cost it about $600 million in revenue growth). Same work, smaller invoice.

Think about long-distance calls in the 1990s. People talked more every year, and the phone companies still looked like they were in trouble, because the price per minute kept collapsing. Nobody called that the end of the telephone.

**The biggest spenders got smarter.** Companies are blocking expensive models on long-running tasks, setting budgets per employee and sending routine work to cheaper models. Kharazian's line is the best summary I've seen: "You can use more AI, but use it for less."

I'll defend Apple a little. Some of that $300 a day was probably waste. If you let anyone run the most expensive model on every task with no limit, some of them will use it to rename files. A budget forces people to think about which jobs deserve the big model. That's healthy.

But look at who's doing the cutting. Ramp's top 1% of firms spent $9,568 per employee per month in September, and about 80% of OpenAI and Anthropic spend on Ramp comes from that 1%. The top 10% spend $600 to $1,000. The median business spends $12 to $15.

Apple's lowest proposed cap for non-engineers, $25, is more than the median company spends per person in an entire month.

Now for the business part. You are not Apple. You're not overspending on AI. You're more likely underfed, and prices are now on your side. Four moves:

**Know your number.** Add up every AI subscription and API bill your company pays, then divide by headcount. If it takes you more than ten minutes to find, that tells you something.

**Spend where the thinking is.** Apple's engineers are about to learn routing the hard way. You can learn it the easy way. A fast, cheap model like Claude Haiku 5.5 is fine for sorting email or tagging invoices. Anything a client will read, or anything touching money, gets the best model you have.

**Give allowances, not bans.** If one person on your team is hitting usage limits every afternoon, that's your best user, not your problem. Move them to a bigger plan. (Last month's issue on who Anthropic loses money on still applies.)

**Count outcomes, not tokens.** Once a quarter, ask each person one question: what got faster? If nobody can answer, you have a training problem, not a spending problem.

Apple is trimming a $300-a-day habit. Most of you are still deciding whether to start a $20-a-month one. Which side of that would you rather be on in two years?

## From the Field

### Claude Can Read Your Bank Accounts Now. Start With Your Own.

Back in October I wrote about connecting Claude to your finances through a third-party connector. As of November 5, it's built in.

Anthropic launched Personal Finance in Claude, a beta rolling out now on the Pro, Max and Ultra plans in the US. You connect your bank and card accounts through Plaid, and Claude can answer questions about your money in plain English.

Setup takes about five minutes:

**1\. Open Personal Finance** from Claude's sidebar.

**2\. Connect one account.** You sign in to your bank yourself through Plaid and approve read-only access. Claude never sees your bank password, and it can't move, manage or invest money.

**3\. Ask one question.** "Where did my money go this month?" is a good start. Then push: "Is that more than usual?" and "Anything else I'm missing?"

Claude sees only the accounts you connect: the bank name, account names and types, the last four digits, balances, credit limits and up to two years of transactions. It looks for duplicate charges, surprise fees and bills that creep up every month. Anthropic says conversations in the Personal Finance hub aren't used to train its models. Anything you share outside the hub follows your normal privacy settings, so keep money questions in the hub.

Two things I'd do. First, ask it to list every AI subscription you're paying for. (See the Deep Dive. You might find your number faster than you expected.) Second, whenever it gives you a figure, ask which transactions support it. Anthropic itself says to check important numbers with your bank.

If you're an advisor, pay attention to one line: Anthropic says it isn't designed for investment advice and is exploring how to work with licensed professionals and regulated firms. Your clients will walk in having already asked Claude about their spending. Better to have tried it yourself.

**Why this travels:** Grilling Claude about numbers you already know cold, your own, is the fastest way to learn when to trust it with numbers you don't.

## AI News Worth Your Time

### Three Stories From This Week

### Claude Enterprise gets a security report card

On November 5, Anthropic added a batch of security tools for Claude Enterprise. The headliner is a Security center (in beta) that compares your settings for chat, Cowork and Claude Code against Anthropic's recommended configuration, links you to each setting and exports a report you can hand to auditors. Prompt hooks that send prompts through your existing data-loss-prevention tools are now generally available, and admins can sign someone out of every session or block personal accounts on company computers. Anthropic notes the report is guidance, not a certification.

**My take:** For RIAs and anyone else with an auditor, this is the most useful thing in the release. Back in August I wrote about how "are we allowed to do that?" stalls finance firms for months. A downloadable report that shows exactly how Claude is configured makes that conversation shorter. It doesn't make the call for you, though. Your compliance person still signs off. [READ THE ANTHROPIC ANNOUNCEMENT →](https://claude.com/resources/articles/claude-enterprise-security-updates)

### Meta's Muse will now build you a little app

Meta launched Spaces on November 6, a new section in the Muse sidebar. Describe an idea in chat and Muse builds a tracker, planner or project board, then keeps it updated in the background from connected apps. Meta's examples are mostly personal: trip planning, gift lists, weddings. Muse hit 10 million users in the US and Canada less than two months after launch, according to Meta's October earnings call, and a day earlier Meta let US users video chat with their Muse agent.

**My take:** "Describe it and get a working tool" is becoming a standard feature in every major assistant. Claude has been doing this for a while with artifacts and dashboards. The business lesson is the same either way: before you pay for another small tracking subscription, spend fifteen minutes describing what you need to the AI you already pay for. [READ THE TECHCRUNCH REPORT →](https://techcrunch.com/2026/11/06/meta-introduces-spaces-a-new-way-to-collaborate-with-your-muse-agent/)

### Researchers found 800 AI hacking tools sitting open on the internet

Security firm Censys found more than 800 deployments of Artex, a free, Chinese-made AI tool that automatically probes systems for weaknesses, reachable on the web without a password, TechCrunch reported on November 6. Not every copy is malicious, but Artex has been linked to attacks on South Korea's financial industry in September and to Chinese-linked hackers spying on thousands of organizations in October. Microsoft describes it as AI agents that can run an attack "from reconnaissance through data exfiltration" with little human help. Its developers say future versions will be paid-only, but dozens of copies of the code are still out there.

**My take:** The scary detail isn't the AI. It's how the attacks got in: weak or known passwords and no multi-factor authentication. AI makes it cheap for attackers to try every door, so the open ones get found faster. This week, turn on MFA for email, banking and anything an employee logs into from home. It's the least exciting thing in this issue and probably the most important. [READ THE TECHCRUNCH REPORT →](https://techcrunch.com/2026/11/06/hundreds-of-artex-ai-hacking-tools-found-publicly-exposed-to-the-web/)

That's it for this week.

If this was useful, forward it to the person who runs your budget and thinks AI is the first line item to cut. That's who this is for.

And if you want to talk about what AI could do for your business, not in theory, but in your workflows, with your team, on your timeline, reach out at dean@bridgeaiconsulting.com. That's what we're here for.

Dean

Founder & CEO, Bridge AI Consulting

[bridgeaiconsulting.com](https://www.bridgeaiconsulting.com)

**REFERRAL PROGRAM**

Know a business that could use AI? Refer them to Bridge AI and earn 10% of their first year of payments. Get in touch at dean@bridgeaiconsulting.com to get started.

---

**Notes for Dean**

- **Numbers to double-check:** Apple caps ($300 to $200, $100, $25) come from Bloomberg's Nov 4 report via [TechCrunch](https://techcrunch.com/2026/11/04/apple-is-reportedly-cutting-budgets-for-its-internal-ai-usage/), anonymous sources. Ramp figures: 1.5%, 42%, 8.9%, the $12 to $15 median, $600 to $1,000 top 10%, and the OpenAI/Anthropic price cuts and $600M come from [TechCrunch, Nov 6](https://techcrunch.com/2026/11/06/ramp-data-shows-ai-spending-stalling-just-as-anthropic-nears-its-ipo/); the $9,568 top-1% figure and "80% of OpenAI and Anthropic spend from 1% of firms" come from Ramp's own [Oct 14 post](https://ramp.com/data/ai-index-oct-2026). I couldn't find the median and top-10% tiers on Ramp's page itself.
- **Left out on purpose:** Anthropic's IPO valuation (reports range from $1.2T to $1.6T depending on the outlet and week) and OpenAI's new cyber model (sources disagree on its name). Uber's "four rides booked by AI agents" stat was tempting for the Deep Dive but I couldn't confirm it against an official transcript.
- **Your story would help:** In "Know your number," if you have a real client who added up their AI spend and was surprised (either direction), swap it in.
- **Deep Dive image:** A simple bar chart, log scale, of monthly AI spend per employee: median firm ($12 to $15), top 10% ($600 to $1,000), top 1% ($9,568), and Apple's new engineering cap at roughly $4,200 a month ($200 a day x 21 workdays). The gap is the story.
- Week was security-heavy, so two of the three news items lean that way. If you'd rather vary it, Airbnb's planned AI travel agent (TechCrunch, Nov 5) is the swap.
