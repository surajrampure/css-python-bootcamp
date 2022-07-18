---
layout: home
title: Home
nav_exclude: false
nav_order: 1
---

# {{ site.tagline }} 🐍
{: .mb-2 }
{{ site.description }}
{: .mb-2 .fs-6 }

---

**Instructor:** Suraj Rampure (rampure@ucsd.edu)

**Teaching Assistants:** TBD

---

🎉 <span style='color:#00649c'><b>Welcome to the website for Week 1 of the CSS Summer Bootcamp!</b></span> 🎉 <br>More details to come.

{% for module in site.modules %}
{{ module }}
{% endfor %}