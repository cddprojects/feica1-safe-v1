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
        h: "A second job for essentials",
        p: "In August 2023, 34.9% of people with more than one job said their main reason was paying for groceries, housing and other essentials. Decide how many hours you can work alongside your main job, then search Job Bank for a suitable title and use the remote and part-time filters. Read the pay guide before treating an advertised range as your expected wage.",
        href: "article-pay-and-province.html",
        link: "Pay and a second job"
      },
      extra: {
        h: "Extra income, with a limit on hours",
        p: "Almost the same share, 34.8%, said they wanted extra income. Decide how many hours you can realistically work. Part-time employees receive regular pay statements, while contract income may vary from month to month.",
        href: "flexible-work-canada.html",
        link: "Flexible hours"
      },
      craft: {
        h: "Build experience in a field",
        p: "14.5% said they held a second job to do work they were passionate about. Start with a skill you can demonstrate and include a relevant result on your resume. Search for a suitable job title rather than relying on the words “work from home” alone.",
        href: "article-remote-cv.html",
        link: "The resume guide"
      },
      hours: {
        h: "Hours that fit the rest of your life",
        p: "School, family responsibilities, health needs or a preference for a shorter schedule are among the reasons people work part-time. North Desk focuses on flexible hours for online or remote work.",
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
      var subject = "North Desk" + (v("topic") ? ": " + v("topic") : "");
      var body = "Name: " + v("name") + "\nEmail: " + v("email") + "\nProvince or territory: " + v("province") + "\n\n" + v("msg");
      form.hidden = true;
      var done = document.getElementById("form-ok");
      done.hidden = false;
      done.focus();
      window.location.href = "mailto:desk@northdesk.ca?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    });
  }
})();
