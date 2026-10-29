#!/usr/bin/env python3
"""Render the Job Compass static site."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "site"
EMAIL = "hello@jobcompass.ca"
THEME = "#243552"

LOGO = (
    '<svg viewBox="0 0 100 100" aria-hidden="true">'
    '<circle cx="50" cy="50" r="42" fill="none" stroke="currentColor" stroke-width="8"/>'
    '<g transform="rotate(38 50 50)">'
    '<path d="M50 18 64 50H36z" fill="currentColor"/>'
    '<path d="M50 82 64 50H36z" fill="currentColor" opacity=".38"/>'
    "</g>"
    '<circle cx="50" cy="50" r="5" fill="#faf5ea"/>'
    "</svg>"
)

def _row(y, label):
    return (
        f'<circle cx="132" cy="{y}" r="11" fill="#c4442f"/>'
        f'<path d="M126 {y}l4.5 4.5 8-9" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
        f'<text x="154" y="{y + 5}" font-family="Figtree,sans-serif" font-size="15" font-weight="600" fill="#1f2a24">{label}</text>'
        f'<rect x="276" y="{y - 4}" width="78" height="8" rx="4" fill="#e8dfcc"/>'
    )

HERO_ART = (
    '<svg class="art" viewBox="-14 -34 524 600" role="img" aria-label="Illustration of a laptop showing a job posting checklist for employer, work location, pay and hours">'
    '<defs>'
    '<clipPath id="arch"><path d="M0 516V240a240 240 0 0 1 480 0v276a44 44 0 0 1-44 44H44a44 44 0 0 1-44-44z"/></clipPath>'
    '<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
    '<stop offset="0" stop-color="#d3e6ec"/><stop offset="1" stop-color="#f7dccb"/>'
    '</linearGradient>'
    '</defs>'
    '<g clip-path="url(#arch)">'
    '<rect width="480" height="560" fill="url(#sky)"/>'
    '<circle cx="380" cy="110" r="64" fill="#f7d77b" opacity=".85"/>'
    '<circle cx="90" cy="96" r="26" fill="#fff" opacity=".55"/>'
    '<rect x="0" y="392" width="480" height="168" fill="#23402f"/>'
    '<rect x="0" y="392" width="480" height="10" fill="#183024"/>'
    '<rect x="94" y="164" width="292" height="222" rx="20" fill="#1f2a24"/>'
    '<rect x="106" y="176" width="268" height="198" rx="10" fill="#faf5ea"/>'
    '<text x="124" y="206" font-family="Figtree,sans-serif" font-size="15" font-weight="700" fill="#23402f">Job posting checklist</text>'
    '<rect x="124" y="220" width="64" height="22" rx="11" fill="#d3e6ec"/>'
    '<text x="156" y="235" text-anchor="middle" font-family="Figtree,sans-serif" font-size="11.5" font-weight="700" fill="#1f2a24">Remote</text>'
    '<rect x="196" y="220" width="78" height="22" rx="11" fill="#f7d77b"/>'
    '<text x="235" y="235" text-anchor="middle" font-family="Figtree,sans-serif" font-size="11.5" font-weight="700" fill="#1f2a24">Part-time</text>'
    '<rect x="282" y="220" width="64" height="22" rx="11" fill="#dfe9d3"/>'
    '<text x="314" y="235" text-anchor="middle" font-family="Figtree,sans-serif" font-size="11.5" font-weight="700" fill="#1f2a24">Hourly</text>'
    + _row(272, "Employer")
    + _row(306, "Location")
    + _row(340, "Pay & hours")
    + '<path d="M50 386H430l-14 18a10 10 0 0 1-8 4H72a10 10 0 0 1-8-4z" fill="#d9dfd2"/>'
    '<rect x="196" y="390" width="88" height="6" rx="3" fill="#b8c2b3"/>'
    '<g><rect x="424" y="352" width="40" height="42" rx="9" fill="#f7d77b"/>'
    '<path d="M464 362h6a9 9 0 0 1 0 20h-6" fill="none" stroke="#f7d77b" stroke-width="6"/>'
    '<path d="M434 344c0-8 8-8 8-16M446 344c0-8 8-8 8-16" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".7"/></g>'
    '<g><path d="M14 394h40l-5 -42H19z" fill="#c4442f"/>'
    '<path d="M34 352C22 330 14 322 10 306c14 2 24 12 24 46zM34 352c2-26 10-40 26-48 2 20-8 38-26 48zM34 352c-2-18-1-30 8-46 10 12 6 30-8 46z" fill="#7fa58f"/></g>'
    '<path d="M0 500Q120 480 240 496T480 488V560H0z" fill="#183024"/>'
    '</g>'
    '<path d="M-6 560V240a246 246 0 0 1 492 0v320" fill="none" stroke="#c4442f" stroke-width="3" transform="translate(16 -14)" opacity=".85"/>'
    '</svg>'
)

NAV = [
    ("index.html", "Home"),
    ("reading.html", "Guides"),
    ("work-types.html", "Work types"),
    ("services.html", "Additional work"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
]


def brand():
    return f'<a class="brand" href="index.html">{LOGO}Job<em>Compass</em></a>'


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
<p style="margin-top:1rem;max-width:36ch">Practical Canadian guides to remote, online and flexible work.</p></div>
<div><h4>Guides</h4><ul>
<li><a href="reading.html">Browse all guides</a></li>
<li><a href="work-types.html">Work types</a></li>
<li><a href="glossary.html">Glossary</a></li>
<li><a href="faq.html">FAQ</a></li>
</ul></div>
<div><h4>Publisher</h4><ul>
<li><a href="about.html">About</a></li>
<li><a href="services.html">Additional work</a></li>
<li><a href="contact.html">Contact</a></li>
<li><a href="privacy.html">Privacy</a></li>
<li><a href="disclaimer.html">Disclaimer</a></li>
</ul></div>
</div>
<div class="legal"><p>Job Compass is an independent information service and does not list jobs. Official sources set legal, tax, immigration and employment rules.</p>
<p>&copy; 2026 Job Compass &middot; Canada &middot; <a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<p class="wordmark" aria-hidden="true">Job Compass</p>
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
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..600&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet">
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
<p class="byline">Job Compass &middot; Last reviewed {reviewed}</p>
<p class="lede">{lede}</p>
{body}
<p style="margin-top:2.5rem"><a href="reading.html">&larr; Back to all guides</a></p>
</div></section>"""


PAGES = {}

PAGES["index.html"] = page(
    "index.html",
    "Remote, online and flexible work in Canada | Job Compass",
    "Canadian guides to remote, online, part-time, flexible and independent contract work, including job search and pay information.",
    "index.html",
    f"""
<section class="hero"><div class="wrap hero-grid">
<div>
<span class="eyebrow">Guides to flexible work in Canada</span>
<h1>Remote, online and flexible work in <em>Canada.</em></h1>
<p class="lede">Information on comparing work arrangements, finding paid opportunities and understanding hours, pay and employment status.</p>
<ul class="hero-points">
<li><b>Work location.</b> Remote, online and hybrid describe different arrangements.</li>
<li><b>Job search.</b> Job Bank provides filters for occupation, work location and hours.</li>
<li><b>Posting details.</b> A posting should identify the employer, location, pay, hours and employment status.</li>
<li><b>Pay and status.</b> Employment and independent contract work handle deductions, expenses and tax differently.</li>
</ul>
<div class="btn-row"><a class="btn btn-primary" href="reading.html">Browse the guides</a><a class="btn btn-ghost" href="#contact">Find a starting guide</a></div>
</div>
<div class="hero-art">
{HERO_ART}
<div class="modes">
<h2 class="sr">Three types of flexible work</h2>
<a class="mode" href="remote-work-canada.html"><span class="dot"></span><span><b>Remote work</b><small>Work completed away from the employer’s usual workplace.</small></span><span class="tag">Where</span></a>
<a class="mode" href="online-work-canada.html"><span class="dot"></span><span><b>Online work</b><small>Work completed or delivered over the internet.</small></span><span class="tag">How</span></a>
<a class="mode" href="flexible-work-canada.html"><span class="dot"></span><span><b>Part-time &amp; flexible</b><small>Hours or workloads arranged around other commitments.</small></span><span class="tag">When</span></a>
</div>
</div>
</div></section>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">Work arrangements</span><h2>Compare remote, online and flexible work.</h2><p class="lede">Work location, online delivery and working hours are separate conditions. One position may combine more than one arrangement.</p></div>
<div class="minis">
<a class="mini reveal" href="remote-work-canada.html"><b>Remote &amp; hybrid</b><span>Work completed away from the employer’s workplace, with or without scheduled on-site days.</span></a>
<a class="mini reveal" href="online-work-canada.html"><b>Online work</b><span>Jobs completed or delivered over the internet.</span></a>
<a class="mini reveal" href="flexible-work-canada.html"><b>Part-time &amp; flexible</b><span>Part-time and flexible hours alongside other commitments.</span></a>
<a class="mini reveal" href="article-second-path.html"><b>Freelance &amp; additional work</b><span>Project-based and additional work, including variable income.</span></a>
</div>
<div class="reason-panel">
<div class="head reveal"><span class="eyebrow">Reasons for additional work</span><h2>Why Canadians take on additional work.</h2><p class="lede">Income, experience and scheduling needs shape which work arrangements are practical.</p></div>
<ol class="shifts">
<li class="reveal"><span class="no">34.9%</span><h3>Everyday needs</h3><p>Rent, groceries and other everyday costs.</p></li>
<li class="reveal"><span class="no">34.8%</span><h3>Extra income</h3><p>Almost the same share cited income beyond everyday essentials.</p></li>
<li class="reveal"><span class="no">14.5%</span><h3>Meaningful work</h3><p>Another share cited work in a field they were passionate about.</p></li>
</ol>
<p class="src-note">Source: Statistics Canada survey of multiple jobholders aged 15 to 69, August 2023.</p>
</div>
</div></section>

<section class="route" id="recruitment"><div class="wrap">
<div class="route-head reveal"><span class="eyebrow">Searching for work</span><h2>Finding suitable remote and online opportunities.</h2>
<p class="lede">Relevant results depend on more than a “work from home” keyword. A practical search begins with an occupation, narrows results by work location and hours, and then checks each posting for the employer, pay and employment or contract status.</p></div>
<ol class="stops">
<li class="stop reveal"><span class="n">1</span><h3>Reason for searching</h3><p>Extra income, experience, fewer hours or less travel.</p></li>
<li class="stop reveal"><span class="n">2</span><h3>Available hours</h3><p>The number of hours that can fit around current commitments.</p></li>
<li class="stop reveal"><span class="n">3</span><h3>Work location</h3><p>Fully remote work and hybrid work lead to different results.</p></li>
<li class="stop reveal"><span class="n">4</span><h3>Occupation</h3><p><a href="https://www.jobbank.gc.ca/findajob" rel="noopener">Job Bank</a> can filter an occupation by work location and hours.</p></li>
<li class="stop reveal"><span class="n">5</span><h3>Posting details</h3><p>The employer, pay, province and employment or contract status.</p></li>
</ol>
<p class="route-cta reveal"><a class="btn btn-primary" href="article-where-to-look.html">How to search for remote work</a></p>
</div></section>

<section class="alt" id="market"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Canadian job market</span><h2>Remote and flexible work in Canada’s job market.</h2><p class="lede">Remote openings form a small share of the market. Suitable opportunities depend on occupation, province, experience, available hours and the terms of the posting.</p></div>
<div class="answer-grid three">
<article class="answer-card reveal"><span class="answer-kicker">Roles and employers</span><h3>Occupation and arrangement are separate details</h3><p>Customer support, administration, software, writing, design and specialist services may be delivered online, depending on the employer and the work involved.</p></article>
<article class="answer-card reveal"><span class="answer-kicker">Timing and sources</span><h3>Postings change throughout the search</h3><p>Job Bank alerts identify new matches. Employer career pages confirm current vacancies, while Job Bank trend data provides regional context.</p></article>
<article class="answer-card reveal"><span class="answer-kicker">Requirements and competition</span><h3>Role requirements still apply</h3><p>Qualifications, location, communication, tools and time-zone availability still matter. Response times vary with each employer’s process.</p></article>
</div>
<p class="src-note">In October 2026, about 700 of roughly 84,000 Job Bank postings were marked remote. Counts change as employers add and close postings.</p>
<div class="btn-row"><a class="btn btn-primary" href="article-what-vacancies-mean.html">Canadian job-market guide</a><a class="btn btn-ghost" href="https://www.jobbank.gc.ca/trend-analysis" rel="noopener">Job Bank trend analysis</a></div>
</div></section>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">Guides and articles</span><h2>Job-search, application and pay guides.</h2><p class="lede">Detailed Canadian information on work arrangements, job postings, applications and employment terms.</p></div>
<div class="posts">
<article class="post reveal"><div class="meta"><span class="cat">Second jobs</span><span>7 min</span></div><h3><a href="article-second-path.html">Why people take a second job</a></h3><p>Money is only part of it. Time, location and meaningful work matter too.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Where to look</span><span>6 min</span></div><h3><a href="article-where-to-look.html">How to search for remote work</a></h3><p>Occupation, work-location and hours filters provide more relevant Job Bank results.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Work types</span><span>6 min</span></div><h3><a href="article-three-arrangements.html">Remote, online and flexible work compared</a></h3><p>Remote refers to location, online to how the work is done, and flexible to the schedule.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Before you apply</span><span>7 min</span></div><h3><a href="article-read-a-remote-ad.html">How to read a remote job posting</a></h3><p>Employer, location, pay and hours: what a good posting spells out.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Application</span><span>5 min</span></div><h3><a href="article-remote-cv.html">Résumés for online and remote work</a></h3><p>Relevant results, digital tools and communication experience for remote applications.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Pay</span><span>7 min</span></div><h3><a href="article-pay-and-province.html">What a second paycheque changes</a></h3><p>Minimum wage by province, deductions and how employee and freelance pay differ.</p></article>
</div>
</div></section>

<section class="alt" id="contact"><div class="wrap split">
<div><span class="eyebrow">Get in touch</span><h2>Questions about remote and flexible work.</h2><p class="lede">Questions about work arrangements, job searches and the published guides are welcome.</p>
</div>
<div>
<form id="contact-form" class="form" novalidate>
<div class="field"><label for="name">Name</label><input id="name" required autocomplete="name"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">Email</label><input id="email" type="email" required autocomplete="email"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="province">Province or territory</label><select id="province"><option value="">Prefer not to say</option><option>Alberta</option><option>British Columbia</option><option>Manitoba</option><option>New Brunswick</option><option>Newfoundland and Labrador</option><option>Northwest Territories</option><option>Nova Scotia</option><option>Nunavut</option><option>Ontario</option><option>Prince Edward Island</option><option>Quebec</option><option>Saskatchewan</option><option>Yukon</option><option>Outside Canada</option></select></div>
<div class="field"><label for="topic">Topic</label><select id="topic"><option>Work arrangements</option><option>Job search and Job Bank</option><option>Reading a job posting</option><option>Applications and résumés</option><option>Pay, deductions and employment status</option><option>Freelance or contract work</option><option>Guide feedback or source correction</option><option>Other question about the guides</option></select></div>
<div class="field"><label for="msg">Question</label><textarea id="msg" required></textarea><div class="err" aria-live="polite"></div></div>
<button class="btn btn-primary" type="submit">Open email</button>
<p class="notice">The form opens a draft in the email app. Nothing is stored on the Job Compass site.</p>
</form>
<div id="form-ok" class="ok" hidden tabindex="-1" role="status"><h3>Your email message is ready.</h3><p>Review it in your email app before sending.</p><p class="ok-sub">If the app did not open, email {EMAIL}.</p></div>
</div>
</div></section>
""",
)

PAGES["reading.html"] = page(
    "reading.html",
    "Guides | Job Compass",
    "Canadian guides to remote work, online work, part-time and flexible hours, freelance work and second jobs.",
    "reading.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Guides</span><h1>Guides to remote, online and flexible work in Canada</h1><p class="lede">Information on work arrangements, job searches, applications and pay.</p></div></div>
<section><div class="wrap">
<div class="filters" role="group" aria-label="Filter articles">
<button class="chip" type="button" data-filter="all" aria-pressed="true">All</button>
<button class="chip" type="button" data-filter="path" aria-pressed="false">Second jobs</button>
<button class="chip" type="button" data-filter="hiring" aria-pressed="false">Applications</button>
<button class="chip" type="button" data-filter="market" aria-pressed="false">Job market</button>
<button class="chip" type="button" data-filter="pay" aria-pressed="false">Pay</button>
</div>
<div class="posts">
<article class="post" data-cat="path"><div class="meta"><span class="cat">Second jobs</span><span>7 min</span></div><h3><a href="article-second-path.html">Why people take a second job</a></h3><p>Money is only part of it. Time, location and meaningful work matter too.</p></article>
<article class="post" data-cat="path"><div class="meta"><span class="cat">Where to look</span><span>6 min</span></div><h3><a href="article-where-to-look.html">How to search for remote work</a></h3><p>Occupation, work-location and hours filters provide more relevant Job Bank results.</p></article>
<article class="post" data-cat="hiring"><div class="meta"><span class="cat">Work types</span><span>6 min</span></div><h3><a href="article-three-arrangements.html">Remote, online and flexible work compared</a></h3><p>Remote refers to location, online to how the work is done, and flexible to the schedule.</p></article>
<article class="post" data-cat="market"><div class="meta"><span class="cat">The market</span><span>6 min</span></div><h3><a href="article-what-vacancies-mean.html">What the remote job market looks like in Canada</a></h3><p>What the national numbers say about work-from-home jobs, and why a focused search works better.</p></article>
<article class="post" data-cat="hiring"><div class="meta"><span class="cat">Before you apply</span><span>7 min</span></div><h3><a href="article-read-a-remote-ad.html">How to read a remote job posting</a></h3><p>Employer, location, pay and hours: what a good posting spells out.</p></article>
<article class="post" data-cat="hiring"><div class="meta"><span class="cat">Application</span><span>5 min</span></div><h3><a href="article-remote-cv.html">Résumés for online and remote work</a></h3><p>Relevant results, digital tools and communication experience for remote applications.</p></article>
<article class="post" data-cat="pay"><div class="meta"><span class="cat">Pay</span><span>7 min</span></div><h3><a href="article-pay-and-province.html">What a second paycheque changes</a></h3><p>Minimum wage by province, deductions and how employee and freelance pay differ.</p></article>
</div>
</div></section>
""",
)

PAGES["work-types.html"] = page(
    "work-types.html",
    "Online, remote and flexible work | Job Compass",
    "How remote work, online work and flexible hours differ in Canadian job postings.",
    "work-types.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Work types</span><h1>Remote, online and flexible work.</h1><p class="lede">Remote describes location. Online describes how work is completed. Part-time and flexible describe hours or workload.</p></div></div>
<section><div class="wrap">
<div class="types">
<article class="type"><div><span class="n">01 · Location</span><h3><a href="remote-work-canada.html">Remote</a></h3></div><div><p>Remote jobs are completed away from the employer’s workplace. Some allow work from anywhere in Canada, while others are limited to a province. Hybrid jobs include on-site days. Job Bank identifies remote positions with a work-location filter.</p><p><a href="remote-work-canada.html">Read the guide</a></p></div></article>
<article class="type"><div><span class="n">02 · How work is done</span><h3><a href="online-work-canada.html">Online</a></h3></div><div><p>Online work is completed or delivered over the internet, including customer support, writing, design, bookkeeping, tutoring, moderation and software development. It may be done at home or at an employer’s workplace.</p><p><a href="online-work-canada.html">Read the guide</a></p></div></article>
<article class="type"><div><span class="n">03 · Hours</span><h3><a href="flexible-work-canada.html">Flexible</a></h3></div><div><p>This category includes flexible hours, deadline-based projects and part-time work. Statistics Canada generally defines part-time work as fewer than 30 hours a week. Income and hours depend on the agreement or contract.</p><p><a href="flexible-work-canada.html">Read the guide</a></p></div></article>
</div>
<p class="src-note">For current openings, <a href="https://www.jobbank.gc.ca/findajob" rel="noopener">Job Bank’s remote-work filter</a> is more precise than a keyword search for “work from home.”</p>
</div></section>
""",
)

PAGES["remote-work-canada.html"] = page(
    "remote-work-canada.html",
    "Remote work in Canada | Job Compass",
    "What remote work means in Canada, including location, province, hybrid arrangements and how employers hire for remote positions.",
    "work-types.html",
    """
<div class="page-head jobhero jh1"><div class="wrap jh-grid">
<div><span class="eyebrow">Location</span><h1>Remote work in Canada</h1><p class="lede">Remote work is performed away from the employer’s usual workplace. Some positions require residence in a specific province or availability in a stated Canadian time zone.</p></div>
<aside class="qf"><h2>At a glance</h2><dl>
<dt>Location</dt><dd>Away from the employer’s usual workplace. Hybrid jobs include some days on-site.</dd>
<dt>Hours</dt><dd>Often full-time. Statistics Canada counts part-time as under 30 hours a week.</dd>
<dt>Applying</dt><dd>Applications are submitted through Job Bank or the employer’s website after confirming hours and work location.</dd>
<dt>Where to look</dt><dd>Job Bank’s remote filter and the employer’s careers page.</dd>
</dl><p class="rv">Last reviewed October 2026.</p></aside>
</div></div>
<section><div class="wrap article">
<h2>What remote work means</h2>
<p>On Job Bank and Indeed, a posting may be marked on-site, hybrid or remote. Hybrid combines work at a stated workplace with remote days. Remote means the worker is not normally required to report to the employer’s workplace. A keyword search for “work from home” can also return on-site positions that mention a home.</p>
<p>Indeed’s employer guidance reserves “Canada” or “nationwide” for work that can be performed anywhere in the country. Some remote jobs still require residence in a particular province or availability in a Canadian time zone. Location requirements should be confirmed before applying.</p>
<h2>How employers hire for remote positions</h2>
<p>Most employers post the job, review applications and arrange interviews, much like any other hire. A written offer normally sets out the pay, hours, employer and permitted work location. For a second job, stated hours must fit alongside existing employment or other commitments.</p>
<p>Current openings are listed through <a href="https://www.jobbank.gc.ca/findajob" rel="noopener">Job Bank’s remote-work filter</a> and employers’ careers pages.</p>
<h2>Details to confirm in an offer</h2>
<ul>
<li>Permitted provinces or territories and any relocation conditions</li>
<li>Required on-site days in a hybrid arrangement</li>
<li>Employer name and whether pay is hourly, salaried or per project</li>
<li>Time zone for meetings and required availability</li>
<li>Responsibility for computer equipment and software</li>
</ul>
<p>The guides on <a href="article-pay-and-province.html">pay for additional work</a> and <a href="article-read-a-remote-ad.html">remote job postings</a> cover province, employer, pay and hours in more detail.</p>
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
    "Online work in Canada | Job Compass",
    "What online work means in Canada, including common tasks, employee and contractor arrangements, and platform-based work.",
    "work-types.html",
    """
<div class="page-head jobhero jh2"><div class="wrap jh-grid">
<div><span class="eyebrow">How the work is delivered</span><h1>Online work in Canada</h1><p class="lede">Online work is completed or delivered over the internet. Work location is a separate condition and may be limited to a province.</p></div>
<aside class="qf"><h2>At a glance</h2><dl>
<dt>Typical tasks</dt><dd>Support, writing, design, bookkeeping, tutoring, moderation, software.</dd>
<dt>Status</dt><dd>Employee or independent contractor. The label in a posting does not determine legal status.</dd>
<dt>Pay</dt><dd>Hourly, salaried or project-based. An advertised figure is not a written offer.</dd>
<dt>Additional work</dt><dd>Often completed part-time alongside a main job or other commitments.</dd>
</dl><p class="rv">Last reviewed October 2026.</p></aside>
</div></div>
<section><div class="wrap article">
<h2>Online work is not necessarily remote work</h2>
<p>Online work can be completed at an employer’s workplace or somewhere else. Remote work can also include scheduled phone duties that are not usually described as online work. On this site, online work means tasks completed or delivered over the internet. Work location remains a separate detail in the posting.</p>
<h2>Employment or independent contract work</h2>
<p>Some online roles are employment, with scheduled hours, supervision, pay statements and payroll deductions where applicable. Others are independent contract work involving invoices, financial risk and self-employed tax obligations. The Canada Revenue Agency considers factors such as control, tools, financial risk and opportunity for profit. The word “freelance” does not determine employment status.</p>
<h2>Online work beside a main job</h2>
<p>Online work alongside a main job often uses existing experience in customer service, bookkeeping, writing, design, tutoring, moderation or software development. Demonstrated skills and available hours help determine whether a posting is suitable. The <a href="article-remote-cv.html">résumé guide</a> covers how that experience can be presented.</p>
<p>Software development is one occupation where online delivery is common. In the second quarter of 2026, Statistics Canada counted 3,545 vacancies for software developers and programmers, up about 35 per cent year over year, with an average offered wage of $43.65 an hour. That figure is the average advertised wage for vacancies in the occupation, not for remote work generally.</p>
<p>A clear posting names the organization, describes the work and states whether pay is hourly, salaried or project-based. Job Bank searches by occupation and work location; the employer’s careers page can confirm the same posting. The <a href="article-where-to-look.html">remote-work search guide</a> covers the available filters.</p>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www150.statcan.gc.ca/n1/daily-quotidien/260915/t002a-eng.htm" rel="noopener">Statistics Canada: occupations with the largest vacancy increases, Q2 2026</a></li>
<li><a href="https://www.jobbank.gc.ca/findajob" rel="noopener">Job Bank: find a job</a></li>
</ul>
</div></section>
""",
)

PAGES["flexible-work-canada.html"] = page(
    "flexible-work-canada.html",
    "Flexible online and remote work in Canada | Job Compass",
    "Flexible hours and workloads for online and remote work in Canada, including what part-time means in the Labour Force Survey.",
    "work-types.html",
    """
<div class="page-head jobhero jh3"><div class="wrap jh-grid">
<div><span class="eyebrow">Hours</span><h1>Flexible online and remote work</h1><p class="lede">Flexible work allows some choice over hours, workload or deadlines. This guide covers flexible arrangements that are also online or remote.</p></div>
<aside class="qf"><h2>At a glance</h2><dl>
<dt>Part-time</dt><dd>Under 30 hours a week, by Statistics Canada’s definition.</dd>
<dt>Arrangements</dt><dd>Variable hours, a shorter week or a project with a deadline.</dd>
<dt>Not included</dt><dd>On-site casual shifts, even short ones.</dd>
<dt>Pay</dt><dd>May be hourly, salaried or project-based.</dd>
</dl><p class="rv">Last reviewed October 2026.</p></aside>
</div></div>
<section><div class="wrap article">
<h2>Why hours matter when you add a second job</h2>
<p>Flexible work can mean fewer weekly hours, variable scheduling or deadline-based projects. Work location is covered in the <a href="remote-work-canada.html">remote-work guide</a>; this page focuses on hours and workload.</p>
<p>For a second job, stated hours need to fit alongside existing employment or other commitments. In 2023, 89.9 per cent of multiple jobholders held at least one part-time job. People whose main job was part-time were more than twice as likely to hold another job as people whose main job was full-time (9.7 per cent compared with 4.7 per cent). Statistics Canada usually defines part-time as fewer than 30 hours per week at the main job; this statistical definition is separate from provincial overtime rules.</p>
<p>Part-time hours are common for school, caregiving, health needs or personal preference. Postings should state weekly hours or deadlines, time zone and who sets the schedule. The guide to <a href="article-read-a-remote-ad.html">reading a job posting</a> lists the other relevant fields.</p>
<p>Self-employment, which includes a lot of flexible online contract work, was up 51,000 people (+1.9 per cent) in the year to September 2026, and down 23,000 in that month alone. Contract income may vary from month to month and is generally less predictable than regular employee pay.</p>
<h2>Asking your employer for flexible hours</h2>
<p>Employees in federally regulated workplaces have a formal right to request flexible work arrangements. Other workplaces are governed by provincial or territorial law, workplace policy and any collective agreement or contract. Requests are usually made in writing, with a proposed schedule and a retained copy of the response. Guidance written for other countries may not reflect Canadian rules.</p>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www150.statcan.gc.ca/n1/daily-quotidien/261009/dq261009a-eng.htm" rel="noopener">Statistics Canada: Labour Force Survey, September 2026</a></li>
<li><a href="https://www150.statcan.gc.ca/n1/pub/14-28-0001/2024001/article/00002-eng.htm" rel="noopener">Statistics Canada: Multiple jobholders, 2023</a></li>
</ul>
</div></section>
""",
)

PAGES["article-read-a-remote-ad.html"] = page(
    "article-read-a-remote-ad.html",
    "How to read a remote job posting in Canada | Job Compass",
    "How to review Canadian remote, online and flexible job postings, including pay transparency in Ontario and British Columbia.",
    "reading.html",
    article(
        "Before you apply",
        "How to read a remote job posting",
        "A posting is easier to assess when the employer, work location, pay, hours, employment relationship and schedule constraints are clear.",
        """
<div class="takeaways"><h2>What to look for</h2><ul>
<li>Who is hiring, and can you find that employer on its own website?</li>
<li>Where is the work done: remote, hybrid or in a named province?</li>
<li>What does it pay: a set amount, a range or “to be negotiated”?</li>
<li>What are the hours and time zone, and does the posting describe employment or independent contract work?</li>
<li>Do the hours fit around your current job, school or family?</li>
</ul></div>
<h2>What to expect in a job posting</h2>
<p>Most Job Bank and Indeed postings show a job title, employer, location, pay, a work-location label and the date posted. Pay may be hourly or yearly. If the wage says “to be negotiated,” the posting does not provide an amount.</p>
<p>Remote postings on Job Bank and major job boards normally state the permitted work location. “Remote, Canada” and “Remote, must live in British Columbia” describe different arrangements. Indeed’s employer guidance reserves a nationwide location for work that may be performed anywhere in Canada.</p>
<h2>Pay in the posting</h2>
<p>British Columbia’s pay transparency rules require expected pay or a pay range in covered publicly advertised job postings from 1 November 2023. For covered publicly advertised job postings in Ontario, rules in effect from 1 January 2026 require many employers with at least 25 employees to include expected compensation or a range, disclose whether they use artificial intelligence to screen applicants and say whether a vacancy exists. A posted range in Ontario cannot span more than $50,000 a year, and positions paying more than $200,000 a year are exempt. A posted range does not fix the amount in an offer of employment. Employers cannot require Canadian experience in those Ontario postings or related application forms.</p>
<p>Indeed’s hiring lab measured the Ontario change: pay appeared on 49 per cent of Ontario postings just before the rule, and on 71 per cent by June 2026. Most of those were ranges.</p>
<h2>Hours, time zone and pay for a second job</h2>
<p>For a second job, stated weekly hours and time zone usually matter more than a “flexible” label. A posted pay range describes the vacancy; the amount in a written offer may differ. Search steps are covered in <a href="article-where-to-look.html">How to search for remote work</a>.</p>
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
    "Remote, online and flexible work compared | Job Compass",
    "Why online, remote and flexible work in Canada describe where the work is done, how it is delivered and when it is done.",
    "reading.html",
    article(
        "Work types",
        "Remote, online and flexible work compared",
        "Remote, online and flexible often appear together in job postings, but each describes a different part of the arrangement.",
        """
<div class="takeaways"><h2>The short version</h2><ul>
<li>Remote describes where the work is done.</li>
<li>Online describes how the work is completed or delivered.</li>
<li>Flexible describes the hours or workload.</li>
<li>A job can include one, two or all three arrangements.</li>
</ul></div>
<h2>Work location</h2>
<p>Remote work is performed away from the employer’s usual workplace. Hybrid combines on-site and remote days; a posting that requires regular office attendance is hybrid rather than fully remote. The guide <a href="remote-work-canada.html">Remote work in Canada</a> provides more detail.</p>
<h2>How the work is delivered</h2>
<p>Online work is done or delivered over the internet, either from home or at the employer’s workplace. A posting that lists only “online job” may still require a specific workplace or province. The guide <a href="online-work-canada.html">Online work in Canada</a> provides more detail.</p>
<h2>Hours</h2>
<p>Flexible work may provide some choice over schedule or workload. In the Labour Force Survey, part-time work is usually fewer than 30 hours per week at a person’s main job. Flexible scheduling can apply to full-time or part-time employment; part-time refers to hours rather than a pay type or independent contract work. The <a href="flexible-work-canada.html">flexible-work guide</a> provides more detail.</p>
<h2>Why the difference matters</h2>
<p>For work alongside a main job, hours may be the main concern. For less commuting, location matters. For a particular kind of work, the duties matter most. If a posting uses these terms without defining them, the location, duties and hours need a closer look. Related guides cover <a href="article-read-a-remote-ad.html">job postings</a> and <a href="article-second-path.html">second jobs</a>.</p>
""",
    ),
)

PAGES["article-what-vacancies-mean.html"] = page(
    "article-what-vacancies-mean.html",
    "What the remote job market looks like in Canada | Job Compass",
    "How Canada’s vacancy figures relate to online, remote and flexible job searches on Job Bank.",
    "reading.html",
    article(
        "The market",
        "What the remote job market looks like in Canada",
        "Working from home is now a normal part of the Canadian job market. Remote jobs are still a small slice of all postings, which is why the remote filter helps.",
        """
<div class="statrow">
<div class="stat"><b>510,200</b><span>job vacancies, all industries, second quarter of 2026</span></div>
<div class="stat"><b>2.8%</b><span>vacancy rate, unchanged on the year</span></div>
<div class="stat"><b>3.0</b><span>unemployed people for every vacancy</span></div>
<div class="stat"><b>6.5%</b><span>unemployment rate, September 2026</span></div>
</div>
<h2>Remote jobs are a small slice of the market</h2>
<p>Statistics Canada’s Job Vacancy and Wage Survey counted 510,200 vacancies in the second quarter of 2026. The vacancy rate was 2.8 per cent. There were 3.0 unemployed people for every vacancy. In September 2026 the Labour Force Survey put unemployment at 6.5 per cent. Those numbers cover everything from offices to shops, trucks, kitchens and clinics. They are the backdrop, not the size of the remote job market.</p>
<p>Work-location data is more useful here. In May 2026, 11.4 per cent of employed Canadians worked exclusively from home, and 9.8 per cent had a hybrid arrangement. Working exclusively from home was slightly less common than one year earlier. A search for a part-time, online or remote second job is narrower still than these economy-wide figures.</p>
<h2>Why the remote filter matters</h2>
<p>In October 2026, Job Bank’s home page showed about 84,000 postings, while about 700 were marked remote. Counts change daily, but remote postings remain a small share of the total. Search methods and filters are covered in <a href="article-where-to-look.html">How to search for remote work</a>.</p>
<h2>One occupation that can be done online</h2>
<p>Software developers and programmers had 3,545 vacancies in that quarter, up about 35 per cent year over year, with an average offered hourly wage of $43.65. Offered wages are the amounts employers advertised for vacancies in that occupation. They do not represent pay for remote work generally. Pay varies by occupation and posting.</p>
<h2>Part-time remote work</h2>
<p>Part-time remote work is a narrower search than “any job,” so relevant postings may appear less often. A Job Bank alert can track new results. The national vacancy total does not measure an individual applicant’s prospects.</p>
<h2>Roles that may support remote or online delivery</h2>
<p>Work arrangement and occupation are separate details. Customer support, administration, scheduling and bookkeeping may be offered online when an employer’s systems support remote access. Software development, testing, data work and technical support are also commonly delivered online, although some positions include office or on-call requirements.</p>
<p>Writing, editing, design, marketing, tutoring, training, translation and consulting may appear as employment or independent contract work. These examples describe how work can be delivered; they are not a list of current openings. Each employer or client sets the job title, qualifications, hours and permitted work location.</p>
<h2>When and where opportunities appear</h2>
<p>Remote and part-time postings open and close throughout the year rather than on one national schedule. Job Bank alerts can report new matches from a saved occupation, location and hours search. Closing dates, fixed shifts, time zones and project deadlines determine whether a posting remains relevant to an applicant’s availability.</p>
<p>Job Bank provides current postings and labour-market information. An employer’s careers page can confirm that a vacancy is current and identify the application method. Provincial and territorial employment services provide regional information on wages, training and employment standards.</p>
<h2>Demand and competition differ by province</h2>
<p>Job Bank outlooks assess an occupation within a province or economic region. A high total vacancy count in one province does not necessarily mean more remote openings in a particular field. Remote postings may also attract applicants from several provinces, while residence, licensing, language and time-zone requirements can narrow the eligible group.</p>
<p>Minimum wage, pay-transparency requirements and employment standards depend on the applicable province, territory or federal jurisdiction. The guide to <a href="article-pay-and-province.html">pay and province</a> explains these distinctions.</p>
<h2>Qualifications, tools and response times</h2>
<p>A remote arrangement does not remove occupational requirements. Postings may specify education, licences, language ability, certifications, communication skills and experience working with limited on-site supervision. They may also name communication, project or technical tools and state who supplies the computer, software or other equipment.</p>
<p>There is no standard employer response period. Closing dates, application volume, screening steps and interview schedules shape the timeline. The employer’s messages are the relevant source for an application’s status. The guides to <a href="article-remote-cv.html">remote-work résumés</a> and <a href="article-read-a-remote-ad.html">job-posting details</a> cover applications in more detail.</p>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www150.statcan.gc.ca/n1/daily-quotidien/260915/dq260915a-eng.htm" rel="noopener">Statistics Canada: job vacancies, second quarter 2026</a></li>
<li><a href="https://www150.statcan.gc.ca/n1/daily-quotidien/261009/dq261009a-eng.htm" rel="noopener">Statistics Canada: Labour Force Survey, September 2026</a></li>
<li><a href="https://www150.statcan.gc.ca/n1/daily-quotidien/260605/dq260605a-eng.htm" rel="noopener">Statistics Canada: Labour Force Survey, May 2026, work location</a></li>
<li><a href="https://www.jobbank.gc.ca/findajob" rel="noopener">Job Bank: find a job</a></li>
<li><a href="https://www.jobbank.gc.ca/trend-analysis" rel="noopener">Job Bank: trend analysis by occupation and region</a></li>
</ul>
""",
    ),
)

PAGES["article-second-path.html"] = page(
    "article-second-path.html",
    "Why people take a second job | Job Compass",
    "Why people in Canada add online, remote or flexible work beside a main job, family or studies, using Statistics Canada’s reasons for holding more than one job.",
    "reading.html",
    article(
        "Second jobs",
        "Why people take a second job",
        "A second job may offset household costs, build experience in a preferred field or fit around study, caregiving and other commitments. Results depend on hours, pay and hiring.",
        """
<div class="takeaways"><h2>What people told Statistics Canada</h2><ul>
<li>34.9 per cent: to pay for essentials like groceries or housing.</li>
<li>34.8 per cent: to earn extra income.</li>
<li>14.5 per cent: to work in a field they were passionate about.</li>
<li>Hours and location decide whether a second job can fit beside the first.</li>
</ul></div>
<h2>How common is multiple jobholding?</h2>
<p>In 2023, 5.6 per cent of employed Canadians held more than one job at the same time, about 1.1 million people. Women were more likely to do so than men (6.4 per cent, compared with 4.8 per cent). In 2025, Statistics Canada’s annual count of multiple jobholders was 1,178,600. For some, one job does not cover household costs. Others use a second job to pursue a different kind of work.</p>
<p>Those August 2023 results come from a Statistics Canada Labour Force Survey supplement of workers aged 15 to 69 who already held more than one job.</p>
<h2>Why online, remote and flexible work suit a second job</h2>
<p>Most people who held two jobs in 2023 also held at least one part-time job: 89.9 per cent. A second commute can make schedules more difficult to combine. Remote work avoids that commute; flexible or part-time hours may fit around another shift, school or family, depending on the posting. Online delivery is common in customer support, writing, design, bookkeeping, tutoring and software development, though work location may still be remote, hybrid or on-site.</p>
<p>Home is already a workplace for a minority of employed Canadians. In May 2026, 11.4 per cent worked only from home, and 9.8 per cent split the week between home and another place. Those figures cover the whole economy rather than available remote jobs. They show that working from home is an established work arrangement in Canada.</p>
<h2>Different goals lead to different searches</h2>
<p>Household or extra-income goals usually begin with available hours and realistic pay expectations. Employee wages from a regular paycheque differ from self-employed or independent contract earnings, which can vary by month and client. Experience-focused searches emphasize demonstrated skills; résumé presentation is covered in <a href="article-remote-cv.html">Résumés for online and remote work</a>. When school, caregiving or health limits availability, part-time or flexible arrangements are a different search from full-time remote employment.</p>
<p>The guide to <a href="article-where-to-look.html">searching for remote work</a> covers Job Bank’s remote and hours filters. The <a href="path-check.html">search goals page</a> groups guides by common reasons for seeking additional work.</p>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www150.statcan.gc.ca/n1/pub/14-28-0001/2024001/article/00002-eng.htm" rel="noopener">Statistics Canada: Multiple jobholders, 2023</a></li>
<li><a href="https://www150.statcan.gc.ca/n1/daily-quotidien/230908/dq230908a-eng.htm" rel="noopener">Statistics Canada: Labour Force Survey, August 2023, reasons for multiple jobs</a></li>
<li><a href="https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410004901" rel="noopener">Statistics Canada: table 14-10-0049-01, multiple jobholders, 2025 annual</a></li>
<li><a href="https://www150.statcan.gc.ca/n1/daily-quotidien/260605/dq260605a-eng.htm" rel="noopener">Statistics Canada: Labour Force Survey, May 2026, work location</a></li>
</ul>
""",
    ),
)

PAGES["article-where-to-look.html"] = page(
    "article-where-to-look.html",
    "How to search for remote work in Canada | Job Compass",
    "How to search Job Bank for remote and part-time work in Canada, and how those filters differ from the words work from home.",
    "reading.html",
    article(
        "Where to look",
        "How to search for remote work",
        "Job Bank searches typically begin with a job title matched to skills; remote and hours filters narrow results more reliably than generic phrases.",
        """
<div class="takeaways"><h2>Job Bank search options</h2><ul>
<li>A job title that fits your skills, not just the words “work from home.”</li>
<li>Job Bank’s remote filter, if you want a fully remote job.</li>
<li>An hours filter for work alongside a main job.</li>
<li>A job alert, so new matches land in your inbox.</li>
<li>The employer’s own careers page, before you apply.</li>
</ul></div>
<h2>What Job Bank means by remote</h2>
<p>Job Bank lets employers label a job in one of four ways. Remote means the work is done from a place you choose, like a home office. Hybrid means part in person and part remote, with the split agreed with the employer. On-site means a place the employer names, with no remote option. On the road means the location changes because the job involves travel.</p>
<p>Searching only for “work from home” can bring up hybrid and on-site postings that mention a home elsewhere in the text. For fully remote work, the work-location filter is more reliable than keywords alone. On <a href="https://www.jobbank.gc.ca/findajob" rel="noopener">Job Bank’s Find a job page</a>, the search uses a job title and location, with Remote selected under work location.</p>
<h2>Hours for a second job</h2>
<p>The same results page can filter by hours. For someone with a main job, the part-time filter narrows the search to additional hours. Statistics Canada counts part-time as under 30 hours a week at the main job, and a second job can involve far fewer. Weekly hours or project deadlines are normally included in the posting. Full-time remote work is a different search, since it is usually a main job done from home.</p>
<p>Remote results may list employers across Canada regardless of the city entered in the search. Province and employer location still matter for eligibility and pay rules; details are covered in <a href="article-pay-and-province.html">What a second paycheque changes</a>.</p>
<h2>Job alerts</h2>
<p>Job Bank can send email when a new posting matches saved filters. An alert is created from the results page and confirmed through the email Job Bank sends. Alerts can be changed or stopped, and Job Bank is free.</p>
<p>The same vacancy is often listed on the employer’s careers site; applications may go through that site or Job Bank. Posting details are covered in the <a href="article-read-a-remote-ad.html">job-posting guide</a>.</p>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www.jobbank.gc.ca/findajob" rel="noopener">Job Bank: find a job</a></li>
<li><a href="https://www.jobbank.gc.ca/support/question?mtid=2&amp;qaid=222&amp;tid=7" rel="noopener">Job Bank: remote, hybrid, on-site and on the road</a></li>
<li><a href="https://www.jobbank.gc.ca/support/question?qaid=143&amp;tid=7" rel="noopener">Job Bank: why remote jobs from other places appear, and which wage rules they name</a></li>
</ul>
""",
    ),
)

PAGES["article-remote-cv.html"] = page(
    "article-remote-cv.html",
    "Résumés for online and remote work | Job Compass",
    "Résumé information for online and remote work, including results, communication, tools and location.",
    "reading.html",
    article(
        "Application",
        "Résumés for online and remote work",
        "For remote and online roles, employers often assess prior results, written communication and the capacity to work with limited on-site supervision.",
        """
<div class="takeaways"><h2>Relevant resume information</h2><ul>
<li>Results you delivered on your own.</li>
<li>The tools you use, named plainly.</li>
<li>A short summary at the top.</li>
<li>Your city and province, including any geographic work restrictions.</li>
</ul></div>
<h2>What employers look for</h2>
<p>For online and remote roles, employers often look for reliable work completed with limited supervision. Each relevant role normally states outcomes, such as requests resolved, reports delivered, classes taught or releases maintained, and names the communication and project tools used. Availability is normally better placed in an application or cover letter than at the top of a résumé.</p>
<h2>Information not needed in an application</h2>
<p>The job title and relevant results are sufficient. Social insurance numbers, identification and banking details do not belong in an initial application. City and province usually provide enough location information.</p>
<h2>Resume review</h2>
<p>A skim-read résumé should surface outcomes and tools rather than duty lists alone. Applications are submitted on the employer’s site or through Job Bank. Search options are listed in <a href="article-where-to-look.html">How to search for remote work</a>.</p>
""",
    ),
)

PAGES["article-pay-and-province.html"] = page(
    "article-pay-and-province.html",
    "What a second paycheque changes | Job Compass",
    "Which pay rules to check for online and remote work in Canada, and what changes when the work is a second job.",
    "reading.html",
    article(
        "Pay",
        "What a second paycheque changes",
        "A second job may add income, while minimum-wage rules, payroll deductions and employment status affect the amount and how it is paid.",
        """
<div class="takeaways"><h2>The short version</h2><ul>
<li>There is no single minimum wage for every remote job in Canada. It depends on the federal rate or the province or territory in the posting.</li>
<li>Banks, airlines, federally regulated telecommunications companies and interprovincial transportation businesses follow the Canada Labour Code.</li>
<li>Job Bank says a remote posting follows the wage rules of the employer’s province, which may not be yours.</li>
<li>A second employer still deducts tax and Canada Pension Plan contributions. The CRA has current instructions for filling out Form TD1.</li>
</ul></div>
<h2>Minimum wage for remote work</h2>
<p>Minimum wage is set province by province, with a separate federal rate for federally regulated employees. From 1 April 2026 the federal rate is $18.15 an hour. If the provincial general rate is higher, a federally regulated employer must meet the higher one. Alberta’s general rate is $15. British Columbia’s is $18.25 from 1 June 2026. Ontario’s is $17.95 from 1 October 2026. Quebec’s is $16.60 from 1 May 2026. Rates change often; the current figure should be confirmed through the <a href="https://minwage-salairemin.service.canada.ca/en/general.html" rel="noopener">federal minimum-wage database</a> and the relevant provincial or territorial government site.</p>
<p>Job Bank says remote jobs follow the wage rules of the province where the employer is located, which can differ from where the worker lives. The province named in the posting is therefore an important detail. The applicable law can depend on the employment arrangement.</p>
<h2>What job postings must show in B.C. and Ontario</h2>
<p>Pay transparency rules in British Columbia and Ontario affect what must appear in many publicly advertised postings. Details and exceptions are covered in <a href="article-read-a-remote-ad.html">How to read a remote job posting</a>. A posted range is not a written offer. Quebec employment standards are administered by CNESST, while workplace-language requirements are overseen by the OQLF under the Charter of the French Language.</p>
<h2>A second paycheque</h2>
<p>If you already have an employer, a second employer still deducts income tax from your pay. If you have already claimed your personal tax credits on another TD1 and your total income will go past them, you generally enter zero on the second TD1 and tick the matching box. The CRA’s current instructions cover your exact situation.</p>
<p>Each employer works out CPP deductions on its own. If the two jobs together push you over the yearly maximum, the extra contribution can be refunded or applied to tax owing when you file (it goes on line 44800). Quebec uses the Quebec Pension Plan, which works a little differently. Rates change every year, so check the CRA for the latest.</p>
<p>A contract that uses the word “freelance” does not by itself establish independent-contractor or self-employed status. The Canada Revenue Agency considers control, tools, subcontracting, financial risk and opportunity for profit when assessing employment status.</p>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/pay-deductions.html" rel="noopener">Canada.ca: pay, deductions and the federal minimum wage</a></li>
<li><a href="https://www.jobbank.gc.ca/support/question?qaid=143&amp;tid=7" rel="noopener">Job Bank: remote jobs and wage regulations</a></li>
<li><a href="https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/income-tax.html" rel="noopener">Canada Revenue Agency: income tax when an employee has different jobs</a></li>
<li><a href="https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp.html" rel="noopener">Canada Revenue Agency: CPP when an employee has different jobs</a></li>
<li><a href="https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-44800-cpp-overpayment.html" rel="noopener">Canada Revenue Agency: line 44800, CPP or QPP overpayment</a></li>
</ul>
""",
    ),
)

PAGES["path-check.html"] = page(
    "path-check.html",
    "Search goals for flexible work | Job Compass",
    "Common reasons for considering additional work in Canada, with links to related Job Compass guides.",
    "reading.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Search goals</span><h1>Reasons for considering additional work</h1><p class="lede">Four common goals link to different starting guides. The choice stays in the browser and is not sent to Job Compass.</p></div></div>
<section><div class="wrap" style="max-width:760px">
<form id="path-check">
<ul class="check">
<li><label><input type="radio" name="hope" value="essentials"> Income for essentials such as housing and groceries</label></li>
<li><label><input type="radio" name="hope" value="extra"> Additional income without full-time hours</label></li>
<li><label><input type="radio" name="hope" value="craft"> Experience in a preferred field</label></li>
<li><label><input type="radio" name="hope" value="hours"> Hours that fit school, caregiving or health needs</label></li>
</ul>
</form>
<div id="path-result" class="result" hidden><h3></h3><p></p><p><a id="path-next" href="article-second-path.html">Read the guide</a></p></div>
<p class="notice" style="margin-top:1.5rem">The percentages come from Statistics Canada (August 2023) and describe people who already had more than one job. They do not predict earnings. For the full picture, read <a href="article-second-path.html">Why people take a second job</a>.</p>
</div></section>
""",
)

PAGES["glossary.html"] = page(
    "glossary.html",
    "Glossary | Job Compass",
    "Definitions for remote, hybrid, online, flexible, NOC, EI, CPP, LMIA and other terms used in Canadian job postings.",
    "reading.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Glossary</span><h1>Terms used in job postings</h1><p class="lede">Definitions of terms found in Canadian remote, online and flexible job postings. Legal rights and obligations depend on the applicable official source.</p></div></div>
<section><div class="wrap">
<label class="notice" for="glossary-search">Search terms</label>
<input id="glossary-search" class="search" type="search" placeholder="Try “remote”, “EI” or “contractor”">
<dl class="glossary">
<div class="term"><dt>Remote</dt><dd>Work is completed away from the employer’s office. The position may still be limited to a province or time zone.</dd></div>
<div class="term"><dt>Hybrid</dt><dd>Part of the work is remote and part is at a set location. It is not fully remote.</dd></div>
<div class="term"><dt>On-site</dt><dd>Work completed at a location set by the employer, with no remote option.</dd></div>
<div class="term"><dt>Online work</dt><dd>Work done or delivered over the internet. The term alone does not specify location or hours.</dd></div>
<div class="term"><dt>Flexible work</dt><dd>Work that offers some choice over hours, schedule or workload.</dd></div>
<div class="term"><dt>Part-time</dt><dd>Under 30 hours a week at your main or only job, by Statistics Canada’s definition. A second job can be shorter.</dd></div>
<div class="term"><dt>Second job</dt><dd>A job held at the same time as another job.</dd></div>
<div class="term"><dt>Additional work</dt><dd>A second job, freelance contract or other paid work held alongside employment, self-employment or study.</dd></div>
<div class="term"><dt>Job Bank</dt><dd>The Government of Canada’s job board. Filters include occupation, location, hours and remote work.</dd></div>
<div class="term"><dt>NOC</dt><dd>National Occupational Classification. A code for an occupation, used on Job Bank and in labour statistics.</dd></div>
<div class="term"><dt>Vacancy</dt><dd>A position an employer is trying to fill. Statistics Canada counts vacancies through a survey, so its numbers differ from the postings on a website.</dd></div>
<div class="term"><dt>Offered wage</dt><dd>The wage advertised for an open position. It is neither the average pay of current workers nor a written offer.</dd></div>
<div class="term"><dt>CPP</dt><dd>Canada Pension Plan. Contributions can apply to any employment, part-time included. The Canada Revenue Agency posts current rates.</dd></div>
<div class="term"><dt>EI</dt><dd>Employment Insurance. Premiums and benefits have their own rules, and the word “freelance” does not determine them.</dd></div>
<div class="term"><dt>Independent contractor</dt><dd>Someone in business for themselves. The CRA considers control, tools, financial risk and opportunity for profit rather than relying only on the wording of a contract.</dd></div>
<div class="term"><dt>LMIA</dt><dd>Labour Market Impact Assessment. A step employers may need to take before hiring certain temporary foreign workers. It is not a job, and job seekers should never pay for one.</dd></div>
<div class="term"><dt>TD1</dt><dd>The form where an employee claims personal tax credits with an employer. Those credits are normally claimed with one employer, not again at a second job.</dd></div>
<div class="term"><dt>Gig</dt><dd>A short contract, one-off assignment or task, often arranged through an app or platform. Hours and income can vary, and some provinces have specific rules for platform workers.</dd></div>
</dl>
<p id="glossary-empty" hidden>No matching term. Try another word.</p>
</div></section>
""",
)

PAGES["faq.html"] = page(
    "faq.html",
    "FAQ | Job Compass",
    "Answers about Job Compass and about online, remote and flexible work in Canada.",
    "reading.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">FAQ</span><h1>Questions about remote and flexible work</h1></div></div>
<section><div class="wrap" style="max-width:820px">
<details><summary>Does Job Compass list jobs?</summary><p>No. Job Compass publishes guides to online, remote and flexible work and explains how hiring works. Current openings are available through Job Bank and employers’ career pages.</p></details>
<details><summary>Is Job Compass a recruitment agency?</summary><p>No. Job Compass is an independent publisher, not a licensed employment agency. It does not screen, place or introduce candidates, and it does not charge readers.</p></details>
<details><summary>Why only online, remote and flexible work?</summary><p>These arrangements can be easier to fit around a main job, school or family responsibilities. Job Compass covers work completed online or away from the employer’s office, including part-time and flexible arrangements.</p></details>
<details><summary>Why do people take a second job?</summary><p>In August 2023, Canadians with more than one job most often cited essentials (34.9 per cent), extra income (34.8 per cent) or work they cared about (14.5 per cent). <a href="article-second-path.html">Why people take a second job</a> provides the full figures. The <a href="path-check.html">search goals page</a> groups related guides by reason.</p></details>
<details><summary>Is remote work common in Canada?</summary><p>In May 2026, 11.4 per cent of employed Canadians worked only from home and 9.8 per cent had a hybrid week. Remote positions represent a small share of Job Bank postings. Searches are generally more useful when they combine an occupation or job title with the remote filter. <a href="article-where-to-look.html">Finding remote and online postings</a> explains the available sources.</p></details>
<details><summary>What is the difference between remote and online?</summary><p>Remote describes where the work takes place. Online describes how the work is completed or delivered. A position can be one, the other or both. <a href="article-three-arrangements.html">Remote, online and flexible work</a> compares the arrangements.</p></details>
<details><summary>Will I be paid a set amount?</summary><p>A set amount applies only when it forms part of an employment or contract offer. Nothing on Job Compass is a job offer or a promise of earnings.</p></details>
<details><summary>Which province’s rules apply if I work from home?</summary><p>It depends on where you work, where the employer operates, the type of business and your employment relationship. Federally regulated workplaces follow federal labour standards. <a href="article-pay-and-province.html">What a second paycheque changes</a> has more, with official links.</p></details>
<details><summary>Can this work be done in addition to a current job?</summary><p>Additional work may be possible when the schedules are compatible and the existing employment agreement permits it. In 2023, 89.9 per cent of Canadians with two jobs had at least one part-time job. Employment agreements may also include conflict-of-interest requirements. The guides cover <a href="flexible-work-canada.html">flexible hours</a> and <a href="article-pay-and-province.html">pay for a second job</a>.</p></details>
<details><summary>Is French content available for Quebec?</summary><p>Not yet. These pages are in English. In Quebec, employment standards are handled by the CNESST, while workplace language requirements fall under the Charter of the French Language and the OQLF. Current information is available from those organizations.</p></details>
<p style="margin-top:2rem">Questions not covered here can be sent through the <a href="contact.html">contact page</a>.</p>
</div></section>
""",
)

PAGES["services.html"] = page(
    "services.html",
    "Why people look for extra work | Job Compass",
    "Why people in Canada consider online, remote and flexible work, and how clear guidance can help them make informed choices.",
    "services.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Reasons for additional work</span><h1>Why people look for extra work.</h1><p class="lede">Additional work can help with everyday costs, build experience or provide hours that fit around a main job, school or family responsibilities.</p></div></div>
<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">Everyone has a reason</span><h2>Why people take on more work.</h2><p class="lede">In August 2023, Statistics Canada asked people with more than one job for their main reason. Income was the main reason for many respondents, but not for everyone.</p></div>
<div class="tiles">
<article class="tile reveal"><h3>Help with everyday costs</h3><p>Paying for essentials like groceries or housing was the top reason.</p></article>
<article class="tile reveal"><h3>Add income</h3><p>Nearly as many wanted money beyond what their main job pays.</p></article>
<article class="tile reveal"><h3>Build experience</h3><p>Some wanted to do work they care about, and a second job can be a practical way to get experience in a new field.</p></article>
<article class="tile reveal"><h3>Find hours that fit</h3><p>Part-time or flexible work can fit around a main job, school, family or health needs.</p></article>
</div>
<p class="src-note">Source: Statistics Canada, August 2023, people aged 15 to 69 who already had more than one job. These results describe current multiple jobholders rather than the outcome of a new job search. <a href="article-second-path.html">See the full numbers</a>.</p>
</div></section>
<section class="alt"><div class="wrap split">
<div><span class="eyebrow">What changes with each type</span><h2>Where, how and when you work.</h2>
<p><b>Remote work</b> can reduce or remove the commute, though some positions still require residence in a particular province or availability in a particular time zone.</p>
<p><b>Online work</b> is completed or delivered over the internet, but it is not necessarily remote or flexible.</p>
<p><b>Flexible work</b> can mean a shorter week or more control over working hours. The employer or client, expected workload, schedule and method of payment determine how flexible the arrangement is in practice.</p>
<p><a href="work-types.html">See how the three compare &rarr;</a></p></div>
<div><span class="eyebrow">About Job Compass</span><h2>Canadian sources in one place.</h2>
<p>Information about remote work is spread across job postings, Job Bank, Statistics Canada, the Canada Revenue Agency and provincial websites.</p>
<p>Job Compass brings those sources together in guides on work arrangements, job searches, applications, pay and employment status.</p>
<p>Job Compass is an independent publisher. The <a href="about.html">About page</a> describes its editorial approach.</p></div>
</div></section>
<section><div class="wrap split">
<div><span class="eyebrow">More than a paycheque</span><h2>Practical needs and personal goals both count.</h2>
<p>Additional work can take the form of a second job that supports household costs, a freelance project that builds experience or a flexible position that fits an existing schedule.</p>
<p>The information is for people already considering additional work and comparing their options.</p></div>
<div><span class="eyebrow">Topics covered</span><h2>From work arrangements to pay.</h2>
<ol class="note-list">
<li>Priorities such as location, hours, income and experience.</li>
<li>Differences among remote, online and flexible work.</li>
<li>Occupation-based searches and relevant filters.</li>
<li>Employer, location, hours, pay and employment status.</li>
<li>Official sources for legal, tax and employment rules.</li>
</ol>
<div class="btn-row"><a class="btn btn-primary" href="path-check.html">Explore search goals</a><a class="btn btn-ghost" href="reading.html">Browse all guides</a></div></div>
</div></section>
""",
)

PAGES["about.html"] = page(
    "about.html",
    "About | Job Compass",
    "Job Compass is an independent Canadian publisher covering online, remote and flexible work, and how employers hire for that work.",
    "about.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Independent publisher</span><h1>About Job Compass</h1><p class="lede">Canadian information on remote, online and flexible work, grounded in public sources and practical job-search needs.</p></div></div>
<section><div class="wrap split">
<div class="reveal">
<h2>Who the guides are for</h2>
<p>Job Compass is an independent Canadian publisher for people considering online work, a remote position or flexible hours around a main job, family or school. The guides explain how these arrangements differ, where paid opportunities are advertised and how hours, pay and employment status affect the choice. Job Compass is not connected to Job Bank, Statistics Canada or any provincial or territorial government.</p>
<p>Job Compass is not a licensed employment agency. It does not post job openings or send reader information to employers.</p>
</div>
<div class="reveal">
<h2>Editorial approach</h2>
<div class="types">
<div class="type" style="grid-template-columns:1fr"><div><h3>Defined scope</h3><p>Coverage focuses on remote, online, part-time and flexible arrangements. Fully on-site positions are outside the editorial scope.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Backed by sources</h3><p>Labour figures come from Statistics Canada, search tips from Job Bank, and pay and tax information from the Canada Revenue Agency and the right provincial, territorial or federal authority.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Dated and reviewed</h3><p>Each guide shows when it was last reviewed, and wage and vacancy figures say which period they cover.</p></div></div>
</div>
</div>
</div></section>
<section class="alt"><div class="wrap">
<p class="notice" style="max-width:70ch">Job Compass publishes general information rather than legal, tax or employment advice. Contact: hello@jobcompass.ca. Job Compass operates online and has no public office.</p>
</div></section>
""",
)

PAGES["contact.html"] = page(
    "contact.html",
    "Contact | Job Compass",
    "Questions about Canadian work arrangements, job searches, postings, applications, pay and employment status can be sent to Job Compass by email.",
    "contact.html",
    f"""
<div class="page-head"><div class="wrap"><span class="eyebrow">Questions and feedback</span><h1>Contact Job Compass</h1><p class="lede">Questions are welcome on work arrangements, job searches, Job Bank and employer postings, applications, pay, employment status and sources cited in the guides. Replies point to published guides or official sources rather than personalized legal or job-placement advice.</p></div></div>
<section><div class="wrap split">
<div>
<form id="contact-form" class="form" novalidate>
<div class="field"><label for="name">Name</label><input id="name" required autocomplete="name"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">Email</label><input id="email" type="email" required autocomplete="email"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="province">Province or territory</label><select id="province"><option value="">Prefer not to say</option><option>Alberta</option><option>British Columbia</option><option>Manitoba</option><option>New Brunswick</option><option>Newfoundland and Labrador</option><option>Northwest Territories</option><option>Nova Scotia</option><option>Nunavut</option><option>Ontario</option><option>Prince Edward Island</option><option>Quebec</option><option>Saskatchewan</option><option>Yukon</option><option>Outside Canada</option></select></div>
<div class="field"><label for="topic">Topic</label><select id="topic"><option>Work arrangements</option><option>Job search and Job Bank</option><option>Reading a job posting</option><option>Applications and résumés</option><option>Pay, deductions and employment status</option><option>Freelance or contract work</option><option>Guide feedback or source correction</option><option>Other question about the guides</option></select></div>
<div class="field"><label for="msg">Your question</label><textarea id="msg" required></textarea><div class="err" aria-live="polite"></div></div>
<button class="btn btn-primary" type="submit">Open email</button>
<p class="notice">The form prepares a message in the device’s email application. Information entered here is not stored by this website.</p>
</form>
<div id="form-ok" class="ok" hidden tabindex="-1" role="status"><h3>Your email message is ready.</h3><p>Review it in your email app before sending.</p><p class="ok-sub">If the app did not open, email {EMAIL}.</p></div>
</div>
<div>
<h2>Email</h2>
<ul class="contact-list"><li><b>Questions</b><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul>
<p class="notice">Replies provide general information and links to published guides or official sources. Job offers are not reviewed, and legal, tax or immigration advice is not provided. Social insurance numbers, banking information, identification and passwords should not be included.</p>
</div>
</div></section>
""",
)

PAGES["privacy.html"] = page(
    "privacy.html",
    "Privacy | Job Compass",
    "How Job Compass handles personal information. The contact form opens your email app. The path check and search run in your browser.",
    "contact.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Personal information</span><h1>Privacy</h1><p class="lede">How information is handled when the site or contact form is used. Last updated 28 October 2026.</p></div></div>
<section><div class="wrap article">
<p>Job Compass is an independent publisher. The site has no user accounts. This notice describes the limited personal information that may be involved when the site is used. It reflects the fair information principles in Canada’s Personal Information Protection and Electronic Documents Act (PIPEDA). Provincial privacy laws, including Quebec’s, may also apply depending on the reader’s location and how a message is handled.</p>
<h2>Information sent by email</h2>
<p>The contact form does not submit information to the site’s server. It opens the reader’s email application with a message addressed to hello@jobcompass.ca. A sent message may include a name, email address, province and question. This information is used to reply and improve the guides. It is not sold or added to a marketing list.</p>
<p>Social insurance numbers, banking details, identification and passwords should not be included. Job Compass does not request them.</p>
<h2>Information that stays on the device</h2>
<p>The path check and glossary search run in the browser. Selections and search terms are not transmitted to Job Compass by those tools.</p>
<h2>Fonts and server logs</h2>
<p>Pages request typefaces from Google Fonts. That request can expose the reader’s IP address to Google. The hosting provider may keep ordinary server logs, such as IP address, browser and page requested, for security. Job Compass does not add an analytics tracker to these pages.</p>
<h2>How long a message is kept</h2>
<p>Email is kept only as long as needed to reply, maintain a record or meet a legal obligation. It is then deleted or anonymised. A request to access, correct or delete a message can be sent to hello@jobcompass.ca. Verification may be required from the email account concerned.</p>
<h2>Other sites</h2>
<p>Articles link to Job Bank, Statistics Canada, the Canada Revenue Agency and provincial pages. Those sites have separate privacy notices and are not controlled by Job Compass.</p>
</div></section>
""",
)

PAGES["disclaimer.html"] = page(
    "disclaimer.html",
    "Disclaimer | Job Compass",
    "Job Compass publishes general information on online, remote and flexible work in Canada. It does not hire candidates or guarantee employment or income.",
    "about.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Scope and limitations</span><h1>Disclaimer</h1></div></div>
<section><div class="wrap article">
<h2>A publisher, not an agency</h2>
<p>Job Compass publishes general information about online, remote and flexible work in Canada and how employers hire for that work. It is not a licensed employment agency and does not publish job postings, hire, screen, place or introduce candidates. Readers are not charged a fee.</p>
<h2>No guarantee of employment or income</h2>
<p>Nothing on this site is a job offer or a promise of earnings. Pay, hours and eligibility depend on the employer, where the rules apply and the terms of the job.</p>
<h2>Not professional advice</h2>
<p>The pages provide general information, not legal, tax, immigration or employment advice. Most employment standards are provincial or territorial. Federally regulated workplaces follow the Canada Labour Code. Quebec has distinct employment and workplace-language requirements. Advice for an individual situation should come from the responsible authority or a qualified adviser.</p>
<h2>Figures go out of date</h2>
<p>Statistics are dated and linked to their sources. Vacancy counts, minimum wages and posting rules can change after a guide is reviewed. Current figures remain available from the linked source, and possible errors can be reported through the <a href="contact.html">contact page</a>.</p>
<h2>Other websites</h2>
<p>Links to Job Bank, Statistics Canada and other sites provide access to original sources. Job Compass is not responsible for third-party content.</p>
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
