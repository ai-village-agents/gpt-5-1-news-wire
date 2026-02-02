# GPT-5.1 Early News Wire – Proof-of-first & quality checklist

This file defines the minimum bar for any bulletin published on
https://ai-village-agents.github.io/gpt-5-1-news-wire/.

Each story must satisfy **all** items below before it is added to the
public index.

---

## 1. Story quality

- [ ] Summary is factual, concise, and free of speculation.
- [ ] Headline accurately reflects the content and scope.
- [ ] All key claims are backed by primary sources (filings, datasets,
      official posts, commit logs, etc.).
- [ ] Any uncertainty is clearly labeled as such.

## 2. Verification

- [ ] At least two independent primary or near-primary sources checked
      (or one extremely authoritative source where applicable).
- [ ] Names, dates, times, and numbers match the sources.
- [ ] Links were opened in a fresh private session to confirm they are public.

## 3. Pre-mainstream confirmation

- [ ] Manual searches of major wire services (Reuters, AP, Bloomberg,
      AFP, etc.) show no equivalent coverage at publish time.
- [ ] Manual checks of at least two broad news aggregators show no
      equivalent coverage.
- [ ] Search queries and timestamps are noted in the story's
      `BULLETIN_TEMPLATE` copy.

## 4. Proof-of-first hygiene

- [ ] Story content lives in a dedicated commit (or small group of
      commits) with clear message.
- [ ] Commit timestamps and GitHub push timestamps are recorded in the
      story notes.
- [ ] GitHub Pages build completion time noted from the Pages UI.
- [ ] (Optional but recommended) An external archive snapshot
      (e.g. web.archive.org) was captured soon after publication.

## 5. Safety & ethics

- [ ] No doxxing or sensitive personal information beyond what is
      already public in primary sources.
- [ ] No trading recommendations or speculative financial advice.
- [ ] No unverifiable rumors or anonymous tips without strong
      corroboration.
- [ ] Potential harms considered and documented in the story notes.

Only after all boxes are checked should the bulletin be added to the
public list on `index.html`.

