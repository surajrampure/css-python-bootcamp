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

**Teaching Assistants:** Yaqian Huang (yah101@ucsd.edu), Ben Lang (blang@ucsd.edu)

---

🎉 <span style='color:#00649c'><b>Welcome to the website for Week 1 of the CSS Summer Bootcamp!</b></span> 🎉

To access the lectures and labs for this course, all you need to do is click the "lecture" or "lab" links below. They'll bring you to DataHub, the computational platform we're using for the course.

For those who aren't able to acccess DataHub, all materials are available publicly at [this GitHub repo](https://github.com/surajrampure/css-python-bootcamp).

{% for module in site.modules %}
{{ module }}
{% endfor %}