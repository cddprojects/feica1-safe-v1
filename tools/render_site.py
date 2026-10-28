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
<p style="margin-top:1rem;max-width:36ch">An independent Canadian publisher on online, remote and flexible work, for people building that work as a second path.</p></div>
<div><h4>Reading</h4><ul>
<li><a href="reading.html">All articles</a></li>
<li><a href="work-types.html">Work types</a></li>
<li><a href="path-check.html">Which guide fits</a></li>
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
<div class="legal"><p>North Desk is an independent publisher. We are not Job Bank, Statistics Canada, or a provincial employment service, and we are not a licensed employment agency. We do not recruit, screen, place or introduce candidates, and we do not publish vacancies. Guides are general information, not legal, tax or employment advice. Confirm pay, tax and workplace rules on the official page for your situation.</p>
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
<link rel="icon" href="favicon.svg" type="image/svg+xml">
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
    "Remote, online and flexible work in Canada | North Desk",
    "Explore independent Canadian guides to work from home, remote work, part-time roles, online work, freelance work and side jobs.",
    "index.html",
    f"""
<section class="hero"><div class="wrap hero-grid">
<div>
<span class="eyebrow">More ways to shape your working week</span>
<h1>Work that fits where life is going.</h1>
<p class="lede">Thinking about work from home, a part-time role, online work or a freelance side job? North Desk brings the choices into focus with thoughtful Canadian stories and practical guides. We are an independent publisher—not a job board or recruitment agency.</p>
<div class="btn-row"><a class="btn btn-primary" href="reading.html">Explore the guides</a><a class="btn btn-ghost" href="path-check.html">Find your starting point</a></div>
</div>
<div class="modes">
<h2>Three ways work can fit</h2>
<a class="mode" href="remote-work-canada.html"><span class="dot"></span><span><b>Remote work</b><small>Less time travelling, with a clear agreement about where you can work.</small></span><span class="tag">Where</span></a>
<a class="mode" href="online-work-canada.html"><span class="dot"></span><span><b>Online work</b><small>Use skills such as support, writing, design, bookkeeping, tutoring or software online.</small></span><span class="tag">What</span></a>
<a class="mode" href="flexible-work-canada.html"><span class="dot"></span><span><b>Part-time &amp; flexible</b><small>Build work around a main job, studies, family or the week you want.</small></span><span class="tag">When</span></a>
</div>
</div></section>

<section class="alt"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Why a second path matters</span><h2>More breathing room. A new direction. Or work that feels more like yours.</h2></div>
<ol class="shifts">
<li class="reveal"><span class="no">34.9%</span><h3>Everyday needs</h3><p>Some people add work to create a little more room for housing, groceries and other essentials.</p></li>
<li class="reveal"><span class="no">34.8%</span><h3>Something extra</h3><p>For almost the same share, a second job was a way to add income beyond the basics.</p></li>
<li class="reveal"><span class="no">14.5%</span><h3>Work they cared about</h3><p>For others, the second path opened a field they felt drawn to.</p></li>
<li class="reveal"><span class="no">Your week</span><h3>Hours that belong</h3><p>Part-time and flexible work can sit beside school, family, health or a main job.</p></li>
</ol>
<p class="src-note">Statistics Canada asked people aged 15 to 69 who held more than one job about their main reason in August 2023. These figures describe their answers—not an expected result for a new reader.</p>
</div></section>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">Start where you are</span><h2>A clearer question makes for a better search.</h2><p class="lede">Choose the guide that speaks to the change you want: a different place to work, hours that fit, a useful second income, or a new direction for your skills.</p></div>
<div class="posts">
<article class="post reveal"><div class="meta"><span class="cat">Second path</span><span>7 min</span></div><h3><a href="article-second-path.html">Why people build a second work path</a></h3><p>Extra income is only part of the story. Time, place and meaningful work matter too.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Where to look</span><span>6 min</span></div><h3><a href="article-where-to-look.html">A calmer way to search for remote work</a></h3><p>Start with a role you can do, then use Job Bank’s remote and hours filters to narrow the field.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Work types</span><span>6 min</span></div><h3><a href="article-three-arrangements.html">Remote, online or flexible: which one do you need?</a></h3><p>One changes where you work, one describes the work itself, and one changes the shape of your week.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Before you apply</span><span>7 min</span></div><h3><a href="article-read-a-remote-ad.html">Read a remote job posting with confidence</a></h3><p>See the employer, location, pay, hours and working arrangement before you decide it fits.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Your application</span><span>5 min</span></div><h3><a href="article-remote-cv.html">Shape your CV for online and remote work</a></h3><p>Bring finished work, digital tools and clear communication to the front of the page.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Pay</span><span>7 min</span></div><h3><a href="article-pay-and-province.html">What a second paycheque changes</a></h3><p>Pay rules, province, deductions and the difference between employment and freelance work.</p></article>
</div>
</div></section>

<section class="alt" id="recruitment"><div class="wrap split">
<div class="reveal"><span class="eyebrow">From interest to a useful search</span><h2>Begin with what you need—not every opening.</h2></div>
<div class="reveal">
<p class="lede">Remote work, online work and freelance projects can look similar in a search result. A few choices make it easier to recognise the arrangement that belongs in your life.</p>
<ol class="note-list">
<li>Start with the change you want: more room in the budget, a different field, fewer hours or less travel.</li>
<li>Set an honest amount of time for a part-time role or side job.</li>
<li>Decide whether you need fully remote work or simply want some work-from-home days.</li>
<li>Search <a href="https://www.jobbank.gc.ca/findajob" rel="noopener">Job Bank</a> by occupation, then use the remote and hours filters.</li>
<li>Before you apply, check the employer, pay, province and whether the work is employment or freelance.</li>
</ol>
<p><a href="article-where-to-look.html">Build a more focused search &rarr;</a></p>
</div>
</div></section>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">Choose what matters most</span><h2>Flexibility can mean more than one thing.</h2></div>
<div class="minis">
<a class="mini reveal" href="remote-work-canada.html"><b>Work from home</b><span>Understand fully remote and hybrid arrangements.</span></a>
<a class="mini reveal" href="online-work-canada.html"><b>Online work</b><span>Explore work that can be completed over the internet.</span></a>
<a class="mini reveal" href="flexible-work-canada.html"><b>Part-time &amp; flexible</b><span>Look at hours that can fit around the rest of your week.</span></a>
<a class="mini reveal" href="article-second-path.html"><b>Freelance &amp; side work</b><span>Consider a second path without assuming a set income.</span></a>
</div>
</div></section>

<section class="alt" id="contact"><div class="wrap split">
<div><span class="eyebrow">Help shape the next guide</span><h2>What would make your search clearer?</h2><p class="lede">Send a question, a story idea or a correction. We use reader questions to plan future coverage. North Desk cannot place you in a job, and you should never send identification or banking details.</p></div>
<div>
<form id="contact-form" class="form" novalidate>
<div class="field"><label for="name">Name</label><input id="name" required autocomplete="name"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">Email</label><input id="email" type="email" required autocomplete="email"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="province">Province or territory</label><select id="province"><option value="">Prefer not to say</option><option>Alberta</option><option>British Columbia</option><option>Manitoba</option><option>New Brunswick</option><option>Newfoundland and Labrador</option><option>Northwest Territories</option><option>Nova Scotia</option><option>Nunavut</option><option>Ontario</option><option>Prince Edward Island</option><option>Quebec</option><option>Saskatchewan</option><option>Yukon</option><option>Outside Canada</option></select></div>
<div class="field"><label for="topic">Topic</label><select id="topic"><option>A second job beside my main one</option><option>Online work</option><option>Remote work</option><option>Flexible hours</option><option>A correction</option><option>A story idea</option></select></div>
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
    "Canadian guides to work from home, remote work, online work, part-time roles, freelance work and second jobs.",
    "reading.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Reading</span><h1>Ideas for a working week that fits.</h1><p class="lede">Thoughtful Canadian guides to remote work, online work, part-time hours, freelance paths and the choices behind them.</p></div></div>
<section><div class="wrap">
<div class="filters" role="group" aria-label="Filter articles">
<button class="chip" type="button" data-filter="all" aria-pressed="true">All</button>
<button class="chip" type="button" data-filter="path" aria-pressed="false">Second path</button>
<button class="chip" type="button" data-filter="hiring" aria-pressed="false">Hiring</button>
<button class="chip" type="button" data-filter="market" aria-pressed="false">Market</button>
<button class="chip" type="button" data-filter="pay" aria-pressed="false">Pay</button>
</div>
<div class="posts">
<article class="post" data-cat="path"><div class="meta"><span class="cat">Second path</span><span>7 min</span></div><h3><a href="article-second-path.html">Why people build a second work path</a></h3><p>Extra income is only part of the story. Time, place and meaningful work matter too.</p></article>
<article class="post" data-cat="path"><div class="meta"><span class="cat">Where to look</span><span>6 min</span></div><h3><a href="article-where-to-look.html">A calmer way to search for remote work</a></h3><p>Start with a role you can do, then let the right filters narrow the field.</p></article>
<article class="post" data-cat="hiring"><div class="meta"><span class="cat">Work types</span><span>6 min</span></div><h3><a href="article-three-arrangements.html">Remote, online or flexible: which one do you need?</a></h3><p>Where you work, what you do online, and how your hours fit are three different choices.</p></article>
<article class="post" data-cat="market"><div class="meta"><span class="cat">The market</span><span>6 min</span></div><h3><a href="article-what-vacancies-mean.html">What the remote job market looks like in Canada</a></h3><p>Put national numbers, work-from-home figures and a focused job search in the right context.</p></article>
<article class="post" data-cat="hiring"><div class="meta"><span class="cat">Before you apply</span><span>7 min</span></div><h3><a href="article-read-a-remote-ad.html">Read a remote job posting with confidence</a></h3><p>See the employer, location, pay, hours and working arrangement before you decide it fits.</p></article>
<article class="post" data-cat="hiring"><div class="meta"><span class="cat">Your application</span><span>5 min</span></div><h3><a href="article-remote-cv.html">Shape your CV for online and remote work</a></h3><p>Bring finished work, digital tools and clear communication to the front of the page.</p></article>
<article class="post" data-cat="pay"><div class="meta"><span class="cat">Pay</span><span>7 min</span></div><h3><a href="article-pay-and-province.html">What a second paycheque changes</a></h3><p>Pay rules, province, deductions and the difference between employment and freelance work.</p></article>
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
<div class="page-head"><div class="wrap"><span class="eyebrow">Work types</span><h1>Choose the flexibility that matters to you.</h1><p class="lede">Work from home changes the place. Online work describes what can be delivered over the internet. Part-time and flexible work change the shape of the week.</p></div></div>
<section><div class="wrap">
<div class="types">
<article class="type"><div><span class="n">01 · Place</span><h3><a href="remote-work-canada.html">Remote</a></h3></div><div><p>You are not required to sit in the employer’s office. The ad should say whether that means anywhere in a province, anywhere in Canada, or a hybrid split. Job Bank files this under a remote filter, separate from a keyword search.</p><p><a href="remote-work-canada.html">Read the guide</a></p></div></article>
<article class="type"><div><span class="n">02 · Work</span><h3><a href="online-work-canada.html">Online</a></h3></div><div><p>The tasks and completed work move over the internet: support, writing, design, bookkeeping, tutoring, moderation or software. Online does not always mean work from home. Read where the posting says the work must be done.</p><p><a href="online-work-canada.html">Read the guide</a></p></div></article>
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
<dt>Recruitment</dt><dd>Apply on Job Bank or the employer’s site. The offer names hours and place.</dd>
<dt>Where to look</dt><dd>Job Bank’s remote filter, and the employer’s own careers page.</dd>
</dl><p class="rv">Reviewed October 2026. Not a vacancy.</p></aside>
</div></div>
<section><div class="wrap article">
<h2>What the word is doing</h2>
<p>On Job Bank and Indeed, a posting is marked on-site, hybrid or remote. Those are three agreements. Hybrid means some days in a stated place. Remote means you are not required to report to the office. A keyword search for “work from home” is not the same as the remote filter: it also returns on-site jobs that mention a home somewhere in the text.</p>
<p>Indeed’s own posting rules tell employers to use “Canada” or “nationwide” only when the person can do the work from anywhere in the country. Many so-called remote roles still say “must reside in Ontario” or “must be in a Canadian time zone.” That line is the real location.</p>
<h2>How recruitment usually runs</h2>
<p>A careful employer posts the role, takes applications, and has someone from the organisation speak with you. The offer names the pay, the hours, who employs you, and where you are allowed to work from. If this would be a second job, those hours are the part you compare with the week you already have.</p>
<p>North Desk does not carry those postings. When you want live ads, open <a href="https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=remote" rel="noopener">Job Bank</a> and filter for remote.</p>
<h2>What to ask before you agree</h2>
<ul>
<li>Which provinces may I work from, and what happens if I move?</li>
<li>Is any day in an office required? If yes, it is hybrid.</li>
<li>Who employs me, and is the pay hourly, salary, or per project?</li>
<li>Which time zone are meetings in?</li>
<li>Who provides the computer and software?</li>
</ul>
<p>Pay rules are covered in <a href="article-pay-and-province.html">What a second paycheque changes</a>. When you have a posting open, read <a href="article-read-a-remote-ad.html">how to check it with confidence</a>.</p>
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
<div><span class="eyebrow">How the work is delivered</span><h1>Online work in Canada</h1><p class="lede">Online means the work is completed or delivered over the internet. It does not always mean that a person can work from home or from any province.</p></div>
<aside class="qf"><h2>At a glance</h2><dl>
<dt>Typical tasks</dt><dd>Support, writing, design, bookkeeping, tutoring, moderation, software.</dd>
<dt>Status</dt><dd>Employee or independent contractor. The label on the ad is not the legal test.</dd>
<dt>Pay</dt><dd>Hourly, salary, or per project. An advertised figure is not yet your offer.</dd>
<dt>Second path</dt><dd>Often a shorter week of support, writing, books, design, tutoring or software.</dd>
</dl><p class="rv">Reviewed October 2026. Not a vacancy.</p></aside>
</div></div>
<section><div class="wrap article">
<h2>Online is not the same word as remote</h2>
<p>A person can do online work in an office. A person can also do remote work that is not “online” in the casual sense, such as a phone roster with set shifts. When North Desk says online, we mean the deliverable travels by internet and the seat is not an employer’s floor. If the ad also requires a city, read it as a location rule, not as a mood.</p>
<h2>Employee or contractor</h2>
<p>Some online work is employment: a schedule, a manager, a pay stub, Canada Pension Plan and Employment Insurance when the rules say so. Some is contract work: you invoice, you carry the risk of a quiet month, and you handle your own tax. The Canada Revenue Agency looks at control, tools, financial risk and the chance of profit. Calling it freelance in the posting does not decide the question. Confirm with CRA if the status is unclear. This page is not tax advice.</p>
<h2>Work people add beside a main job</h2>
<p>A second path online is usually an ordinary occupation done over the internet for part of the week: answering customers, keeping books, writing, designing, tutoring, moderating, or building software. The useful question is whether you can already do a piece of that work, and whether the hours fit. The <a href="article-remote-cv.html">CV guide</a> is about showing that piece of work.</p>
<p>Software development is one occupation where online delivery is common. In the second quarter of 2026, Statistics Canada counted 3,545 vacancies for software developers and programmers, up about 35 per cent on the year, with an average offered wage of $43.65 an hour. That is the wage advertised on empty jobs in that occupation. It is not a remote salary, and it is not an offer to you.</p>
<p>Recruitment for this work still names an organisation, a task, and how you are paid. When you are ready to look, use <a href="article-where-to-look.html">Job Bank’s remote filter</a> and the employer’s own careers page.</p>
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
<h2>Why the hours are the point of a second path</h2>
<p>Readers use flexible for three different hopes: fewer hours, hours they pick, or freedom from a building. We keep the third one under <a href="remote-work-canada.html">remote</a>. This guide is about hours and load, for work that is already online or remote.</p>
<p>A second job beside a full-time one only works if the hours fit. In 2023, 89.9 per cent of multiple jobholders held at least one part-time job. People whose main job was already part-time were more than twice as likely to hold another job as people whose main job was full-time (9.7 per cent, compared with 4.7 per cent). Statistics Canada’s part-time line is usually under 30 hours a week at the main job. A second job can be much shorter than that. The line is statistical. It is not the overtime threshold in your province.</p>
<p>People also work a shorter week because of school, care for children or other family, their own health, or a preference for fewer hours. Those reasons are why a flexible arrangement exists. The posting should still say the weekly hours or the deadline, the time zone, and whether the schedule is yours to set or theirs to roster. Compare that with <a href="article-read-a-remote-ad.html">how to read a posting with confidence</a>.</p>
<p>Self-employment, which includes a lot of flexible online contract work, was up 51,000 people (+1.9 per cent) in the year to September 2026, and down 23,000 in that month alone. A flexible month can be a quiet month. Plan for that before you treat contract work as a wage.</p>
<h2>There is no single national request form</h2>
<p>If you already have an employer and want different hours, the process depends on the province, the contract, and whether the employer is federally regulated. Canada does not have one national flexible-work request with a fixed reply time. Ask in writing, describe the hours, and keep their answer. Do not assume a guideline you read for another country applies here.</p>
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
    "How to read a remote job posting in Canada | North Desk",
    "A field-by-field reading of Canadian remote, online and flexible job ads, including pay transparency in Ontario and British Columbia.",
    "reading.html",
    article(
        "Before you apply",
        "Read a remote job posting with confidence",
        "A few details can tell you whether a role belongs in your life. Start with the employer, then look at location, pay, hours and the working arrangement.",
        """
<div class="takeaways"><h2>Read in this order</h2><ul>
<li>Who is hiring, and can you find that name on a website you looked up yourself?</li>
<li>Where may the work be done: remote, hybrid, or a named province?</li>
<li>What is the pay: an amount, a range, or the phrase “to be negotiated”?</li>
<li>What are the hours, the time zone, and whether you would be an employee or a contractor?</li>
<li>Do those hours fit beside the job, study, or care you already have?</li>
</ul></div>
<h2>The fields a real card has</h2>
<p>Job Bank and Indeed cards carry a title, an employer, a place written as a city and province, pay by the hour or the year, a work-site label (on-site, hybrid or remote), and a date. Sometimes the wage says “to be negotiated.” That is an absence of a number, not a high number.</p>
<p>Remote ads add a constraint the office ads hide in the address: who is allowed to apply from where. “Remote — Canada” and “remote — must live in British Columbia” are different jobs. Indeed tells employers not to post a nationwide location unless people anywhere in the country can do the work.</p>
<h2>Pay on the ad</h2>
<p>British Columbia has required compensation information in public job postings since 1 November 2023. Ontario, from 1 January 2026, requires many employers with at least 25 employees to include the expected compensation or a range, to say whether they use artificial intelligence to screen applicants, and to say whether a vacancy exists. A posted range in Ontario cannot span more than $50,000 a year, and roles above $200,000 a year are exempt. The range is not a promise that you will be offered that pay. Canadian experience cannot be required in those Ontario postings or their application forms.</p>
<p>Indeed’s hiring lab measured the Ontario change: pay appeared on 49 per cent of Ontario postings just before the rule, and on 71 per cent by June 2026. Most of those were ranges.</p>
<h2>A second path needs the hours in writing</h2>
<p>If this job would sit beside another one, the weekly hours and the time zone matter more than the word flexible. A range in an ad is information about the role. It becomes your pay only when that employer offers it to you. The next page, if you are still choosing where to look, is <a href="article-where-to-look.html">where to look</a>.</p>
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
    "Remote, online or flexible: which one do you need? | North Desk",
    "Why online, remote and flexible work in Canada describe where the work is done, how it is delivered and when it is done.",
    "reading.html",
    article(
        "Work types",
        "Remote, online or flexible: which one do you need?",
        "The words often appear together, but each one answers a different question about your working week.",
        """
<div class="takeaways"><h2>Keep them apart</h2><ul>
<li>Remote is a place rule.</li>
<li>Online is how the work travels.</li>
<li>Flexible is an hours or load rule.</li>
<li>A role can be one of these, or all three. The ad should say which.</li>
</ul></div>
<h2>Place</h2>
<p>Remote work is not performed at the employer’s office. Hybrid work is partly there. If the message says remote and then names three office days, believe the office days. Guides: <a href="remote-work-canada.html">remote</a>.</p>
<h2>How the work is delivered</h2>
<p>Online work is delivered over the internet. It can be remote, or it can be a seat in a building with a headset. When a pitch says only “online job,” ask for the place rule in writing. Guide: <a href="online-work-canada.html">online</a>.</p>
<h2>Hours</h2>
<p>Flexible work lets the week move. Statistics Canada’s part-time line is usually under 30 hours at the main job. A flexible arrangement can still be full-time, and a short week can still be poorly paid. Guide: <a href="flexible-work-canada.html">flexible</a>.</p>
<h2>Why the mix-up matters for a second path</h2>
<p>Someone adding hours beside a main job needs the hours. Someone leaving a commute needs the place. Someone who wants the work itself needs the task. A posting that uses all three words without explaining them leaves the important questions unanswered. Read <a href="article-read-a-remote-ad.html">how to check the details</a> next, or start with <a href="article-second-path.html">why people build a second path</a>.</p>
""",
    ),
)

PAGES["article-what-vacancies-mean.html"] = page(
    "article-what-vacancies-mean.html",
    "What the remote job market looks like in Canada | North Desk",
    "How Canada’s vacancy figures and Job Bank’s remote filter should shape a search for online, remote or flexible work.",
    "reading.html",
    article(
        "The market",
        "What the remote job market looks like in Canada",
        "Working from home is an established part of Canada’s labour market. The number of remote postings is smaller than the country’s total job count, so a focused search matters.",
        """
<div class="statrow">
<div class="stat"><b>510,200</b><span>job vacancies, all industries, second quarter of 2026</span></div>
<div class="stat"><b>2.8%</b><span>vacancy rate, unchanged on the year</span></div>
<div class="stat"><b>3.0</b><span>unemployed people for every vacancy</span></div>
<div class="stat"><b>6.5%</b><span>unemployment rate, September 2026</span></div>
</div>
<h2>Start from the arrangement, not the national total</h2>
<p>Statistics Canada’s Job Vacancy and Wage Survey counted 510,200 vacancies in the second quarter of 2026. The vacancy rate was 2.8 per cent. There were 3.0 unemployed people for every vacancy. In September 2026 the Labour Force Survey put unemployment at 6.5 per cent. Those numbers mix offices, shops, trucks, kitchens and clinics. They are the background, not the size of a remote search.</p>
<p>A more useful figure for this desk is where people already work. In May 2026, 11.4 per cent of employed Canadians worked only from home, and 9.8 per cent had a hybrid week. Exclusive home work was lower than a year earlier. It is still a large group of real jobs. A second path is usually a slice of that: fewer hours, online delivery, or both.</p>
<h2>Search the filter, not the whole board</h2>
<p>Job Bank’s home page, when we read it in October 2026, invited people to search on the order of 84,000 postings. A browse the same month showed on the order of 700 marked remote. Both counts move every day. The practical reading is that a title plus the remote filter is a better search than opening the whole board. The words “work from home” are looser still and return hybrid and on-site ads. The steps are in <a href="article-where-to-look.html">where to look</a>.</p>
<h2>One occupation that can be done online</h2>
<p>Software developers and programmers had 3,545 vacancies in that quarter, up about 35 per cent on the year, with an average offered hourly wage of $43.65. Offered wages are what employers advertised for empty jobs in that occupation. They are not the going rate for every remote role, and they are not an offer. Use an occupation you can already do, then read the pay on that posting.</p>
<h2>How to use this when you are adding hours</h2>
<p>Expect a specific search to take time. A part-time remote role is a narrower ask than “any job.” That is a reason to save a Job Bank alert, not a reason to treat a national vacancy total as your chance of being hired. North Desk does not post the ads.</p>
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
    "Why people build a second work path | North Desk",
    "Why people in Canada add online, remote or flexible work beside a main job, family or studies, using Statistics Canada’s reasons for holding more than one job.",
    "reading.html",
    article(
        "Second path",
        "Why people build a second work path",
        "A second path is work that sits beside the life you already have. It may create more room in the budget, open a field you care about, or offer hours that fit more naturally.",
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
<h2>Why the work has to be online, remote, or flexible</h2>
<p>Most people who held two jobs in 2023 also held at least one part-time job: 89.9 per cent. A full second commute, on top of a full first job, is the arrangement that fails first. Remote work removes the trip. Flexible hours let the second block of time sit around a shift, a school run, or a class. Online work is the kind of task that can travel that way: support, writing, design, bookkeeping, tutoring, software.</p>
<p>Home is already a workplace for a minority of employed Canadians. In May 2026, 11.4 per cent worked only from home, and 9.8 per cent split the week between home and another place. That is the whole economy, not a promise that a posting with the word “remote” is waiting. It does show that working from home is a normal arrangement, not a slogan.</p>
<h2>Match the reason to the search</h2>
<p>If the reason is essentials or extra income, start with the hours you can actually give and the pay basis you need: an employee wage, with a pay stub, is easier to plan around than a contract that can go quiet. If the reason is the work itself, start from a skill you can already show, and read <a href="article-remote-cv.html">the CV guide</a>. If the reason is school, care, or health, read <a href="flexible-work-canada.html">flexible hours</a> before you read a posting that says “full-time remote.”</p>
<p>Then look in a specific place. <a href="article-where-to-look.html">Where to look</a> walks through Job Bank’s remote filter and hours filter. <a href="path-check.html">Which guide fits</a> points you at the page that matches your reason. Nothing here is an offer of work or a forecast of earnings.</p>
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
    "A calmer way to search for remote work in Canada | North Desk",
    "How to search Job Bank for remote and part-time work in Canada, and how those filters differ from the words work from home.",
    "reading.html",
    article(
        "Where to look",
        "A calmer way to search for remote work",
        "A broad search can feel endless. Start with work you can already do, then use Job Bank’s remote and hours filters to bring the useful results closer.",
        """
<div class="takeaways"><h2>Search in this order</h2><ul>
<li>A job title you can already do, not the words “work from home” alone.</li>
<li>Job Bank’s remote filter, if the seat must not be an office.</li>
<li>An hours filter, if this work sits beside a main job.</li>
<li>A job alert, so the next match arrives by email.</li>
<li>The employer’s own careers page, before you apply.</li>
</ul></div>
<h2>What Job Bank means by remote</h2>
<p>Job Bank lets an employer mark a job in one of four ways. Remote means the work must be done remotely, from a place you choose, such as a home office. Hybrid means some of the work is in person and some is remote, and the split is discussed with the employer. On-site means a place the employer names, with no remote option. On the road means the location keeps changing because of travel.</p>
<p>A search for the words “work from home” is looser. It can return hybrid and on-site ads that mention a home somewhere in the text. If you need the seat to be remote, use the filter. Open <a href="https://www.jobbank.gc.ca/findajob" rel="noopener">Find a job</a>, enter a title and a location, then choose Remote under work location.</p>
<h2>Hours, for a second job</h2>
<p>The same results page can filter by hours of work. If you already have a main job, part-time is the filter that matches a second block of hours. In the Labour Force Survey, part-time means usually under 30 hours a week at the main job. Your second job can be well under that. A posting should still say the weekly hours or the deadline. Full-time remote is a different search: it is a main job you would do from home, not an add-on.</p>
<p>Job Bank also says remote results can appear from across the country, because the work is not tied to the city you typed. Read the province on the card. Job Bank’s own note is that remote jobs follow the wage rules of the province where the employer is located, and that those rules can differ from the province where you live. <a href="article-pay-and-province.html">Pay and province</a> is the page for that check.</p>
<h2>Save the search</h2>
<p>After the filters look right, Job Bank can email you when a new posting matches. On the results page, choose the alert for that search and confirm the email address they send you. You can change or stop the alert later. The Government of Canada’s board is free to use.</p>
<p>Then open the employer named on the card and find the same role on that employer’s site when you can. Apply there or on Job Bank. North Desk does not carry the postings and does not introduce you. When you have a posting open, <a href="article-read-a-remote-ad.html">read it with confidence</a>.</p>
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
    "Shape your CV for online and remote work | North Desk",
    "What to show on a CV when the recruiter will never see you at a desk: delivery, tools, writing, and time zone.",
    "reading.html",
    article(
        "Your application",
        "Shape your CV for online and remote work",
        "When the work happens at a distance, your CV should make reliability visible: what you finished, how you communicated and which tools helped you deliver.",
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
<p>Do not invent a remote title you did not hold. Do not list a hoped-for daily amount. Do not attach identification, a social insurance number, or banking details to an application. A recruiter does not need those to decide whether to speak with you. If this is a second job, put the hours you can overlap with a team in the header, next to your province.</p>
<h2>A short test before you send it</h2>
<p>Can a stranger tell what you delivered, on what tools, in which time zone, in under a minute? If the page is a list of duties copied from an old posting, rewrite the duties as outcomes. Then apply on the employer’s site or on Job Bank. The search steps are in <a href="article-where-to-look.html">where to look</a>.</p>
""",
    ),
)

PAGES["article-pay-and-province.html"] = page(
    "article-pay-and-province.html",
    "What a second paycheque changes | North Desk",
    "Which pay rules to check for online and remote work in Canada, and what changes when the work is a second job.",
    "reading.html",
    article(
        "Pay",
        "What a second paycheque changes",
        "A second job can add useful income, but it also adds a few details to check: the province tied to the work, the wage floor and how deductions are handled.",
        """
<div class="takeaways"><h2>The short version</h2><ul>
<li>There is no single Canadian minimum wage for a laptop job. Check the federal rate and the province named on the posting.</li>
<li>Banks, airlines, telecoms and interprovincial transport follow the Canada Labour Code.</li>
<li>Job Bank says a remote posting follows the wage rules of the employer’s province, which can differ from yours.</li>
<li>A second employer still deducts tax and Canada Pension Plan. Personal tax credits on Form TD1 are not claimed twice.</li>
</ul></div>
<h2>There is no single Canadian minimum for a laptop job</h2>
<p>Minimum wage is set province by province, with a separate federal rate for federally regulated employees. From 1 April 2026 the federal rate is $18.15 an hour. If the provincial general rate is higher, a federally regulated employer must meet the higher one. Alberta’s general rate is still $15. British Columbia’s is $18.25 from 1 June 2026. Ontario’s is $17.95 from 1 October 2026. Quebec’s is $16.60 from 1 May 2026. Confirm the current figure on the <a href="https://minwage-salairemin.service.canada.ca/en/general.html" rel="noopener">federal minimum wage database</a> and on the province’s own site before you rely on a list, including ours.</p>
<p>Job Bank tells searchers that remote jobs follow the wage regulations of the province where the employer is located, and that those can differ from the rules where you live. Read the province on the card, then confirm it. This page is not a ruling on which statute applies to your contract.</p>
<h2>What the ad must show, in two provinces</h2>
<p>British Columbia has required pay information in public postings since 1 November 2023. Ontario’s rules from 1 January 2026 require many employers to show expected compensation or a range, disclose artificial-intelligence screening, and say whether a vacancy exists. Details and exceptions are in <a href="article-read-a-remote-ad.html">Read a remote job posting with confidence</a>. The posted range is not yet your offer. Quebec has its own employment standards and French-language workplace rules through CNESST.</p>
<h2>A second paycheque</h2>
<p>If you already have an employer, a second employer still deducts income tax from what they pay you. The Canada Revenue Agency says each employer does this whether or not you have another job. Personal tax credit amounts on Form TD1 are claimed with one employer. If you already claimed them on the TD1 for your main job, you do not claim them again at the second job. Claiming them twice can leave you owing tax when both incomes are added up.</p>
<p>Canada Pension Plan works by employment, not by person, when the employers are different. Each employer deducts CPP until you reach the maximum for that employment. If the two jobs together deduct more than the annual maximum, the extra employee contribution is refunded or applied to tax owing when you file. The line for that overpayment is 44800. Quebec uses the Quebec Pension Plan, and the refund path is different. Rates change every year. Read the CRA pages rather than a number copied from a guide, including this one.</p>
<p>A contract that calls you freelance is not the test of whether you are an employee. The Canada Revenue Agency looks at control, tools, subcontracting, financial risk and the chance of profit. North Desk does not set that status. This is not tax advice.</p>
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
    "Which guide fits | North Desk",
    "Choose why you want online, remote or flexible work in Canada, and open the North Desk guide that matches.",
    "reading.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Which guide fits</span><h1>What do you want this work to do?</h1><p class="lede">Pick the reason closest to yours. The note stays in this browser. Nothing is sent to North Desk.</p></div></div>
<section><div class="wrap" style="max-width:760px">
<form id="path-check">
<ul class="check">
<li><label><input type="radio" name="hope" value="essentials"> Cover essentials beside the job I already have.</label></li>
<li><label><input type="radio" name="hope" value="extra"> Earn extra income, with a limit on the hours.</label></li>
<li><label><input type="radio" name="hope" value="craft"> Build a field I care about, from home.</label></li>
<li><label><input type="radio" name="hope" value="hours"> Fit the hours around school, family or health.</label></li>
</ul>
</form>
<div id="path-result" class="result" hidden><h3></h3><p></p><p><a id="path-next" href="article-second-path.html">Open the guide</a></p></div>
<p class="notice" style="margin-top:1.5rem">The percentages in these notes are from Statistics Canada, August 2023, and describe people who already held more than one job. They are not a promise of pay. The full piece is <a href="article-second-path.html">Why people build a second work path</a>.</p>
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
<div class="term"><dt>Part-time</dt><dd>In the Labour Force Survey, usually under 30 hours a week at the main or only job. A second job can be shorter than that.</dd></div>
<div class="term"><dt>Second job</dt><dd>Work you hold at the same time as another job. In August 2023 the most common reasons were essentials, extra income, and work people were passionate about.</dd></div>
<div class="term"><dt>Second dream</dt><dd>North Desk’s name for online, remote or flexible work someone wants beside the life they already have. It is a guide topic, not a job title.</dd></div>
<div class="term"><dt>Job Bank</dt><dd>The Government of Canada’s public job board. Use the remote filter when place is the point.</dd></div>
<div class="term"><dt>NOC</dt><dd>National Occupational Classification. A code for an occupation, used on Job Bank and in labour statistics.</dd></div>
<div class="term"><dt>Vacancy</dt><dd>A job an employer is trying to fill. Statistics Canada measures vacancies by survey. A posting on a board is not the same count.</dd></div>
<div class="term"><dt>Offered wage</dt><dd>The wage advertised for an empty job. It is not the average wage of people already employed, and it is not your offer.</dd></div>
<div class="term"><dt>CPP</dt><dd>Canada Pension Plan. Contributions can apply to employment, including part-time employment. See the Canada Revenue Agency for current rates.</dd></div>
<div class="term"><dt>EI</dt><dd>Employment Insurance. Premiums and benefits have their own rules. A contract that calls you freelance does not automatically decide them.</dd></div>
<div class="term"><dt>Independent contractor</dt><dd>A worker who is in business for themselves. CRA looks at control, tools, risk and chance of profit, not only the contract’s title.</dd></div>
<div class="term"><dt>LMIA</dt><dd>A Labour Market Impact Assessment. An employer process used in some work-permit hires. It is not a job a reader applies to buy.</dd></div>
<div class="term"><dt>TD1</dt><dd>The form where an employee claims personal tax credits with an employer. Claim those credits with one employer, not again at a second job.</dd></div>
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
<details><summary>Why only online, remote and flexible?</summary><p>Because that is how a second job can exist beside a main job, school, or care at home. A second commute usually does not fit. On-site work, including trades, retail floors, trucking and bedside care, is outside these pages.</p></details>
<details><summary>Why would someone want this as a second job?</summary><p>In August 2023, people who already held more than one job most often named essentials (34.9 per cent), extra income (34.8 per cent), or work they were passionate about (14.5 per cent). <a href="article-second-path.html">The guide</a> puts those figures in context. <a href="path-check.html">Which guide fits</a> points you to the next page.</p></details>
<details><summary>Is remote work common in Canada?</summary><p>In May 2026, 11.4 per cent of employed people worked only from home, and 9.8 per cent had a hybrid week. On Job Bank, a remote filter is a much shorter list than every posting. Both are reasons to search with a title and a filter. <a href="article-where-to-look.html">Where to look</a>.</p></details>
<details><summary>What is the difference between remote and online?</summary><p>Remote is where you are allowed to sit. Online is how the work travels. A job can be one, the other, or both. <a href="article-three-arrangements.html">Read the three agreements</a>.</p></details>
<details><summary>Will I be paid a set amount?</summary><p>Only if an employer offers you that amount in writing. Nothing on North Desk is an offer or a forecast of earnings.</p></details>
<details><summary>Which province’s rules apply if I work from home?</summary><p>For most employers, the rules of the province or territory where you do the work. Federally regulated employers, such as banks, airlines and telecoms, follow the Canada Labour Code. <a href="article-pay-and-province.html">What a second paycheque changes</a> has the detail and the links.</p></details>
<details><summary>Can this sit beside the job I already have?</summary><p>Often, if the hours are short enough and the place is remote. In 2023, 89.9 per cent of people with two jobs held at least one part-time job. Read <a href="flexible-work-canada.html">flexible hours</a> and <a href="article-pay-and-province.html">pay and a second job</a> before you treat two full-time roles as the plan.</p></details>
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
<div class="page-head"><div class="wrap"><span class="eyebrow">What we publish</span><h1>A desk, not a placement service.</h1><p class="lede">We explain why people in Canada add online, remote and flexible work, and how to look for it. The reading is free. There is no account and no fee.</p></div></div>
<section><div class="wrap">
<div class="tiles">
<article class="tile reveal"><h3>Why a second path</h3><p>Essentials, extra income, and work people care about, from Statistics Canada’s count of people who already hold two jobs.</p><a class="more" href="article-second-path.html">Read why</a></article>
<article class="tile reveal"><h3>Where to look</h3><p>Job Bank’s remote filter, an hours filter, and a job alert. Then the employer’s own careers page.</p><a class="more" href="article-where-to-look.html">Start the search</a></article>
<article class="tile reveal"><h3>Which guide fits</h3><p>Essentials, extra income, a field you care about, or hours that fit. One choice opens the matching guide.</p><a class="more" href="path-check.html">Choose a reason</a></article>
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
<p>North Desk is an independent publisher for people in Canada who want online work, a remote role, or flexible hours as a second path: beside a main job, a family, or a course. We explain why people add that work, and how to look for it on the public board. We are not affiliated with Job Bank, Statistics Canada, or any province.</p>
<p>We are not a licensed employment agency. We do not hold jobs, and we do not send your name to an employer.</p>
</div>
<div class="reveal">
<h2>How a piece gets written</h2>
<div class="types">
<div class="type" style="grid-template-columns:1fr"><div><h3>Inside the beat</h3><p>If the work is not online, remote, or flexible in that setting, we do not assign it.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Tied to a source</h3><p>Labour figures come from Statistics Canada. How to search comes from Job Bank. Pay and tax notes come from the Canada Revenue Agency and the province that wrote the rule.</p></div></div>
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
<div class="page-head"><div class="wrap"><span class="eyebrow">Contact</span><h1>Write to the desk.</h1><p class="lede">Questions about a second path, story ideas, and corrections. Do not include a social insurance number or banking details. We cannot place you in a job.</p></div></div>
<section><div class="wrap split">
<div>
<form id="contact-form" class="form" novalidate>
<div class="field"><label for="name">Name</label><input id="name" required autocomplete="name"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">Email</label><input id="email" type="email" required autocomplete="email"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="province">Province or territory</label><select id="province"><option value="">Prefer not to say</option><option>Alberta</option><option>British Columbia</option><option>Manitoba</option><option>New Brunswick</option><option>Newfoundland and Labrador</option><option>Northwest Territories</option><option>Nova Scotia</option><option>Nunavut</option><option>Ontario</option><option>Prince Edward Island</option><option>Quebec</option><option>Saskatchewan</option><option>Yukon</option><option>Outside Canada</option></select></div>
<div class="field"><label for="topic">Topic</label><select id="topic"><option>A second job beside my main one</option><option>Online work</option><option>Remote work</option><option>Flexible hours</option><option>A correction</option><option>A story idea</option></select></div>
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
    "How North Desk handles personal information. The contact form opens your email app. The path check and search run in your browser.",
    "contact.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Privacy</span><h1>Privacy</h1><p class="lede">Last updated 28 October 2026.</p></div></div>
<section><div class="wrap article">
<p>North Desk is an independent publisher. We do not run accounts, and we do not ask you to create one. This notice describes the little personal information the site can involve. It is written with the fair-information principles in Canada’s Personal Information Protection and Electronic Documents Act (PIPEDA) in mind. Provincial privacy laws, including Quebec’s, can also apply depending on where you are and how a message is handled.</p>
<h2>What you can send us</h2>
<p>The contact form does not submit to our server. It opens your own email application with a message addressed to desk@northdesk.ca. If you send that email, we receive whatever you chose to include: typically your name, email address, province and message. We use it to reply, to correct an article, or to consider a topic. We do not sell it, and we do not use it to build a marketing list.</p>
<p>Do not send a social insurance number, banking details, identity documents or passwords. We will not ask for them.</p>
<h2>What stays on your device</h2>
<p>The path check and the glossary search run in your browser. What you choose or type there is not transmitted to us by those tools.</p>
<h2>Fonts and server logs</h2>
<p>Pages request typefaces from Google Fonts. That request can expose your IP address to Google. A host that serves these files may keep ordinary server logs, such as IP address, browser and page requested, for security. We do not add our own analytics tracker to these pages.</p>
<h2>How long a message is kept</h2>
<p>If you email us, we keep the thread long enough to answer and to keep a correction on file, then delete it or reduce it to an anonymous note. You can ask what we still have, ask for a correction, or ask us to delete the thread, by writing to desk@northdesk.ca. We may need to confirm we are writing back to the same address.</p>
<h2>Other sites</h2>
<p>Articles link to Job Bank, Statistics Canada, the Canada Revenue Agency and provincial pages. Those sites have their own notices. We do not control them.</p>
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
