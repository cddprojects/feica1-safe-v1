#!/usr/bin/env python3
"""Render the Job Compass static site."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "site"
EMAIL = "hello@jobcompass.ca"
THEME = "#243552"

LEAF = (
    "M50 2 42 20 35 15 37 34 24 27 21 32 6 24 11 52 1 56 26 77 22 87 46 83 "
    "46 100 54 100 54 83 78 87 74 77 99 56 89 52 94 24 79 32 76 27 63 34 65 15 58 20Z"
)

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
    ("services.html", "Why it matters"),
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
<p style="margin-top:1rem;max-width:36ch">An independent Canadian publisher covering online, remote and flexible work for people considering a second job or an additional source of income.</p></div>
<div><h4>Guides</h4><ul>
<li><a href="reading.html">All articles</a></li>
<li><a href="work-types.html">Work types</a></li>
<li><a href="path-check.html">Find the right guide</a></li>
<li><a href="glossary.html">Glossary</a></li>
<li><a href="faq.html">FAQ</a></li>
</ul></div>
<div><h4>Publisher</h4><ul>
<li><a href="about.html">About</a></li>
<li><a href="services.html">Why this work matters</a></li>
<li><a href="contact.html">Contact</a></li>
<li><a href="privacy.html">Privacy</a></li>
<li><a href="disclaimer.html">Disclaimer</a></li>
</ul></div>
</div>
<div class="legal"><p>Job Compass is an independent publisher. We are not Job Bank, Statistics Canada or a provincial employment service, and we are not a licensed employment agency. We do not recruit, screen, place or introduce candidates, and we do not publish job postings. Our guides provide general information, not legal, tax or employment advice. Confirm the rules that apply to you with the appropriate government authority.</p>
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
<p style="margin-top:2.5rem"><a href="reading.html">&larr; All articles</a></p>
</div></section>"""


PAGES = {}

PAGES["index.html"] = page(
    "index.html",
    "Remote, online and flexible work in Canada | Job Compass",
    "Explore independent Canadian guides to work from home, remote work, part-time roles, online work, freelance work and side jobs.",
    "index.html",
    f"""
<section class="hero"><div class="wrap hero-grid">
<div>
<span class="eyebrow">Independent job guidance for Canadians</span>
<h1>Looking for online or remote work in <em>Canada?</em></h1>
<p class="lede">Free guides for anyone considering work from home, remote, part-time or freelance work, including as a second job. Learn how each type works, where to search and what to check before you apply.</p>
<ul class="hero-points">
<li><b>What the terms mean.</b> Remote, online, hybrid and part-time are not the same thing, and a job posting does not always say which one it is.</li>
<li><b>Where to search.</b> The Job Bank filters that narrow results to remote and part-time positions.</li>
<li><b>What a posting should tell you.</b> Employer, work location, pay, hours and employment status.</li>
<li><b>Pay and tax basics.</b> What changes with a second job, and why your province matters.</li>
</ul>
<div class="btn-row"><a class="btn btn-primary" href="reading.html">Explore the guides</a><a class="btn btn-ghost" href="path-check.html">Find your starting point</a></div>
<p class="hero-note">Job Compass is a guide, not a job board. We do not list jobs or charge fees.</p>
</div>
<div class="hero-art">
{HERO_ART}
<div class="modes">
<h2 class="sr">Three types of flexible work</h2>
<a class="mode" href="remote-work-canada.html"><span class="dot"></span><span><b>Remote work</b><small>Work outside the employer’s regular workplace under a clear location agreement.</small></span><span class="tag">Where</span></a>
<a class="mode" href="online-work-canada.html"><span class="dot"></span><span><b>Online work</b><small>Do work such as customer support, writing, design, bookkeeping, tutoring or software development online.</small></span><span class="tag">How</span></a>
<a class="mode" href="flexible-work-canada.html"><span class="dot"></span><span><b>Part-time &amp; flexible</b><small>Fit work around a main job, studies, family responsibilities or your preferred schedule.</small></span><span class="tag">When</span></a>
</div>
</div>
</div></section>

<section class="alt"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Why people take a second job</span><h2>Extra income, a new field or a schedule that fits.</h2></div>
<ol class="shifts">
<li class="reveal"><span class="no">34.9%</span><h3>Everyday needs</h3><p>Some people take additional work to help pay for housing, groceries and other essentials.</p></li>
<li class="reveal"><span class="no">34.8%</span><h3>Extra income</h3><p>For almost the same share, a second job was a way to earn income beyond the basics.</p></li>
<li class="reveal"><span class="no">14.5%</span><h3>Work they cared about</h3><p>For others, a second job let them work in a field they cared about.</p></li>
</ol>
<p class="src-note">Statistics Canada asked people aged 15 to 69 who held more than one job about their main reason in August 2023. These figures describe their answers—not an expected result for a new reader.</p>
</div></section>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">Popular guides</span><h2>What Canadians ask about flexible work.</h2><p class="lede">Short reads on remote, online and part-time work, with official sources linked.</p></div>
<div class="posts">
<article class="post reveal"><div class="meta"><span class="cat">Second jobs</span><span>7 min</span></div><h3><a href="article-second-path.html">Why people take a second job</a></h3><p>Extra income is only part of the story. Time, location and meaningful work also matter.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Where to look</span><span>6 min</span></div><h3><a href="article-where-to-look.html">How to search for remote work</a></h3><p>Start with a role that matches your skills, then use Job Bank’s remote and hours filters to narrow the results.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Work types</span><span>6 min</span></div><h3><a href="article-three-arrangements.html">Remote, online or flexible: which one do you need?</a></h3><p>One changes where you work, one describes how the work is completed, and one changes your work schedule.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Before you apply</span><span>7 min</span></div><h3><a href="article-read-a-remote-ad.html">How to read a remote job posting</a></h3><p>Check the employer, location, pay and hours before you apply.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Your application</span><span>5 min</span></div><h3><a href="article-remote-cv.html">Tailor your resume for online and remote work</a></h3><p>Highlight completed work, digital tools and clear communication.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Pay</span><span>7 min</span></div><h3><a href="article-pay-and-province.html">What a second paycheque changes</a></h3><p>Pay rules, province, deductions and the difference between employment and freelance work.</p></article>
</div>
</div></section>

<section class="alt" id="recruitment"><div class="wrap split">
<div class="reveal"><span class="eyebrow">Before you apply</span><h2>Five steps before you start searching.</h2></div>
<div class="reveal">
<p class="lede">Remote, online and freelance postings can look alike in search results. These steps help you sort them out.</p>
<ol class="note-list">
<li>Start with the change you want: more room in the budget, a different field, fewer hours or less travel.</li>
<li>Decide how many hours you can realistically work in a part-time job or side job.</li>
<li>Decide whether you need fully remote work or simply want some work-from-home days.</li>
<li>Search <a href="https://www.jobbank.gc.ca/findajob" rel="noopener">Job Bank</a> by occupation, then use the remote and hours filters.</li>
<li>Before you apply, check the employer, pay, province and whether you would be an employee or an independent contractor.</li>
</ol>
<p><a href="article-where-to-look.html">Build a more focused search &rarr;</a></p>
</div>
</div></section>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">Browse by type of work</span><h2>Find the guide that matches the work.</h2></div>
<div class="minis">
<a class="mini reveal" href="remote-work-canada.html"><b>Work from home</b><span>Understand fully remote and hybrid arrangements.</span></a>
<a class="mini reveal" href="online-work-canada.html"><b>Online work</b><span>Explore work that can be completed over the internet.</span></a>
<a class="mini reveal" href="flexible-work-canada.html"><b>Part-time &amp; flexible</b><span>Look at hours that can fit around the rest of your week.</span></a>
<a class="mini reveal" href="article-second-path.html"><b>Freelance work &amp; side jobs</b><span>Consider additional work without assuming a set income.</span></a>
</div>
</div></section>

<section class="alt" id="contact"><div class="wrap split">
<div><span class="eyebrow">Ask a question</span><h2>Not sure where to start?</h2><p class="lede">Ask about online, remote, work-from-home, part-time or flexible work in Canada. We will point you to the right guide or official source. We cannot place you in a job or review a job offer, and please never send identification or banking information.</p></div>
<div>
<form id="contact-form" class="form" novalidate>
<div class="field"><label for="name">Name</label><input id="name" required autocomplete="name"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">Email</label><input id="email" type="email" required autocomplete="email"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="province">Province or territory</label><select id="province"><option value="">Prefer not to say</option><option>Alberta</option><option>British Columbia</option><option>Manitoba</option><option>New Brunswick</option><option>Newfoundland and Labrador</option><option>Northwest Territories</option><option>Nova Scotia</option><option>Nunavut</option><option>Ontario</option><option>Prince Edward Island</option><option>Quebec</option><option>Saskatchewan</option><option>Yukon</option><option>Outside Canada</option></select></div>
<div class="field"><label for="topic">What is your question about?</label><select id="topic"><option>Remote work</option><option>Online work</option><option>Work from home</option><option>Part-time or flexible work</option><option>Freelance or side job</option><option>Pay, tax or employment status</option><option>Another job-related question</option></select></div>
<div class="field"><label for="msg">Your question</label><textarea id="msg" required placeholder="For example: Which Job Bank filter shows fully remote, part-time positions in Alberta?"></textarea><div class="err" aria-live="polite"></div></div>
<button class="btn btn-primary" type="submit">Send my question</button>
<p class="notice">This opens your email app, addressed to {EMAIL}. We do not store the form on a server.</p>
</form>
<div id="form-ok" class="ok" hidden tabindex="-1" role="status"><h3>Your email app should be open.</h3><p>Send the message from there when you are ready.</p><p class="ok-sub">If nothing opened, write to {EMAIL}.</p></div>
</div>
</div></section>
""",
)

PAGES["reading.html"] = page(
    "reading.html",
    "Reading | Job Compass",
    "Canadian guides to work from home, remote work, online work, part-time roles, freelance work and second jobs.",
    "reading.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Guides</span><h1>Guides to online, remote and flexible work.</h1><p class="lede">Everything we have published on remote, online, part-time and freelance work in Canada.</p></div></div>
<section><div class="wrap">
<div class="filters" role="group" aria-label="Filter articles">
<button class="chip" type="button" data-filter="all" aria-pressed="true">All</button>
<button class="chip" type="button" data-filter="path" aria-pressed="false">Second jobs</button>
<button class="chip" type="button" data-filter="hiring" aria-pressed="false">Hiring</button>
<button class="chip" type="button" data-filter="market" aria-pressed="false">Market</button>
<button class="chip" type="button" data-filter="pay" aria-pressed="false">Pay</button>
</div>
<div class="posts">
<article class="post" data-cat="path"><div class="meta"><span class="cat">Second jobs</span><span>7 min</span></div><h3><a href="article-second-path.html">Why people take a second job</a></h3><p>Extra income is only part of the story. Time, location and meaningful work also matter.</p></article>
<article class="post" data-cat="path"><div class="meta"><span class="cat">Where to look</span><span>6 min</span></div><h3><a href="article-where-to-look.html">How to search for remote work</a></h3><p>Start with a job title that fits your skills, then use Job Bank’s remote and hours filters.</p></article>
<article class="post" data-cat="hiring"><div class="meta"><span class="cat">Work types</span><span>6 min</span></div><h3><a href="article-three-arrangements.html">Remote, online or flexible: which one do you need?</a></h3><p>Work location, online delivery and your work schedule are three different considerations.</p></article>
<article class="post" data-cat="market"><div class="meta"><span class="cat">The market</span><span>6 min</span></div><h3><a href="article-what-vacancies-mean.html">What the remote job market looks like in Canada</a></h3><p>Put national numbers, work-from-home figures and a focused job search in the right context.</p></article>
<article class="post" data-cat="hiring"><div class="meta"><span class="cat">Before you apply</span><span>7 min</span></div><h3><a href="article-read-a-remote-ad.html">How to read a remote job posting</a></h3><p>Check the employer, location, pay and hours before you apply.</p></article>
<article class="post" data-cat="hiring"><div class="meta"><span class="cat">Your application</span><span>5 min</span></div><h3><a href="article-remote-cv.html">Tailor your resume for online and remote work</a></h3><p>Highlight completed work, digital tools and clear communication.</p></article>
<article class="post" data-cat="pay"><div class="meta"><span class="cat">Pay</span><span>7 min</span></div><h3><a href="article-pay-and-province.html">What a second paycheque changes</a></h3><p>Pay rules, province, deductions and the difference between employment and freelance work.</p></article>
</div>
</div></section>
""",
)

PAGES["work-types.html"] = page(
    "work-types.html",
    "Online, remote and flexible work | Job Compass",
    "Three guides from Job Compass: remote work, online work and flexible arrangements in Canada.",
    "work-types.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Work types</span><h1>Three kinds of flexible work.</h1><p class="lede">Remote work is about where you work. Online work is about how the work is done. Part-time and flexible work are about your hours.</p></div></div>
<section><div class="wrap">
<div class="types">
<article class="type"><div><span class="n">01 · Location</span><h3><a href="remote-work-canada.html">Remote</a></h3></div><div><p>You are not normally required to work at the employer’s workplace. The job posting should state whether you may work anywhere in a province, anywhere in Canada or under a hybrid arrangement. Job Bank identifies these positions through its remote-work filter.</p><p><a href="remote-work-canada.html">Read the guide</a></p></div></article>
<article class="type"><div><span class="n">02 · Work</span><h3><a href="online-work-canada.html">Online</a></h3></div><div><p>The tasks are completed and delivered online: customer support, writing, design, bookkeeping, tutoring, moderation or software development. Online does not always mean working from home. Check where the posting says the work must be done.</p><p><a href="online-work-canada.html">Read the guide</a></p></div></article>
<article class="type"><div><span class="n">03 · Hours</span><h3><a href="flexible-work-canada.html">Flexible</a></h3></div><div><p>The schedule may include flexible hours, deadline-based projects or part-time work. Statistics Canada defines part-time work as usually fewer than 30 hours a week. Flexible work does not guarantee income, and you should still review the employment agreement or contract.</p><p><a href="flexible-work-canada.html">Read the guide</a></p></div></article>
</div>
<p class="src-note">For current job postings, visit <a href="https://www.jobbank.gc.ca/findajob" rel="noopener">Job Bank</a>. Use the remote-work filter instead of relying only on the phrase “work from home.”</p>
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
<div><span class="eyebrow">Location</span><h1>Remote work in Canada</h1><p class="lede">Remote work is done away from the employer’s regular workplace. The position may still have provincial, territorial or time-zone requirements.</p></div>
<aside class="qf"><h2>At a glance</h2><dl>
<dt>Location</dt><dd>Away from the employer’s regular workplace. Hybrid positions include some on-site work.</dd>
<dt>Hours</dt><dd>Often full-time. Part-time in the national survey is usually under 30 hours.</dd>
<dt>Applying</dt><dd>Apply through Job Bank or the employer’s website. Confirm the hours and work location.</dd>
<dt>Where to look</dt><dd>Job Bank’s remote filter, and the employer’s own careers page.</dd>
</dl><p class="rv">Reviewed October 2026. This is not a job posting.</p></aside>
</div></div>
<section><div class="wrap article">
<h2>What remote work means</h2>
<p>On Job Bank and Indeed, a job posting may be marked on-site, hybrid or remote. Hybrid means you work at a stated location some of the time. Remote means you are not normally required to report to the employer’s workplace. A keyword search for “work from home” is not the same as using the remote filter: it can also return on-site positions that happen to mention a home.</p>
<p>Indeed’s posting rules tell employers to use “Canada” or “nationwide” only when someone can do the work from anywhere in the country. Many remote positions still require applicants to live in a particular province or work in a Canadian time zone. Check the location requirements before applying.</p>
<h2>How employers hire for remote positions</h2>
<p>An employer usually posts the position, reviews applications and arranges interviews. A written offer should state the pay, hours, employer and permitted work location. If this would be a second job, compare the proposed hours with your current schedule.</p>
<p>Job Compass does not publish job postings. To see current opportunities, open <a href="https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=remote" rel="noopener">Job Bank</a> and use the remote-work filter.</p>
<h2>What to ask before you agree</h2>
<ul>
<li>Which provinces or territories may I work from, and would moving affect the arrangement?</li>
<li>Am I required to work on-site on any days? If so, the position is hybrid.</li>
<li>Who employs me, and is the pay hourly, salary, or per project?</li>
<li>Which time zone applies to meetings and working hours?</li>
<li>Who provides the computer and software?</li>
</ul>
<p>Pay rules are covered in <a href="article-pay-and-province.html">What a second paycheque changes</a>. When you have a posting open, read <a href="article-read-a-remote-ad.html">how to check it</a>.</p>
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
<div><span class="eyebrow">How the work is delivered</span><h1>Online work in Canada</h1><p class="lede">Online means the work is completed or delivered over the internet. It does not always mean that a person can work from home or from any province.</p></div>
<aside class="qf"><h2>At a glance</h2><dl>
<dt>Typical tasks</dt><dd>Support, writing, design, bookkeeping, tutoring, moderation, software.</dd>
<dt>Status</dt><dd>Employee or independent contractor. The wording in a job posting does not determine your legal status.</dd>
<dt>Pay</dt><dd>Hourly, salary, or per project. An advertised figure is not yet your offer.</dd>
<dt>Additional work</dt><dd>May include part-time support, writing, bookkeeping, design, tutoring or software work.</dd>
</dl><p class="rv">Reviewed October 2026. This is not a job posting.</p></aside>
</div></div>
<section><div class="wrap article">
<h2>Online work is not necessarily remote work</h2>
<p>Online work can be done at an employer’s workplace or from another location. Remote work can also include scheduled phone-based duties that people may not normally describe as online work. On Job Compass, online work means tasks that are completed or delivered over the internet. Always check the work location stated in the job posting.</p>
<h2>Employee or contractor</h2>
<p>Some online work is employment, with a schedule, a manager and a pay stub. Canada Pension Plan and Employment Insurance deductions may apply. Other online work is contract work: you send invoices, take on financial risk and manage your own taxes. The Canada Revenue Agency considers factors such as control, tools, financial risk and opportunity for profit. Describing a position as freelance does not settle the question. Check with the CRA if your status is unclear. This page is not tax advice.</p>
<h2>Work people add beside a main job</h2>
<p>Online work added alongside a main job is often familiar work done over the internet for part of the week: customer service, bookkeeping, writing, design, tutoring, moderation or software development. Consider which skills you can already demonstrate and whether the hours fit your schedule. The <a href="article-remote-cv.html">resume guide</a> explains how to present that experience.</p>
<p>Software development is one occupation where online delivery is common. In the second quarter of 2026, Statistics Canada counted 3,545 vacancies for software developers and programmers, up about 35 per cent year over year, with an average offered wage of $43.65 an hour. That figure describes wages offered for vacant positions in the occupation. It is not a standard remote-work wage or an offer to you.</p>
<p>A job posting should name the organization, describe the work and explain how you would be paid. When you are ready to search, use <a href="article-where-to-look.html">Job Bank’s remote filter</a> and check the employer’s own careers page.</p>
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
<div><span class="eyebrow">Hours</span><h1>Flexible online and remote work</h1><p class="lede">Flexible work may offer some choice in your hours, workload or deadlines. Job Compass focuses on flexible arrangements that are also online or remote.</p></div>
<aside class="qf"><h2>At a glance</h2><dl>
<dt>Part-time</dt><dd>Usually under 30 hours a week, in Statistics Canada’s survey.</dd>
<dt>Shapes</dt><dd>Chosen hours, a shorter week, or a project with a deadline.</dd>
<dt>Not included</dt><dd>On-site casual shifts, even if the hours are short.</dd>
<dt>Pay</dt><dd>Depends on the role. Nothing here guarantees an amount.</dd>
</dl><p class="rv">Reviewed October 2026. This is not a job posting.</p></aside>
</div></div>
<section><div class="wrap article">
<h2>Why the hours matter in a second job</h2>
<p>Flexible work can mean fewer hours, some choice over when you work or freedom from a workplace. We cover the location question in our <a href="remote-work-canada.html">remote-work guide</a>. This guide focuses on hours and workload for online or remote work.</p>
<p>A second job beside a full-time one only works if the hours fit. In 2023, 89.9 per cent of multiple jobholders held at least one part-time job. People whose main job was already part-time were more than twice as likely to hold another job as people whose main job was full-time (9.7 per cent, compared with 4.7 per cent). Statistics Canada’s part-time line is usually under 30 hours a week at the main job. A second job can be much shorter than that. The line is statistical. It is not the overtime threshold in your province.</p>
<p>People also work fewer hours because of school, care for children or other family members, health needs or a preference for a shorter schedule. A job posting should state the weekly hours or deadlines, the time zone and whether you or the employer sets the schedule. Compare those details with our guide to <a href="article-read-a-remote-ad.html">reading a job posting</a>.</p>
<p>Self-employment, which includes a lot of flexible online contract work, was up 51,000 people (+1.9 per cent) in the year to September 2026, and down 23,000 in that month alone. A flexible month can be a quiet month. Plan for that before you treat contract work as a wage.</p>
<h2>Requesting a flexible arrangement</h2>
<p>Federally regulated employees may have a formal right to request flexible work arrangements. Other processes depend on provincial or territorial law, the workplace and any collective agreement or employment contract. Make your request in writing, describe the schedule you are seeking and keep the employer’s response. Check the rules that apply to your workplace rather than relying on guidance written for another country.</p>
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
        "A few details can help you decide whether a position fits your needs. Start with the employer, then review the location, pay, hours and working arrangement.",
        """
<div class="takeaways"><h2>Read in this order</h2><ul>
<li>Who is hiring, and can you find that name on a website you looked up yourself?</li>
<li>Where may the work be done: remote, hybrid, or a named province?</li>
<li>What is the pay: an amount, a range, or the phrase “to be negotiated”?</li>
<li>What are the hours, the time zone, and whether you would be an employee or a contractor?</li>
<li>Do those hours fit beside the job, study, or care you already have?</li>
</ul></div>
<h2>What to expect in a job posting</h2>
<p>Job Bank and Indeed postings generally include a job title, employer, location, pay, work-location label and posting date. Pay may be listed by the hour or by the year. If the wage says “to be negotiated,” no amount has been provided.</p>
<p>A remote posting should also explain where applicants may live and work. “Remote — Canada” and “remote — must live in British Columbia” have different location requirements. Indeed tells employers not to use a nationwide location unless people anywhere in the country can do the work.</p>
<h2>Pay in the posting</h2>
<p>British Columbia has required compensation information in covered public job postings since 1 November 2023. For covered publicly advertised job postings in Ontario, rules in effect from 1 January 2026 require many employers with at least 25 employees to include expected compensation or a range, disclose whether they use artificial intelligence to screen applicants and say whether a vacancy exists. A posted range in Ontario cannot span more than $50,000 a year, and positions paying more than $200,000 a year are exempt. A range does not guarantee the amount you will be offered. Employers cannot require Canadian experience in those Ontario postings or related application forms.</p>
<p>Indeed’s hiring lab measured the Ontario change: pay appeared on 49 per cent of Ontario postings just before the rule, and on 71 per cent by June 2026. Most of those were ranges.</p>
<h2>Confirm the hours for a second job</h2>
<p>If this would be a second job, the weekly hours and time zone matter more than the word flexible. A pay range in a posting describes the position; it becomes your pay only if the employer includes that amount in an offer. If you are still deciding where to search, read our guide to <a href="article-where-to-look.html">finding remote work</a>.</p>
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
    "Remote, online or flexible: which one do you need? | Job Compass",
    "Why online, remote and flexible work in Canada describe where the work is done, how it is delivered and when it is done.",
    "reading.html",
    article(
        "Work types",
        "Remote, online or flexible: which one do you need?",
        "These terms often appear together in job postings, but each one means something different.",
        """
<div class="takeaways"><h2>In short</h2><ul>
<li>Remote describes where the work is done.</li>
<li>Online describes how the work is completed or delivered.</li>
<li>Flexible describes the hours or workload.</li>
<li>A position can have one, two or all three features. The job posting should explain which ones apply.</li>
</ul></div>
<h2>Work location</h2>
<p>Remote work is done away from the employer’s regular workplace. Hybrid work includes both remote and on-site work. If a posting says remote but requires three days in the office, the position is hybrid. Read our <a href="remote-work-canada.html">remote-work guide</a>.</p>
<h2>How the work is delivered</h2>
<p>Online work is completed or delivered over the internet. It may be done remotely or at an employer’s workplace. If a job posting says only “online job,” ask where you would be required to work. Read our <a href="online-work-canada.html">online-work guide</a>.</p>
<h2>Hours</h2>
<p>Flexible work may allow some choice over your schedule or workload. Statistics Canada generally defines part-time work as fewer than 30 hours a week at the main job. A flexible arrangement can still be full-time, and part-time work does not necessarily pay well. Read our <a href="flexible-work-canada.html">flexible-work guide</a>.</p>
<h2>Why the difference matters</h2>
<p>If you are adding work beside a main job, you need to know the hours. If you want to avoid a commute, check the work-location requirements. If you want a particular kind of work, focus on the duties. A posting that uses all three terms without explaining them leaves important questions unanswered. Next, learn <a href="article-read-a-remote-ad.html">how to check the details</a> or read <a href="article-second-path.html">why people take a second job</a>.</p>
""",
    ),
)

PAGES["article-what-vacancies-mean.html"] = page(
    "article-what-vacancies-mean.html",
    "What the remote job market looks like in Canada | Job Compass",
    "How Canada’s vacancy figures and Job Bank’s remote filter should shape a search for online, remote or flexible work.",
    "reading.html",
    article(
        "The market",
        "What the remote job market looks like in Canada",
        "Working from home is an established part of Canada’s labour market. The number of remote postings is smaller than the country’s total job count, so it helps to search with the remote filter.",
        """
<div class="statrow">
<div class="stat"><b>510,200</b><span>job vacancies, all industries, second quarter of 2026</span></div>
<div class="stat"><b>2.8%</b><span>vacancy rate, unchanged on the year</span></div>
<div class="stat"><b>3.0</b><span>unemployed people for every vacancy</span></div>
<div class="stat"><b>6.5%</b><span>unemployment rate, September 2026</span></div>
</div>
<h2>Look at remote work, not the national total</h2>
<p>Statistics Canada’s Job Vacancy and Wage Survey counted 510,200 vacancies in the second quarter of 2026. The vacancy rate was 2.8 per cent. There were 3.0 unemployed people for every vacancy. In September 2026 the Labour Force Survey put unemployment at 6.5 per cent. Those numbers mix offices, shops, trucks, kitchens and clinics. They are the background, not the size of a remote search.</p>
<p>Work-location data provide more useful context for a remote search. In May 2026, 11.4 per cent of employed Canadians worked exclusively from home, and 9.8 per cent had a hybrid arrangement. Working exclusively from home was less common than a year earlier, but it remained an established work arrangement. People looking for a second job may narrow that group further by seeking fewer hours, online delivery or both.</p>
<h2>Use the remote filter, not the whole board</h2>
<p>When we reviewed Job Bank in October 2026, its home page showed approximately 84,000 job postings, while approximately 700 were marked remote. Both counts change daily. Searching for a job title and applying the remote filter is more useful than browsing all postings. Searching only for “work from home” is less precise and can return hybrid and on-site positions. Follow the steps in our guide to <a href="article-where-to-look.html">finding remote work</a>.</p>
<h2>One occupation that can be done online</h2>
<p>Software developers and programmers had 3,545 vacancies in that quarter, up about 35 per cent year over year, with an average offered hourly wage of $43.65. Offered wages are the amounts employers advertised for vacant positions in that occupation. They are not the typical wage for every remote position, and they are not an offer. Search for an occupation you are qualified for, then review the pay in each posting.</p>
<h2>If you are looking for extra hours</h2>
<p>A focused search may take time. Part-time remote work is a narrower search than “any job.” Save a Job Bank alert rather than treating the national vacancy total as your likelihood of being hired. Job Compass does not publish job postings.</p>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www150.statcan.gc.ca/n1/daily-quotidien/260915/dq260915a-eng.htm" rel="noopener">Statistics Canada: job vacancies, second quarter 2026</a></li>
<li><a href="https://www150.statcan.gc.ca/n1/daily-quotidien/261009/dq261009a-eng.htm" rel="noopener">Statistics Canada: Labour Force Survey, September 2026</a></li>
<li><a href="https://www150.statcan.gc.ca/n1/daily-quotidien/260605/dq260605a-eng.htm" rel="noopener">Statistics Canada: Labour Force Survey, May 2026, work location</a></li>
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
        "A second job or additional source of income may help with household expenses, build experience in a field you care about or provide work that fits around existing commitments.",
        """
<div class="takeaways"><h2>What people said</h2><ul>
<li>34.9 per cent: to pay for essentials such as groceries or housing.</li>
<li>34.8 per cent: to earn extra income.</li>
<li>14.5 per cent: to do work they were passionate about.</li>
<li>The hours and the place decide whether a second job can sit beside the first.</li>
</ul></div>
<h2>A second job is already common</h2>
<p>In 2023, 5.6 per cent of employed Canadians held more than one job at the same time, about 1.1 million people. Women were more likely to do so than men (6.4 per cent, compared with 4.8 per cent). In 2025, Statistics Canada’s annual count of multiple jobholders was 1,178,600. Holding two jobs can mean the main job does not cover the bills. It can also mean someone wants a field the main job does not give them.</p>
<p>Those August 2023 reasons come from a Labour Force Survey supplement. They cover workers aged 15 to 69 who already had more than one job. They are not a forecast of what a new search will pay.</p>
<h2>Why online, remote or flexible work may help</h2>
<p>Most people who held two jobs in 2023 also held at least one part-time job: 89.9 per cent. A second commute can make scheduling more difficult. Remote work removes that trip, while flexible hours may fit around another shift, school, family responsibilities or a class. Online work can include customer support, writing, design, bookkeeping, tutoring and software development.</p>
<p>Home is already a workplace for a minority of employed Canadians. In May 2026, 11.4 per cent worked only from home, and 9.8 per cent split the week between home and another place. That is the whole economy, not a promise that a posting with the word “remote” is waiting. It does show that working from home is a normal arrangement, not a slogan.</p>
<h2>Match the reason to the search</h2>
<p>If your goal is to cover essentials or add income, start with the hours you can realistically work and the type of pay you need. Regular employee earnings may be more predictable than contract income that varies from month to month. If you want to build experience in a field, begin with skills you can already demonstrate and read <a href="article-remote-cv.html">the resume guide</a>. If you need work to fit around school, care or health needs, read about <a href="flexible-work-canada.html">flexible hours</a> before applying to a full-time remote position.</p>
<p>Then search in a specific place. <a href="article-where-to-look.html">Where to look</a> explains Job Bank’s remote and hours filters. <a href="path-check.html">Find the right guide</a> directs you to information that matches your reason. Nothing here is an offer of work or a forecast of earnings.</p>
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
        "Start with a job title you are qualified for, then use Job Bank’s remote and hours filters to narrow the results.",
        """
<div class="takeaways"><h2>Search in this order</h2><ul>
<li>A job title you are qualified for, not just the words “work from home.”</li>
<li>Job Bank’s remote filter, if you need a fully remote position.</li>
<li>An hours filter, if this work sits beside a main job.</li>
<li>A job alert, so the next match arrives by email.</li>
<li>The employer’s own careers page, before you apply.</li>
</ul></div>
<h2>What Job Bank means by remote</h2>
<p>Job Bank lets an employer mark a job in one of four ways. Remote means the work must be done remotely, from a place you choose, such as a home office. Hybrid means some of the work is in person and some is remote, and the split is discussed with the employer. On-site means a place the employer names, with no remote option. On the road means the location keeps changing because of travel.</p>
<p>A search for the words “work from home” is less precise. It can return hybrid and on-site postings that mention a home somewhere in the text. If you need a fully remote position, use the filter. Open <a href="https://www.jobbank.gc.ca/findajob" rel="noopener">Find a job</a>, enter a title and a location, then choose Remote under work location.</p>
<h2>Hours, for a second job</h2>
<p>The same results page can filter by hours of work. If you already have a main job, the part-time filter can help you find additional working hours. In the Labour Force Survey, part-time generally means fewer than 30 hours a week at the main job. A second job can involve far fewer hours. A posting should still state the weekly hours or deadlines. Full-time remote work is a different search: it is generally a main job done from home, not additional work.</p>
<p>Job Bank also says remote results can appear from across the country because the work is not tied to the city you entered. Read the province in the posting. Job Bank notes that remote jobs follow the wage rules of the province where the employer is located, which may differ from the rules where you live. Read <a href="article-pay-and-province.html">Pay and province</a> for more context.</p>
<h2>Save the search</h2>
<p>Once the filters match your needs, Job Bank can email you when a new posting appears. On the results page, create a job alert and confirm it through the email Job Bank sends you. You can change or stop the alert later. Job Bank is free to use.</p>
<p>Note the employer named in the posting and, when possible, find the same position on the employer’s website. Apply there or through Job Bank. Job Compass does not publish job postings or introduce candidates to employers. When you have a posting open, learn how to <a href="article-read-a-remote-ad.html">review it</a>.</p>
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
    "Tailor your resume for online and remote work | Job Compass",
    "What to include on a resume for online and remote work, including results, communication, tools and location.",
    "reading.html",
    article(
        "Your application",
        "Tailor your resume for online and remote work",
        "For work completed at a distance, your resume should show that you can produce results, communicate clearly and work with limited supervision.",
        """
<div class="takeaways"><h2>What to highlight</h2><ul>
<li>Results you achieved while working independently.</li>
<li>The tools you used, described plainly.</li>
<li>A concise professional summary.</li>
<li>Your location and any geographic work restrictions that matter.</li>
</ul></div>
<h2>What an employer wants to learn</h2>
<p>For online and remote positions, employers want to know whether you can complete work reliably with limited supervision. For each relevant role, describe a result: customer requests resolved, reports completed and submitted, classes taught or software releases maintained. Name the communication and project tools you used. If your availability is relevant, include it in your application or cover letter rather than assuming it belongs in the resume header.</p>
<h2>What to leave off</h2>
<p>Do not invent a remote job title you did not hold or include an expected daily income. Do not attach identification, a social insurance number or banking details to an application. An employer does not need that information to decide whether to interview you. State your city and province, and mention any relevant availability in the application or cover letter.</p>
<h2>A short test before you send it</h2>
<p>Can a reader quickly understand what you achieved and which tools you used? If your resume is mainly a list of duties copied from an old posting, rewrite the most relevant points as results. Then apply through the employer’s website or Job Bank. The search steps are in <a href="article-where-to-look.html">where to look</a>.</p>
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
        "A second job can add income, but there are details to check: the province or territory tied to the work, the applicable minimum wage and how deductions are handled.",
        """
<div class="takeaways"><h2>The short version</h2><ul>
<li>There is no single minimum wage for every remote job in Canada. Check the federal rate and the province or territory named in the posting.</li>
<li>Banks, airlines, federally regulated telecommunications companies and interprovincial transportation businesses follow the Canada Labour Code.</li>
<li>Job Bank says a remote posting follows the wage rules of the employer’s province, which can differ from yours.</li>
<li>A second employer still deducts tax and Canada Pension Plan contributions. Follow current CRA instructions when completing Form TD1.</li>
</ul></div>
<h2>Minimum wage for remote work</h2>
<p>Minimum wage is set province by province, with a separate federal rate for federally regulated employees. From 1 April 2026 the federal rate is $18.15 an hour. If the provincial general rate is higher, a federally regulated employer must meet the higher one. Alberta’s general rate is still $15. British Columbia’s is $18.25 from 1 June 2026. Ontario’s is $17.95 from 1 October 2026. Quebec’s is $16.60 from 1 May 2026. Confirm the current figure on the <a href="https://minwage-salairemin.service.canada.ca/en/general.html" rel="noopener">federal minimum wage database</a> and on the province’s own site before you rely on a list, including ours.</p>
<p>Job Bank tells searchers that remote jobs follow the wage regulations of the province where the employer is located, and that those can differ from the rules where you live. Read the province in the posting, then confirm the applicable rules. This page does not determine which law applies to your contract.</p>
<h2>What job postings must show in two provinces</h2>
<p>British Columbia has required pay information in covered public job postings since 1 November 2023. Ontario’s rules from 1 January 2026 require many employers to show expected compensation or a range, disclose artificial-intelligence screening and say whether a vacancy exists. Details and exceptions are in <a href="article-read-a-remote-ad.html">How to read a remote job posting</a>. The posted range is not yet your offer. Quebec employment standards are administered by CNESST, while workplace language requirements are governed under the Charter of the French Language and overseen by the OQLF.</p>
<h2>A second paycheque</h2>
<p>If you already have an employer, a second employer still deducts income tax from your pay. If you have already claimed personal tax credits on another TD1 and your total income will exceed those credits, you generally enter zero and check the appropriate box on the second TD1. Follow current CRA instructions for your situation.</p>
<p>Separate employers generally calculate CPP deductions independently. If the two jobs together result in contributions above the annual maximum, the extra employee contribution may be refunded or applied to tax owing when you file. The line for that overpayment is 44800. Quebec uses the Quebec Pension Plan, and the process is different. Rates change every year, so check the current CRA guidance.</p>
<p>A contract that calls you freelance does not determine whether you are an employee. The Canada Revenue Agency considers control, tools, subcontracting, financial risk and opportunity for profit. Job Compass cannot determine your employment status. This is not tax advice.</p>
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
    "Find the right guide | Job Compass",
    "Choose why you want online, remote or flexible work in Canada, and open the Job Compass guide that matches.",
    "reading.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Find the right guide</span><h1>What do you want this work to do?</h1><p class="lede">Choose the reason closest to yours. Your selection stays in your browser and is not sent to Job Compass.</p></div></div>
<section><div class="wrap" style="max-width:760px">
<form id="path-check">
<ul class="check">
<li><label><input type="radio" name="hope" value="essentials"> Earn additional income to help cover essentials.</label></li>
<li><label><input type="radio" name="hope" value="extra"> Add income without taking on full-time hours.</label></li>
<li><label><input type="radio" name="hope" value="craft"> Build experience in a field I care about.</label></li>
<li><label><input type="radio" name="hope" value="hours"> Find work that fits around school, family or health needs.</label></li>
</ul>
</form>
<div id="path-result" class="result" hidden><h3></h3><p></p><p><a id="path-next" href="article-second-path.html">Open the guide</a></p></div>
<p class="notice" style="margin-top:1.5rem">The percentages in these notes are from Statistics Canada, August 2023, and describe people who already held more than one job. They are not a promise of pay. Read the full article: <a href="article-second-path.html">Why people take a second job</a>.</p>
</div></section>
""",
)

PAGES["glossary.html"] = page(
    "glossary.html",
    "Glossary | Job Compass",
    "Definitions for remote, hybrid, online, flexible, NOC, EI, CPP, LMIA and other terms used in Canadian job postings.",
    "reading.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Glossary</span><h1>Terms used in job postings</h1><p class="lede">Short definitions of terms you will see in online, remote and flexible job postings in Canada. For legal rights or obligations, check the official sources linked from our articles.</p></div></div>
<section><div class="wrap">
<label class="notice" for="glossary-search">Search terms</label>
<input id="glossary-search" class="search" type="search" placeholder="Try remote, EI, contractor">
<dl class="glossary">
<div class="term"><dt>Remote</dt><dd>The work is not performed at the employer’s office. It can still require you to live in a named province or time zone.</dd></div>
<div class="term"><dt>Hybrid</dt><dd>Some of the work is remote and some is at a stated place. It is not fully remote.</dd></div>
<div class="term"><dt>On-site</dt><dd>You attend a workplace. Job Compass does not cover these roles.</dd></div>
<div class="term"><dt>Online work</dt><dd>Work that is completed or delivered over the internet. The term alone does not determine the location or hours.</dd></div>
<div class="term"><dt>Flexible work</dt><dd>Work that may offer some choice in hours, schedule or workload. Job Compass covers it when the work is also online or remote.</dd></div>
<div class="term"><dt>Part-time</dt><dd>In the Labour Force Survey, usually under 30 hours a week at the main or only job. A second job can be shorter than that.</dd></div>
<div class="term"><dt>Second job</dt><dd>Work you hold at the same time as another job. In August 2023 the most common reasons were essentials, extra income, and work people were passionate about.</dd></div>
<div class="term"><dt>Additional work</dt><dd>A second job, freelance assignment or other paid work taken on alongside existing commitments.</dd></div>
<div class="term"><dt>Job Bank</dt><dd>The Government of Canada’s job-search website. Use its remote filter when work location matters.</dd></div>
<div class="term"><dt>NOC</dt><dd>National Occupational Classification. A code for an occupation, used on Job Bank and in labour statistics.</dd></div>
<div class="term"><dt>Vacancy</dt><dd>A position an employer is seeking to fill. Statistics Canada measures vacancies through a survey; its count is not the same as the number of job postings on a website.</dd></div>
<div class="term"><dt>Offered wage</dt><dd>The wage advertised for a vacant position. It is not the average wage of people already employed, and it is not a personal offer.</dd></div>
<div class="term"><dt>CPP</dt><dd>Canada Pension Plan. Contributions can apply to employment, including part-time employment. See the Canada Revenue Agency for current rates.</dd></div>
<div class="term"><dt>EI</dt><dd>Employment Insurance. Premiums and benefits have their own rules. A contract that calls you freelance does not automatically decide them.</dd></div>
<div class="term"><dt>Independent contractor</dt><dd>A worker who is in business for themselves. CRA looks at control, tools, risk and chance of profit, not only the contract’s title.</dd></div>
<div class="term"><dt>LMIA</dt><dd>A Labour Market Impact Assessment. It is a process employers may need to use when hiring certain temporary foreign workers. It is not a job or a document a job seeker purchases.</dd></div>
<div class="term"><dt>TD1</dt><dd>The form where an employee claims personal tax credits with an employer. Claim those credits with one employer, not again at a second job.</dd></div>
<div class="term"><dt>Gig</dt><dd>A short contract, casual assignment or task arranged through a platform. Hours and income may vary. Platform workers in some provinces may be covered by specific rules.</dd></div>
</dl>
<p id="glossary-empty" hidden>No term matches that.</p>
</div></section>
""",
)

PAGES["faq.html"] = page(
    "faq.html",
    "FAQ | Job Compass",
    "Answers about Job Compass and about online, remote and flexible work in Canada.",
    "reading.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">FAQ</span><h1>Short answers.</h1></div></div>
<section><div class="wrap" style="max-width:820px">
<details><summary>Does Job Compass list jobs?</summary><p>No. We publish explanations of online, remote and flexible work, and how employers hire for that work. For current job postings, use Job Bank’s remote filter and employers’ own careers pages.</p></details>
<details><summary>Are you a recruitment agency?</summary><p>No. We are an independent publisher. We are not a licensed employment agency. We do not screen, place or introduce candidates, and we do not charge job seekers.</p></details>
<details><summary>Why only online, remote and flexible work?</summary><p>These arrangements may make it easier to fit a second job around a main job, school or family responsibilities. Job Compass focuses on work that can be completed online or away from an employer’s regular workplace, with part-time or flexible hours. On-site work is outside our scope.</p></details>
<details><summary>Why would someone want this as a second job?</summary><p>In August 2023, people who already held more than one job most often named essentials (34.9 per cent), extra income (34.8 per cent) or work they were passionate about (14.5 per cent). <a href="article-second-path.html">The guide</a> explains those figures in more detail. <a href="path-check.html">Find the right guide</a> points you to relevant information.</p></details>
<details><summary>Is remote work common in Canada?</summary><p>In May 2026, 11.4 per cent of employed people worked only from home, and 9.8 per cent had a hybrid week. On Job Bank, a remote filter is a much shorter list than every posting. Both are reasons to search with a title and a filter. <a href="article-where-to-look.html">Where to look</a>.</p></details>
<details><summary>What is the difference between remote and online?</summary><p>Remote describes where you may work. Online describes how the work is completed or delivered. A job can be one, the other or both. <a href="article-three-arrangements.html">Compare the three arrangements</a>.</p></details>
<details><summary>Will I be paid a set amount?</summary><p>Only if an employer offers you that amount in writing. Nothing on Job Compass is an offer or a forecast of earnings.</p></details>
<details><summary>Which province’s rules apply if I work from home?</summary><p>The applicable jurisdiction can depend on where you work, where the employer operates, the nature of the business and the employment relationship. Federally regulated workplaces follow federal labour standards. <a href="article-pay-and-province.html">What a second paycheque changes</a> provides context and official links.</p></details>
<details><summary>Can I do this in addition to my current job?</summary><p>Possibly, if the hours and your current employment terms allow it. In 2023, 89.9 per cent of people with two jobs held at least one part-time job. Review the proposed schedule, your employment agreement and any conflict-of-interest rules. Read about <a href="flexible-work-canada.html">flexible hours</a> and <a href="article-pay-and-province.html">pay for a second job</a>.</p></details>
<details><summary>Do you cover Quebec in French?</summary><p>These pages are in English. Quebec employment standards are administered by CNESST. Workplace language requirements are governed under the Charter of the French Language and overseen by the OQLF. Check those organizations’ websites for current information.</p></details>
<p style="margin-top:2rem">Have another question? <a href="contact.html">Contact Job Compass</a>.</p>
</div></section>
""",
)

PAGES["services.html"] = page(
    "services.html",
    "Why online, remote and flexible work matters | Job Compass",
    "Why people in Canada consider online, remote and flexible work, and how clear guidance can help them make informed choices.",
    "services.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Why it matters</span><h1>Why people look for extra work.</h1><p class="lede">For some it helps with everyday costs. For others it is a way to build experience or find hours that fit around a main job, school or family. Knowing which applies to you makes the search easier.</p></div></div>
<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">Start with your reason</span><h2>People have different reasons.</h2><p class="lede">Statistics Canada asked people who already held more than one job about their main reason in August 2023. Their answers show that income matters, but it is not the whole story.</p></div>
<div class="tiles">
<article class="tile reveal"><h3>Help with everyday costs</h3><p>Paying for essentials such as groceries or housing was the most common main reason.</p></article>
<article class="tile reveal"><h3>Add income</h3><p>Nearly as many people wanted income beyond what their main job provided.</p></article>
<article class="tile reveal"><h3>Build experience</h3><p>Some wanted to do work they were passionate about. A second job can also be a practical way to develop experience in a field.</p></article>
<article class="tile reveal"><h3>Find hours that fit</h3><p>Part-time or flexible work may fit around a main job, studies, family responsibilities or health needs.</p></article>
</div>
<p class="src-note">Source: Statistics Canada, August 2023, people aged 15 to 69 who already held more than one job. The results do not predict what a new job search will provide. <a href="article-second-path.html">See the full figures</a>.</p>
</div></section>
<section class="alt"><div class="wrap split">
<div><span class="eyebrow">What these arrangements can change</span><h2>Where, how and when you work.</h2>
<p><b>Remote work</b> can reduce or remove a commute, but a position may still require you to live in a particular province or work in a stated time zone.</p>
<p><b>Online work</b> can make some tasks available from a computer, but online does not always mean remote or flexible.</p>
<p><b>Flexible work</b> may offer a shorter schedule or some choice over hours. The posting should still explain who sets the schedule, how much work is available and how you will be paid.</p>
<p><a href="work-types.html">Compare the three work types &rarr;</a></p></div>
<div><span class="eyebrow">The idea behind Job Compass</span><h2>Why Job Compass exists.</h2>
<p>Information about remote work is spread across job postings, Job Bank, Statistics Canada, the Canada Revenue Agency and provincial or territorial websites. It can be difficult to know which details matter to your situation.</p>
<p>Job Compass puts that information in one place. Our guides help you choose a work arrangement, narrow a search, read a job posting, prepare a resume and understand basic questions about pay and employment status.</p>
<p>We provide independent guidance. We do not publish jobs, place candidates or promise a particular income.</p></div>
</div></section>
<section><div class="wrap split">
<div><span class="eyebrow">More than a paycheque</span><h2>Practical needs and personal goals can both matter.</h2>
<p>Taking on more work does not have to mean leaving your main job or finding a perfect role. It can be a second job that supports a household need, a freelance project that builds experience or a flexible position that fits your schedule.</p>
<p>The goal is not to tell every reader that they need another job. It is to help people who are already considering one understand their options, limits and next steps.</p></div>
<div><span class="eyebrow">What you can learn here</span><h2>What you will find here.</h2>
<ol class="note-list">
<li>Decide whether location, hours, income or experience matters most.</li>
<li>Understand the difference between remote, online and flexible work.</li>
<li>Search by occupation and use filters that match your needs.</li>
<li>Check the employer, work location, hours, pay and employment status.</li>
<li>Use official sources when a legal, tax or employment rule affects you.</li>
</ol>
<div class="btn-row"><a class="btn btn-primary" href="path-check.html">Find the right guide</a><a class="btn btn-ghost" href="reading.html">Explore all guides</a></div></div>
</div></section>
""",
)

PAGES["about.html"] = page(
    "about.html",
    "About | Job Compass",
    "Job Compass is an independent Canadian publisher covering online, remote and flexible work, and how employers hire for that work.",
    "about.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">About Job Compass</span><h1>We cover online, remote and flexible work</h1></div></div>
<section><div class="wrap split">
<div class="reveal">
<h2>Who we write for</h2>
<p>Job Compass is an independent publisher for people in Canada who are considering online work, a remote position or flexible hours alongside a main job, family responsibilities or studies. We explain why people take on this work and how to look for it on Job Bank and employers’ websites. We are not affiliated with Job Bank, Statistics Canada or any provincial or territorial government.</p>
<p>We are not a licensed employment agency. We do not publish job openings or send your information to employers.</p>
</div>
<div class="reveal">
<h2>How we prepare an article</h2>
<div class="types">
<div class="type" style="grid-template-columns:1fr"><div><h3>Within our scope</h3><p>We cover online, remote and flexible work. On-site positions are outside our editorial focus.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Based on sources</h3><p>Labour figures come from Statistics Canada. Job-search guidance comes from Job Bank. Pay and tax information comes from the Canada Revenue Agency and the relevant provincial, territorial or federal authority.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Reviewed and dated</h3><p>Articles state when they were last reviewed. Wage and vacancy figures include the period they describe.</p></div></div>
</div>
</div>
</div></section>
<section class="alt"><div class="wrap">
<p class="notice" style="max-width:70ch">Job Compass publishes general information, not legal, tax or employment advice. Contact us at hello@jobcompass.ca. We operate online and do not have a public office.</p>
</div></section>
""",
)

PAGES["contact.html"] = page(
    "contact.html",
    "Contact | Job Compass",
    "Ask Job Compass about online, remote, work-from-home, part-time or flexible work in Canada. The form opens your email app. We do not take identification or banking details.",
    "contact.html",
    f"""
<div class="page-head"><div class="wrap"><span class="eyebrow">Contact</span><h1>Ask us about work in Canada</h1><p class="lede">Want to know more about online, remote, work-from-home, part-time or flexible work? Send your question and we will point you to the right guide or official source.</p></div></div>
<section><div class="wrap split">
<div>
<form id="contact-form" class="form" novalidate>
<div class="field"><label for="name">Name</label><input id="name" required autocomplete="name"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">Email</label><input id="email" type="email" required autocomplete="email"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="province">Province or territory</label><select id="province"><option value="">Prefer not to say</option><option>Alberta</option><option>British Columbia</option><option>Manitoba</option><option>New Brunswick</option><option>Newfoundland and Labrador</option><option>Northwest Territories</option><option>Nova Scotia</option><option>Nunavut</option><option>Ontario</option><option>Prince Edward Island</option><option>Quebec</option><option>Saskatchewan</option><option>Yukon</option><option>Outside Canada</option></select></div>
<div class="field"><label for="topic">What is your question about?</label><select id="topic"><option>Remote work</option><option>Online work</option><option>Work from home</option><option>Part-time or flexible work</option><option>Freelance or side job</option><option>Pay, tax or employment status</option><option>Another job-related question</option></select></div>
<div class="field"><label for="msg">Your question</label><textarea id="msg" required placeholder="For example: Which Job Bank filter shows fully remote, part-time positions in Alberta?"></textarea><div class="err" aria-live="polite"></div></div>
<button class="btn btn-primary" type="submit">Send my question</button>
<p class="notice">Sending opens your email app with the message addressed to {EMAIL}.</p>
</form>
<div id="form-ok" class="ok" hidden tabindex="-1" role="status"><h3>Your email app should be open.</h3><p>Send the message from there when you are ready.</p><p class="ok-sub">If nothing opened, write to {EMAIL}.</p></div>
</div>
<div>
<h2>Email</h2>
<ul class="contact-list"><li><b>Questions</b><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul>
<p class="notice">We can explain how these types of work are described in Canada and where to find official information. We cannot find you a job, review a specific job offer or give legal, tax or immigration advice, and we will not forward your information to an employer. Please do not send a social insurance number or banking information.</p>
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
<div class="page-head"><div class="wrap"><span class="eyebrow">Privacy</span><h1>Privacy</h1><p class="lede">Last updated 28 October 2026.</p></div></div>
<section><div class="wrap article">
<p>Job Compass is an independent publisher. We do not offer user accounts or ask you to create one. This notice describes the limited personal information that may be involved when you use the site. It reflects the fair information principles in Canada’s Personal Information Protection and Electronic Documents Act (PIPEDA). Provincial privacy laws, including Quebec’s, may also apply depending on where you are and how a message is handled.</p>
<h2>What you can send us</h2>
<p>The contact form does not submit to our server. It opens your own email application with a message addressed to hello@jobcompass.ca. If you send that email, we receive whatever you chose to include: typically your name, email address, province and message. We use it to answer your question and to improve our guides. We do not sell it, and we do not use it to build a marketing list.</p>
<p>Do not send a social insurance number, banking details, identity documents or passwords. We will not ask for them.</p>
<h2>What stays on your device</h2>
<p>The path check and the glossary search run in your browser. What you choose or type there is not transmitted to us by those tools.</p>
<h2>Fonts and server logs</h2>
<p>Pages request typefaces from Google Fonts. That request can expose your IP address to Google. Our hosting provider may keep ordinary server logs, such as IP address, browser and page requested, for security. We do not add our own analytics tracker to these pages.</p>
<h2>How long a message is kept</h2>
<p>We retain inquiry emails only while it is needed to answer the message, keep a record of our reply or meet a legal obligation. We then delete or anonymize it. You can ask what information we still have, request a correction or ask us to delete the thread by writing to hello@jobcompass.ca. We may need to verify that the request comes from the email account concerned.</p>
<h2>Other sites</h2>
<p>Articles link to Job Bank, Statistics Canada, the Canada Revenue Agency and provincial pages. Those sites have their own notices. We do not control them.</p>
</div></section>
""",
)

PAGES["disclaimer.html"] = page(
    "disclaimer.html",
    "Disclaimer | Job Compass",
    "Job Compass publishes general information on online, remote and flexible work in Canada. We do not hire candidates or guarantee employment or income.",
    "about.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Disclaimer</span><h1>Disclaimer</h1></div></div>
<section><div class="wrap article">
<h2>A publisher, not an agency</h2>
<p>Job Compass publishes general information about online, remote and flexible work in Canada, and how employers hire for that work. We are not a licensed employment agency. We do not publish job postings, hire, screen, place or introduce candidates. We do not charge readers a fee.</p>
<h2>No guarantee of employment or income</h2>
<p>Nothing on this site is an offer of employment or a prediction of earnings. Pay, hours and eligibility depend on the employer, the applicable jurisdiction and the terms of the working arrangement.</p>
<h2>Not professional advice</h2>
<p>The pages are not legal, tax, immigration or employment advice. Most employment standards are provincial or territorial. Federally regulated workplaces follow the Canada Labour Code. Quebec has distinct employment and workplace-language requirements that should be checked with the appropriate authorities. Confirm details with the authority that governs your situation or with a qualified adviser.</p>
<h2>Figures go out of date</h2>
<p>We date statistics and identify their sources. Vacancy counts, minimum wages and job-posting rules can change after an article’s review date. Check the linked official source for current information and contact us if you find an error.</p>
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
