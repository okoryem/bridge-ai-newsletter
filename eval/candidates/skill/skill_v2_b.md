# Four Rides

Halloween week was Uber's busiest week of October. Costumes, parties, a lot of people who very much should not be driving.

Number of those rides booked by an AI agent: four.

Not four percent. Four rides.

Uber said it on its earnings call last Wednesday, the same week Apple reportedly cut how much its engineers can spend on AI each day and new data from Ramp showed company AI spending flatlining. Put those together and you get the most useful lesson of the year about where AI actually pays. If you're deciding what to point AI at next, this one is for you.

This week:

Why AI agents booked four Uber rides, and how to pick tasks where AI actually earns its keep

How to set up Claude's new Personal Finance tool, and what to check before you trust it

Anthropic tells the SEC it may be close to AI that builds AI, an OpenAI model finds a server-takeover bug in two hours, and hackers leave 800 copies of their AI attack tool wide open

## The Deep Dive

### Four Rides

Here are the numbers, per TechCrunch's report on Uber's third-quarter call on November 4. During Halloween week, four Uber rides were ordered through an AI agent. Uber Eats did better: about 500 orders. CEO Dara Khosrowshahi called the traction "very, very early and very limited." DoorDash said on its own call the week before that it had received only a few hundred orders from agents.

This is not because the agents are bad. Every big lab now has one, and Meta's Muse topped 10 million users last month.

It's because of a number Khosrowshahi shared on the same call. The average time to book a ride in Uber's app is 50 seconds. Reordering a favorite meal takes 90.

You can't save much time on a 50-second task. An agent has to understand you, open the right service, confirm the address and check the price. By the time you've read its summary, you could have just tapped the button.

Now look at the bills. Ramp, which processes spending for thousands of companies, reported that AI token spend grew 1.5% across August and September, after growing 42% from June to July. Usage kept climbing. Spending didn't. And on November 4, Bloomberg reported that Apple cut its engineers' daily AI allowance from $300 to $200 in October, with some heading to $100 and a possible $25 cap outside engineering.

Earlier this year a lot of companies told employees to use AI for everything and figure out the value later. The value conversation has arrived.

I'd push back on the doom version of this story, though. Ramp's lead economist, Ara Kharazian, says the slowdown is driven by competition, not weak demand, and that a buyer's market has emerged. Prices fell hard. Anthropic said in a recent filing that its price cuts reduced revenue growth by about $600 million. That's bad news for an IPO pitch and good news for you.

And four rides is a week-one number for a whole new way of buying things. Early numbers for new habits always look silly.

But the pattern underneath is real. **AI's value is roughly proportional to how slow and annoying the job was before.** Point it at a 50-second task and you pay for tokens to save nothing. Point it at a three-hour task and the same tokens buy you an afternoon.

Now for the business part.

**Time the task before you automate it.** Write down how long the job takes today, start to finish, including the part where someone hunts for the right file. If the answer is under a minute, leave it alone.

**Go after the hours.** The good targets are boring and long: a roofing company turning site photos and notes into a written estimate, an RIA assembling a client meeting packet from four systems, a bookkeeper matching two years of transactions. Those are the jobs where nobody would ever miss the old way.

**Give people a budget, not a mandate.** Ramp says the median company spends $12 to $15 per employee per month on AI, and the top 10% spend $600 to $1,000. You don't need to be in either camp by accident. Put the money where the long jobs are, and stop paying for usage that only makes a dashboard look busy.

**Use the buyer's market.** If a vendor's price hasn't moved since spring, while the models underneath got much cheaper, ask why.

The question isn't whether AI can do the task. It's whether the task was worth doing faster. If the old way takes 50 seconds, keep the old way.

## From the Field

### Claude Can Read Your Bank Accounts Now. Start Here.

Back in October I wrote about connecting your finances to Claude through Era Context. On November 5, Anthropic shipped its own version: Personal Finance in Claude.

It's a beta, US only, rolling out now to Pro, Max and Ultra subscribers. You connect bank and card accounts, and Claude can see balances and up to two years of transactions. Then you ask questions in plain English: where did my money go this month, is this higher than usual, what's left before payday. It flags duplicate charges, unexpected fees and bills that crept up over the year, and it can build spending charts or a due-date calendar.

Setup takes a few minutes:

**1\. Open Personal Finance** in Claude's sidebar.

**2\. Connect one account.** You sign in to your bank yourself through Plaid. Claude never asks for or sees your bank password (nothing should, ever).

**3\. Approve read-only access.** Claude can't move, manage or invest money.

**4\. Ask a real question,** then ask which transactions make up the answer. Anthropic itself recommends asking for the transactions behind a figure and checking important numbers with your bank. That's the human-in-the-loop step, and I wouldn't skip it.

One privacy detail, stated as narrowly as Anthropic states it: conversations in the Personal Finance hub aren't used to train its models. Anything you share outside the hub follows your normal privacy settings. You can unlink an account any time.

This is pitched for personal money, not your company books. I'd still start here. Reconciling two years of transactions is exactly the kind of slow, miserable job from this week's Deep Dive, and trying it on your own accounts is the lowest-risk way to learn how far to trust Claude with financial data.

**Why this travels:** Anthropic says it wants Claude to work alongside licensed professionals and is asking wealth managers for input. If you advise clients on money, some of them will show up to their next meeting with a Claude-built spending summary. Know what it can and can't do before they do.

## AI News Worth Your Time

### Three Stories From This Week

### Anthropic told the SEC it may be close to AI that builds AI

In its revised IPO filing on November 2, Anthropic said its internal estimates suggest it "may imminently meet" its own Responsible Scaling Policy threshold for "dramatically accelerated progress attributable to AI." It also said it has already used AI to develop models whose capability jumps it didn't recognize at the time. No current model has been designated as crossing the line, and Anthropic says it doesn't expect to let Claude build future models without meaningful human supervision.

**My take:** Skeptics note that an S-1 is part disclosure, part sales pitch, and that's fair. The sentence I'd focus on is the admission that the builders missed capability jumps in their own models. If they can miss them, you will too. When the model behind your workflows updates, rerun your test cases instead of assuming last month's results still hold. [READ THE TECHCRUNCH REPORT →](https://techcrunch.com/2026/11/02/anthropic-warns-that-its-very-close-to-rsi-capability-aka-self-building-ai/)

### An OpenAI model found a server-takeover bug in two hours

Max Justicz, CTO of Charge Robotics, asked an OpenAI model to find bugs "as bad or worse" than one he'd already found, and it came back in two hours with a severe flaw that could let attackers take over servers running Ubuntu. Debian patched it, with no known exploitation. He spent about $5,000 finding several exploits. The same week, OpenAI announced a new cybersecurity model for top-tier researchers in its Daybreak program and a $1 billion initiative for defenders of critical infrastructure.

**My take:** Finding serious bugs used to take experts weeks. Now it takes two hours and a few thousand dollars, and the attackers have access to similar tools. That means the gap between "flaw found" and "flaw exploited" keeps shrinking. Turn on automatic updates everywhere you can, and ask whoever runs your IT one question: how many days does it take you to apply a critical patch? [READ THE TECHCRUNCH REPORT →](https://techcrunch.com/2026/11/05/openai-released-a-new-cybersecurity-model-is-that-enough/)

### Hackers left 800 copies of their AI attack tool wide open

Security firm Censys found more than 800 deployments of Artex, an open-source autonomous hacking tool linked to several attacks since July, sitting on the internet with no password, reported November 6. Not all of them are malicious (some belong to authorized testers). Microsoft has said Artex can run attacks from reconnaissance to data theft with little human involvement. Many of the attacks tied to it got in through weak or known passwords and missing multi-factor authentication.

**My take:** The scariest AI hacking tool of the year mostly walks through doors that were already open. And the hackers forgot to lock their own. AI makes attacks faster, but the entry points are the same ones they've always been. If anyone at your company still logs into email, payroll or your CRM without multi-factor authentication, fix that this week. [READ THE TECHCRUNCH REPORT →](https://techcrunch.com/2026/11/06/hundreds-of-artex-ai-hacking-tools-found-publicly-exposed-to-the-web/)

That's it for this week.

If this was useful, forward it to the person on your team who wants to buy an AI agent for a job that currently takes them 50 seconds. That's who this is for.

And if you want to talk about what AI could do for your business, not in theory, but in your workflows, with your team, on your timeline, reach out at dean@bridgeaiconsulting.com. That's what we're here for.

Dean

Founder & CEO, Bridge AI Consulting

[bridgeaiconsulting.com](https://www.bridgeaiconsulting.com)

**REFERRAL PROGRAM**

Know a business that could use AI? Refer them to Bridge AI and earn 10% of their first year of payments. Get in touch at dean@bridgeaiconsulting.com to get started.

---

**Notes for Dean**

- **Uber numbers:** the four rides, ~500 Eats orders and 50/90-second booking times come from TechCrunch's Nov 4 write-up of the earnings call. A side search turned up conflicting attributions (CFO vs. IR) and a disputed total-trips figure, so I left the total out and attributed only the CEO quote. Worth a glance at the official transcript before sending.
- **Spending figures:** Ramp numbers (1.5%, 42%, $12 to $15 median, $600 to $1,000 top 10%), the ~$600M Anthropic price-cut figure, and Apple's $300/$200/$100/$25 caps all come via TechCrunch (Nov 4 and Nov 6), citing Ramp, Anthropic's filing and Bloomberg. I couldn't open the SEC filing itself (too large to fetch), so the S-1/A quotes are TechCrunch's.
- **OpenAI story:** TechCrunch's model naming is inconsistent and I couldn't confirm its Linux (948) and Firefox (81) bug counts elsewhere, so I left them out. All three news links are TechCrunch; I couldn't reach OpenAI's site or find a Censys post to link as primary sources.
- **Your story slot:** if a client has a "we automated the wrong thing" moment, or a long task Claude cut down to minutes, it would land well right before "Now for the business part."
- **Deep Dive image:** a simple two-bar chart, "Uber rides booked by AI agents, Halloween week: 4" next to a dollar-sign bar labeled "Ramp: token spend growth, Aug to Sep: 1.5%," or a phone screenshot style graphic with a stopwatch at 0:50.
