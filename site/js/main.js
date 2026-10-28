(function () {
  var btn = document.querySelector(".menu-btn");
  var list = document.getElementById("nav-list");
  if (btn && list) {
    btn.addEventListener("click", function () {
      var open = list.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      btn.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    });
    list.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        list.classList.remove("open");
        btn.setAttribute("aria-expanded", "false");
        btn.setAttribute("aria-label", "Open menu");
      });
    });
  }

  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("in");
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12 });
    document.querySelectorAll(".reveal").forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll(".reveal").forEach(function (el) { el.classList.add("in"); });
  }

  var chips = document.querySelectorAll(".chip[data-filter]");
  chips.forEach(function (c) {
    c.addEventListener("click", function () {
      chips.forEach(function (x) { x.setAttribute("aria-pressed", x === c ? "true" : "false"); });
      var f = c.dataset.filter;
      document.querySelectorAll(".post[data-cat]").forEach(function (p) {
        p.hidden = !(f === "all" || p.dataset.cat === f);
      });
    });
  });

  var search = document.getElementById("glossary-search");
  if (search) {
    search.addEventListener("input", function () {
      var q = search.value.trim().toLowerCase();
      var n = 0;
      document.querySelectorAll(".term").forEach(function (t) {
        var match = t.textContent.toLowerCase().indexOf(q) > -1;
        t.hidden = !match;
        if (match) n++;
      });
      document.getElementById("glossary-empty").hidden = n > 0;
    });
  }

  var pathForm = document.getElementById("path-check");
  if (pathForm) {
    var pathOut = document.getElementById("path-result");
    var hopes = {
      essentials: {
        h: "Covering the essentials",
        p: "In August 2023, 34.9% of Canadians with more than one job said their main reason was paying for groceries, housing and other essentials. A good first step is working out how many hours you can give alongside your main job, then searching Job Bank by job title with the remote and part-time filters on. A posted pay range isn’t your wage until an employer offers it, so the pay guide is worth a read.",
        href: "article-pay-and-province.html",
        link: "Pay and a second job"
      },
      extra: {
        h: "Extra income without going full-time",
        p: "Almost the same share, 34.8%, said they wanted extra income. Be honest about how many hours you can really work. Part-time employees get regular paycheques, while contract income can swing from month to month.",
        href: "flexible-work-canada.html",
        link: "Flexible hours"
      },
      craft: {
        h: "Building experience in a field you like",
        p: "14.5% said they took a second job to do work they care about. Start with a skill you can already show, and put a real result on your resume. Search by job title, since the words “work from home” alone bring up a lot of noise.",
        href: "article-remote-cv.html",
        link: "Our resume guide"
      },
      hours: {
        h: "Hours that fit your life",
        p: "School, family, health or just wanting a shorter week are common reasons people work part-time. Our flexible work guide looks at hours for online and remote jobs.",
        href: "flexible-work-canada.html",
        link: "Flexible hours"
      }
    };
    pathForm.addEventListener("change", function () {
      var picked = pathForm.querySelector("input:checked");
      if (!picked || !hopes[picked.value]) { pathOut.hidden = true; return; }
      var item = hopes[picked.value];
      var next = document.getElementById("path-next");
      pathOut.hidden = false;
      pathOut.querySelector("h3").textContent = item.h;
      pathOut.querySelector("p").textContent = item.p;
      if (next) {
        next.href = item.href;
        next.textContent = item.link;
      }
    });
  }

  var form = document.getElementById("contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var ok = true;
      form.querySelectorAll("[required]").forEach(function (field) {
        var err = field.parentElement.querySelector(".err");
        var bad = !field.value.trim() || (field.type === "email" && !/^\S+@\S+\.\S+$/.test(field.value));
        if (err) err.textContent = bad ? (field.type === "email" ? "Enter an email address." : "This field is required.") : "";
        field.setAttribute("aria-invalid", bad ? "true" : "false");
        if (bad) ok = false;
      });
      if (!ok) return;
      var v = function (id) {
        var el = document.getElementById(id);
        return el ? el.value.trim() : "";
      };
      var subject = "Job Compass inquiry" + (v("topic") ? ": " + v("topic") : "");
      var body = "Name: " + v("name") + "\nEmail: " + v("email") + "\nProvince or territory: " + v("province") + "\nTopic: " + v("topic") + "\n\n" + v("msg");
      form.hidden = true;
      var done = document.getElementById("form-ok");
      done.hidden = false;
      done.focus();
      window.location.href = "mailto:hello@jobcompass.ca?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    });
  }
})();
