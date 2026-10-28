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
<p style="margin-top:1rem;max-width:36ch">Practical guides to remote, online and flexible work in Canada.</p></div>
<div><h4>Guides</h4><ul>
<li><a href="reading.html">Browse all guides</a></li>
<li><a href="work-types.html">Work types</a></li>
<li><a href="services.html">Additional work</a></li>
<li><a href="glossary.html">Glossary</a></li>
<li><a href="faq.html">FAQ</a></li>
</ul></div>
<div><h4>About</h4><ul>
<li><a href="about.html">About</a></li>
<li><a href="contact.html">Contact</a></li>
<li><a href="privacy.html">Privacy</a></li>
<li><a href="disclaimer.html">Disclaimer</a></li>
</ul></div>
</div>
<div class="legal"><p>Job Compass publishes guides, not job listings. General information only; check official sources for the rules that apply to you.</p>
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
    "Explore independent Canadian guides to work from home, remote work, part-time roles, online work, freelance work and side jobs.",
    "index.html",
    f"""
<section class="hero"><div class="wrap hero-grid">
<div>
<span class="eyebrow">Guides to flexible work in Canada</span>
<h1>Remote, online and flexible work in <em>Canada.</em></h1>
<p class="lede">Clear Canadian guidance for comparing work types, finding relevant postings and checking hours, pay and employment terms before you apply.</p>
<div class="btn-row"><a class="btn btn-primary" href="reading.html">Browse the guides</a><a class="btn btn-ghost" href="work-types.html">Compare work types</a></div>
<p class="hero-note">For current openings, search Job Bank or an employer’s careers page.</p>
</div>
<div class="hero-art">
{HERO_ART}
<div class="modes">
<h2 class="sr">Work arrangements</h2>
<a class="mode" href="remote-work-canada.html"><span class="dot"></span><span><b>Remote work</b><small>Describes where the work is completed.</small></span><span class="tag">Location</span></a>
<a class="mode" href="online-work-canada.html"><span class="dot"></span><span><b>Online work</b><small>Describes how the work is completed or delivered.</small></span><span class="tag">Delivery</span></a>
<a class="mode" href="flexible-work-canada.html"><span class="dot"></span><span><b>Part-time and flexible work</b><small>Part-time describes hours; flexible describes choice over schedule or workload.</small></span><span class="tag">Hours</span></a>
</div>
</div>
</div></section>

<section class="alt"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Canadian context</span><h2>Why people hold more than one job.</h2><p class="lede">Statistics Canada asked multiple jobholders aged 15 to 69 for their main reason in August 2023.</p></div>
<ol class="shifts">
<li class="reveal"><span class="no">34.9%</span><h3>Everyday needs</h3><p>Rent, groceries and other everyday costs.</p></li>
<li class="reveal"><span class="no">34.8%</span><h3>Extra income</h3><p>Almost the same share wanted money beyond the basics.</p></li>
<li class="reveal"><span class="no">14.5%</span><h3>Work they cared about</h3><p>This group cited work they were passionate about.</p></li>
</ol>
<p class="src-note">Source: Statistics Canada, August 2023. <a href="article-second-path.html">Read why people take a second job</a>.</p>
</div></section>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">A practical sequence</span><h2>From understanding the terms to applying.</h2><p class="lede">Each guide answers the next question that commonly arises during a remote or flexible job search.</p></div>
<div class="posts">
<article class="post reveal"><div class="meta"><span class="cat">Work types</span><span>6 min</span></div><h3><a href="article-three-arrangements.html">Remote, online and flexible work compared</a></h3><p>Remote refers to location, online to how the work is done, and flexible to the schedule.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Job market</span><span>6 min</span></div><h3><a href="article-what-vacancies-mean.html">What remote-work statistics can tell you</a></h3><p>Work-from-home figures and vacancy figures measure different parts of the labour market.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Job search</span><span>6 min</span></div><h3><a href="article-where-to-look.html">How to search for remote work</a></h3><p>A job title plus Job Bank’s work-location and hours filters can narrow the results.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Before you apply</span><span>7 min</span></div><h3><a href="article-read-a-remote-ad.html">How to read a remote job posting</a></h3><p>Employer, location, pay and hours: what a good posting spells out.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Your application</span><span>5 min</span></div><h3><a href="article-remote-cv.html">Tailor your resume for online and remote work</a></h3><p>Show results, the tools you use and how you communicate.</p></article>
<article class="post reveal"><div class="meta"><span class="cat">Pay</span><span>7 min</span></div><h3><a href="article-pay-and-province.html">Pay and deductions for additional work</a></h3><p>Minimum wage, payroll deductions and employee or contractor status.</p></article>
</div>
</div></section>

<section class="alt"><div class="wrap split">
<div><span class="eyebrow">More information</span><h2>Questions about a guide?</h2><p class="lede">Questions about the terms, figures or links in a guide can be sent by email.</p></div>
<div class="btn-row"><a class="btn btn-primary" href="contact.html">Contact Job Compass</a><a class="btn btn-ghost" href="faq.html">Read common questions</a></div>
</div></section>
""",
)

PAGES["reading.html"] = page(
    "reading.html",
    "Reading | Job Compass",
    "Canadian guides to work from home, remote work, online work, part-time roles, freelance work and second jobs.",
    "reading.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Guides</span><h1>Guides to remote, online and flexible work in Canada</h1><p class="lede">Information on work arrangements, job searches, applications and pay.</p></div></div>
<section><div class="wrap">
<div class="filters" role="group" aria-label="Filter articles">
<button class="chip" type="button" data-filter="all" aria-pressed="true">All</button>
<button class="chip" type="button" data-filter="types" aria-pressed="false">Work types</button>
<button class="chip" type="button" data-filter="search" aria-pressed="false">Job search</button>
<button class="chip" type="button" data-filter="hiring" aria-pressed="false">Applications</button>
<button class="chip" type="button" data-filter="path" aria-pressed="false">Second jobs</button>
<button class="chip" type="button" data-filter="market" aria-pressed="false">Job market</button>
<button class="chip" type="button" data-filter="pay" aria-pressed="false">Pay</button>
</div>
<div class="posts">
<article class="post" data-cat="path"><div class="meta"><span class="cat">Second jobs</span><span>7 min</span></div><h3><a href="article-second-path.html">Why people take a second job</a></h3><p>Money is only part of it. Time, location and meaningful work matter too.</p></article>
<article class="post" data-cat="search"><div class="meta"><span class="cat">Job search</span><span>6 min</span></div><h3><a href="article-where-to-look.html">How to search for remote work</a></h3><p>A job title plus Job Bank’s work-location and hours filters can narrow the results.</p></article>
<article class="post" data-cat="types"><div class="meta"><span class="cat">Work types</span><span>6 min</span></div><h3><a href="article-three-arrangements.html">Remote, online and flexible work compared</a></h3><p>Remote refers to location, online to how the work is done, and flexible to the schedule.</p></article>
<article class="post" data-cat="market"><div class="meta"><span class="cat">The market</span><span>6 min</span></div><h3><a href="article-what-vacancies-mean.html">What remote-work statistics can tell you</a></h3><p>Work-from-home figures and vacancy figures measure different parts of the labour market.</p></article>
<article class="post" data-cat="hiring"><div class="meta"><span class="cat">Before you apply</span><span>7 min</span></div><h3><a href="article-read-a-remote-ad.html">How to read a remote job posting</a></h3><p>Employer, location, pay and hours: what a good posting spells out.</p></article>
<article class="post" data-cat="hiring"><div class="meta"><span class="cat">Your application</span><span>5 min</span></div><h3><a href="article-remote-cv.html">Tailor your resume for online and remote work</a></h3><p>Show results, the tools you use and how you communicate.</p></article>
<article class="post" data-cat="pay"><div class="meta"><span class="cat">Pay</span><span>7 min</span></div><h3><a href="article-pay-and-province.html">Pay and deductions for additional work</a></h3><p>Minimum wage, payroll deductions and employee or contractor status.</p></article>
</div>
</div></section>
""",
)

PAGES["work-types.html"] = page(
    "work-types.html",
    "Online, remote and flexible work | Job Compass",
    "How remote, online and flexible work differ in Canada.",
    "work-types.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Work types</span><h1>Remote, online and flexible work.</h1><p class="lede">Remote describes location. Online describes how work is completed. Part-time and flexible describe hours or workload.</p></div></div>
<section><div class="wrap">
<div class="types">
<article class="type"><div><span class="n">01 · Location</span><h3><a href="remote-work-canada.html">Remote</a></h3></div><div><p>Remote jobs are completed away from the employer’s workplace. Some allow work from anywhere in Canada, while others are limited to a province. Hybrid jobs include on-site days. Job Bank identifies remote positions with a work-location filter.</p><p><a href="remote-work-canada.html">Read the guide</a></p></div></article>
<article class="type"><div><span class="n">02 · How work is done</span><h3><a href="online-work-canada.html">Online</a></h3></div><div><p>Online work is completed or delivered over the internet, including customer support, writing, design, bookkeeping, tutoring, moderation and software development. It may be done at home or at an employer’s workplace.</p><p><a href="online-work-canada.html">Read the guide</a></p></div></article>
<article class="type"><div><span class="n">03 · Hours</span><h3><a href="flexible-work-canada.html">Flexible</a></h3></div><div><p>Flexible work provides some choice over schedule, hours or workload. Part-time work describes hours and may still have a fixed schedule. Project work may be flexible, but deadlines and availability requirements still matter.</p><p><a href="flexible-work-canada.html">Read the guide</a></p></div></article>
</div>
<p class="src-note">Once the arrangement is clear, <a href="https://www.jobbank.gc.ca/findajob" rel="noopener">Job Bank</a> can filter an occupation by work location or hours.</p>
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
<div><span class="eyebrow">Location</span><h1>Remote work in Canada</h1><p class="lede">With remote work you do the job away from the employer’s office. Some remote jobs still need you to live in a certain province or work in a Canadian time zone.</p></div>
<aside class="qf"><h2>At a glance</h2><dl>
<dt>Location</dt><dd>Away from the employer’s office. Hybrid jobs include some days on-site.</dd>
<dt>Hours</dt><dd>May be full-time or part-time; the posting should state the schedule and time zone.</dd>
<dt>Applying</dt><dd>Follow the application method in a verified posting on Job Bank or the employer’s website.</dd>
<dt>Where to look</dt><dd>Job Bank’s remote filter and the employer’s careers page.</dd>
</dl><p class="rv">Last reviewed October 2026.</p></aside>
</div></div>
<section><div class="wrap article">
<h2>What remote work means</h2>
<p>Job sites may label positions on-site, hybrid or remote. Hybrid positions require some attendance at a stated workplace. Remote positions are completed away from the employer’s workplace, but they may still be limited to a province, territory or time zone.</p>
<p>A search for “work from home” is less precise than a work-location filter because the phrase can also appear in hybrid or on-site postings.</p>
<h2>How employers hire for remote positions</h2>
<p>Remote hiring generally follows the same process as other hiring: application, review, interview and written offer. The offer should identify the employer, pay, hours and permitted work location. The schedule and time zone should match the applicant’s availability.</p>
<p>To find current openings, use <a href="https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=remote" rel="noopener">Job Bank’s remote-work filter</a>.</p>
<h2>Details to confirm in an offer</h2>
<ul>
<li>Permitted province or territory</li>
<li>Required on-site days</li>
<li>Employer identity and pay basis</li>
<li>Working time zone and required availability</li>
<li>Responsibility for equipment and software</li>
</ul>
<p>For pay rules, see <a href="article-pay-and-province.html">Pay and deductions for additional work</a>. Use the <a href="article-read-a-remote-ad.html">job-posting guide</a> to check the employer, location, pay and hours.</p>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www.jobbank.gc.ca/findajob" rel="noopener">Job Bank: find a job</a></li>
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
<dt>Location</dt><dd>May be remote, hybrid or on-site; “online” alone does not specify where the work is done.</dd>
</dl><p class="rv">Last reviewed October 2026.</p></aside>
</div></div>
<section><div class="wrap article">
<h2>Online work is not necessarily remote work</h2>
<p>Online work can be done from an employer’s office or somewhere else. Remote work can also include scheduled phone duties that are not usually described as online work. Here, online work means tasks completed or delivered over the internet. Work location is a separate detail in the posting.</p>
<h2>Employee or contractor</h2>
<p>Some online jobs are regular employment: you get a schedule, a manager and a pay stub, and Canada Pension Plan and Employment Insurance deductions may apply. Others are contract work, where you send invoices, carry the financial risk and handle your own taxes. The Canada Revenue Agency considers factors such as control, tools, financial risk and opportunity for profit. The word “freelance” does not determine employment status.</p>
<h2>Online work beside a main job</h2>
<p>Online work alongside a main job often uses existing skills such as customer service, bookkeeping, writing, design, tutoring, moderation or software development. Relevant experience and compatible hours are useful criteria when comparing postings. The <a href="article-remote-cv.html">resume guide</a> covers how to present that experience.</p>
<p>Search by occupation, then use the posting to confirm the work location, hours, employer and pay arrangement. The guide to <a href="article-where-to-look.html">searching for remote work</a> covers Job Bank filters and employer verification.</p>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4110/employee-self-employed.html" rel="noopener">Canada Revenue Agency: Employee or Self-employed?</a></li>
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
<div><span class="eyebrow">Hours</span><h1>Flexible online and remote work</h1><p class="lede">Flexible work gives you some say in your hours, workload or deadlines. Here we look at flexible jobs that are also online or remote.</p></div>
<aside class="qf"><h2>At a glance</h2><dl>
<dt>Part-time</dt><dd>Under 30 hours a week, by Statistics Canada’s definition.</dd>
<dt>Arrangements</dt><dd>Choice over start and finish times, workload or project deadlines.</dd>
<dt>Location</dt><dd>Flexible work may be remote, hybrid or on-site.</dd>
<dt>Pay</dt><dd>May be hourly, salaried or project-based.</dd>
</dl><p class="rv">Last reviewed October 2026.</p></aside>
</div></div>
<section><div class="wrap article">
<h2>What flexible work can mean</h2>
<p>Flexible work can mean fewer hours, some control over start and finish times, or work organized around deadlines. Part-time describes the number of hours, not whether the schedule is flexible. A part-time job may have a fixed schedule, while a flexible arrangement may still be full-time.</p>
<p>A posting should identify the weekly hours or deadlines, required availability, time zone and who sets the schedule. The guide to <a href="article-read-a-remote-ad.html">reading a job posting</a> covers the other details to compare.</p>
<p>Contract work may provide scheduling flexibility, but income and workload can vary. Deadlines, expected availability and the method of payment belong in the written agreement.</p>
<h2>Asking your employer for flexible hours</h2>
<p>A request for a different schedule may be governed by employment standards, workplace policy, a collective agreement or an employment contract. The applicable provincial, territorial or federal authority provides the current rules.</p>
<h2>Sources</h2>
<ul class="sources">
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
        "A useful posting identifies the employer, work location, pay, hours and working arrangement.",
        """
<div class="takeaways"><h2>What to look for</h2><ul>
<li>Who is hiring, and can you find that employer on its own website?</li>
<li>Where is the work done: remote, hybrid or in a named province?</li>
<li>What does it pay: a set amount, a range or “to be negotiated”?</li>
<li>What are the hours and time zone, and would you be an employee or a contractor?</li>
<li>Do the hours fit around your current job, school or family?</li>
</ul></div>
<h2>What to expect in a job posting</h2>
<p>A useful posting identifies the job title, employer, location, pay basis, work arrangement and date posted. Pay may be hourly or yearly. If the wage says “to be negotiated,” the posting does not provide an amount.</p>
<p>Remote postings normally include the permitted work location. “Remote, Canada” and “Remote, must live in British Columbia” describe different arrangements and different applicant pools.</p>
<h2>Pay in the posting</h2>
<p>British Columbia has required compensation information in covered public job postings since 1 November 2023. For covered publicly advertised job postings in Ontario, rules in effect from 1 January 2026 require many employers with at least 25 employees to include expected compensation or a range, disclose whether they use artificial intelligence to screen applicants and say whether a vacancy exists. A posted range in Ontario cannot span more than $50,000 a year, and positions paying more than $200,000 a year are exempt. A range does not guarantee the amount you will be offered. Employers cannot require Canadian experience in those Ontario postings or related application forms.</p>
<h2>Check whether the arrangement fits</h2>
<p>Confirm the weekly hours, time zone, required availability and any on-site days. Advertised pay remains posting information until it appears in a written offer or contract. The guide to <a href="article-where-to-look.html">finding remote work</a> covers where to search.</p>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www.ontario.ca/document/your-guide-employment-standards-act-0/requirements-related-publicly-advertised-job" rel="noopener">Ontario: requirements for publicly advertised job postings</a></li>
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
        "You will often see these three words together in job postings, but each one means something different.",
        """
<div class="takeaways"><h2>The short version</h2><ul>
<li>Remote describes where the work is done.</li>
<li>Online describes how the work is completed or delivered.</li>
<li>Flexible describes the hours or workload.</li>
<li>A job can include one, two or all three arrangements.</li>
</ul></div>
<h2>Work location</h2>
<p>Remote work is done away from the employer’s office. Hybrid mixes remote and on-site days, so a “remote” posting that wants you in the office three days a week is really hybrid. More in our <a href="remote-work-canada.html">remote work guide</a>.</p>
<h2>How the work is delivered</h2>
<p>Online work is done or delivered over the internet, either from home or at the employer’s office. If a posting only says “online,” check its work-location field and required workplace. More in our <a href="online-work-canada.html">online work guide</a>.</p>
<h2>Hours</h2>
<p>Flexible work may provide some choice over schedule or workload. Statistics Canada generally defines part-time work as fewer than 30 hours a week at the main job. A flexible arrangement can still be full-time, and part-time describes hours rather than pay. See the <a href="flexible-work-canada.html">flexible-work guide</a>.</p>
<h2>Why the difference matters</h2>
<p>For work alongside a main job, hours may be the main concern. For less commuting, location matters. For a particular kind of work, the duties matter most. If a posting uses these terms without defining them, the location, duties and hours need a closer look. Related guides cover <a href="article-read-a-remote-ad.html">job postings</a> and <a href="article-second-path.html">second jobs</a>.</p>
""",
    ),
)

PAGES["article-what-vacancies-mean.html"] = page(
    "article-what-vacancies-mean.html",
    "What the remote job market looks like in Canada | Job Compass",
    "How work-from-home figures, vacancies and Job Bank filters relate to a search for remote work in Canada.",
    "reading.html",
    article(
        "The market",
        "What the remote job market looks like in Canada",
        "Work-from-home statistics describe current workers, while vacancy statistics describe open positions. Neither figure alone shows how many suitable remote jobs are available.",
        """
<p>In May 2026, 11.4 per cent of employed Canadians worked exclusively from home and 9.8 per cent had a hybrid arrangement. These figures describe employed people, not current remote vacancies.</p>
<h2>Why the remote filter matters</h2>
<p>Remote postings are mixed among occupation-specific results. A job-title search with the work-location filter is more precise than relying on the phrase “work from home,” which can also appear in hybrid and on-site postings. See <a href="article-where-to-look.html">how to search for remote work</a>.</p>
<h2>Part-time remote work</h2>
<p>Part-time and remote are separate filters. Combining them produces a narrower set of results, so a saved search or alert can help track newly posted matches.</p>
<h2>Sources</h2>
<ul class="sources">
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
        "A second job or side income can help with household costs, build experience in a field you care about or fit around the rest of your life.",
        """
<div class="takeaways"><h2>What people told Statistics Canada</h2><ul>
<li>34.9 per cent: to pay for essentials like groceries or housing.</li>
<li>34.8 per cent: to earn extra income.</li>
<li>14.5 per cent: to do work they cared about.</li>
<li>Hours and location decide whether a second job can fit beside the first.</li>
</ul></div>
<h2>How common is multiple jobholding?</h2>
<p>In 2023, 5.6 per cent of employed Canadians held more than one job at the same time. For some, one job did not cover household costs. Others used a second job to pursue a different kind of work.</p>
<p>Those August 2023 results come from a Statistics Canada Labour Force Survey supplement of workers aged 15 to 69 who already held more than one job.</p>
<h2>Why online, remote and flexible work suit a second job</h2>
<p>Most people who held two jobs in 2023 also held at least one part-time job: 89.9 per cent. A second commute can make schedules more difficult to combine. Remote work may remove that commute, while flexible hours may make two schedules easier to manage. Online work can include customer support, writing, design, bookkeeping, tutoring and software development.</p>
<h2>Different goals lead to different searches</h2>
<p>Different goals call for different criteria. Income-focused searches emphasize hours, pay basis and predictability. Experience-focused searches emphasize relevant duties. Schedule-focused searches emphasize required availability. Related guides cover <a href="article-remote-cv.html">resumes</a> and <a href="flexible-work-canada.html">flexible hours</a>.</p>
<p>The guide to <a href="article-where-to-look.html">searching for remote work</a> covers Job Bank’s remote and hours filters. The <a href="path-check.html">search goals page</a> groups guides by common reasons for seeking additional work.</p>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www150.statcan.gc.ca/n1/pub/14-28-0001/2024001/article/00002-eng.htm" rel="noopener">Statistics Canada: Multiple jobholders, 2023</a></li>
<li><a href="https://www150.statcan.gc.ca/n1/daily-quotidien/230908/dq230908a-eng.htm" rel="noopener">Statistics Canada: Labour Force Survey, August 2023, reasons for multiple jobs</a></li>
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
        "Pick a job title that matches your skills, then let Job Bank’s remote and hours filters narrow the list.",
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
<p>Searching only for “work from home” can bring up hybrid and on-site postings that mention a home elsewhere in the text. For a fully remote job, use the filter instead. On <a href="https://www.jobbank.gc.ca/findajob" rel="noopener">Job Bank’s Find a job page</a>, enter a job title and location, then choose Remote under work location.</p>
<h2>Hours for a second job</h2>
<p>The same results page can filter by hours. For someone with a main job, the part-time filter narrows results by weekly hours; part-time work may be a main or additional job. Statistics Canada counts part-time as under 30 hours a week at the main job, and a second job can involve far fewer. Weekly hours or project deadlines are normally included in the posting. Full-time remote work is a different search, since it is usually a main job done from home.</p>
<p>Remote results may come from across the country because the work is not tied to the city entered in the search. The province in each posting still matters, but it may not by itself determine which employment standards apply. Check the relevant provincial, territorial or federal authority. See <a href="article-pay-and-province.html">pay and deductions for additional work</a>.</p>
<h2>Job alerts</h2>
<p>When available, save the filtered search or create an alert for new matches.</p>
<p>Before applying, verify that the position also appears on the employer’s website and compare the employer, location, hours and pay details. The <a href="article-read-a-remote-ad.html">job-posting guide</a> provides a checklist.</p>
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
        "A resume for remote or online work can make relevant results, communication experience and tools easy to identify.",
        """
<div class="takeaways"><h2>Relevant resume information</h2><ul>
<li>Results you delivered on your own.</li>
<li>Examples of work completed with limited supervision.</li>
<li>Relevant communication, collaboration and project tools.</li>
<li>Your city and province when location eligibility matters.</li>
</ul></div>
<h2>What employers look for</h2>
<p>For online and remote jobs, employers want to know you can get the work done reliably without close supervision. For each relevant job, say what you achieved: customer requests resolved, reports delivered, classes taught, software releases maintained. Name the communication and project tools you used. If your availability matters, mention it in your application or cover letter instead of the top of your resume.</p>
<h2>Information not needed in an application</h2>
<p>Use the job title you held and describe relevant results. Do not include a social insurance number, identification or banking details in an application. Your city and province are sufficient.</p>
<h2>Resume review</h2>
<p>Results are easier to assess than copied duty lists. Concise examples can include requests resolved, reports delivered, classes taught or software releases maintained. The <a href="article-where-to-look.html">search guide</a> covers where to find postings.</p>
""",
    ),
)

PAGES["article-pay-and-province.html"] = page(
    "article-pay-and-province.html",
    "Pay and deductions for additional work | Job Compass",
    "Which pay rules to check for online and remote work in Canada, and what changes when the work is a second job.",
    "reading.html",
    article(
        "Pay",
        "Pay and deductions for additional work",
        "Additional work may involve minimum-wage rules, payroll deductions and different treatment for employees and independent contractors.",
        """
<div class="takeaways"><h2>The short version</h2><ul>
<li>There is no single minimum wage for every remote job in Canada. It depends on the federal rate or the province or territory in the posting.</li>
<li>Banks, airlines, federally regulated telecommunications companies and interprovincial transportation businesses follow the Canada Labour Code.</li>
<li>The applicable employment standards can depend on the employer, worker, workplace and whether the business is federally regulated.</li>
<li>A second employer still deducts tax and Canada Pension Plan contributions. The CRA has current instructions for filling out Form TD1.</li>
</ul></div>
<h2>Minimum wage for remote work</h2>
<p>Minimum wages change regularly and differ across federal, provincial and territorial jurisdictions. The <a href="https://minwage-salairemin.service.canada.ca/en/general.html" rel="noopener">federal minimum-wage database</a> and the applicable government employment-standards page provide current rates.</p>
<p>The applicable employment standards can depend on the employer, worker, workplace and whether the business is federally regulated. The location in a remote posting is relevant, but it does not always settle jurisdiction by itself.</p>
<h2>What job postings must show in B.C. and Ontario</h2>
<p>British Columbia has required pay information in covered public job postings since 1 November 2023. Ontario’s rules from 1 January 2026 require many employers to show expected compensation or a range, disclose artificial-intelligence screening and say whether a vacancy exists. Details and exceptions are in <a href="article-read-a-remote-ad.html">How to read a remote job posting</a>. A posted range is not a written offer. </p>
<h2>Payroll deductions from a second job</h2>
<p>A second employer still makes required payroll deductions. Multiple jobs can affect TD1 claims and may produce excess CPP or QPP contributions. The Canada Revenue Agency’s current instructions explain how to complete payroll forms and report contributions when filing a return.</p>
<p>A contract that uses the word “freelance” does not by itself establish self-employment. The Canada Revenue Agency considers control, tools, subcontracting, financial risk and opportunity for profit when assessing employment status.</p>
<h2>Sources</h2>
<ul class="sources">
<li><a href="https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/pay-deductions.html" rel="noopener">Canada.ca: pay, deductions and the federal minimum wage</a></li>
<li><a href="https://www.jobbank.gc.ca/support/question?qaid=143&amp;tid=7" rel="noopener">Job Bank: remote jobs and wage regulations</a></li>
<li><a href="https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/income-tax.html" rel="noopener">Canada Revenue Agency: income tax when an employee has different jobs</a></li>
<li><a href="https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp.html" rel="noopener">Canada Revenue Agency: CPP when an employee has different jobs</a></li>
</ul>
""",
    ),
)

PAGES["path-check.html"] = page(
    "path-check.html",
    "Search goals for flexible work | Job Compass",
    "Choose why you want online, remote or flexible work in Canada, and open the Job Compass guide that matches.",
    "reading.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Search goals</span><h1>Reasons for looking for additional work</h1><p class="lede">These four common goals lead to different starting guides. The selection stays in the browser and is not sent to Job Compass.</p></div></div>
<section><div class="wrap" style="max-width:760px">
<form id="path-check">
<ul class="check">
<li><label><input type="radio" name="hope" value="essentials"> Bring in more money to help cover essentials.</label></li>
<li><label><input type="radio" name="hope" value="extra"> Earn extra without going full-time.</label></li>
<li><label><input type="radio" name="hope" value="craft"> Get experience in a field I care about.</label></li>
<li><label><input type="radio" name="hope" value="hours"> Find work that fits around school, family or health.</label></li>
</ul>
</form>
<div id="path-result" class="result" hidden><h3></h3><p></p><p><a id="path-next" href="article-second-path.html">Read the guide</a></p></div>
<p class="notice" style="margin-top:1.5rem">These goals are starting points rather than recommendations. Compare the hours, pay basis, location and employment terms in any posting.</p>
</div></section>
""",
)

PAGES["glossary.html"] = page(
    "glossary.html",
    "Glossary | Job Compass",
    "Definitions for remote, hybrid, online, flexible, NOC, EI, CPP, LMIA and other terms used in Canadian job postings.",
    "reading.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Glossary</span><h1>Terms used in job postings</h1><p class="lede">Plain-language definitions of terms found in Canadian job postings.</p></div></div>
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
<div class="term"><dt>Additional work</dt><dd>Paid work taken on alongside another job, studies, caregiving or other commitments.</dd></div>
<div class="term"><dt>Job Bank</dt><dd>The Government of Canada’s job search website. Its remote filter helps when location matters.</dd></div>
<div class="term"><dt>NOC</dt><dd>National Occupational Classification. A code for an occupation, used on Job Bank and in labour statistics.</dd></div>
<div class="term"><dt>Vacancy</dt><dd>A position an employer is trying to fill. Statistics Canada counts vacancies through a survey, so its numbers differ from the postings on a website.</dd></div>
<div class="term"><dt>Offered wage</dt><dd>The wage advertised for an open position. It is neither the average pay of current workers nor a written offer.</dd></div>
<div class="term"><dt>CPP</dt><dd>Canada Pension Plan. A public pension plan funded through eligible employment contributions outside Quebec; Quebec uses QPP.</dd></div>
<div class="term"><dt>EI</dt><dd>Employment Insurance. A federal program that provides temporary benefits to eligible workers; premiums are generally deducted from insurable employment.</dd></div>
<div class="term"><dt>Independent contractor</dt><dd>Someone in business for themselves. The CRA looks at control, tools, risk and chance of profit, not just what the contract calls you.</dd></div>
<div class="term"><dt>LMIA</dt><dd>Labour Market Impact Assessment. An assessment that some employers need before hiring a temporary foreign worker. The employer, not the worker, applies for it.</dd></div>
<div class="term"><dt>TD1</dt><dd>A federal, provincial or territorial form employees use so an employer can calculate income-tax deductions.</dd></div>
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
<details><summary>How do remote, online and flexible work differ?</summary><p>Remote describes location, online describes how work is completed or delivered, and flexible describes schedule or workload. A position can include one, two or all three. <a href="article-three-arrangements.html">Compare the arrangements</a>.</p></details>
<details><summary>Why do people take a second job?</summary><p>Common reasons include household costs, additional income, experience and work that fits other commitments. <a href="article-second-path.html">Why people take a second job</a> provides the Statistics Canada figures.</p></details>
<details><summary>Is remote work common in Canada?</summary><p>In May 2026, 11.4 per cent of employed Canadians worked only from home and 9.8 per cent had a hybrid arrangement. These figures describe current workers rather than available vacancies. <a href="article-what-vacancies-mean.html">Read how to interpret the numbers</a>.</p></details>
<details><summary>Does advertised pay guarantee what I will earn?</summary><p>No. A posting describes expected compensation; pay is established by the employer’s written offer or contract.</p></details>
<details><summary>Which province’s rules apply if I work from home?</summary><p>It depends on where you work, where the employer operates, the type of business and your employment relationship. Federally regulated workplaces follow federal labour standards. <a href="article-pay-and-province.html">Pay and deductions for additional work</a> has more, with official links.</p></details>
<details><summary>Can a second job be combined with a current job?</summary><p>Check the schedules, employment agreement, workplace policies and possible conflicts of interest before combining jobs. See the guides on <a href="flexible-work-canada.html">flexible hours</a> and <a href="article-pay-and-province.html">pay and deductions</a>.</p></details>
<details><summary>Where can Quebec readers verify employment rules?</summary><p>CNESST provides employment-standards information. The OQLF provides information about workplace-language requirements.</p></details>
<p style="margin-top:2rem">Still have a question? <a href="contact.html">Get in touch</a>.</p>
</div></section>
""",
)

PAGES["services.html"] = page(
    "services.html",
    "Additional work in Canada | Job Compass",
    "How to compare hours, location, pay and employment status when considering additional work in Canada.",
    "services.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Additional work</span><h1>Comparing options for additional work.</h1><p class="lede">Hours, location, pay basis and employment status all affect whether additional work fits an existing schedule.</p></div></div>
<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">Four points to compare</span><h2>What changes from one arrangement to another.</h2></div>
<div class="tiles">
<article class="tile reveal"><h3>Available hours</h3><p>Weekly hours, required availability and time zone need to fit existing commitments.</p></article>
<article class="tile reveal"><h3>Pay basis</h3><p>Employee pay is normally scheduled. Contract payment may be hourly, project-based or tied to milestones.</p></article>
<article class="tile reveal"><h3>Work location</h3><p>Remote, hybrid and on-site arrangements create different location and commuting requirements.</p></article>
<article class="tile reveal"><h3>Employment status</h3><p>Employees and independent contractors have different arrangements for deductions, expenses and workplace control.</p></article>
</div>
</div></section>
<section class="alt"><div class="wrap split">
<div><span class="eyebrow">What changes with each type</span><h2>Where, how and when you work.</h2>
<p><b>Remote work</b> can cut or remove the commute, though some jobs still need you to live in a certain province or work in a certain time zone.</p>
<p><b>Online work</b> is completed or delivered over the internet, but it is not necessarily remote or flexible.</p>
<p><b>Flexible work</b> may offer a shorter week or some choice over hours. The posting or agreement should identify who sets the schedule, how much work is available and how payment is calculated.</p>
<p><a href="work-types.html">See how the three compare &rarr;</a></p></div>
<div><span class="eyebrow">Employee and contract work</span><h2>How the working relationship differs.</h2>
<p>Employee roles normally provide scheduled pay and payroll deductions. Contract work may provide more control over workload, but payment, expenses and taxes are handled differently.</p>
<p>The label in a posting does not by itself determine employment status. The Canada Revenue Agency considers the actual working relationship.</p>
<p><a href="article-pay-and-province.html">Read about pay and deductions &rarr;</a></p></div>
</div></section>
<section><div class="wrap split">
<div><span class="eyebrow">Fit with existing commitments</span><h2>Hours are only one part of the decision.</h2>
<p>Required availability, commute or on-site days, expected income, equipment costs and possible conflicts with existing work can all affect whether an arrangement is practical.</p>
<p><a href="article-second-path.html">Read why people take a second job &rarr;</a></p></div>
<div><span class="eyebrow">A practical sequence</span><h2>From priorities to a written offer.</h2>
<ol class="note-list">
<li>Identify the hours, location, income or experience that matters most.</li>
<li>Compare remote, online and flexible arrangements.</li>
<li>Search by occupation and apply the relevant filters.</li>
<li>Review the employer, location, hours, pay and employment status.</li>
<li>Verify legal, tax and employment rules with the linked government source.</li>
</ol>
<div class="btn-row"><a class="btn btn-primary" href="path-check.html">Explore search goals</a><a class="btn btn-ghost" href="reading.html">Browse all guides</a></div></div>
</div></section>
""",
)

PAGES["about.html"] = page(
    "about.html",
    "About | Job Compass",
    "About Job Compass, an editorial publisher covering remote, online and flexible work in Canada.",
    "about.html",
    """
<div class="page-head"><div class="wrap"><span class="eyebrow">Independent editorial publisher</span><h1>About Job Compass</h1></div></div>
<section><div class="wrap article">
<h2>Independent information about work in Canada</h2>
<p>Job Compass is an editorial publisher covering remote, online and flexible work in Canada. The site is for readers comparing work arrangements, searching for reliable job information or reviewing the terms in a posting.</p>
<p>Job Compass publishes guides rather than job listings. It is not affiliated with Job Bank, Statistics Canada, the Canada Revenue Agency or any federal, provincial or territorial government.</p>
<h2>Topics covered</h2>
<ul>
<li>Remote, hybrid, online, part-time and flexible work</li>
<li>Job Bank search filters and employer career pages</li>
<li>Job postings, resumes and written offers</li>
<li>Pay, payroll deductions and employee or contractor status</li>
</ul>
</div></section>
""",
)

PAGES["contact.html"] = page(
    "contact.html",
    "Contact | Job Compass",
    "Contact Job Compass about its guides to remote, online and flexible work in Canada. Please do not send identification or banking information.",
    "contact.html",
    f"""
<div class="page-head"><div class="wrap"><span class="eyebrow">Contact</span><h1>Get in touch</h1><p class="lede">Questions about a published guide or one of its sources can be sent by email.</p></div></div>
<section><div class="wrap split">
<div>
<form id="contact-form" class="form" novalidate>
<div class="field"><label for="name">Name</label><input id="name" required autocomplete="name"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">Email</label><input id="email" type="email" required autocomplete="email"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="province">Province or territory</label><select id="province"><option value="">Prefer not to say</option><option>Alberta</option><option>British Columbia</option><option>Manitoba</option><option>New Brunswick</option><option>Newfoundland and Labrador</option><option>Northwest Territories</option><option>Nova Scotia</option><option>Nunavut</option><option>Ontario</option><option>Prince Edward Island</option><option>Quebec</option><option>Saskatchewan</option><option>Yukon</option><option>Outside Canada</option></select></div>
<div class="field"><label for="topic">Topic</label><select id="topic"><option>Remote work</option><option>Online work</option><option>Work from home</option><option>Part-time or flexible work</option><option>Freelance or side job</option><option>Pay, tax or employment status</option><option>Another job-related question</option></select></div>
<div class="field"><label for="msg">Your question</label><textarea id="msg" required></textarea><div class="err" aria-live="polite"></div></div>
<button class="btn btn-primary" type="submit">Open email</button>
<p class="notice">This form creates a message in your email app; it does not submit information to this website. Review the message before sending.</p>
</form>
<div id="form-ok" class="ok" hidden tabindex="-1" role="status"><h3>Your email message is ready.</h3><p>Review it in your email app before sending.</p><p class="ok-sub">If the app did not open, email {EMAIL}.</p></div>
</div>
<div>
<h2>Email</h2>
<ul class="contact-list"><li><b>Questions</b><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul>
<p class="notice">We can answer questions about published content and point to public sources. We cannot assess a job offer or provide individual legal, tax, immigration or employment advice. Do not include a social insurance number, government identification, passwords or banking information.</p>
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
<p>This notice explains the limited personal information involved when you use Job Compass. The site does not offer user accounts.</p>
<h2>What you can send us</h2>
<p>The contact form creates an email in your email application; it does not submit information to this website. If you send the message, Job Compass receives the information included in it, such as your name, email address, province or territory, topic and message. That information is used to respond and, where relevant, improve published guides. Contact information is not sold or added to a marketing list.</p>
<p>Do not send a social insurance number, banking details, identification or passwords. Job Compass will not ask for them.</p>
<h2>What stays on your device</h2>
<p>The path check and the glossary search run in your browser. What you choose or type there is not transmitted to us by those tools.</p>
<h2>Fonts and server logs</h2>
<p>Pages request typefaces from Google Fonts. That request can expose your IP address to Google. Our hosting provider may keep ordinary server logs, such as IP address, browser and page requested, for security. We do not add our own analytics tracker to these pages.</p>
<h2>How long a message is kept</h2>
<p>We keep emails only as long as we need them to reply, keep a record or meet a legal obligation. After that, we delete or anonymize them. You can ask what information we still have, request a correction or ask us to delete the thread by writing to hello@jobcompass.ca. We may need to verify that the request comes from the email account concerned.</p>
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
<h2>About this publication</h2>
<p>Job Compass publishes general information about remote, online and flexible work in Canada. It does not list jobs, recruit or place candidates, or act on behalf of employers.</p>
<h2>No guarantee</h2>
<p>Nothing on this site is a job offer or a promise of employment, income, hours or eligibility. Those matters depend on the employer, the position and the applicable rules.</p>
<h2>General information</h2>
<p>The site does not provide individual legal, tax, immigration or employment advice. Consult the appropriate authority or a qualified adviser about individual circumstances.</p>
<h2>Currency and sources</h2>
<p>Statistics, wages, vacancies and employment rules can change. Review the date shown on a guide and check its linked sources for current information.</p>
<h2>External links</h2>
<p>Links are provided for reference. Third-party sites control their own content, availability and privacy practices.</p>
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
