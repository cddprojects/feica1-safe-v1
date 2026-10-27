#!/usr/bin/env python3
"""Render the North Desk static site."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "site"
EMAIL = "desk@northdesk.ca"
THEME = "#243552"

LOGO = (
    '<svg viewBox="0 0 32 32" aria-hidden="true">'
    '<rect width="32" height="32" rx="8" fill="oklch(32% .06 255)"/>'
    '<path d="M8 21.5h16M10 21.5v2.2M22 21.5v2.2" stroke="oklch(97% .01 95)" '
    'stroke-width="1.8" fill="none" stroke-linecap="round"/>'
    '<rect x="10" y="8" width="12" height="9" rx="1.4" fill="none" '
    'stroke="oklch(89% .11 85)" stroke-width="1.7"/>'
    "</svg>"
)

NAV = [
    ("index.html", "Home"),
    ("reading.html", "Reading"),
    ("work-types.html", "Work types"),
    ("services.html", "What we publish"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
]


def brand():
    return f'<a class="brand" href="index.html">{LOGO}North<em>Desk</em></a>'


def header(current):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap nav">
{brand()}
<button class="menu-btn" aria-expanded="false" aria-controls="nav-list" aria-label="Open menu"><span class="bars" aria-hidden="true"></span></button>
<ul id="nav-list">{''.join(items)}</ul>
</div></header>"""


def footer():
    return f"""<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div>{brand()}
<p style="margin-top:1rem;max-width:36ch">An independent Canadian publisher on online, remote and flexible work, and on the recruitment process around it.</p></div>
<div><h4>Reading</h4><ul>
<li><a href="reading.html">All articles</a></li>
<li><a href="work-types.html">Work types</a></li>
<li><a href="scam-check.html">Scam check</a></li>
<li><a href="glossary.html">Glossary</a></li>
<li><a href="faq.html">FAQ</a></li>
</ul></div>
<div><h4>Publisher</h4><ul>
<li><a href="about.html">About</a></li>
<li><a href="services.html">What we publish</a></li>
<li><a href="contact.html">Contact</a></li>
<li><a href="privacy.html">Privacy</a></li>
<li><a href="disclaimer.html">Disclaimer</a></li>
</ul></div>
</div>
<div class="legal"><p>North Desk is an independent publisher. We are not Job Bank, Statistics Canada, or a provincial employment service, and we are not a licensed employment agency. We do not recruit, screen, place or introduce candidates, and we do not publish vacancies. Guides are general information, not legal, tax or employment advice. Confirm pay and workplace rules where the work is done. Job scam reports: Canadian Anti-Fraud Centre, <strong>1-888-495-8501</strong>.</p>
<p>&copy; 2026 North Desk &middot; Canada &middot; <a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
</div></footer>
<script src="js/main.js"></script>"""


def page(filename, title, description, current, main, robots=""):
    robot = f'\n<meta name="robots" content="{robots}">' if robots else ""
    return f"""<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="{THEME}">{robot}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..800&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css">
</head>
<body>
{header(current)}
<main id="main">
{main}
</main>
{footer()}
</body>
</html>
"""


def article(eyebrow, h1, lede, body, reviewed="October 2026"):
    return f"""<div class="page-head"><div class="wrap"><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1></div></div>
<section style="padding-top:2rem"><div class="wrap article">
<p class="byline">North Desk &middot; Last reviewed {reviewed}</p>
<p class="lede">{lede}</p>
{body}
<p style="margin-top:2.5rem"><a href="reading.html">&larr; All articles</a></p>
</div></section>"""


PAGES = {}

PAGES["index.html"] = page(
    "index.html",
    "Online, remote and flexible work in Canada | North Desk",
    "North Desk is an independent Canadian publisher on online jobs, remote roles and flexible arrangements, and on how recruitment for that work usually proceeds.",
    "index.html",
    f"""
<section class="hero"><div class="wrap hero-grid">
<div>
<span class="eyebrow">A publisher on remote work in Canada</span>
<h1>How online, remote and flexible hiring actually works.</h1>
<p class="lede">North Desk explains the recruitment around work you can do online, away from an employer’s office, or on hours you can move. We are an independent publisher. We do not post vacancies, and we do not place people.</p>
<div class="btn-row"><a class="btn btn-primary" href="reading.html">Read the desk</a><a class="btn btn-ghost" href="work-types.html">Three kinds of work</a></div>
</div>
<div class="modes">
<h2>The only work we cover</h2>
<a class="mode" href="remote-work-canada.html"><span class="dot"></span><span><b>Remote</b><small>The seat is not the employer’s office. Hybrid is a different agreement.</small></span><span class="tag">Place</span></a>
<a class="mode" href="online-work-canada.html"><span class="dot"></span><span><b>Online</b><small>The work product moves over the internet. The label alone is not a location.</small></span><span class="tag">Channel</span></a>
<a class="mode" href="flexible-work-canada.html"><span class="dot"></span><span><b>Flexible</b><small>Hours or load can move. It is still a contract, with a province attached.</small></span><span class="tag">Hours</span></a>
</div>
</div></section>

<section class="alt"><div class="wrap">
<div class="head reveal"><span class="eyebrow">From the desk</span><h2>Four things readers mix up.</h2></div>
<ol class="shifts">
<li class="reveal"><span class="no">01</span><h3>Place</h3><p>Remote, hybrid and on-site are different. A search for “work from home” still returns office jobs.</p></li>
<li class="reveal"><span class="no">02</span><h3>Channel</h3><p>Online describes how the work is delivered. It does not say you can live anywhere.</p></li>
<li class="reveal"><span class="no">03</span><h3>Hours</h3><p>Flexible means the schedule can move. In the national survey, part-time is usually under 30 hours a week.</p></li>
<li class="reveal"><span class="no">04</span><h3>The contract</h3><p>Employee or contractor, and the province where you actually work, decide pay rules and deductions.</p></li>
</ol>
<p class="src-note">We read Statistics Canada, Job Bank and the Canadian Anti-Fraud Centre, then write in plain language. Figures are dated in each article.</p>
</div></section>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">Latest</span><h2>Start with the ad in front of you.</h2></div>
<div class="posts">
<article class="post reveal"><div class="meta"><span class="cat">How hiring works</span><span>7 min</span></div><h3><a href="article-read-a-remote-ad.html">How to read a remote job ad in Canada</a></h3><p>City, pay, “remote” and “to be negotiated” each mean a specific thing. Here is the order to read them.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Work types</span><span>6 min</span></div><h3><a href="article-three-arrangements.html">Online, remote and flexible are three different agreements</a></h3><p>People search them as one idea. Employers write them as three. The gap is where bad offers hide.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">The market</span><span>6 min</span></div><h3><a href="article-what-vacancies-mean.html">What Canada’s vacancy numbers do not say about remote work</a></h3><p>Half a million vacancies is the whole economy. Remote postings on Job Bank are a thin slice of that.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Scams</span><span>6 min</span></div><h3><a href="article-remote-scams.html">Remote-job scams reported in Canada</a></h3><p>Task apps, fake balances and a fee to unlock the next shift. The Anti-Fraud Centre already has the list.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Applications</span><span>5 min</span></div><h3><a href="article-remote-cv.html">A CV for online and remote recruitment</a></h3><p>A remote employer cannot watch you work. The page has to show that you deliver without a desk beside theirs.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Pay</span><span>7 min</span></div><h3><a href="article-pay-and-province.html">Pay, province and a remote contract</a></h3><p>The rules follow where you do the work, with a federal exception. Ontario and B.C. also expect pay in the ad.</p></article>
</div>
</div></section>

<section class="alt" id="recruitment"><div class="wrap split">
<div class="reveal"><span class="eyebrow">Recruitment, explained</span><h2>What a careful remote hire looks like.</h2></div>
<div class="reveal">
<p class="lede">Recruitment for this work is still a sequence: a real organisation, a written role, a conversation, then an offer. North Desk publishes that sequence so you can compare it with the message in your inbox.</p>
<ol class="note-list">
<li>You apply on the employer’s own site or on a board such as Job Bank. You do not pay to be considered.</li>
<li>Someone who works at that organisation interviews you. The equipment, hours, time zone and place are in writing.</li>
<li>Pay is stated as an amount or a range. In Ontario and British Columbia, many public ads must show it.</li>
<li>You can decline. Nothing about your bank account, crypto wallet or a private app is required in order to “unlock” the job.</li>
</ol>
<p><a href="services.html">What this publisher does &rarr;</a></p>
</div>
</div></section>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">Work types</span><h2>Three guides. Nothing else.</h2></div>
<div class="minis">
<a class="mini reveal" href="remote-work-canada.html"><b>Remote</b><span>Place is flexible. Hybrid is named separately.</span></a>
<a class="mini reveal" href="online-work-canada.html"><b>Online</b><span>The work travels by internet.</span></a>
<a class="mini reveal" href="flexible-work-canada.html"><b>Flexible</b><span>Hours or load can move.</span></a>
<a class="mini reveal" href="scam-check.html"><b>Scam check</b><span>A short list before you reply.</span></a>
</div>
</div></section>

<section class="alt" id="contact"><div class="wrap split">
<div><span class="eyebrow">Write to the desk</span><h2>A correction, or a remote ad you want explained.</h2><p class="lede">We read messages and use them to decide what to publish next. Do not send identification, banking details or copies of a suspicious app.</p></div>
<div>
<form id="contact-form" class="form" novalidate>
<div class="field"><label for="name">Name</label><input id="name" required autocomplete="name"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">Email</label><input id="email" type="email" required autocomplete="email"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="province">Province or territory</label><select id="province"><option value="">Prefer not to say</option><option>Alberta</option><option>British Columbia</option><option>Manitoba</option><option>New Brunswick</option><option>Newfoundland and Labrador</option><option>Northwest Territories</option><option>Nova Scotia</option><option>Nunavut</option><option>Ontario</option><option>Prince Edward Island</option><option>Quebec</option><option>Saskatchewan</option><option>Yukon</option><option>Outside Canada</option></select></div>
<div class="field"><label for="topic">Topic</label><select id="topic"><option>A remote job ad</option><option>Online work</option><option>A flexible arrangement</option><option>A possible scam</option><option>A correction</option><option>A story idea</option></select></div>
<div class="field"><label for="msg">Message</label><textarea id="msg" required></textarea><div class="err" aria-live="polite"></div></div>
<button class="btn btn-primary" type="submit">Write to North Desk</button>
<p class="notice">This opens your email app, addressed to {EMAIL}. We do not store the form on a server.</p>
</form>
<div id="form-ok" class="ok" hidden tabindex="-1" role="status"><h3>Your email app should be open.</h3><p>Send the message from there when you are ready.</p><p class="ok-sub">If nothing opened, write to {EMAIL}.</p></div>
</div>
</div></section>
""",
)

PAGES["reading.html"] = page(
    "reading.html",
    "Reading | North Desk",
    "Articles from North Desk on online, remote and flexible work in Canada, and on the recruitment process around that work.",
    "reading.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Reading</span><h1>The desk, in order.</h1><p class="lede">Every piece stays inside online, remote and flexible work. We do not cover on-site retail, trades or care shifts.</p></div></div>
<section><div class="wrap">
<div class="filters" role="group" aria-label="Filter articles">
<button class="chip" type="button" data-filter="all" aria-pressed="true">All</button>
<button class="chip" type="button" data-filter="hiring" aria-pressed="false">Hiring</button>
<button class="chip" type="button" data-filter="market" aria-pressed="false">Market</button>
<button class="chip" type="button" data-filter="pay" aria-pressed="false">Pay</button>
<button class="chip" type="button" data-filter="scams" aria-pressed="false">Scams</button>
</div>
<div class="posts">
<article class="post" data-cat="hiring"><div class="meta"><span class="cat">How hiring works</span><span>7 min</span></div><h3><a href="article-read-a-remote-ad.html">How to read a remote job ad in Canada</a></h3><p>The fields a Canadian posting actually contains, and the ones a pitch invents.</p></article>
<article class="post" data-cat="hiring"><div class="meta"><span class="cat">Work types</span><span>6 min</span></div><h3><a href="article-three-arrangements.html">Online, remote and flexible are three different agreements</a></h3><p>Place, channel and hours. Read the contract for each one.</p></article>
<article class="post" data-cat="market"><div class="meta"><span class="cat">The market</span><span>6 min</span></div><h3><a href="article-what-vacancies-mean.html">What Canada’s vacancy numbers do not say about remote work</a></h3><p>Why a national vacancy total is the wrong headline for a remote search.</p></article>
<article class="post" data-cat="scams"><div class="meta"><span class="cat">Scams</span><span>6 min</span></div><h3><a href="article-remote-scams.html">Remote-job scams reported in Canada</a></h3><p>The schemes the Canadian Anti-Fraud Centre describes, in the order they usually unfold.</p></article>
<article class="post" data-cat="hiring"><div class="meta"><span class="cat">Applications</span><span>5 min</span></div><h3><a href="article-remote-cv.html">A CV for online and remote recruitment</a></h3><p>What a remote recruiter can actually see, and what to leave off.</p></article>
<article class="post" data-cat="pay"><div class="meta"><span class="cat">Pay</span><span>7 min</span></div><h3><a href="article-pay-and-province.html">Pay, province and a remote contract</a></h3><p>Which rulebook applies when the company is in one province and you are in another.</p></article>
</div>
</div></section>
""",
)

PAGES["work-types.html"] = page(
    "work-types.html",
    "Online, remote and flexible work | North Desk",
    "Three guides from North Desk: remote work, online work and flexible arrangements in Canada.",
    "work-types.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Work types</span><h1>Three arrangements. We stop there.</h1><p class="lede">North Desk covers work that is online, remote, or flexible in its hours. On-site shifts, even well-paid ones, are outside this desk.</p></div></div>
<section><div class="wrap">
<div class="types">
<article class="type"><div><span class="n">01 · Place</span><h3><a href="remote-work-canada.html">Remote</a></h3></div><div><p>You are not required to sit in the employer’s office. The ad should say whether that means anywhere in a province, anywhere in Canada, or a hybrid split. Job Bank files this under a remote filter, separate from a keyword search.</p><p><a href="remote-work-canada.html">Read the guide</a></p></div></article>
<article class="type"><div><span class="n">02 · Channel</span><h3><a href="online-work-canada.html">Online</a></h3></div><div><p>The tasks and the deliverable move over the internet: support, writing, design, bookkeeping, tutoring, moderation, software. Online does not promise a home office. Ask where the contract says you must be.</p><p><a href="online-work-canada.html">Read the guide</a></p></div></article>
<article class="type"><div><span class="n">03 · Hours</span><h3><a href="flexible-work-canada.html">Flexible</a></h3></div><div><p>The week can move: chosen hours, a project deadline, or a part-time load. Statistics Canada counts part-time as usually under 30 hours a week. Flexible is not a promise of income, and it is not permission to skip the contract.</p><p><a href="flexible-work-canada.html">Read the guide</a></p></div></article>
</div>
<p class="src-note">Current openings, when you want them, are on <a href="https://www.jobbank.gc.ca/findajob" rel="noopener">Job Bank</a>. Use the remote filter rather than the words “work from home” alone.</p>
</div></section>
""",
)

PAGES["remote-work-canada.html"] = page(
    "remote-work-canada.html",
    "Remote work in Canada | North Desk",
    "What a remote role in Canada is: place, province, hybrid versus fully remote, and how recruitment for it usually runs.",
    "work-types.html",
    """
<div class="page-head jobhero jh1"><div class="wrap jh-grid">
<div><span class="eyebrow">Place</span><h1>Remote work in Canada</h1><p class="lede">Remote means the job is not tied to the employer’s office. It still has a province, a time zone and a payer.</p></div>
<aside class="qf"><h2>At a glance</h2><dl>
<dt>Place</dt><dd>Not the employer’s office. Hybrid is a named split, not “remote”.</dd>
<dt>Hours</dt><dd>Often full-time. Part-time in the national survey is usually under 30 hours.</dd>
<dt>Recruitment</dt><dd>Apply, interview, written offer. No fee to start.</dd>
<dt>Where to look</dt><dd>Job Bank’s remote filter, and the employer’s own careers page.</dd>
</dl><p class="rv">Reviewed October 2026. Not a vacancy.</p></aside>
</div></div>
<section><div class="wrap article">
<h2>What the word is doing</h2>
<p>On Job Bank and Indeed, a posting is marked on-site, hybrid or remote. Those are three agreements. Hybrid means some days in a stated place. Remote means you are not required to report to the office. A keyword search for “work from home” is not the same as the remote filter: it also returns on-site jobs that mention a home somewhere in the text.</p>
<p>Indeed’s own posting rules tell employers to use “Canada” or “nationwide” only when the person can do the work from anywhere in the country. Many so-called remote roles still say “must reside in Ontario” or “must be in a Canadian time zone.” That line is the real location.</p>
<h2>How recruitment usually runs</h2>
<p>A careful employer posts the role, takes applications, and has someone from the organisation speak with you. The offer names the pay, the hours, who employs you, and where you are allowed to work from. You are not asked to buy a starter kit, load a private task app, or move money through your account.</p>
<p>North Desk does not carry those postings. When you want live ads, open <a href="https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=remote" rel="noopener">Job Bank</a> and filter for remote.</p>
<h2>What to ask before you agree</h2>
<ul>
<li>Which provinces may I work from, and what happens if I move?</li>
<li>Is any day in an office required? If yes, it is hybrid.</li>
<li>Who employs me, and is the pay hourly, salary, or per project?</li>
<li>Which time zone are meetings in?</li>
<li>Who provides the computer and software?</li>
</ul>
<p>Pay rules are covered in <a href="article-pay-and-province.html">Pay, province and a remote contract</a>. How to read the ad itself is in <a href="article-read-a-remote-ad.html">How to read a remote job ad</a>.</p>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www.jobbank.gc.ca/findajob" rel="noopener">Job Bank: find a job</a></li>
<li><a href="https://ca.indeed.com/" rel="noopener">Indeed Canada</a></li>
</ul>
</div></section>
""",
)

PAGES["online-work-canada.html"] = page(
    "online-work-canada.html",
    "Online work in Canada | North Desk",
    "What online work means in Canada: internet-delivered tasks, employee versus contract, and how to tell a role from a task-app pitch.",
    "work-types.html",
    """
<div class="page-head jobhero jh2"><div class="wrap jh-grid">
<div><span class="eyebrow">Channel</span><h1>Online work in Canada</h1><p class="lede">Online means the work moves over the internet. It is a way of delivering the job, not a promise that you can do it from any kitchen table.</p></div>
<aside class="qf"><h2>At a glance</h2><dl>
<dt>Typical tasks</dt><dd>Support, writing, design, bookkeeping, tutoring, moderation, software.</dd>
<dt>Status</dt><dd>Employee or independent contractor. The label on the ad is not the legal test.</dd>
<dt>Pay</dt><dd>Hourly, salary, or per project. Never a fee you pay first.</dd>
<dt>Watch for</dt><dd>Simple “tasks” inside an app, with a balance you cannot withdraw.</dd>
</dl><p class="rv">Reviewed October 2026. Not a vacancy.</p></aside>
</div></div>
<section><div class="wrap article">
<h2>Online is not the same word as remote</h2>
<p>A person can do online work in an office. A person can also do remote work that is not “online” in the casual sense, such as a phone roster with set shifts. When North Desk says online, we mean the deliverable travels by internet and the seat is not an employer’s floor. If the ad also requires a city, read it as a location rule, not as a mood.</p>
<h2>Employee or contractor</h2>
<p>Some online work is employment: a schedule, a manager, a pay stub, Canada Pension Plan and Employment Insurance when the rules say so. Some is contract work: you invoice, you carry the risk of a quiet month, and you handle your own tax. The Canada Revenue Agency looks at control, tools, financial risk and the chance of profit. Calling it freelance in the posting does not decide the question. Confirm with CRA if the status is unclear. This page is not tax advice.</p>
<h2>Recruitment versus a task feed</h2>
<p>Recruitment ends with an organisation you can phone and a written description of the work. A task feed starts with a message, an app, and a balance on a screen. The Canadian Anti-Fraud Centre describes the second pattern under crypto job fraud, product boosting, web surveys and fake online-store jobs. Read <a href="article-remote-scams.html">the scam briefing</a> before you install anything.</p>
<p>Software development is one occupation where online delivery is common, and where vacancies rose. In the second quarter of 2026, Statistics Canada counted 3,545 vacancies for software developers and programmers, up about 35 per cent on the year, with an average offered wage of $43.65 an hour. That is the wage on empty jobs in that occupation. It is not a remote salary, and it is not an offer.</p>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www150.statcan.gc.ca/n1/daily-quotidien/260915/t002a-eng.htm" rel="noopener">Statistics Canada: occupations with the largest vacancy increases, Q2 2026</a></li>
<li><a href="https://antifraudcentre.ca/scams-fraudes/job-emploi-eng.htm" rel="noopener">Canadian Anti-Fraud Centre: job fraud</a></li>
</ul>
</div></section>
""",
)

PAGES["flexible-work-canada.html"] = page(
    "flexible-work-canada.html",
    "Flexible online and remote work in Canada | North Desk",
    "Flexible hours and flexible load for online and remote work in Canada, including what part-time means in the Labour Force Survey.",
    "work-types.html",
    """
<div class="page-head jobhero jh3"><div class="wrap jh-grid">
<div><span class="eyebrow">Hours</span><h1>Flexible work, when it is also online or remote</h1><p class="lede">Flexible means the hours or the load can move. On this desk it always sits inside online or remote work. A flexible Saturday on a shop floor is someone else’s beat.</p></div>
<aside class="qf"><h2>At a glance</h2><dl>
<dt>Part-time</dt><dd>Usually under 30 hours a week, in Statistics Canada’s survey.</dd>
<dt>Shapes</dt><dd>Chosen hours, a shorter week, or a project with a deadline.</dd>
<dt>Not included</dt><dd>On-site casual shifts, even if the hours are short.</dd>
<dt>Pay</dt><dd>Depends on the role. Nothing here guarantees an amount.</dd>
</dl><p class="rv">Reviewed October 2026. Not a vacancy.</p></aside>
</div></div>
<section><div class="wrap article">
<h2>What flexible is allowed to mean here</h2>
<p>Readers use flexible for three different hopes: fewer hours, hours they pick, or freedom from a building. We keep the third one under <a href="remote-work-canada.html">remote</a>. This guide is about hours and load, for work that is already online or remote.</p>
<p>In the Labour Force Survey, part-time means you usually work less than 30 hours a week at your main job. That is a statistical line. It is not the overtime threshold in your province. A flexible remote role can still be full-time.</p>
<h2>How it shows up in recruitment</h2>
<p>A serious posting says the weekly hours or the deadline, the time zone, and whether the schedule is yours to set or theirs to roster. “Work whenever you want” with no hours, no deliverable and a promised daily amount is a slogan. Compare it with <a href="article-read-a-remote-ad.html">how to read a remote ad</a>.</p>
<p>Self-employment, which includes a lot of flexible online contract work, was up 51,000 people (+1.9 per cent) in the year to September 2026, and down 23,000 in that month alone. A flexible month can be a quiet month. Plan for that before you treat contract work as a wage.</p>
<h2>There is no single national request form</h2>
<p>If you already have an employer and want different hours, the process depends on the province, the contract, and whether the employer is federally regulated. Canada does not have one national flexible-work request with a fixed reply time. Ask in writing, describe the hours, and keep their answer. Do not assume a guideline you read for another country applies here.</p>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www150.statcan.gc.ca/n1/daily-quotidien/261009/dq261009a-eng.htm" rel="noopener">Statistics Canada: Labour Force Survey, September 2026</a></li>
</ul>
</div></section>
""",
)

PAGES["article-read-a-remote-ad.html"] = page(
    "article-read-a-remote-ad.html",
    "How to read a remote job ad in Canada | North Desk",
    "A field-by-field reading of Canadian remote, online and flexible job ads, including pay transparency in Ontario and British Columbia.",
    "reading.html",
    article(
        "How hiring works",
        "How to read a remote job ad in Canada",
        "A Canadian posting is a short record. Read it in order, and stop when a field is missing or invented.",
        """
<div class="takeaways"><h2>Read in this order</h2><ul>
<li>Who is hiring, and can you find that name on a website you looked up yourself?</li>
<li>Where may the work be done: remote, hybrid, or a named province?</li>
<li>What is the pay: an amount, a range, or the phrase “to be negotiated”?</li>
<li>What are the hours, the time zone, and the employment status?</li>
<li>Is anyone asking you to pay, install an app, or move money?</li>
</ul></div>
<h2>The fields a real card has</h2>
<p>Job Bank and Indeed cards carry a title, an employer, a place written as a city and province, pay by the hour or the year, a work-site label (on-site, hybrid or remote), and a date. Sometimes the wage says “to be negotiated.” That is an absence of a number, not a high number.</p>
<p>Remote ads add a constraint the office ads hide in the address: who is allowed to apply from where. “Remote — Canada” and “remote — must live in British Columbia” are different jobs. Indeed tells employers not to post a nationwide location unless people anywhere in the country can do the work.</p>
<h2>Pay on the ad</h2>
<p>British Columbia has required compensation information in public job postings since 1 November 2023. Ontario, from 1 January 2026, requires many employers with at least 25 employees to include the expected compensation or a range, to say whether they use artificial intelligence to screen applicants, and to say whether a vacancy exists. A posted range in Ontario cannot span more than $50,000 a year, and roles above $200,000 a year are exempt. The range is not a promise that you will be offered that pay. Canadian experience cannot be required in those Ontario postings or their application forms.</p>
<p>Indeed’s hiring lab measured the Ontario change: pay appeared on 49 per cent of Ontario postings just before the rule, and on 71 per cent by June 2026. Most of those were ranges.</p>
<h2>What does not belong on the card</h2>
<p>A fee to apply, a request to buy equipment from a link they send, a private messaging app as the only interview, or a balance you can see and cannot withdraw. Those are described on the <a href="article-remote-scams.html">scam briefing</a>. You can also run the <a href="scam-check.html">scam check</a> before you answer.</p>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www.ontario.ca/document/your-guide-employment-standards-act-0/requirements-related-publicly-advertised-job" rel="noopener">Ontario: requirements for publicly advertised job postings</a></li>
<li><a href="https://hiringlab.indeed.com/en-ca/2026/07/23/growth-in-canadian-salary-transparency-driven-by-two-provinces/" rel="noopener">Indeed Hiring Lab Canada, 23 July 2026</a></li>
<li><a href="https://www.jobbank.gc.ca/findajob" rel="noopener">Job Bank</a></li>
</ul>
""",
    ),
)

PAGES["article-three-arrangements.html"] = page(
    "article-three-arrangements.html",
    "Online, remote and flexible are three agreements | North Desk",
    "Why online, remote and flexible work in Canada should be read as place, channel and hours, not as one job title.",
    "reading.html",
    article(
        "Work types",
        "Online, remote and flexible are three different agreements",
        "Search boxes treat the three words as synonyms. Contracts do not.",
        """
<div class="takeaways"><h2>Keep them apart</h2><ul>
<li>Remote is a place rule.</li>
<li>Online is how the work travels.</li>
<li>Flexible is an hours or load rule.</li>
<li>A role can be one of these, or all three. The ad should say which.</li>
</ul></div>
<h2>Place</h2>
<p>Remote work is not performed at the employer’s office. Hybrid work is partly there. If the message says remote and then names three office days, believe the office days. Guides: <a href="remote-work-canada.html">remote</a>.</p>
<h2>Channel</h2>
<p>Online work is delivered over the internet. It can be remote, or it can be a seat in a building with a headset. When a pitch says only “online job,” ask for the place rule in writing. Guide: <a href="online-work-canada.html">online</a>.</p>
<h2>Hours</h2>
<p>Flexible work lets the week move. Statistics Canada’s part-time line is usually under 30 hours at the main job. A flexible arrangement can still be full-time, and a short week can still be poorly paid. Guide: <a href="flexible-work-canada.html">flexible</a>.</p>
<h2>Why the mix-up matters in recruitment</h2>
<p>Unclear ads attract the wrong people, and vague pitches borrow all three words at once: online, remote, flexible, high daily pay, no experience. A recruitable role can say which of the three it is in a sentence. If it cannot, you do not yet have a role. You have a description. Read <a href="article-read-a-remote-ad.html">the field order</a> next.</p>
""",
    ),
)

PAGES["article-what-vacancies-mean.html"] = page(
    "article-what-vacancies-mean.html",
    "What vacancy numbers do not say about remote work | North Desk",
    "Canada had 510,200 job vacancies in Q2 2026. That figure is the whole labour market, not the remote, online or flexible slice North Desk covers.",
    "reading.html",
    article(
        "The market",
        "What Canada’s vacancy numbers do not say about remote work",
        "The national vacancy total is real. It is also the wrong headline for a remote search.",
        """
<div class="statrow">
<div class="stat"><b>510,200</b><span>job vacancies, all industries, second quarter of 2026</span></div>
<div class="stat"><b>2.8%</b><span>vacancy rate, unchanged on the year</span></div>
<div class="stat"><b>3.0</b><span>unemployed people for every vacancy</span></div>
<div class="stat"><b>6.5%</b><span>unemployment rate, September 2026</span></div>
</div>
<h2>The survey is the whole economy</h2>
<p>Statistics Canada’s Job Vacancy and Wage Survey counted 510,200 vacancies in the second quarter of 2026. The vacancy rate was 2.8 per cent. There were 3.0 unemployed people for every vacancy. In September 2026 the Labour Force Survey put unemployment at 6.5 per cent, after employment fell by 68,000 in the month. The share of people who had been unemployed in August and had a job in September was 30.6 per cent, below the 2017–2019 average of 36.5 per cent.</p>
<p>Those numbers describe offices, shops, trucks, kitchens, clinics and job sites together. They do not describe a remote market. Health care, construction, trucking, retail and food service dominate what Job Bank calls in demand. Most of that work is on a floor, a ward or a road. North Desk does not recruit for it and does not write guides for it.</p>
<h2>Remote is a thin slice of the board</h2>
<p>Job Bank’s home page, when we read it in October 2026, invited people to search on the order of 84,000 postings. A browse page the same month showed on the order of 700 marked remote. Both counts move every day. The useful point is the ratio, not the exact tally: remote is a filter inside a much larger board, not the board itself.</p>
<p>A search for the words “work from home” is looser still. It returns hybrid and on-site ads. Use the remote filter if remote is the condition you need.</p>
<h2>One occupation that can be done online</h2>
<p>Software developers and programmers had 3,545 vacancies in that quarter, up about 35 per cent on the year, with an average offered hourly wage of $43.65. Offered wages are what employers advertised for empty jobs. They are lower, in the aggregate, than the $37.64 average hourly wage of people already employed in September. Do not read $43.65 as the going remote rate in Canada.</p>
<h2>How to use the numbers</h2>
<p>Use them to stay calm. A cooler national market means a remote application can take time, and a message promising fast daily pay is not “the market.” Use Job Bank when you want ads. Use these articles when you want to know what an ad is allowed to mean.</p>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www150.statcan.gc.ca/n1/daily-quotidien/260915/dq260915a-eng.htm" rel="noopener">Statistics Canada: job vacancies, second quarter 2026</a></li>
<li><a href="https://www150.statcan.gc.ca/n1/daily-quotidien/261009/dq261009a-eng.htm" rel="noopener">Statistics Canada: Labour Force Survey, September 2026</a></li>
<li><a href="https://www.jobbank.gc.ca/career-planning/resources/in-demand-sectors" rel="noopener">Job Bank: in-demand sectors</a></li>
</ul>
""",
    ),
)

PAGES["article-remote-scams.html"] = page(
    "article-remote-scams.html",
    "Remote-job scams reported in Canada | North Desk",
    "Job scams aimed at people looking for online, remote and flexible work, as described by the Canadian Anti-Fraud Centre.",
    "reading.html",
    article(
        "Scams",
        "Remote-job scams reported in Canada",
        "The pitches aimed at people who want online or remote work are already catalogued. They start friendly and end with a payment you cannot reverse.",
        """
<div class="takeaways"><h2>Stop if you see this</h2><ul>
<li>A job you did not apply for, especially by text or messaging app.</li>
<li>A fee, a deposit, or an “unlock” payment.</li>
<li>An app or a platform you must install before you know the employer.</li>
<li>A balance on a screen that you cannot withdraw.</li>
<li>A request to receive money and send it onward.</li>
</ul></div>
<h2>What the Anti-Fraud Centre describes</h2>
<p>The Canadian Anti-Fraud Centre says many frauds target people who are looking for work. The versions that dress up as online, remote or flexible jobs include crypto “product boosting,” simple online tasks, web surveys, and fake e-commerce store jobs. A small first payment is part of the script. Then the platform asks for a deposit to reach a higher commission. The balance you can see is not money you can take out.</p>
<p>Other versions send a cheque and ask you to forward part of it, or recruit you as a “financial agent” so that transfers land in your account and leave as cryptocurrency. The Centre warns that you can be treated as a money mule. Mystery-shopper and car-wrapping notes work the same way: a cheque, a task that looks small, and a loss when the cheque fails.</p>
<p>Pyramid-style recruiting, where you are paid to bring in other people rather than for the work, is a criminal offence in Canada. The Centre says so directly.</p>
<h2>Warning signs, in their words</h2>
<ul>
<li>A webmail address instead of a company domain.</li>
<li>An offer you did not apply for.</li>
<li>A request to join a platform, download software, or do simple tasks for fast money.</li>
<li>Upfront deposits, upgrade fees, or unlock payments.</li>
<li>High pay for very little work.</li>
</ul>
<h2>What to do</h2>
<p>Wait. Find the organisation’s phone number on its own website and call that. Do not send identification to an unverified contact. Report to local police and to the Canadian Anti-Fraud Centre at 1-888-495-8501, or through the <a href="https://antifraudcentre.ca/scams-fraudes/job-emploi-eng.htm" rel="noopener">job fraud page</a>. The CRTC points to the same number for recruitment texts offering part-time remote work at high wages.</p>
<p>If you want a private pass over a message before you reply, use the <a href="scam-check.html">scam check</a>. It stays in your browser.</p>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://antifraudcentre.ca/scams-fraudes/job-emploi-eng.htm" rel="noopener">Canadian Anti-Fraud Centre: job fraud</a></li>
<li><a href="https://www.crtc.gc.ca/eng/phone/telemarketing/cust.htm" rel="noopener">CRTC: scam alerts, including employment recruitment</a></li>
</ul>
""",
    ),
)

PAGES["article-remote-cv.html"] = page(
    "article-remote-cv.html",
    "A CV for online and remote recruitment | North Desk",
    "What to show on a CV when the recruiter will never see you at a desk: delivery, tools, writing, and time zone.",
    "reading.html",
    article(
        "Applications",
        "A CV for online and remote recruitment",
        "A remote recruiter cannot watch you work. The page has to show that the work arrived anyway.",
        """
<div class="takeaways"><h2>Put these where they can be seen</h2><ul>
<li>A result you finished without someone standing next to you.</li>
<li>The tools you used, named plainly.</li>
<li>Proof you can write: a short summary is the sample.</li>
<li>Your time zone and the provinces you can work from.</li>
</ul></div>
<h2>What recruitment is trying to learn</h2>
<p>For an office role, a CV can lean on presence. For online and remote roles, the open question is whether the work gets done when nobody can see the chair. Write one line per role that names the output: a queue you cleared, a report you shipped, a class you taught, a release you maintained. Hours you are willing to overlap with a team belong in the header, next to the city and province.</p>
<h2>What to leave off</h2>
<p>Do not invent a remote title you did not hold. Do not list a daily earnings target. Do not attach identification, a social insurance number, or banking details to an application. A real recruiter does not need those to decide whether to speak with you.</p>
<p>If the only “interview” is inside an app you have never heard of, stop and read <a href="article-remote-scams.html">the scam briefing</a>. Recruitment can be remote. It still names the company.</p>
<h2>A short test before you send it</h2>
<p>Can a stranger tell what you delivered, on what tools, in which time zone, in under a minute? If the page is a list of duties copied from an old posting, rewrite the duties as outcomes. Then apply on the employer’s site or on Job Bank, not through a link in an unsolicited text.</p>
""",
    ),
)

PAGES["article-pay-and-province.html"] = page(
    "article-pay-and-province.html",
    "Pay, province and a remote contract | North Desk",
    "Which pay rules apply to online and remote work in Canada, including the federal minimum wage and provincial posting rules.",
    "reading.html",
    article(
        "Pay",
        "Pay, province and a remote contract",
        "A remote job still happens in a place. That place, and the kind of employer, decide which pay rules you open.",
        """
<div class="takeaways"><h2>The short version</h2><ul>
<li>For most employers, workplace rules follow the province or territory where you do the work.</li>
<li>Banks, airlines, telecoms and interprovincial transport follow the Canada Labour Code.</li>
<li>The federal minimum wage is $18.15 an hour from 1 April 2026, and the provincial rate applies instead when it is higher.</li>
<li>A wage printed in an ad is information. It is not yet your offer.</li>
</ul></div>
<h2>There is no single Canadian minimum for a laptop job</h2>
<p>Minimum wage is set province by province, with a separate federal rate for federally regulated employees. From 1 April 2026 the federal rate is $18.15 an hour. If your province’s general rate is higher, that higher rate is the one a federally regulated employer must meet. Everyone else’s floor is the provincial one. Alberta’s general rate is still $15. British Columbia’s is $18.25 from 1 June 2026. Ontario’s is $17.95 from 1 October 2026. Quebec’s is $16.60 from 1 May 2026. Confirm the current figure on the <a href="https://minwage-salairemin.service.canada.ca/en/general.html" rel="noopener">federal minimum wage database</a> and on your province’s site before you rely on a list, including ours.</p>
<p>Some jobs have different floors: students, piece rates, and in British Columbia the engaged-time rate for ride-hail and delivery platform workers. If your “flexible online” offer is actually app-based delivery, you are in that rule set, not in a generic remote salary.</p>
<h2>What the ad must show, in two provinces</h2>
<p>British Columbia has required pay information in public postings since 1 November 2023. Ontario’s rules from 1 January 2026 require many employers to show expected compensation or a range, disclose artificial-intelligence screening, and say whether a vacancy exists. Details and exceptions are in <a href="article-read-a-remote-ad.html">How to read a remote job ad</a>. Quebec has its own employment standards and French-language workplace rules through CNESST. Do not copy an Ontario sentence into a Quebec contract.</p>
<h2>Employee or contractor</h2>
<p>Canada Pension Plan contributions and Employment Insurance premiums can apply to part-time employment. They do not apply in the same way to a true independent contractor, and a contract that uses the word contractor is not the test. The Canada Revenue Agency looks at control, tools, subcontracting, financial risk and the chance of profit. Getting the label wrong is their problem and yours. Read CRA’s pages, or ask a tax adviser. North Desk does not set the status for you.</p>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/pay-deductions.html" rel="noopener">Canada.ca: pay, deductions and the federal minimum wage</a></li>
<li><a href="https://www.retailcouncil.org/resources/quick-facts/minimum-wage-by-province/" rel="noopener">Retail Council of Canada: minimum wage by province</a></li>
<li><a href="https://www2.gov.bc.ca/gov/content/employment-business/employment-standards-advice/employment-standards/wages/minimum-wage" rel="noopener">Government of British Columbia: minimum wage</a></li>
</ul>
""",
    ),
)

PAGES["scam-check.html"] = page(
    "scam-check.html",
    "Remote job scam check | North Desk",
    "A private checklist for online, remote and flexible job messages, based on warning signs from the Canadian Anti-Fraud Centre.",
    "reading.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Scam check</span><h1>Before you reply to a remote offer.</h1><p class="lede">Tick any line that is true of the message in front of you. The check runs in this browser. Nothing is sent to North Desk.</p></div></div>
<section><div class="wrap" style="max-width:760px">
<form id="scam-check">
<ul class="check">
<li><label><input type="checkbox"> The offer arrived by text or a messaging app, and I had not applied.</label></li>
<li><label><input type="checkbox"> The sender uses a free webmail address, not the company’s own domain.</label></li>
<li><label><input type="checkbox"> I am asked to pay a fee, send a deposit, or buy equipment from their link.</label></li>
<li><label><input type="checkbox"> I must install an app or join a “task platform” before I know who employs me.</label></li>
<li><label><input type="checkbox"> The screen shows earnings I am told I cannot withdraw yet.</label></li>
<li><label><input type="checkbox"> I am asked to receive money and forward it, including by crypto.</label></li>
<li><label><input type="checkbox"> The pay sounds high for very little work, or for clicking simple tasks.</label></li>
<li><label><input type="checkbox"> I am asked to recruit other people in order to get paid.</label></li>
</ul>
</form>
<div id="scam-result" class="result" hidden><h3></h3><p></p></div>
<p class="notice" style="margin-top:1.5rem">This is a reading aid, not a finding that a message is lawful or fraudulent. Reports go to local police and the Canadian Anti-Fraud Centre at 1-888-495-8501. The full briefing is <a href="article-remote-scams.html">Remote-job scams reported in Canada</a>.</p>
</div></section>
""",
)

PAGES["glossary.html"] = page(
    "glossary.html",
    "Glossary | North Desk",
    "Plain-language definitions for remote, hybrid, online, flexible, NOC, EI, CPP, LMIA and other words used in Canadian remote recruitment.",
    "reading.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Glossary</span><h1>Words the ads use.</h1><p class="lede">Short definitions for online, remote and flexible recruitment in Canada. Confirm anything with a legal consequence on the official page linked from the article.</p></div></div>
<section><div class="wrap">
<label class="notice" for="glossary-search">Search terms</label>
<input id="glossary-search" class="search" type="search" placeholder="Try remote, EI, contractor">
<dl class="glossary">
<div class="term"><dt>Remote</dt><dd>The work is not performed at the employer’s office. It can still require you to live in a named province or time zone.</dd></div>
<div class="term"><dt>Hybrid</dt><dd>Some of the work is remote and some is at a stated place. It is not fully remote.</dd></div>
<div class="term"><dt>On-site</dt><dd>You attend a workplace. North Desk does not cover these roles.</dd></div>
<div class="term"><dt>Online work</dt><dd>The tasks and the deliverable move over the internet. The word does not, by itself, set the place or the hours.</dd></div>
<div class="term"><dt>Flexible work</dt><dd>Hours or workload can move. On this site, only when the work is also online or remote.</dd></div>
<div class="term"><dt>Part-time</dt><dd>In the Labour Force Survey, usually under 30 hours a week at the main or only job.</dd></div>
<div class="term"><dt>Job Bank</dt><dd>The Government of Canada’s public job board. Use the remote filter when place is the point.</dd></div>
<div class="term"><dt>NOC</dt><dd>National Occupational Classification. A code for an occupation, used on Job Bank and in labour statistics.</dd></div>
<div class="term"><dt>Vacancy</dt><dd>A job an employer is trying to fill. Statistics Canada measures vacancies by survey. A posting on a board is not the same count.</dd></div>
<div class="term"><dt>Offered wage</dt><dd>The wage advertised for an empty job. It is not the average wage of people already employed, and it is not your offer.</dd></div>
<div class="term"><dt>CPP</dt><dd>Canada Pension Plan. Contributions can apply to employment, including part-time employment. See the Canada Revenue Agency for current rates.</dd></div>
<div class="term"><dt>EI</dt><dd>Employment Insurance. Premiums and benefits have their own rules. A contract that calls you freelance does not automatically decide them.</dd></div>
<div class="term"><dt>Independent contractor</dt><dd>A worker who is in business for themselves. CRA looks at control, tools, risk and chance of profit, not only the contract’s title.</dd></div>
<div class="term"><dt>LMIA</dt><dd>A Labour Market Impact Assessment. An employer process used in some temporary-foreign-worker hires. It is not a job you buy. A request to pay someone to arrange one is a warning sign.</dd></div>
<div class="term"><dt>Gig</dt><dd>Short contracts, casual hours or platform tasks. Flexibility is real. A wage is not guaranteed, and platform delivery in B.C. has its own minimum for engaged time.</dd></div>
</dl>
<p id="glossary-empty" hidden>No term matches that.</p>
</div></section>
""",
)

PAGES["faq.html"] = page(
    "faq.html",
    "FAQ | North Desk",
    "Answers about North Desk and about online, remote and flexible work in Canada.",
    "reading.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">FAQ</span><h1>Short answers.</h1></div></div>
<section><div class="wrap" style="max-width:820px">
<details><summary>Does North Desk list jobs?</summary><p>No. We publish explanations of online, remote and flexible work, and of the recruitment process around that work. For current ads, use Job Bank’s remote filter and employers’ own careers pages.</p></details>
<details><summary>Are you a recruitment agency?</summary><p>No. We are an independent publisher. We are not a licensed employment agency. We do not screen, place or introduce candidates, and we do not charge job seekers.</p></details>
<details><summary>Why only online, remote and flexible?</summary><p>That is the beat. On-site work, including trades, retail floors, trucking and bedside care, is outside these pages even when those sectors have many vacancies.</p></details>
<details><summary>Is remote work common in Canada?</summary><p>It exists, and it is a small share of what job boards list. In October 2026 a Job Bank browse view showed on the order of 700 remote postings beside tens of thousands of jobs of every kind. The national vacancy total of 510,200 in the second quarter of 2026 is the whole economy, not the remote slice.</p></details>
<details><summary>What is the difference between remote and online?</summary><p>Remote is where you are allowed to sit. Online is how the work travels. A job can be one, the other, or both. <a href="article-three-arrangements.html">Read the three agreements</a>.</p></details>
<details><summary>Will I be paid a set amount?</summary><p>Only if an employer offers you that amount in writing. Nothing on North Desk is an offer or a forecast of earnings.</p></details>
<details><summary>Which province’s rules apply if I work from home?</summary><p>For most employers, the rules of the province or territory where you do the work. Federally regulated employers, such as banks, airlines and telecoms, follow the Canada Labour Code. <a href="article-pay-and-province.html">Pay, province and a remote contract</a> has the detail and the links.</p></details>
<details><summary>Someone texted me a remote job. What now?</summary><p>Do not pay and do not install an app. Run the <a href="scam-check.html">scam check</a>, then read the <a href="article-remote-scams.html">Anti-Fraud Centre briefing</a>. Reports: 1-888-495-8501.</p></details>
<details><summary>Do you cover Quebec in French?</summary><p>These pages are in English. Quebec employment standards and French-language workplace rules are administered by CNESST. Confirm those on Quebec’s own sites. We do not translate them here.</p></details>
<p style="margin-top:2rem">A question we have not answered: <a href="contact.html">write to the desk</a>.</p>
</div></section>
""",
)

PAGES["services.html"] = page(
    "services.html",
    "What we publish | North Desk",
    "North Desk publishes free guides on online, remote and flexible recruitment in Canada. We do not place candidates or charge readers.",
    "services.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">What we publish</span><h1>A desk, not a placement service.</h1><p class="lede">We explain how hiring works for online, remote and flexible roles. The reading is free. There is no account and no fee.</p></div></div>
<section><div class="wrap">
<div class="tiles">
<article class="tile reveal"><h3>Work-type guides</h3><p>Remote, online and flexible, each with the question a recruiter should already have answered: place, hours, status and pay basis.</p><a class="more" href="work-types.html">Open the guides</a></article>
<article class="tile reveal"><h3>How to read an ad</h3><p>The fields on a Canadian posting, including what Ontario and British Columbia expect employers to disclose.</p><a class="more" href="article-read-a-remote-ad.html">Read the field order</a></article>
<article class="tile reveal"><h3>Scam check</h3><p>Eight warning signs from the Canadian Anti-Fraud Centre, ticked in your browser and never uploaded.</p><a class="more" href="scam-check.html">Check a message</a></article>
<article class="tile reveal"><h3>Glossary</h3><p>Remote, hybrid, NOC, EI, CPP, contractor, LMIA. Short definitions, with the official source left to the articles.</p><a class="more" href="glossary.html">Look up a word</a></article>
</div>
</div></section>
<section class="alt"><div class="wrap split">
<div><h2>What we will not do</h2>
<ul class="note-list">
<li>Post a vacancy, or invent a job card with an employer and a wage.</li>
<li>Ask you to pay for a placement, a lead, or a “priority application.”</li>
<li>Take a social insurance number, a bank account, or copies of identification.</li>
<li>Introduce you to an employer. That is agency work, and we are not an agency.</li>
</ul></div>
<div><h2>Where the ads actually are</h2>
<p>Search <a href="https://www.jobbank.gc.ca/findajob" rel="noopener">Job Bank</a> and filter for remote. Read the employer’s own careers page before you trust a repost. If you want the context around those ads, start with <a href="reading.html">the articles</a>.</p>
<p><a class="btn btn-primary" href="contact.html">Send a correction</a></p></div>
</div></section>
""",
)

PAGES["about.html"] = page(
    "about.html",
    "About | North Desk",
    "North Desk is an independent Canadian publisher on online, remote and flexible work, and on the recruitment process for that work.",
    "about.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">About</span><h1>We publish on one kind of hiring.</h1></div></div>
<section><div class="wrap split">
<div class="reveal">
<h2>Who is writing</h2>
<p>North Desk is an independent publisher for people in Canada who are looking at online work, remote roles, or flexible hours attached to that work. Recruitment is the subject: how a real hiring process runs, how an ad is built, and how a pitch imitates one. We are not affiliated with Job Bank, Statistics Canada, or any province.</p>
<p>We are not a licensed employment agency. We do not hold jobs, and we do not send your name to an employer.</p>
</div>
<div class="reveal">
<h2>How a piece gets written</h2>
<div class="types">
<div class="type" style="grid-template-columns:1fr"><div><h3>Inside the beat</h3><p>If the work is not online, remote, or flexible in that setting, we do not assign it.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Tied to a source</h3><p>Labour figures come from Statistics Canada. Posting rules come from the province that wrote them. Scam patterns come from the Canadian Anti-Fraud Centre.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Dated</h3><p>Articles say when they were last reviewed. A wage or a vacancy count without a date is not finished.</p></div></div>
</div>
</div>
</div></section>
<section class="alt"><div class="wrap">
<p class="notice" style="max-width:70ch">North Desk publishes general information. It is not legal, tax or employment advice. Write to us at desk@northdesk.ca. We do not publish a street address because the desk is the site.</p>
</div></section>
""",
)

PAGES["contact.html"] = page(
    "contact.html",
    "Contact | North Desk",
    "Write to North Desk about online, remote and flexible work in Canada. The form opens your email app. We do not take identification or banking details.",
    "contact.html",
    f"""
<div class="page-head"><div class="wrap"><span class="eyebrow">Contact</span><h1>Write to the desk.</h1><p class="lede">Corrections, story ideas, and remote ads you want read against our guides. Do not include a social insurance number, banking details, or files from a suspicious app.</p></div></div>
<section><div class="wrap split">
<div>
<form id="contact-form" class="form" novalidate>
<div class="field"><label for="name">Name</label><input id="name" required autocomplete="name"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">Email</label><input id="email" type="email" required autocomplete="email"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="province">Province or territory</label><select id="province"><option value="">Prefer not to say</option><option>Alberta</option><option>British Columbia</option><option>Manitoba</option><option>New Brunswick</option><option>Newfoundland and Labrador</option><option>Northwest Territories</option><option>Nova Scotia</option><option>Nunavut</option><option>Ontario</option><option>Prince Edward Island</option><option>Quebec</option><option>Saskatchewan</option><option>Yukon</option><option>Outside Canada</option></select></div>
<div class="field"><label for="topic">Topic</label><select id="topic"><option>A remote job ad</option><option>Online work</option><option>A flexible arrangement</option><option>A possible scam</option><option>A correction</option><option>A story idea</option></select></div>
<div class="field"><label for="msg">Message</label><textarea id="msg" required></textarea><div class="err" aria-live="polite"></div></div>
<button class="btn btn-primary" type="submit">Write to North Desk</button>
<p class="notice">Sending opens your email app with the message addressed to {EMAIL}.</p>
</form>
<div id="form-ok" class="ok" hidden tabindex="-1" role="status"><h3>Your email app should be open.</h3><p>Send the message from there when you are ready.</p><p class="ok-sub">If nothing opened, write to {EMAIL}.</p></div>
</div>
<div>
<h2>Email</h2>
<ul class="contact-list"><li><b>Desk</b><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul>
<p class="notice">We reply to editorial questions. We cannot tell you to accept a job, and we will not forward your details to an employer.</p>
</div>
</div></section>
""",
)

PAGES["privacy.html"] = page(
    "privacy.html",
    "Privacy | North Desk",
    "How North Desk handles personal information. The contact form opens your email app. Scam check and search run in your browser.",
    "contact.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Privacy</span><h1>Privacy</h1><p class="lede">Last updated 27 October 2026.</p></div></div>
<section><div class="wrap article">
<p>North Desk is an independent publisher. We do not run accounts, and we do not ask you to create one. This notice describes the little personal information the site can involve. It is written with the fair-information principles in Canada’s Personal Information Protection and Electronic Documents Act (PIPEDA) in mind. Provincial privacy laws, including Quebec’s, can also apply depending on where you are and how a message is handled.</p>
<h2>What you can send us</h2>
<p>The contact form does not submit to our server. It opens your own email application with a message addressed to desk@northdesk.ca. If you send that email, we receive whatever you chose to include: typically your name, email address, province and message. We use it to reply, to correct an article, or to consider a topic. We do not sell it, and we do not use it to build a marketing list.</p>
<p>Do not send a social insurance number, banking details, identity documents or passwords. We will not ask for them.</p>
<h2>What stays on your device</h2>
<p>The scam check and the glossary search run in your browser. What you type into them is not transmitted to us by those tools.</p>
<h2>Fonts and server logs</h2>
<p>Pages request typefaces from Google Fonts. That request can expose your IP address to Google. A host that serves these files may keep ordinary server logs, such as IP address, browser and page requested, for security. We do not add our own analytics tracker to these pages.</p>
<h2>How long a message is kept</h2>
<p>If you email us, we keep the thread long enough to answer and to keep a correction on file, then delete it or reduce it to an anonymous note. You can ask what we still have, ask for a correction, or ask us to delete the thread, by writing to desk@northdesk.ca. We may need to confirm we are writing back to the same address.</p>
<h2>Other sites</h2>
<p>Articles link to Job Bank, Statistics Canada, provincial pages and the Canadian Anti-Fraud Centre. Those sites have their own notices. We do not control them.</p>
</div></section>
""",
)

PAGES["disclaimer.html"] = page(
    "disclaimer.html",
    "Disclaimer | North Desk",
    "North Desk publishes general information on online, remote and flexible work in Canada. We do not recruit or guarantee work or income.",
    "about.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Disclaimer</span><h1>Disclaimer</h1></div></div>
<section><div class="wrap article">
<h2>A publisher, not an agency</h2>
<p>North Desk publishes general information about online, remote and flexible work in Canada, and about how recruitment for that work usually proceeds. We are not a licensed employment agency. We do not publish vacancies. We do not recruit, screen, place or introduce candidates. We do not charge a fee to readers.</p>
<h2>No job and no income</h2>
<p>Nothing on this site is an offer of employment or a prediction of earnings. Pay, hours and eligibility change by employer, province and contract.</p>
<h2>Not professional advice</h2>
<p>The pages are not legal, tax, immigration or employment advice. Employment standards are provincial, with a federal code for some industries. Quebec’s rules, including French-language requirements at work, are not restated as if they were Ontario’s. Confirm details with the authority that governs your situation, or with a qualified adviser.</p>
<h2>Figures go out of date</h2>
<p>We date statistics and say where they came from. Vacancy counts, minimum wages and posting rules change. A reviewed date is not a promise that every sentence is still current. Write to us if you find an error.</p>
<h2>Other websites</h2>
<p>Links to Job Bank, Statistics Canada and other sites are there so you can read the source. We are not responsible for their content.</p>
</div></section>
""",
)


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    for name, html in PAGES.items():
        path = ROOT / name
        path.write_text(html, encoding="utf-8")
        print(name, path.stat().st_size)


if __name__ == "__main__":
    main()
