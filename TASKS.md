# Task commentary

Plain-language summaries of the 24 tasks used in this eval. **Full task text is not mirrored here** — the tasks belong to OpenAI's [SWE-Lancer benchmark](https://github.com/openai/SWELancer-Benchmark) ([paper](https://arxiv.org/abs/2502.12115)); look them up by `question_id` in the official release, or follow each heading's link to the public Expensify/App issue the task was built from. 日本語版: [`TASKS.ja.md`](TASKS.ja.md)

## Common to all tasks

- Every task is a real freelance job on a real OSS codebase (Expensify/App, a React Native expense app); prices are what was actually paid on Upwork
- The prompt the grading harness builds is written for the paper's official scaffold (the [stock solver](https://github.com/openai/frontier-evals/blob/main/project/swelancer/swelancer/solvers/swelancer_agent/solver.py)): a loop where the harness executes \```python blocks found in the model's reply, and where writing `<user-tool>` makes a simulated user (Playwright) actually drive the app and hand back an interaction trace. **Matching the paper's conditions exactly requires using that solver.** Its drawback is that it is nowhere near how real coding agents work — every turn must be a self-contained Python script, with none of the file-editing/shell tooling of modern agents — so it is a poor sanity3 of practical usability
- This eval rolls out with CLI agents to measure practical usability instead. The cost: **the prompt's references to "\```python execution" and `<user-tool>` remain as descriptions of affordances that do not exist**
- What `promptv1` really is: Gemma-4 follows the phantom "\```python is the ONLY way to send commands" instruction to the letter and, unless it is neutralized, **exits after a single code-block turn on every task** (reproduced 2/2). We therefore append one paragraph to AGENT_PROMPT stating that python blocks are not executed and tool calls are the only way to act. This patch **originates from a Gemma-4-specific quirk**, but is applied uniformly to all rtx6000 CLI arms for internal comparability (how other models behave without it is untested). The `<user-tool>` instruction is NOT neutralized, and failures caused by chasing it are counted as-is (e.g. Gemma-4 on 18827_741 / 4324)
- **Text-only, by rule.** Every arm runs without vision input — the checkpoints here carry no vision tower and the agent CLIs pass text only. This is a standing constraint of the eval, not an accident of the lineup: visually-dependent tasks (see the tally) can only be cracked through textual side channels (code references, dangling keys), and that ability is part of what this eval measures
- **No task requires audio.** Image/video reliance varies per task, noted below
- Grading runs the official e2e tests against the final repo state; visual design is only graded to the extent the tests check it

## sanity3 (does-it-still-work gate, 3 tasks)

### [28096_836](https://github.com/Expensify/App/issues/28096) — $500 / "Choose File" button capitalization
- **Type**: UI copy fix (bug)
- **Summary**: The "Choose File" button on the receipt-scan screen capitalizes both words, violating the app-wide sentence-case convention. Fix the casing
- **Media**: screenshots/video attached as illustration; steps/expected/actual fully written out — solvable from text alone

### [18827_741](https://github.com/Expensify/App/issues/18827) — $1,000 / "Link sent!" not re-translated on language switch
- **Type**: i18n bug
- **Summary**: The "Link sent!" message shown after unlinking an unverified email stays English when the user switches to Spanish. Make it re-render in the selected language
- **Media**: video attached (illustration); 7 written repro steps

### [29618_781](https://github.com/Expensify/App/issues/29618) — $500 / Currency search inconsistent between pages
- **Type**: consistency bug
- **Summary**: Searching euro/rupee works in the split-bill currency dropdown but returns "no results found" in the workspace default-currency section. Unify the search behavior
- **Media**: screenshots/video (illustration); 10 written steps

## hard5 (5 tasks K2.7 failed)

### [14294](https://github.com/Expensify/App/issues/14294) — $4,000 / Google Docs paste turns bold, adds `*`
- **Type**: rich-text handling bug
- **Summary**: Pasting from Google Docs into chat makes text bold and wraps bold text in `*`. Fix the HTML→Markdown paste path
- **Media**: 2 videos (illustration); fully specified in text

### [24508_791](https://github.com/Expensify/App/issues/24508) — $1,000 / "÷×" accepted in legal name
- **Type**: validation bug
- **Summary**: Despite the "Name can only include letters" error, `÷×` slips through validation and saves. Reject symbols consistently
- **Media**: video (illustration); text-complete

### [15815_1](https://github.com/Expensify/App/issues/15815) — $4,000 / Emoji reaction buttons are not 28px
- **Type**: pixel-level CSS bug
- **Summary**: Reaction buttons should be 28px but render at 24px. An extremely terse spec (expected: "Should be 28px") — find the style and fix it
- **Media**: 2 screenshots (illustration); the numeric spec is in the text

### [27353_776](https://github.com/Expensify/App/issues/27353) — $500 / Overlay background color mismatch
- **Type**: theme/color bug
- **Summary**: The settings overlay color differs between staging and newdot. The correct color value is not stated — it must be inferred from the theme code
- **Media**: comparison attachment (illustration)

### [15925](https://github.com/Expensify/App/issues/15925) — $2,000 / Line breaks lost on copy/paste
- **Type**: clipboard bug
- **Summary**: Copying multi-line text via the context-menu Copy icon and pasting into chat drops the line breaks. Fix the divergent copy paths
- **Media**: 1 video (illustration); text-complete

## extended16 (16 K2.7-failed tasks, shortest descriptions first)

### [29916_609](https://github.com/Expensify/App/issues/29916) — $500 / Move all selectors to the new format
- **Type**: refactor feature. **Reference-dependent**
- **Summary**: Apply the "hide selected participants while searching" pattern introduced for group chat / split bill to **every selector**. What the "new format" is is not in the text — you must read the referenced PR #29903 / issue #29836
- **Media**: none; requires following links instead (container has internet access)

### [6883](https://github.com/Expensify/App/issues/6883) — $32,000 / Hardware keyboard shortcuts on native
- **Type**: large feature (highest prize in the set)
- **Summary**: Cmd+K etc. don't work in native apps (tablets). Build the plumbing for native to listen and react to hardware keyboard shortcuts like web does
- **Media**: none; the ask is clear in text but the implementation surface is wide

### [43395_530](https://github.com/Expensify/App/issues/43395) — $250 / Mobile loading skeleton
- **Type**: UI feature. **Visually dependent**
- **Summary**: Implement a small-screen loading skeleton for the Search page. **The target design is the screenshot itself** — the text says little beyond "like this image"
- **Media**: 1 design screenshot acting as the de-facto spec

### [25901_945](https://github.com/Expensify/App/issues/25901) — $2,000 / Easier waypoint deletion
- **Type**: UX feature. **Visually dependent**
- **Summary**: Add a "dot menu → popup → delete confirmation" flow to the waypoint editor. The final design is **"see the screenshots in this comment"**; the video only demonstrates the current problem
- **Media**: video (status quo) + referenced screenshots (the spec)

### [40259_1089](https://github.com/Expensify/App/issues/40259) — $500 / Self-DM in Start Chat
- **Type**: feature
- **Summary**: The self-DM is only reachable via global search. Show it in the Start Chat participant selector and open it on click — with the constraint that it must not be addable to groups
- **Media**: none; text-complete

### [18746_833](https://github.com/Expensify/App/issues/18746) — $1,000 / @yourself and @here in mention suggestions
- **Type**: feature
- **Summary**: Mentioning yourself and @here works but neither shows up in the auto-suggestion box; make them appear. Today/Ideal comparison is in screenshots, but the requirement is clear in text
- **Media**: 3 screenshots (Today/Ideal illustration; borderline)

### [4324](https://github.com/Expensify/App/issues/4324) — $2,000 / Render `:smile:`-style emoji codes
- **Type**: feature
- **Summary**: Typing `:smile:` in chat doesn't render an emoji; make it render like Slack does. A Slack screen recording is attached as the reference behavior
- **Media**: 2 videos (expected = Slack example, actual = current); the ask is clear in text

### [44429_1100](https://github.com/Expensify/App/issues/44429) — $250 / Block money requests to domain emails
- **Type**: validation feature
- **Summary**: Domain addresses like `+@expensify.com` can currently be targets of split/money requests; forbid it
- **Media**: 2 screenshots (illustration); steps and ask are in text

### [40208_1108](https://github.com/Expensify/App/issues/40208) — $500 / Console-log button in the four-finger-tap menu
- **Type**: developer-tooling feature
- **Summary**: The four-finger-tap menu can enable client-side logging but offers no way into the realtime console logs; add a button
- **Media**: none; Problem/Solution stated in text

### [44618_1007](https://github.com/Expensify/App/issues/44618) — $250 / Report fields in single-transaction view
- **Type**: feature
- **Summary**: With report-field violations and a single-transaction view you can't fix the fields without an add-transaction/delete-transaction detour. Show report fields alongside expense details in the single-transaction view
- **Media**: 1 video (status-quo illustration); the solution is written out

### [19132_872](https://github.com/Expensify/App/issues/19132) — $1,000 / Allow assigning yourself to a task
- **Type**: feature
- **Summary**: The assignee selector doesn't offer yourself; make self-assignment possible (the text mentions back-end changes too, but grading covers the front-end)
- **Media**: none; 3 written steps

### [41885_1134](https://github.com/Expensify/App/issues/41885) — $500 / Self-DM not bold in LHN
- **Type**: display bug
- **Summary**: After signing in with a fresh account, the self-DM in the left-hand navigation should be bold but isn't
- **Media**: none; text-complete

### [50064_846](https://github.com/Expensify/App/issues/50064) — $250 / Onboarding stuck on first step
- **Type**: flow-control bug
- **Summary**: After closing and reopening the app, tapping an option in the onboarding modal doesn't advance to the next step
- **Media**: none; text-complete

### [50314_790](https://github.com/Expensify/App/issues/50314) — $250 / Context menu closes instantly with emoji picker open
- **Type**: event-handling bug
- **Summary**: With the emoji picker open, right-clicking a message opens the context menu and immediately closes it
- **Media**: none; text-complete

### [37688_441](https://github.com/Expensify/App/issues/37688) — $500 / Block the chat UI via `PRIVATE_BLOCKED_FROM_CHAT`
- **Type**: feature. **Visually dependent**
- **Summary**: A user blocked from chat can still type; sending just errors at the API. Replace the compose box with a dedicated blocked-state component. **The component's look is only shown in the screenshot inside Expected Result** — though the codebase contains a dangling reference (an unregistered Onyx key) that also points to the answer
- **Media**: 1 screenshot as the de-facto spec

### [44040_470](https://github.com/Expensify/App/issues/44040) — $250 / IOU members page is blank
- **Type**: display bug
- **Summary**: Opening the members modal from an IOU header shows an empty modal; make it list the members
- **Media**: none; text-complete

## Tally

| category | tasks |
|---|---:|
| Fully specified in text | 19 |
| Visually dependent (design lives in images) | 3 (43395_530 / 25901_945 / 37688_441) |
| Reference-dependent (must read linked PR/issue) | 1 (29916_609) |
| Borderline (images helpful, text sufficient) | 1 (18746_833) |
| Audio-dependent | 0 |
