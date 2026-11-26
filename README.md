<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img src="assets/hero-light.svg" alt="Bogdan Ljubinković. Building things worth using with people worth building with." width="100%">
</picture>

<br>

<a href="https://www.linkedin.com/in/ljubogdan/"><img src="assets/badge-linkedin.svg" alt="LinkedIn: ljubogdan" height="28"></a>
<a href="https://x.com/ljubogdan"><img src="assets/badge-x.svg" alt="X: @ljubogdan" height="28"></a>
<a href="https://ordoverse.com"><img src="assets/badge-ordoverse.svg" alt="Building ordoverse.com" height="28"></a>
<img src="assets/badge-location.svg" alt="Based in Novi Sad, Serbia" height="28">

</div>

<br>

I'm a software engineering student in Novi Sad. I like problems where a wrong answer costs real money or time, and I want every result traceable to where it came from. Right now that means **multi-agent AI systems you can audit**, **software for regulated, unglamorous industries**, and the **systems fundamentals** under both.

<table>
<tr>
<td width="33%" valign="top">

**🛠️ Building**<br>
[Ordoverse](https://ordoverse.com): software that brings order to the work a company depends on. First product: **BZR autopilot**, for occupational-safety agencies.

</td>
<td width="33%" valign="top">

**🤖 Exploring**<br>
Agent teams that check each other: parallel investigators, verifiers, and knowing when to say *no*. Most recently on [Mozaik](https://github.com/jigjoy-ai/mozaik).

</td>
<td width="33%" valign="top">

**📚 Studying**<br>
Distributed systems, storage engines, parallel computing, graphics and ML at FTN, Novi Sad.

</td>
</tr>
</table>

## ✦ Featured work

<table>
<tr>
<td width="50%" valign="top">

### [🛩️ blackbox](https://github.com/ljubogdan/blackbox)
**A flight recorder for purchases made by AI agents.** Parallel agent investigators stop a risky payment before it settles, and when a customer disputes one, they work out who was at fault and split the liability. Every figure traces back to a sealed record.

`TypeScript` `Mozaik` `Claude` `Stripe test mode`<br>
<sub>JigJoy Black Friday AI Hackathon · Agents in Finance</sub>

</td>
<td width="50%" valign="top">

### [🤝 prenup](https://github.com/ljubogdan/prenup)
**Research partnerships, agreed up front.** Agents pair researchers with companies, negotiate IP and publication terms before anyone meets, check every fact against the data, and decline when there's no good match.

`TypeScript` `Mozaik` `Node 22` `59 tests`<br>
<sub>NTP Novi Sad × JigJoy Hackathon · EINSTEIN track · [▶ live board](https://prenup-board.onrender.com)</sub>

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [🧹 unfluff](https://github.com/ljubogdan/unfluff)
**See how much of your LinkedIn feed is noise, then hide it.** A browser extension that measures ads, suggested posts and engagement bait, then collapses, removes or labels them. No network requests, no tracking.

`JavaScript` `Chrome extension` `Manifest V3`

</td>
<td width="50%" valign="top">

### [🔎 ai-diff-review-service](https://github.com/ljubogdan/ai-diff-review-service)
**Async AI code review for unified diffs.** A FastAPI service with job polling, replayable SSE streams, idempotency, caching and rate limiting. Ships a deterministic mock scorer and a Gemini provider that fails cleanly.

`Python` `FastAPI` `SSE` `Gemini` `Railway`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [☁️ cloud-social-analytics](https://github.com/ljubogdan/cloud-social-analytics)
**Serverless social-data lakehouse on AWS.** Pulls Twitter and Hacker News data through bronze, silver and gold layers with Lambda, then serves Superset dashboards and Discord alerts.

`Python` `AWS CDK` `Lambda` `Superset`

</td>
<td width="50%" valign="top">

### [🗄️ NASP-NoSQL-Engine](https://github.com/ljubogdan/NASP-NoSQL-Engine)
**A key-value storage engine from scratch.** WAL, memtable, SSTables with Bloom filters and Merkle trees, an LRU cache, prefix and range scans, and token-bucket rate limiting.

`Go` `LSM tree` `Bloom filter` `Merkle tree`

</td>
</tr>
</table>

## 🔒 Private repositories

**21 of my repos are private**, plus two Ordoverse repos I work on. Some hold client or course material I can't publish, and some are products in progress. **Want access?** Message me on [LinkedIn](https://www.linkedin.com/in/ljubogdan/) or [X](https://x.com/ljubogdan) with your GitHub username and the repo you'd like to see.

<details open>
<summary><b>🚀 Products in progress</b></summary>
<br>

| | Project | What it is | Stack |
|:-:|---|---|---|
| 🔒 | **bzr-autopilot** | Web app for Serbian occupational-safety (BZR) agencies: tracks every client's training, medical exams and inspections, emails reminders before deadlines, imports and exports Excel, and drafts risk-assessment acts with AI. *Ordoverse product.* | Next.js · Supabase · Postgres RLS · Vercel · Claude |
| 🔒 | **archomaly** | Local-first pull-request verification. Compares a change against its base, structure and history, then issues a replayable **Change Passport** of impact, anomalies and evidence, all tied to exact SHAs. Useful with every LLM turned off. *Pre-alpha.* | Python · Git · static analysis |
| 🔒 | **ordoverse webpage** | Landing site for [ordoverse.com](https://ordoverse.com), with product pages and i18n. | HTML · CSS · JS · Cloudflare Workers |

</details>

<details open>
<summary><b>🌐 Distributed &amp; concurrent systems</b></summary>
<br>

| | Project | What it is | Stack |
|:-:|---|---|---|
| 🔒 | **nvt-2026** · *OnlyKicks* | A scalable sneaker marketplace: load-balanced backend replicas behind Nginx, event streaming, caching, presigned S3 media uploads and monitoring. | Java · Spring Boot · React · PostgreSQL · Kafka · RabbitMQ · Redis · SeaweedFS · Grafana |
| 🔒 | **mini-scada** | Distributed SCADA system: secure real-time collection, processing and monitoring of temperature sensors, with BFT consensus. | C# · .NET 8 · SignalR · PostgreSQL · Docker |
| 🔒 | **chaotic-cupid** | A real-time matchmaking simulation with background services and thread-safe registries. | C# · ASP.NET Core · SignalR · Spectre.Console |
| 🔒 | **job-processing-system** | A multithreaded job system with a priority queue, producers and consumers, and a stochastic IO/prime workload. | C# · .NET |
| 🔒 | **parallel-web-scraper-tbb** | A four-stage parallel pipeline (fetch → parse → analyze → store) with concurrent data structures, retries and automatic page discovery. | C++20 · Intel TBB · libcurl · CMake |

</details>

<details open>
<summary><b>🎮 Graphics, games &amp; algorithms</b></summary>
<br>

| | Project | What it is | Stack |
|:-:|---|---|---|
| 🔒 | **rg-aquarium** | A 2D aquarium in modern OpenGL: fish, a crab, bubbles, food and a treasure chest, with custom shaders and textures. | C++17 · OpenGL 3.3 · GLFW · GLEW |
| 🔒 | **genetic-timetable-scheduler** | A genetic algorithm that schedules 60+ lectures and labs across 5 rooms and a full week under hard and soft constraints. | Python · NumPy |
| 🔒 | **checkers-python** | Checkers with a Minimax + alpha-beta AI, a SQLite transposition table and time-aware search depth. | Python · Pygame · SQLite |
| 🔒 | **OOP2-Minotaur** | A console maze game: procedural labyrinth, a chasing Minotaur, fog of war and power-ups. | C++17 |
| 🔒 | **typescript-blackjack** | A command-line Blackjack (21) game. | TypeScript · Node.js |

</details>

<details>
<summary><b>🧠 Machine learning</b> (5 repos)</summary>
<br>

| | Project | What it is | Stack |
|:-:|---|---|---|
| 🔒 | **solar-cycle-lstm** | Predicts solar cycles and storm risk from sunspot time series with an LSTM and Huber loss. | TensorFlow · Keras · Jupyter |
| 🔒 | **tweet-emotion-classifier** | An RNN that sorts tweets into emotion classes. | TensorFlow · NLP |
| 🔒 | **medinsurance-ann-tensorflow** | Predicts insurance premiums with linear regression vs. a neural network, plus EDA and feature engineering. | TensorFlow · scikit-learn |
| 🔒 | **GSP633-imgclassify-tensorflow** | A CNN that classifies Fashion-MNIST images. | TensorFlow · Jupyter |
| 🔒 | **GSP632-convolution** | Image convolutions and pooling by hand: 3×3 filters and their effects. | NumPy · SciPy · Google Cloud |

</details>

<details>
<summary><b>📐 Software design &amp; team projects</b> (3 repos)</summary>
<br>

| | Project | What it is | Stack |
|:-:|---|---|---|
| 🔒 | **usi-course-project** · *LangLang* | Desktop app for language schools: courses, exams, grading, penalty points and director reports. Built by a team of four. | C# · WPF · .NET |
| 🔒 | **DefenseLogistics** | Information-system design for defense procurement and logistics, from tender to delivery, testing and maintenance (EER modelling). | Database design · CASE tools |
| 🔒 | **SSAM-project** | Requirements and UML design for a software system: use cases, class, sequence and activity diagrams. | UML · requirements analysis |

</details>

<sub>Also private: <b>project-management-app</b> (React + TypeScript, early WIP) and <b>TESOL-ArizonaStateUniversity</b> (teaching materials from ASU's TESOL course).</sub>

## ⚙️ Toolbox

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,js,python,go,java,cs,cpp,nodejs,react,nextjs,spring,dotnet,fastapi&perline=13" alt="Languages and frameworks"><br>
  <img src="https://skillicons.dev/icons?i=postgres,supabase,redis,kafka,rabbitmq,docker,nginx,aws,cloudflare,vercel,opengl,tensorflow,linux&perline=13" alt="Data, infrastructure and tools">
</p>

<p align="center">
  <sub>Also: Claude & Gemini APIs · Mozaik · SignalR · WPF · Intel TBB · AWS CDK · Grafana · Playwright · Vitest · pytest</sub>
</p>

---

<div align="center">
<sub>Have something worth building? <a href="https://www.linkedin.com/in/ljubogdan/">Let's talk.</a></sub>
</div>
