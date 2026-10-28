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
        p: "In August 2023, 34.9% of Canadians with more than one job cited groceries, housing and other essentials as their main reason. Guides on part-time hours, Job Bank filters and pay are relevant to this goal.",
        href: "article-pay-and-province.html",
        link: "Pay and a second job"
      },
      extra: {
        h: "Extra income without going full-time",
        p: "Almost the same share, 34.8%, cited extra income. Part-time employment usually provides regular pay statements, while contract income can vary from month to month.",
        href: "flexible-work-canada.html",
        link: "Flexible hours"
      },
      craft: {
        h: "Building experience in a field you like",
        p: "Another 14.5% cited work they cared about. The resume guide covers relevant skills and results, while the search guide explains why a job title is more precise than “work from home.”",
        href: "article-remote-cv.html",
        link: "Our resume guide"
      },
      hours: {
        h: "Hours that fit your life",
        p: "School, family responsibilities, health needs and a preference for a shorter week are common reasons for part-time work. The flexible-work guide covers hours and schedules for online and remote jobs.",
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
